
# Q6V5和remoteproc子系统_PIL固件加载_Qcacld_Init_Tx_RX

/*
**q6v5_start 和 q6v5_mpss_load 是与高通（Qualcomm）SoC 中的 Hexagon DSP  或 调制解调器子系统（Modem Subsystem）  相关的函数或操作。
**它们通常出现在高通的驱动程序代码中，用于启动和加载调制解调器固件（如 MPSS，Modem Processor SubSystem Software）
*/
```c
 q6v5_probe 
    -> 	rproc = rproc_alloc(&pdev->dev, pdev->name, &q6v5_ops, mba_image, sizeof(*qproc));
    -> rproc_add(rproc); //通过过滤这个关键字，可以看到kernel 里面众多dsp子系统，wcnss(qcom_wcnss.c),pas(qcom_q6v5_pas.c),mss（qcom_q6v5_mss.c）等
        -> rproc_char_device_add(rproc);/* add char device for this remoteproc 后面start，stop 某个dsp 子系统就是通过往这个字符设备发"start","stop","detach"命令*/ 

kernel_platform/msm-kernel/drivers/remoteproc/qcom_q6v5_mss.c
    static const struct rproc_ops q6v5_ops = {
	.start = q6v5_start,
	.stop = q6v5_stop,
	.parse_fw = qcom_q6v5_register_dump_segments,
	.load = q6v5_load,
};

static struct platform_driver q6v5_driver = {
	.probe = q6v5_probe,
	.remove = q6v5_remove,
	.driver = {
		.name = "qcom-q6v5-mss",
		.of_match_table = q6v5_of_match,
	},
};
module_platform_driver(q6v5_driver);

msm-kernel/drivers/remoteproc/remoteproc_cdev.c
    ->rproc_cdev_write(rproc); /*start, stop, detach 发给某个dsp*/
        ->rproc_boot(rproc);

msm-kernel/drivers/remoteproc/remoteproc_core.c
        ->request_firmware(&firmware_p, rproc->firmware, dev);  /* load firmware */
        ->rproc_fw_boot                                         /*take a firmware and boot a remote processor with it.*/
            ->rproc_start
                ->rproc_prepare_subdevices(rproc);
                ->rproc->ops->start(rproc);       /* power up the remote processor , 就是下面的q6v5_start*/
                ->rproc_start_subdevices(rproc);  /* Start any subdevices for the remote processor */
                
 q6v5_start
    ->q6v5_mpss_load(qproc) ;//加载mpss 固件
        ->request_firmware(&fw, fw_name, qproc->dev);
        ->ret = q6v5_mpss_init_image(qproc, fw);
        ->qcom_pil_info_store("modem", qproc->mpss_phys, qproc->mpss_size);
```
/*
****icnss_probe 是高通（Qualcomm）SoC 中 ICNSS（Integrated Chipset Subsystem）  驱动程序的一个关键函数，用于初始化和配置无线通信子系统（如 Wi-Fi 和蓝牙）。
*****它是 Linux 内核中设备驱动程序模型的一部分，当内核检测到与 ICNSS 相关的硬件设备时，会调用 icnss_probe 函数来完成设备的初始化
*/
```c
qcom/opensource/wlan/platform/icnss2/main.c
     icnss_probe(struct platform_device *pdev)
       ->INIT_WORK(&wpss_loader, icnss_wpss_load);
       -> icnss_wpss_load 
            -> priv->rproc = rproc_get_by_phandle(rproc_phandle);
            -> rproc_boot(priv->rproc)

opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_main.c
    hdd_module_init 
        -> hdd_driver_load
            -> hdd_qdf_init()
            -> hdd_init()           /*Initialize Driver*/
            -> hdd_component_init() /*Initialize all components*/
            ->  pld_init()
            -> hdd_register_driver_retry() ->wlan_hdd_register_driver ->pld_register_driver(&wlan_drv_ops) 
    
opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_driver_ops.c
     wlan_hdd_register_driver
        -> pld_register_driver(&wlan_drv_ops)
            ->pld_pcie_register_driver
                -> pci_register_driver(&pld_pcie_ops); /* pld_pcie_probe() - Probe function for PCIE platform driver */
                
            ->pld_snoc_register_driver()
                ->icnss_register_driver(&pld_snoc_ops);
                
            ->pld_snoc_fw_sim_register_driver()
                -> icnss_register_driver(&pld_snoc_fw_sim_ops);
                
            ->pld_pcie_fw_sim_register_driver()
                ->cnss_fw_sim_wlan_register_driver(&pld_pcie_fw_sim_ops)
                
            ->pld_usb_register_driver()
                ->cnss_usb_wlan_register_driver(&pld_usb_ops)
                
            -> pld_ipci_register_driver()
                ->icnss_register_driver(&pld_ipci_ops)
```
     通过以上pld_register_driver(&wlan_drv_ops)注册 wlan_drv_ops 驱动，设备和对应驱动match 之后，wlan_hdd_pld_probe 会被调用
