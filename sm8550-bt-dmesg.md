```c
kalama:/ # dmesg | grep bt
[  124.282758] ufs_qcom(E) qnoc_crow(E) bwmon(E) qcom_dcvs(E) icc_rpmh(E) ufshcd_crypto_qti(E) mem_buf(E) crypto_qti_common(E) msm_qmp(E) phy_qcom_ufs_qrbtc_sdm845(E) camcc_kalama(E) dcvs_fp(E) icc_bcm_vote
r(E) phy_qcom_ufs_qmp_v4_crow(E) mem_buf_msgq(E) sdhci_msm(E) arm_smmu(E) qcom_tsens(E) videocc_kalama(E) qcom_dma_heaps(E) tcsrcc_kalama(E) dispcc_kalama(E) qcom_cpu_vendor_hooks(E) clk_dummy(E) gcc_kalama
(E) dispcc_crow(E) phy_qcom_ufs_qmp_v4_kalama(E) gh_virt_wdt(E) rpmh_regulator(E) gcc_crow(E) clk_rpmh(E) phy_qcom_ufs(E) qcom_aoss(E) bcl_pmic5(E) qcom_rpmh(E) clk_qcom(E) pmu_scmi(E) pinctrl_kalama(E) qco
m_iommu_util(E) msm_rtb(E) qcom_logbuf_vh(E) dcc_v2(E) mem_buf_dev(E) thermal_minidump(E) qrtr(E) gunyah(E) crypto_qti_hwkm(E) pinctrl_crow(E) qcom_wdt_core(E) thermal_pause(E) qcom_dload_mode(E) memory_dum
p_v2(E) pinctrl_msm(E) qcom_pdc(E) qcom_ipc_logging(E) nvme(E) qcom_pmu_lib(E) sched_walt(E) stub_regulator(E) secure_buffer(E) minidump(E) gdsc_regulator(E)
[  236.435144] btfm_slim_hw_init: PGD Enum Addr: mfr id:217 prod code:221 dev ind:01 ins:00
[  236.435161] btfm_slim_hw_init: chipset soc version:40170200
[  236.435170] btfm_slim_hw_init: chipset is Hamliton, overwriting EA
[  236.435177] btfm_slim_hw_init: PGD Enum Addr: manu id:217 prod code:220 dev idx:01 instance:00
[  236.435186] btfm_slim_hw_init: IFD Enum Addr: manu id:217 prod code:220 dev idx:00 instance:00
[  236.435195] btfm_slim_get_logical_addr:
[  236.488968] btfm_slim_get_logical_addr:
[  236.509365] btfm_slim_alloc_port: chipset soc version:40170200
[  236.511065] btfm_slim_slave_hw_init: read (1) reg 0x2
[  236.699304] btfm_slim_dai_prepare: dai->name: btfm_bt_sco_a2dp_slim_rx, dai->id: 2, dai->rate: 44100 direction: 0
[  236.699342] btfm_slim_write: Write to IFD
[  236.705395] btfm_slim_enable_ch: port: 16, ch: 157
[  236.705421] btfm_slim_enable_ch: chipset soc version:40170200
[  236.712113] btfm_slim_enable_ch: btfm_num_ports_open: 1
[  240.989752] btfm_slim_disable_ch: port:16
[  240.989765] btfm_slim_disable_ch: disconnecting the ports, removing the channel
[  240.998754] btfm_slim_write: Write to IFD
[  240.998945] btfm_slim_disable_ch: ch->dai.sconfig.chs is already NULL
[  241.006822] btfm_slim_disable_ch: btfm_num_ports_open: 0
[  241.006833] btfm_slim_disable_ch: SB reset needed after all ports disabled, sleeping
[  241.209414] btfm_slim_hw_deinit:
[  247.949325] btfm_slim_hw_init: PGD Enum Addr: mfr id:217 prod code:220 dev ind:01 ins:00
[  247.949341] btfm_slim_hw_init: chipset soc version:40170200
[  247.949349] btfm_slim_hw_init: chipset is Hamliton, overwriting EA
[  247.949357] btfm_slim_hw_init: PGD Enum Addr: manu id:217 prod code:220 dev idx:01 instance:00
[  247.949511] btfm_slim_hw_init: IFD Enum Addr: manu id:217 prod code:220 dev idx:00 instance:00
[  247.949521] btfm_slim_get_logical_addr:
[  248.001982] btfm_slim_get_logical_addr:
[  248.017910] btfm_slim_alloc_port: chipset soc version:40170200
[  248.018669] btfm_slim_slave_hw_init: read (1) reg 0x2
[  248.186243] btfm_slim_dai_prepare: dai->name: btfm_bt_sco_a2dp_slim_rx, dai->id: 2, dai->rate: 44100 direction: 0
[  248.186275] btfm_slim_write: Write to IFD
[  248.189261] btfm_slim_enable_ch: port: 16, ch: 157
[  248.189278] btfm_slim_enable_ch: chipset soc version:40170200
[  248.194103] btfm_slim_enable_ch: btfm_num_ports_open: 1
[  250.761745] btfm_slim_disable_ch: port:16
[  250.761768] btfm_slim_disable_ch: disconnecting the ports, removing the channel
[  250.769629] btfm_slim_write: Write to IFD
[  250.769919] btfm_slim_disable_ch: ch->dai.sconfig.chs is already NULL
[  250.777693] btfm_slim_disable_ch: btfm_num_ports_open: 0
[  250.777713] btfm_slim_disable_ch: SB reset needed after all ports disabled, sleeping
[  250.981270] btfm_slim_hw_deinit:
[  261.903823] btfm_slim_hw_init: PGD Enum Addr: mfr id:217 prod code:220 dev ind:01 ins:00
[  261.903848] btfm_slim_hw_init: chipset soc version:40170200
[  261.903858] btfm_slim_hw_init: chipset is Hamliton, overwriting EA
[  261.903866] btfm_slim_hw_init: PGD Enum Addr: manu id:217 prod code:220 dev idx:01 instance:00
[  261.903888] btfm_slim_hw_init: IFD Enum Addr: manu id:217 prod code:220 dev idx:00 instance:00
[  261.903897] btfm_slim_get_logical_addr:
[  261.957308] btfm_slim_get_logical_addr:
[  261.972959] btfm_slim_alloc_port: chipset soc version:40170200
[  261.973808] btfm_slim_slave_hw_init: read (1) reg 0x2
[  262.118694] btfm_slim_dai_prepare: dai->name: btfm_bt_sco_a2dp_slim_rx, dai->id: 2, dai->rate: 44100 direction: 0
[  262.118726] btfm_slim_write: Write to IFD
[  262.122979] btfm_slim_enable_ch: port: 16, ch: 157
[  262.122999] btfm_slim_enable_ch: chipset soc version:40170200
[  262.125843] btfm_slim_enable_ch: btfm_num_ports_open: 1
[  358.904454] btfm_slim_disable_ch: port:16
[  358.904479] btfm_slim_disable_ch: disconnecting the ports, removing the channel
[  358.909785] btfm_slim_write: Write to IFD
[  358.909967] btfm_slim_disable_ch: ch->dai.sconfig.chs is already NULL
[  358.917429] btfm_slim_disable_ch: btfm_num_ports_open: 0
[  358.917441] btfm_slim_disable_ch: SB reset needed after all ports disabled, sleeping
[  359.121652] btfm_slim_hw_deinit:
[  430.159729] btfm_slim_hw_init: PGD Enum Addr: mfr id:217 prod code:220 dev ind:01 ins:00
[  430.159746] btfm_slim_hw_init: chipset soc version:40170200
[  430.159753] btfm_slim_hw_init: chipset is Hamliton, overwriting EA
[  430.159759] btfm_slim_hw_init: PGD Enum Addr: manu id:217 prod code:220 dev idx:01 instance:00
[  430.159766] btfm_slim_hw_init: IFD Enum Addr: manu id:217 prod code:220 dev idx:00 instance:00
[  430.159774] btfm_slim_get_logical_addr:
[  430.212511] btfm_slim_get_logical_addr:
[  430.228669] btfm_slim_alloc_port: chipset soc version:40170200
[  430.231371] btfm_slim_slave_hw_init: read (1) reg 0x2
[  430.375794] btfm_slim_dai_prepare: dai->name: btfm_bt_sco_a2dp_slim_rx, dai->id: 2, dai->rate: 44100 direction: 0
[  430.375829] btfm_slim_write: Write to IFD
[  430.379389] btfm_slim_enable_ch: port: 16, ch: 157
[  430.379404] btfm_slim_enable_ch: chipset soc version:40170200
[  430.383301] btfm_slim_enable_ch: btfm_num_ports_open: 1
[  434.834375] btfm_slim_disable_ch: port:16
[  434.834394] btfm_slim_disable_ch: disconnecting the ports, removing the channel
[  434.843202] btfm_slim_write: Write to IFD
[  434.843534] btfm_slim_disable_ch: ch->dai.sconfig.chs is already NULL
[  434.851036] btfm_slim_disable_ch: btfm_num_ports_open: 0
[  434.851053] btfm_slim_disable_ch: SB reset needed after all ports disabled, sleeping
[  435.053406] btfm_slim_hw_deinit:
[  439.908537] btfm_slim_hw_init: PGD Enum Addr: mfr id:217 prod code:220 dev ind:01 ins:00
[  439.908558] btfm_slim_hw_init: chipset soc version:40170200
[  439.908565] btfm_slim_hw_init: chipset is Hamliton, overwriting EA
[  439.908570] btfm_slim_hw_init: PGD Enum Addr: manu id:217 prod code:220 dev idx:01 instance:00
[  439.908578] btfm_slim_hw_init: IFD Enum Addr: manu id:217 prod code:220 dev idx:00 instance:00
[  439.908585] btfm_slim_get_logical_addr:
[  439.962030] btfm_slim_get_logical_addr:
[  439.979342] btfm_slim_alloc_port: chipset soc version:40170200
[  439.979977] btfm_slim_slave_hw_init: read (1) reg 0x2
[  440.126091] btfm_slim_dai_prepare: dai->name: btfm_bt_sco_a2dp_slim_rx, dai->id: 2, dai->rate: 44100 direction: 0
[  440.126119] btfm_slim_write: Write to IFD
[  440.129566] btfm_slim_enable_ch: port: 16, ch: 157
[  440.129582] btfm_slim_enable_ch: chipset soc version:40170200
[  440.133309] btfm_slim_enable_ch: btfm_num_ports_open: 1
[  546.868478] btfm_slim_disable_ch: port:16
[  546.868487] btfm_slim_disable_ch: disconnecting the ports, removing the channel
[  546.877512] btfm_slim_write: Write to IFD
[  546.877733] btfm_slim_disable_ch: ch->dai.sconfig.chs is already NULL
[  546.885223] btfm_slim_disable_ch: btfm_num_ports_open: 0
[  546.885228] btfm_slim_disable_ch: SB reset needed after all ports disabled, sleeping
[  547.089107] btfm_slim_hw_deinit:
```
```c

```