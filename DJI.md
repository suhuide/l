# MAVIC4 Pro
```mermaid
graph TB
A[无人机] -->|OcuSync 视频流| B[遥控器]
A <--> |OcuSync控制| B
A <--> |BLE控制| C[手机]
A --> |Wi-Fi直连| C
B --> |USB/蓝牙| C

%% 4G模块部分
A <--> |4G链路| D[4G基站]
D <--> |4G网络| B
D <--> |4G网络| C
```

|无线协议|功能|特点|
|--|--|--|
|OcuSync|图传<br>控制|控制延迟5ms<br>1080p/4K视频流,延迟130ms|
|4G|图传<br>控制|抗遮挡备份,OcuSync信号弱/断开启用<br>延迟100-200ms<br>流量消耗|
|Wi-Fi|图传|720p视频流,延迟200ms+|
|Bluetooth|控制<br>状态同步|延迟20-50ms<br>仅适用于起降、慢速平移等简单操作|

```mermaid
graph TB
  A[OcuSync信号强度] -->|≥70%| B[纯OcuSync传输]
  A -->|30%-70%| C[OcuSync+4G并行]
  A -->|≤30%| D[纯4G传输]
  C --> E[视频分片传输]
  D --> F[指令优先加密]
```
```mermaid
graph TB
  A[视频流] -->|H.265编码| B[关键帧 I帧]
  A -->|H.265编码| C[增量帧 P/B帧]
  B -->|OcuSync链路| D[接收端]
  C -->|4G链路| D
  D -->|帧重组| E[完整视频]
```
```mermaid
barChart
title 延迟对比
xAxis 协议类型
yAxis 延迟(ms)
series
    OcuSync控制：5
    OcuSync视频：130
    4G图传：180
    手机直连控制：220
    BLE状态：40
    4G状态：100
```


```mermaid
graph TB
  A[摄像头传感器] -->|MIPI/CSI 接口| B[RK3566/OpenHD<br>自适应码率控制<br>前向纠错 FEC<br>自动重传请求 ARQ<br>动态跳频机制]
  B <-->|H.264/H.265 压缩流| C[Wi-Fi 模块]
  C <-->|无线射频信号<br>空中传输| D[接收端 Wi-Fi]
  D <--> E[OpenHD协议栈解包处理]
  E --> F[视频解码器]
  F --> G[显示设备]
  subgraph     
    A
    B
    C
  end
  subgraph   
    D
    E
    F
    G
  end
  %% classDef path fill:#f9f,stroke:#333,stroke-width:2px;
  %%class A,B,C,D,E,F,G,H,I,J path;
```

# MIC2
```mermaid
graph LR
A[发射器 TX1] -->|2.4GHz 专有协议| B[接收器 RX]
A2[发射器 TX2] -->|2.4GHz 专有协议| B
A -->|蓝牙HFP| C[手机]
A2 -->|蓝牙HFP| C
B -->|USB-C/Lightning 数字信号| C
B -->|3.5mm TRS 模拟信号| D[相机]
C & D --> E[视频+音频录制]
```

通讯路径    
- 手机蓝牙直连模式(无接收器)  
    ○ TX 发射器 -> 手机:蓝牙 BR/EDR HFP 协议  
    ○ 接单个TX, 传输单声道音频  
    ○ 未来可能支持LE Audio  
    ○ 延迟20-50ms  
- 接收器  
    ○ TX -> RX, 2.4GHz 专有协议  
    ○ TX -> RX, GFSK 调制, 抗干扰强  
    ○ TX -> RX, 可接两个TX, 传输立体声音频  
    ○ RX -> 手机/相机:有线连接(数字或模拟输出)  
    ○ 安全音轨，TX端保存  
    ○ 延迟仅10ms  

```mermaid
graph TB
  subgraph 发射端 TX
    A[麦克风拾音] --> B[TX增益调节]
    B --> C[32位浮点ADC]
    C --> D[8GB 内录音频存储]
    C --> E[2.4GHz专有协议编码]
    C --> F[蓝牙直连手机]
  end

  subgraph 接收端 RX
    E --> G[2.4GHz专有协议解码]
    G --> H[RX增益调节]
    H --> I[AI降噪+DSP处理]
    I --> J[USB-C/Lightning输出]
    I --> K[3.5mm TRS输出]
  end

  subgraph     
    J --> L[手机/电脑]
    K --> M[相机]
    F -->|无降噪| N[手机]
  end

```    