```c     
     struct pld_driver_ops wlan_drv_ops = {
            .probe      = wlan_hdd_pld_probe, /*用于在系统启动时初始化 Wi-Fi 子系统,会调用 Linux 内核的网络子系统 API 来创建和注册网络接口设备  wlan_hdd_pld_probe -> hdd_soc_probe ->__hdd_soc_probe -> hdd_psoc_create_vdevs -> hdd_open_adapters_for_mode -> hdd_open_concurrent_interface -> hdd_open_adapter_no_trans->hdd_open_adapter() -> hdd_register_interface(...) -> hdd_register_netdevice(adapter, dev, params)*/
            .remove     = wlan_hdd_pld_remove,
            .idle_shutdown = wlan_hdd_pld_idle_shutdown,
            .idle_restart = wlan_hdd_pld_idle_restart,
            ....
```
/*
*SNOC  和 IPCI  是高通（Qualcomm）SoC 中的重要组件，分别代表 System NOC (Network on Chip)  和 Inter-Processor Communication Interface
*SNOC ，IPCI 分别用于
*/
```c
                /**
                * enum qdf_bus_type - Supported Bus types
                * @QDF_BUS_TYPE_NONE: None Bus type for error check
                * @QDF_BUS_TYPE_PCI: PCI Bus
                * @QDF_BUS_TYPE_AHB: AHB Bus
                * @QDF_BUS_TYPE_SNOC: SNOC Bus
                * @QDF_BUS_TYPE_SIM: Simulator
                * @QDF_BUS_TYPE_USB: USB Bus
                * @QDF_BUS_TYPE_IPCI: IPCI Bus
                */
                enum qdf_bus_type {
                    QDF_BUS_TYPE_NONE = -1,
                    QDF_BUS_TYPE_PCI = 0,
                    QDF_BUS_TYPE_AHB,
                    QDF_BUS_TYPE_SNOC,
                    QDF_BUS_TYPE_SIM,
                    QDF_BUS_TYPE_SDIO,
                    QDF_BUS_TYPE_USB,
                    QDF_BUS_TYPE_IPCI
                };

qcom/opensource/wlan/qcacld-3.0/core/pld/src/pld_ipci.c
     pld_ipci_register_driver(void) 
        -> icnss_register_driver(&pld_ipci_ops)
            ->  pld_ipci_probe 
                -> pld_add_dev(pld_context, dev, NULL, PLD_BUS_TYPE_IPCI);
    
qcom/opensource/wlan/qcacld-3.0/core/pld/src/pld_snoc.c
      pld_snoc_register_driver()
        -> icnss_register_driver(&pld_snoc_ops)
           ->pld_snoc_probe
                -> pld_add_dev(pld_context, dev, NULL, PLD_BUS_TYPE_SNOC);
                ->pld_context->ops->probe(dev, PLD_BUS_TYPE_SNOC,..) /* 上面wlan_hdd_driver_ops.c 的wlan_hdd_pld_probe*/
                    -> hdd_soc_probe(dev, bdev, id, bus_type);
                        ->hdd_wlan_startup
                            -> hdd_wlan_start_modules(hdd_ctx, false) /*初始化HDD的子模块，hif cds dp cfg ... */

qcom/opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_main.c
    hdd_wlan_start_modules(struct hdd_context *hdd_ctx, bool reinit)
        ->pld_power_on   //start powe on WLAN HW
        ->hdd_hif_open(qdf_dev->dev, qdf_dev->drv_hdl, qdf_dev->bid,..)  //start initialization
qcom/opensource/wlan/qcacld-3.0/core/pld/src/pld_common.c
     pld_power_on(struct device *dev)  // Power on WLAN hardware
```     
     

