# 初始化
def initialize(context):
    # 设置基准指数
    set_benchmark("000300.XSHG")
    # 股票池对应指数代码 - 同时包含中小板和创业板
    g.index_list = ["399101.XBHS", "399006.XBHS"]  # 中小板综 + 创业板综
    # 持有股票数量
    g.buy_stock_count = 5
    # 策略资金分配
    g.start_cost = 50000
    # 筛选股票数量
    g.screen_stock_count = 15
    
    # 调整：放宽风控参数
    g.max_position_per_stock = 0.25  # 单股票仓位限制25%（略微放宽）
    g.stop_loss_rate = 0.15  # 止损15%（放宽止损）
    g.take_profit_rate = 0.20  # 止盈30%（放宽止盈）
    
    # 调整：缩短冷却期
    g.cool_down_days = 1  # 卖出后1天内不再买入同一股票（缩短冷却期）
    g.sell_history = {}  # 记录卖出历史 {股票代码: 卖出日期}
    
    if not is_trade():
        set_backtest()  # 设置回测条件


# 设置回测条件
def set_backtest():
    set_limit_mode("UNLIMITED")


# 盘前处理
def before_trading_start(context, data):
    # 清理过期的卖出记录
    current_date = context.current_dt.date()
    g.sell_history = {stock: sell_date for stock, sell_date in g.sell_history.items() 
                     if (current_date - sell_date).days <= g.cool_down_days}
    
    # 获取中小板和创业板的所有股票
    all_stock_list = []
    for index in g.index_list:
        all_stock_list.extend(get_index_stocks(index))
    
    g.pre_position_list = list(get_positions().keys())
    g.stock_list = list(set(all_stock_list))  # 去重

    # 1. 获取所有股票的流通市值数据
    df = get_fundamentals(g.stock_list, "valuation", fields=["total_value", "a_floats", "float_value"],
                          date=context.previous_date).sort_values(by="float_value").head(150)

    stock_list_tmp = df.index.tolist()  # 初始股票池（已按市值排序）

    # 2. 剔除ST、停牌、退市股票
    stock_list_tmp = filter_stock_by_status(stock_list_tmp, filter_type=["ST", "HALT", "DELISTING"])

    # 3. 保留状态筛选后的股票，并取流通市值最小的15个
    df = df[df.index.isin(stock_list_tmp)]  # 筛选有效股票
    g.df = df.head(g.screen_stock_count)    # 存储前15只到全局变量g.df
    stock_list_tmp = g.df.index.tolist()    # 更新股票池

    # 4. 国九条筛选（净利润、营业收入）
    income_data = get_fundamentals(
        security=stock_list_tmp,
        table='income_statement',
        fields=['net_profit', 'operating_revenue'],
        report_types='4',
        start_year=str(context.previous_date.year-1),
        end_year=str(context.previous_date.year-1)
    )

    if income_data is not None:
        mask = (income_data['net_profit'] >= 0) | (income_data['operating_revenue'] >= 1e8)        
        g.stock_list = income_data[mask]
    
    log.info(f"最终股票池：{g.stock_list}")
    

# 盘中处理
def handle_data(context, data):
    # 只在特定条件下执行止损止盈（避免过于频繁）
    if context.current_dt.hour == 14 and context.current_dt.minute >= 30:  # 只在下午2:30后检查
        execute_stop_loss_take_profit(context, data)
    
    buy_stocks = get_trade_stocks(context, data)
    log.info("buy_stocks:%s" % buy_stocks)
    trade(context, buy_stocks)