//初始化网络接口 通过过调用hdd_open_adapter_no_trans 函数，完成不同类型网络接口的创建
```c
/PYO/sm6225/LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_main.c or wlan_hdd_mlo.c

    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_STA_MODE, in hdd_wlan_register_mlo_interfaces()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_P2P_DEVICE_MODE, in hdd_open_p2p_interface()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_OCB_MODE, in hdd_open_ocb_interface()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_STA_MODE, in hdd_open_concurrent_interface()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_STA_MODE, in hdd_open_adapters_for_mission_mode()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_NAN_DISC_MODE, in hdd_open_adapters_for_mission_mode()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_FTM_MODE, in hdd_open_adapters_for_ftm_mode()
    status = hdd_open_adapter_no_trans(hdd_ctx, QDF_MONITOR_MODE, in hdd_open_adapters_for_monitor_mode()
```
//三种HIF 底层通讯接口 SDIO、USB、CE、Wifi3.0的pipe
```c
/PYO/sm6225/LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/qca-wifi-host-cmn/hif/src/sdio/transfer/
 adma.c      rx_comp = device->hif_callbacks.rxCompletionHandler;  //走控制 dl_data_avail_cb -> hif_read_write -> rx_comp
 mailbox.c    rxCompletion = pdev->hif_callbacks.rxCompletionHandler; //走数据

/PYO/sm6225/LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/qca-wifi-host-cmn/hif/src/usb/
 usbdrv.c     device->htc_callbacks.rxCompletionHandler 
    hif_start -> usb_hif_start_recv_pipes -> usb_hif_post_recv_transfers -> usb_hif_usb_recv_complete -> HIF_USB_SCHEDULE_WORK -> usb_hif_io_comp_tasklet - > usb_hif_io_complete(pipe) - device->htc_callbacks.rxCompletionHandler(..)


/PYO/sm6225/LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/qca-wifi-host-cmn/hif/src/ce/
   ce_main.c    rxCompletionHandler(msg_callbacks->Context,..) 
   ce_tasklet -> ce_per_engine_service -> CE_state->service -> ce_engine_service_reg -> CE_state->recv_cb -> hif_pci_ce_recv_data -> hif_ce_do_recv -> rxCompletionHandler


/PYO/sm6225/LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/qca-wifi-host-cmn/dp/wifi3.0/
   dp_internal.h     hif_pipe_callbacks.rxCompletionHandler = callback; 
   dp_htt.c          connect.EpCallbacks.EpRecv = dp_htt_t2h_msg_handler;

Rx:
     (htcCallbacks.rxCompletionHandler =)htc_rx_completion_handler -> do_recv_completion_pkt -> pEndpoint->EpCallBacks.EpRecv
        ->htt_t2h_msg_handler ->ol_rx_in_order_indication_handler -> peer->rx_opt_proc(vdev, peer, tid, head_msdu) 
            -> ol_rx_deliver -> ol_rx_data_process -> ol_rx_data_handler ->hdd_rx_pkt_thread_enqueue_cbk/ hdd_rx_packet_cbk -> hdd_rx_deliver_to_stack -> netif_receive_skb

Tx:
    hdd_hard_start_xmit -> __hdd_hard_start_xmit -> adapter->tx_fn(soc, adapter->vdev_id, (qdf_nbuf_t)skb)  //将数据包传递给硬件或固件

或者通过IPA 路径
drivers/platform/msm/ipa_fmwk/ipa_fmwk.c
    ipa_fmwk_ctx->ipa_eth_register_ready_cb(ready_info)
    
/dataipa/drivers/platform/msm/ipa/ipa_clients/ipa_eth.c
    static DECLARE_WORK(ipa_eth_ready_notify, ipa_eth_ready_notify_work);
     ipa_eth_uc_rdy_cb -> ipa_eth_ready_notify_work
        entry->info->notify(entry->info->userdata)
            ->ipa->notify = wlan_ipa_i2w_cb;
               ->wlan_ipa_i2w_cb 
                    ->wlan_ipa_send_pkt_to_tl(iface_context, ipa_tx_desc)
                        ->cdp_ipa_tx_send_data_frame 
                            ->arch_ops->tx_hw_enqueue 

qcacld-3.0/core/dp/txrx/ol_txrx.c
    .ipa_tx_data_frame = ol_tx_send_ipa_data_frame ->... ->ol_tx_enqueue(pdev, txq, tx_desc, &tx_msdu_info); ->... -> htt_tx_send_std ->..->htc_send_data_pkt(pdev->htc_pdev, &pkt->htc_pkt, more_data)->hif_send_head ->SDIO/CE/USB
    
qcacld-3.0/core/dp/txrx/dp_main.c
    .ipa_tx_data_frame = dp_tx_send_ipa_data_frame -> dp_tx_send(soc_hdl, vdev_id, skb);->dp_tx_send_msdu_single -> arch_ops->tx_hw_enqueue ->li/be 的HW SRNG

wlan/qca-wifi-host-cmn/dp/wifi3.0/li/dp_li.c
    arch_ops->tx_hw_enqueue = dp_tx_hw_enqueue_li;
    
wlan/qca-wifi-host-cmn/dp/wifi3.0/li/dp_be.c
    arch_ops->tx_hw_enqueue = dp_tx_hw_enqueue_be;
```
/*
*SRNG(Shared Ring)
*   是一种环形缓冲区（Ring Buffer）结构，广泛用于现代 Wi-Fi 芯片（尤其是 Qualcomm 的 Wi-Fi 驱动和固件架构）中，用于在主机（Host）和目标设备（Target，通常是 Wi-Fi 芯片的固件）之间高效地传递数据和控制信息
*/
```c
wlan/qca-wifi-host-cmn/hal/wifi3.0/hal_internal.h //HAL_SRNG_SRC_RING, HAL_SRNG_DST_RING

    
msm-kernel/drivers/net/wireless/ath/ath11k/wmi.h  //支持的底层WMI 消息，配置参数，支持哪些功能，可以配置哪些参数，可以从这里cmd/event message开始查找
enum wmi_tlv_cmd_id {
enum wmi_tlv_event_id {
enum wmi_tlv_pdev_param {
enum wmi_tlv_vdev_param {
enum wmi_tlv_service {

qca-wifi-host-cmn/wmi/inc/wmi_unified_param.h  /*Host based ENUM IDs for events to abstract target enums for event_id*/
    

LINUX/android/vendor/qcom/opensource/wlan/qcacld-3.0/core/mac/inc/wni_api.h //SME request messages from HDD or upper layer
enum eWniMsgTypes {
	eWNI_SME_MSG_TYPES_BEGIN = SIR_SME_MSG_TYPES_BEGIN,
	eWNI_SME_SYS_READY_IND = SIR_SME_MSG_TYPES_BEGIN + 1,
	eWNI_SME_JOIN_REQ = SIR_SME_MSG_TYPES_BEGIN + 2,
	eWNI_SME_JOIN_RSP = SIR_SME_MSG_TYPES_BEGIN + 3,
    ...
    CM_BSS_PEER_CREATE_REQ = SIR_SME_MSG_TYPES_BEGIN + 171,
	CM_CONNECT_REQ = SIR_SME_MSG_TYPES_BEGIN + 172,
	CM_DISCONNECT_REQ = SIR_SME_MSG_TYPES_BEGIN + 173,
	CM_REASSOC_REQ = SIR_SME_MSG_TYPES_BEGIN + 174,
	CM_PREAUTH_REQ = SIR_SME_MSG_TYPES_BEGIN + 175,
	eWNI_SME_CSA_REQ = SIR_SME_MSG_TYPES_BEGIN + 176,
	CM_ABORT_CONN_TIMER = SIR_SME_MSG_TYPES_BEGIN + 177,
	eWNI_SME_MSG_TYPES_END = SIR_SME_MSG_TYPES_BEGIN + 178
   }

wlan/qca-wifi-host-cmn/umac/cmn_services/inc/wlan_cmn.h //哪些模块
      /**
   * enum wlan_umac_comp_id - UMAC component id
   * @WLAN_UMAC_COMP_MLME:          MLME
   * @WLAN_UMAC_COMP_MGMT_TXRX:     MGMT Tx/Rx
   * @WLAN_UMAC_COMP_SERIALIZATION: Serialization
   * @WLAN_UMAC_COMP_SCAN: SCAN -   as scan module uses services provided by
   ...
qcacld-3.0/core/hdd/src/wlan_hdd_cfg80211.c
    hdd_cfg80211_wiphy_alloc()中以下代码段，将hdd_ctx 做为 wipy的私有数据（绑定到wiphy->priv）
        struct hdd_context *hdd_ctx;
        wiphy = wiphy_new(&wlan_hdd_cfg80211_ops, sizeof(*hdd_ctx));
        hdd_ctx = wiphy_priv(wiphy);
        hdd_ctx->wiphy = wiphy;
        
LA.VENDOR.13.2.1.r1/LINUX/android/vendor/qcom/opensource/wlan/fw-api/fw/htt.h  //WIFI FW 到 驱动 ，target -> host messages

qcacld-3.0/core/hdd/src/wlan_hdd_main.c 中 hdd_component_init(void) 完成个模块的初始化， hdd_register_driver_retry()-> wlan_hdd_register_driver -> wlan_hdd_pld_probe ->...__hdd_soc_probe->hdd_wlan_startup(hdd_ctx)-> hdd_wlan_start_modules
```
+-------------------------------------------------------------+
|                    用户空间层 (User Space)                  |
|                                                             |
|   +-------------------+     +---------------------------+   |
|   | 应用程序/工具     |     | 网络管理工具 (iw, wpa_cli) |   |
|   +-------------------+     +---------------------------+   |
|           ↓                           ↓                     |
+-------------------------------------------------------------+
|                    内核空间层 (Kernel Space)                |
|                                                             |
|   +-----------------------------------------------------+   |
|   |               UMAC (Upper MAC)                      |   |
|   |                                                     |   |
|   | - 帧过滤、QoS、加密/解密                            |   |
|   | - 扫描、连接管理                                    |   |
|   +-----------------------------------------------------+   |
|           ↓                           ↓                     |
|   +-------------------+     +---------------------------+   |
|   | WMI (Wireless      |     | HTT (High Throughput      |   |
|   | Module Interface)  |     | Transport)                |   |
|   | - 控制命令传递     |     | - 数据包传输              |   |
|   +-------------------+     +---------------------------+   |
|           ↓                           ↓                     |
|   +-----------------------------------------------------+   |
|   | HTC (HIF Transport|                                   |   |
|   | Component)        |                                   |   |
|   | - 消息传输        |                                   |   |
|   | - 端点管理        |                                   |   |
|   +-----------------------------------------------------+   |
|           ↓                                                 |
|   +-----------------------------------------------------+   |
|   | HIF (Host Interface Layer)                          |   |
|   | - PCIe/SDIO/USB 接口                                |   |
|   | - 硬件抽象层                                       |   |
|   +-----------------------------------------------------+   |
|           ↓                                                 |
|   +-----------------------------------------------------+   |
|   | CE (Copy Engine)                                   |   |
|   | - 零拷贝传输                                       |   |
|   | - 批量处理                                         |   |
|   +-----------------------------------------------------+   |
+-------------------------------------------------------------+
|                    固件层 (Firmware)                         |
|                                                             |
|   +-----------------------------------------------------+   |
|   | PE (Packet Engine)                                  |   |
|   | - 加密/解密                                         |   |
|   | - 校验和计算                                       |   |
|   +-----------------------------------------------------+   |
|           ↓                                                 |
|   +-----------------------------------------------------+   |
|   | 硬件层 (Hardware)                                   |   |
|   | - 信号调制、信道选择                                |   |
|   | - 物理层操作                                       |   |
|   +-----------------------------------------------------+   |
+-------------------------------------------------------------+
```c
/*数据发送 路径*/
wlan/qca-wifi-host-cmn/umac/mlme/connection_mgr/core/src/wlan_cm_sm.c
   	{
        (uint8_t)WLAN_CM_SS_REASSOC,
        (uint8_t)WLAN_CM_S_ROAMING,
        (uint8_t)WLAN_SM_ENGINE_STATE_NONE,
        false,
        "REASSOC",
        cm_subst_reassoc_entry,
        cm_subst_reassoc_exit,
        cm_subst_reassoc_event
        ...
     }
wlan/qca-wifi-host-cmn/umac/mlme/connection_mgr/core/src/wlan_cm_roam_sm.c //事件状态机处理
   cm_subst_reassoc_event 
        -> cm_reassoc_active(cm_ctx, data)
            cm_resume_reassoc_after_peer_create(cm_ctx, cm_id);
                status = mlme_cm_reassoc_req(cm_ctx->vdev, req);
            
wlan/qca-wifi-host-cmn/umac/mlme/mlme_objmgr/dispatcher/src/wlan_cmn_mlme_main.c
     mlme_cm_reassoc_req ->  glbl_ops->mlme_cm_ext_reassoc_req_cb(vdev, req)
     
qcacld-3.0/components/umac/mlme/connection_mgr/core/src/wlan_cm_vdev_connect.c
    cm_handle_connect_req
        msg.type = CM_CONNECT_REQ;
        status = scheduler_post_message(QDF_MODULE_ID_MLME,QDF_MODULE_ID_PE,QDF_MODULE_ID_PE, &msg);

qcacld-3.0/core/mac/src/pe/lim/lim_process_sme_req_messages.c
    lim_process_messages 
        ->case CM_CONNECT_REQ:
            cm_process_join_req(msg);
        -> bool lim_process_sme_req_messages(struct mac_context *mac, struct scheduler_msg *pMsg) //SME request messages from HDD or upper layer
    
qcacld-3.0/core/mac/src/pe/lim/lim_send_management_frames.c


qca-wifi-host-cmn/umac/mlme/mlme_objmgr/dispatcher/inc/wlan_vdev_mlme_main.h  //Vdev 事件定义
   /**
   * enum wlan_vdev_sm_evt - VDEV SM event
   * @WLAN_VDEV_SM_EV_START:               Start VDEV UP operation
   * @WLAN_VDEV_SM_EV_ROAM:                Notifiction on ROAMING


wlan/qcacld-3.0/core/wma/src/wma_main.c  //  wma_open 函数里面注册了一系列的回调函数和事件处理函数,可以通过过滤 wmi_unified_register_event_handler 关键字来看各模块（）通过wma 注册想关注的WMI 的事件以及处理函数
    /* register for STA kickout function */
     wmi_unified_register_event/wmi_unified_register_event_handler(wma_handle->wmi_handle,wmi_peer_sta_kickout_event_id,wma_peer_sta_kickout_event_handler,WMA_RX_SERIALIZER_CTX);  // 调用 wmi_register_event_handler_with_ctx

wlan/qca-wifi-host-cmn/wmi/src/wmi_unified.c
    wmi_register_event_handler_with_ctx -> wmi_handle->event_handler[idx] = handler_func; //register event handler with exec ctx and buffer type
    
wlan/qca-wifi-host-cmn/wmi/src/wmi_unified.c
     __wmi_control_rx -> wmi_handle->event_handler[idx] (wmi_handle->scn_handle,..)  /* Call the WMI registered event handler */

/*可设置工作模式， Mission，FMTM，MOnitor，EPPING*/
static const hdd_open_mode_handler
hdd_open_mode_handlers[QDF_GLOBAL_MAX_MODE] = {
	[QDF_GLOBAL_MISSION_MODE] = hdd_open_adapters_for_mission_mode,
	[QDF_GLOBAL_FTM_MODE] = hdd_open_adapters_for_ftm_mode,
	[QDF_GLOBAL_MONITOR_MODE] = hdd_open_adapters_for_monitor_mode,
	[QDF_GLOBAL_EPPING_MODE] = hdd_open_adapters_for_epping_mode,
};

wlan/qcacld-3.0/core/mac/src/pe /* Policy Engine */
    lim/   //漫游管理在这下面，Link Independent Module
    nan/   //支持设备间的服务发现， Neighbor Awareness Networking
    rrm/   //收集邻居报告，支持 LIM 的漫游决策，Radio Resource Management
    sch/   //cheduler  这个模块是 MAC 层的时间调度器，负责协调 Beacon 发送、DTIM 周期、PS-Poll 响应等定时事件 以及根据优先级调度数据包的发送时间

opensource/wlan/qcacld-3.0/core/mac/src/cfg/cfgUtil/dot11f.frms  //80211帧格式定义
reg_sched_chan_change_cbks_sb()  //Schedule north bound channel change callbacks
    reg_call_chan_change_cbks(psoc, pdev, load->ch_avoid_ind,&load->avoid_info);

reg_sched_chan_change_cbks_nb()  //Schedule south bound channel change callbacks
    reg_call_chan_change_cbks(psoc, pdev, load->ch_avoid_ind,&load->avoid_info);

wpa_supplicant_8/src/drivers/nl80211_copy.h  //supported nl80211 commands
wpa_supplicant_8/wpa_supplicant/wpa_client_include/libwpa_client/qca-vendor.h //QCA nl80211 vendor command

qcom/wlan/qcwcn/wpa_supplicant_8_lib/driver_cmd_nl80211.c
android/external/wpa_supplicant_8/src/drivers/driver_nl80211.c
android/vendor/qcom/opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_cfg80211.c // /* vendor specific events */

/*************/
*****扫描****
*************/
packages/modules/Wifi/service/java/com/android/server/wifi/scanner/WificondScannerImpl.java
    startSingleScan() -> mWifiNative.scan
packages/modules/Wifi/service/java/com/android/server/wifi/WifiNative.java
    mWifiCondManager.startScan2
frameworks/base/wifi/java/src/android/net/wifi/nl80211/WifiNl80211Manager.java
    scannerImpl.scanRequest(settings);
android/system/connectivity/wificond/scanning/scanner_impl.cpp
    scan_utils_->Scan(...)
android/system/connectivity/wificond/scanning/scan_utils.cpp
    netlink_manager_->SendMessageAndGetAckOrError(trigger_scan...)
android/system/connectivity/wificond/net/netlink_manager.cpp
    SendMessageAndGetSingleResponseOrError(packet, &response)
kernel_platform/msm-kernel/net/wireless/nl80211.c
    .cmd = NL80211_CMD_TRIGGER_SCAN,
    .doit = nl80211_trigger_scan, ->  cfg80211_scan(rdev) && nl80211_send_scan_start(rdev, wdev) -> rdev_scan(rdev, request) ->rdev->ops->scan(&rdev->wiphy, request) //发给rdev,调用回调 cfg80211_ops->scan 处理
    
vendor/qcom/opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_cfg80211.c
    cfg80211_ops wlan_hdd_cfg80211_ops = {.scan = wlan_hdd_cfg80211_scan,..}
     wlan_hdd_cfg80211_scan

vendor/qcom/opensource/wlan/qcacld-3.0/core/hdd/src/wlan_hdd_scan.c
     __wlan_hdd_cfg80211_scan(wiphy, request, NL_SCAN) 
        -> wlan_cfg80211_scan(vdev, request, &params);
            wlan_schedule_scan_start_request(pdev, request,...)
                 ucfg_scan_start(scan_start_req);

qcom/opensource/wlan/qca-wifi-host-cmn/os_if/linux/scan/src/wlan_cfg80211_scan.c



qcom/opensource/wlan/qca-wifi-host-cmn/umac/scan/dispatcher/src/wlan_scan_api.c
    wlan_scan_start(struct scan_start_request *req)
        ->msg.callback = scm_scan_start_req;
    
com/opensource/wlan/qca-wifi-host-cmn/umac/scan/core/src/wlan_scan_manager.c  //这里加入到序列化队列，等待序列执行
    scm_scan_start_req
        cmd.cmd_cb = scm_scan_serialize_callback;
            -> scm_activate_scan_request(req)
                ->tgt_scan_start(req);
   
qcom/opensource/wlan/qca-wifi-host-cmn/umac/scan/dispatcher/src/wlan_scan_tgt_api.c
    scan_ops->scan_start(pdev, req); //scan->scan_start = target_if_scan_start
    
qcom/opensource/wlan/qca-wifi-host-cmn/target_if/scan/src/target_if_scan.c
     target_if_scan_start->wmi_unified_scan_start_cmd_send(pdev_wmi_handle, &req->scan_req);
        ->wmi_handle->ops->send_scan_start_cmd

qcom/opensource/wlan/qca-wifi-host-cmn/wmi/src/wmi_unified_tlv.c
    send_scan_start_cmd_tlv -> wmi_unified_cmd_send(wmi_handle, wmi_buf,..)

qcom/opensource/wlan/qca-wifi-host-cmn/wmi/src/wmi_unified.c
    wmi_unified_cmd_send_fl(wmi_unified_t wmi_handle...)
        ->wmi_htc_send_pkt(wmi_handle, pkt, func, line)
            ->htc_send_pkt(wmi_handle->htc_handle, pkt);

qcom/opensource/wlan/qca-wifi-host-cmn/htc/htc_send.c
     __htc_send_pkt(htc_handle, htc_packet);
        ->htc_issue_packets(...)
            ->qdf_nbuf_map(target->osdev,GET_HTC_PACKET_NET_BUF_CONTEXT(pPacket),QDF_DMA_TO_DEVICE);  //DMA
            -> hif_send_head(...)
         
        
lim_message_processor() - Process messages from LIM.
lim_process_mlm_rsp_messages() - processes various MLM response (CNF/IND)

cds_register_all_modules(...) //Register message queues in given order, QDF_MODULE_ID_PE, QDF_MODULE_ID_SME, QDF_MODULE_ID_SCAN...

wlan_schedule_scan_start_request() - Schedule scan start request

wma_mc_process_msg() - process wma messages and call appropriate function.
rrm_process_radio_measurement_request - Process rrm request
wma_data_tx_ack_work_handler() - process data tx ack
ol_tx_pkt_capture_tx_completion_process()- process tx packets
ol_rx_frag_indication_handler（） -Process incoming fragments

tdls_process_rx_frame() - process tdls rx frames
lim_process_auth_frame_no_session - Pass the received Auth frame
lim_handle80211_frames() - process 802.11 frames


//nl80211 -> cfg80211-> cfg80211_registered_device
//这个cfg80211_registered_device 是在wiphy = wiphy_new(...) - wiphy_new_nm(...)中初始化的
kernel_platform/common/net/netlink/genetlink.c
    genl_family_rcv_msg_doit(family, skb, nlh,...) -> ops->doit(skb, &info);
    
KERNEL.PLATFORM.2.0/kernel_platform/common/net/wireless/nl80211.c
     nl80211_trigger_scan(struct sk_buff *skb, struct genl_info *info) -> cfg80211_scan(rdev) -> rdev_scan(rdev, request) -> rdev->ops->scan(&rdev->wiphy, request) ->wlan_hdd_cfg80211_scan  ( wlan_hdd_cfg80211_ops 中的scan指针)
     
//rx interrupter
/opensource/wlan/qca-wifi-host-cmn/hif/src/ce/ce_tasklet.c
        tasklet_init(&hif_ce_state->tasklets[i].intr_tq,ce_tasklet,...)
/opensource/wlan/qca-wifi-host-cmn/hif/src/ce/ce_service.c
        ce_tasklet -> ce_per_engine_service(struct hif_softc *scn, unsigned int CE_id)-> CE_state->service(scn, CE_id) //Guts of interrupt handler for per-engine interrupts on a particular CE., (CE_state->service = ce_engine_service_reg;)

pensource/wlan/qca-wifi-host-cmn/hif/src/usb/hif_usb.c
       hif_start(struct hif_opaque_softc *scn) -> usb_hif_prestart_recv_pipes(device);
       hif_usb_bus_resume -> usb_hif_start_recv_pipes(device) ->usb_hif_post_recv_transfers(pipe, buf_len)/usb_hif_post_recv_bundle_transfers(pipe,...)
            ->usb_fill_bulk_urb(urb,recv_pipe->device->udev,.,usb_hif_usb_recv_complete,.) -> usb_submit_urb(urb, GFP_ATOMIC)  //URB提交给核心,核心进一步传递给控制器,将数据转化成TD(Transfer Descripter) 挂到对应的QH(Queue Head,端点的传输队列),控制器读取 QH 和 TD,开始执行 DMA 数据传输
       
wlan/qca-wifi-host-cmn/hif/src/sdio/hif_sdio_dev.c
     hif_dev_process_pending_irqs -> hif_dev_recv_message_pending_handler -> hif_dev_recv_packet(pdev, pkt,..)
        ->rxCompletion = pdev->hif_callbacks.rxCompletionHandler;
                ->htc_rx_completion_handler  (qca-wifi-host-cmn/htc/htc_recv.c)
                    ->do_recv_completion_pkt(pEndpoint, pPacket) ->EpCallbacks.EpRecv  (connect.EpCallbacks.EpRecv = htt_t2h_msg_handler; in  htt_htc_attach)
                        ->htt_t2h_msg_handler; //target to host Msg/event  handler
                            ->ol_rx_indication_handler(pdev->txrx_pdev,..) (dp/txrx/ol_rx.c)
                                
```      
----------------------------------------------------------------------------------------------------------------------
HT Capabilities IE             描述设备的高吞吐量（HT）功能，适用于 802.11n 网络。        IEEE 802.11n            ----
----------------------------------------------------------------------------------------------------------------------
VHT Capabilities IE            描述设备的甚高吞吐量（VHT）功能，适用于 802.11ac 网络。    IEEE 802.11ac           ----
----------------------------------------------------------------------------------------------------------------------
Operating Mode Notification IE 动态通知客户端当前的操作模式（如信道宽度、空间流数量等）。 IEEE 802.11ac, 802.11ax ----
----------------------------------------------------------------------------------------------------------------------
Extended Capabilities IE       提供设备的扩展功能信息，例如频段支持、DFS、QoS 等。        IEEE 802.11k/v/r        ----
----------------------------------------------------------------------------------------------------------------------
Multi-Band Operation IE        描述设备的多频段操作能力，帮助客户端选择更优的频段。       IEEE 802.11k/v/r        ----
----------------------------------------------------------------------------------------------------------------------