# 交易函数
def trade(context, buy_stocks):
    # 卖出不在买入列表的股票
    for stock in context.portfolio.positions:
        if stock not in buy_stocks and context.portfolio.positions[stock].amount > 0:
            order_target_value(stock, 0)
            # 记录卖出历史
            g.sell_history[stock] = context.current_dt.date()
            log.info("sell:%s" % stock)
    
    # 买入逻辑 - 恢复原始的资金分配方式
    position_list = [position.sid for position in context.portfolio.positions.values()
                     if position.amount != 0]
    position_count = len(position_list)
    if g.buy_stock_count > position_count:
        value = context.portfolio.cash / (g.buy_stock_count - position_count)
        for stock in buy_stocks:
            if stock not in context.portfolio.positions:
                # 检查冷却期
                if stock in g.sell_history:
                    days_since_sell = (context.current_dt.date() - g.sell_history[stock]).days
                    if days_since_sell <= g.cool_down_days:
                        log.info(f"跳过 {stock}，仍在冷却期内")
                        continue
                
                # 检查仓位限制
                current_position_value = 0
                if stock in context.portfolio.positions:
                    current_position_value = context.portfolio.positions[stock].value
                
                if current_position_value + value <= context.portfolio.total_value * g.max_position_per_stock:
                    order_target_value(stock, value)
                    log.info(f"买入: {stock}, 金额: {value:.2f}")


# 止损止盈执行函数 - 条件放宽
def execute_stop_loss_take_profit(context, data):
    """只在尾盘执行止损止盈，避免过早卖出"""
    for stock, position in context.portfolio.positions.items():
        if position.amount > 0:
            try:
                current_price = data[stock].price
                cost_price = position.cost_basis
                
                if cost_price > 0:  # 确保有成本价
                    profit_rate = (current_price - cost_price) / cost_price
                    
                    # 止损检查 - 只在亏损较大时止损
                    if profit_rate <= -g.stop_loss_rate:
                        order_target_value(stock, 0)
                        g.sell_history[stock] = context.current_dt.date()
                        log.info(f"止损卖出: {stock}, 亏损: {profit_rate:.2%}")
                    
                    # 止盈检查 - 只在盈利较大时止盈
                    elif profit_rate >= g.take_profit_rate:
                        order_target_value(stock, 0)
                        g.sell_history[stock] = context.current_dt.date()
                        log.info(f"止盈卖出: {stock}, 盈利: {profit_rate:.2%}")
                        
            except Exception as e:
                log.warning(f"检查 {stock} 止损止盈时出错: {e}")


# 获取买入股票池（涨停股不参与换仓）
def get_trade_stocks(context, data):
    # 获取持仓中涨停的标的
    hold_up_limit_stock = []
    for stock in g.pre_position_list:
        try:
            limit_status = check_limit(stock, data)
            if stock in limit_status and limit_status[stock] == 1:
                hold_up_limit_stock.append(stock)
        except:
            continue
    
    df = g.df
    if df.empty:
        return hold_up_limit_stock
    df["code"] = df.index
    # 计算当时最新的流通市值（昨日的流通股本*最新价）
    df["curr_float_value"] = df.apply(lambda x: x["a_floats"] * data[x["code"]].price, axis=1)
    df = df[df["curr_float_value"] != 0]
    # 获取股票标的（按流通市值从小到大排序）        
    stocks = df.sort_values(by="curr_float_value").index.tolist()
    # 计算本次拟买入的数量（最大持仓量-持仓中涨停的数量（因为涨停股不卖））
    count = g.buy_stock_count - len(hold_up_limit_stock)
    check_out_lists = stocks[:count]
    check_out_lists = check_out_lists + hold_up_limit_stock
    
    # 过滤掉冷却期内的股票
    final_list = []
    for stock in check_out_lists:
        if stock in g.sell_history:
            days_since_sell = (context.current_dt.date() - g.sell_history[stock]).days
            if days_since_sell <= g.cool_down_days:
                continue
        final_list.append(stock)
    
    return final_list


# 辅助函数：检查涨停状态 - 简化版本
def check_limit(stock, data):
    """
    检查股票是否涨停
    简化版本，避免复杂逻辑
    """
    try:
        # 直接使用data对象获取涨停状态
        if hasattr(data[stock], 'high_limit') and hasattr(data[stock], 'price'):
            high_limit = data[stock].high_limit
            current_price = data[stock].price
            
            # 如果当前价格接近涨停价（考虑微小误差），认为涨停
            if high_limit and current_price and current_price >= high_limit * 0.995:
                return {stock: 1}
    except Exception as e:
        pass
    
    return {stock: 0}