https://www.wi-fi.org/discover-wi-fi/specifications //Wifi 协议规格
http://androidref.com    //wifi 通用接口源码可以参考这里
http://aospxref.com     //Android 源码
KERNEL.PLATFORM.2.0/kernel_platform/qcom/proprietary/devicetree/qcom/bengal.dtsi  //bengal 平台 device tree ，compatible = "qcom,pil-tz-generic";
    
vendor/qcom/opensource/wlan/utils/sigma-dut/ap.c  /*自动化测试框架，用于测试 Wi-Fi 设备的功能和性能。*/
vendor/qcom/opensource/wlan/utils/sigma-dut/sigma_dut.c  /*使用说明*/

Wireshark分析特定的Wifi包类型

管理帧过滤（管理帧和其子类型的一些例子）:
    wlan.fc.type == 0 过滤所有类型为管理帧的包。
    wlan.fc.type_subtype == 0x08 用于过滤信标帧。
    wlan.fc.type_subtype == 0x04 用于过滤探测请求。
    wlan.fc.type_subtype == 0x05 用于过滤探测响应。

控制帧过滤（控制帧和其子类型的一些例子）：
    wlan.fc.type == 1 过滤所有类型为控制帧的包。
    wlan.fc.type_subtype == 0x1b 过滤RTS帧。
    wlan.fc.type_subtype == 0x1c 过滤CTS帧。
    wlan.fc.type_subtype == 0x1d 过滤ACK帧。
    wlan.fc.type_subtype == 0x0d && wlan.action.category == 34 FTM Action Frame  被发出，并检查其字段是否包含时间戳同步信息

数据帧过滤（数据帧和其他子类型的一些例子）：
    wlan.fc.type == 2 过滤所有类型为数据帧的包。
    wlan.fc.type_subtype == 0x20 过滤数据帧。

    
https://mcsindex.com/

