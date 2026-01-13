```
# dmesg | grep tty*
[    0.000000] Kernel command line: init=/init console=ttyS0,921600 no_console_suspend earlycon=aml-uart,0xfe07a000 ramoops.pstore_en=1 ramoops.record_size=0x8000 ramoops.console_size=0x4000 loop.max_part=4 scramble_reg=0xfe02e030 rootfstype=ramfs otg_device=1 logo=osd0,loaded,0x00300000 vout=1080p60hz,enable panel_type=rgb_0 frac_rate_policy=1 osd_reverse=0 video_reverse=0 irq_check_en=0 androidboot.selinux=enforcing androidboot.firstboot=1 jtag=disable androidboot.bootloader=01.01.240814.132335 androidboot.hardware=amlogic androidboot.serialno=ap2223c291cd6645287cb androidboot.wificountrycode=US panel_type=rgb_0 androidboot.force_normal_boot=1 reboot_mode=cold_boot
[    0.000000] srcu_init: Setting srcu_struct sizes based on contention.
[    0.001421] RCU Tasks: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.001470] RCU Tasks Rude: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.001523] RCU Tasks Trace: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.031256] Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.106032] fe07a000.serial: ttyS0 at MMIO 0xfe07a000 (irq = 18, base_baud = 1500000) is a meson_uart
[    0.106077] console [ttyS0] enabled
[    0.424894] fe078000.serial: ttyS1 at MMIO 0xfe078000 (irq = 21, base_baud = 1500000) is a meson_uart
[    0.704605] attach success!
[    0.783676] create amvideo_poll attribute (null) fail
[    0.851594] xhci-hcd-meson xhci-hcd-meson.0.auto: Resetting HCD
[    0.851660] xhci-hcd-meson xhci-hcd-meson.0.auto: // Setting Max device slots reg = 0x20.
[    0.851717] xhci-hcd-meson xhci-hcd-meson.0.auto: // Setting command ring address to 0x0000000001072001
[    0.867740] xhci-hcd-meson xhci-hcd-meson.1.auto: Resetting HCD
[    0.867802] xhci-hcd-meson xhci-hcd-meson.1.auto: // Setting Max device slots reg = 0x20.
[    0.867856] xhci-hcd-meson xhci-hcd-meson.1.auto: // Setting command ring address to 0x0000000007eee001
[    1.450934] meson-rtc fe08e600.rtc: setting system clock to 1970-01-01T00:00:00 UTC (0)
[    1.527167] aml_cust_setting
[    1.665136] snd_tdm fe330000.audiobus:tdm@0: Error applying setting, reverse things back
[    1.829476] tl1_acodec fe01a000.acodec: ASoC: source widget Left DAC overwritten
[    4.225303] <aml_driv_attach> 1372:enter Here
[    4.227500] <running> aml_driv_attach 1397 insmod country: WW
[    4.232207] <running> aml_driv_attach 1487  drv_priv->drv_ratectrl_size = 0
[    4.236173] <wifi_mac_cap_attach> 1742:<running>
[    4.244354] <eth%d> wifi_mac_sta_vattach wnet_vif->vm_mainsta= 0000000000000000
[    4.248720] vm_p2p_attach ++
[    4.254699] <wifi_mac_mode_vattach_ex> 4231:wnet_vif->vm_mac_mode=14
[    4.264562] <eth%d> wifi_mac_sta_vattach wnet_vif->vm_mainsta= 0000000000000000
[    4.268962] vm_p2p_attach ++
[    4.274909] <wifi_mac_mode_vattach_ex> 4231:wnet_vif->vm_mac_mode=14
```
```
# dmesg | grep bt*
[    0.000000] Linux version 6.6.18-g4992358b91bd (ls@ls-VirtualBox) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 10.2.1 20201103, GNU ld (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 2.35.1.20201028) #1 SMP PREEMPT Wed Aug 14 13:02:46 CST 2024
[    0.000000] KASLR enabled
[    0.000000] [Firmware Bug]: Kernel image misaligned at boot, please fix your bootloader!
[    0.000000] Reserved memory: failed to reserve memory for node 'linux,meson-fb': base 0x000000003f000000, size 0 MiB
[    0.000000] 0x000000003d800000..0x000000003f7fffff (32768 KiB) map reusable linux,ion-dev
[    0.000000] 0x000000003c800000..0x000000003d7fffff (16384 KiB) map reusable linux,codec_mm_cma
[    0.000000] 0x000000003f800000..0x000000003f7fffff (0 KiB) map non-reusable linux,codec_mm_reserved
[    0.000000] 0x0000000004f00000..0x0000000004ffffff (1024 KiB) map non-reusable linux,iotrace
[    0.000000] 0x0000000005000000..0x0000000005bfffff (12288 KiB) nomap non-reusable linux,secmon
[    0.000000] 0x0000000005c00000..0x0000000005cfffff (1024 KiB) map non-reusable ramoops@7400000
[    0.000000] node linux,meson-fb compatible matching fail
[    0.000000] Movable zone start for each node
[    0.000000]   node   0: [mem 0x0000000005000000-0x0000000005bfffff]
[    0.000000] probing for conduit method from DT.
[    0.000000] Embedded 29 pages/cpu s79336 r8192 d31256 u118784
[    0.000000] kernel page table isolation forced ON by KASLR
[    0.000000] detected: Kernel page table isolation (KPTI)
[    0.000000] applying boot alternatives
[    0.000000] Kernel command line: init=/init console=ttyS0,921600 no_console_suspend earlycon=aml-uart,0xfe07a000 ramoops.pstore_en=1 ramoops.record_size=0x8000 ramoops.console_size=0x4000 loop.max_part=4 scramble_reg=0xfe02e030 rootfstype=ramfs otg_device=1 logo=osd0,loaded,0x00300000 vout=1080p60hz,enable panel_type=rgb_0 frac_rate_policy=1 osd_reverse=0 video_reverse=0 irq_check_en=0 androidboot.selinux=enforcing androidboot.firstboot=1 jtag=disable androidboot.bootloader=01.01.240814.132335 androidboot.hardware=amlogic androidboot.serialno=ap2223c291cd6645287cb androidboot.wificountrycode=US panel_type=rgb_0 androidboot.force_normal_boot=1 reboot_mode=cold_boot
                root=/dev/system rootfstype=squashfs init=/sbin/init kernel_version=upstream androidboot.verifiedbootstate=green
[    0.000000] Unknown kernel command line parameters "scramble_reg=0xfe02e030 otg_device=1 logo=osd0,loaded,0x00300000 vout=1080p60hz,enable panel_type=rgb_0 frac_rate_policy=1 osd_reverse=0 video_reverse=0 irq_check_en=0 jtag=disable reboot_mode=cold_boot kernel_version=upstream", will be passed to user space.
[    0.000000] Dentry cache hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.000000] Inode-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 258048
[    0.000000] page_trace_pre_work, trace buffer:ffffff803aa00000, size:200000, end:ffffff803ac00000, module: ffffffc000000000
[    0.000000] SWIOTLB bounce buffer size adjusted to 1MB
[    0.000000]        .bss : 0xffffffea8199f008 - 0xffffffea81a24a78   (   535 KB) 0x319f008
[    0.000000] Memory: 919268K/1048576K available (14784K kernel code, 2364K rwdata, 3588K rodata, 4864K init, 534K bss, 71964K reserved, 57344K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] trace event string verifier disabled
[    0.000000] Preemptible hierarchical RCU implementation.
[    0.000000]  RCU event tracing is enabled.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000]  Rude variant of Tasks RCU enabled.
[    0.000000]  Tracing variant of Tasks RCU enabled.
[    0.000000] GIC: GICv2 detected, but range too small and irqchip.gicv2_force_probe not set
[    0.000000] srcu_init: Setting srcu_struct sizes based on contention.
[    0.000000] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000288] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
[    0.000350] initializing lsm=capability,integrity
[    0.000406] Mount-cache hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.000414] Mountpoint-cache hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.000944] Unable to detect cache hierarchy for CPU 0
[    0.001421] RCU Tasks: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.001470] RCU Tasks Rude: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.001523] RCU Tasks Trace: Setting shift to 2 and lim to 1 rcu_task_cb_adjust=1.
[    0.005264] detected: 32-bit EL0 Support
[    0.014267] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.014393] initialized pinctrl subsystem
[    0.016246] found 6 breakpoint and 4 watchpoint registers.
[    0.017191] console [ramoops-1] enabled
[    0.017574] Registered ramoops as persistent store backend
[    0.029406] 2G module region forced by RANDOMIZE_MODULE_REGION_FULL
[    0.030950] SCSI subsystem initialized
[    0.031064] usbcore: registered new interface driver usbfs
[    0.031092] usbcore: registered new interface driver hub
[    0.031121] usbcore: registered new device driver usb
[    0.031484] SCMI protocol bus registered
[    0.057115] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.057784] tcp_listen_portaddr_hash hash table entries: 512 (order: 1, 8192 bytes, linear)
[    0.057805] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.057820] TCP established hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.057900] TCP bind hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    0.058049] Hash tables configured (established 8192 bind 8192)
[    0.058143] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.058165] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.059054] PCI: CLS 0 bytes, default 64
[    0.065900] workingset: timestamp_bits=46 max_order=18 bucket_order=0
[    0.085144] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    0.085160] io scheduler kyber registered
[    0.085188] io scheduler bfq registered
[    0.092761] brd: module loaded
[    0.097908] usbcore: registered new interface driver asix
[    0.097939] usbcore: registered new interface driver ax88179_178a
[    0.097971] usbcore: registered new interface driver cdc_ether
[    0.097999] usbcore: registered new interface driver net1080
[    0.098030] usbcore: registered new interface driver rndis_host
[    0.098057] usbcore: registered new interface driver cdc_subset
[    0.098085] usbcore: registered new interface driver zaurus
[    0.098122] usbcore: registered new interface driver cdc_ncm
[    0.098150] usbcore: registered new interface driver r8153_ecm
[    0.098355] usbcore: registered new interface driver uas
[    0.098385] usbcore: registered new interface driver usb-storage
[    0.100670] scmi_protocol scmi_dev.1: Enabled polling mode TX channel - prot_id:16
[    0.100951] arm-scmi firmware:scmi: SCMI Notifications - Core Enabled.
[    0.101894] usbcore: registered new interface driver usbhid
[    0.101907] usbhid: USB HID core driver
[    0.102484] enabled with armv8_pmuv3 PMU driver, 7 counters available
[    0.103016] Hard watchdog permanently disabled
[    0.104884] Mobile IPv6
[    0.106032] fe07a000.serial: ttyS0 at MMIO 0xfe07a000 (irq = 18, base_baud = 1500000) is a meson_uart
[    0.106077] console [ttyS0] enabled
[    0.276327] fiq_phy_addr:50f8000, fiq_buf_size: 1000, fiq_virt_addr:ffffffc08004d000
[    0.309251] reserve_mem_size:0xb00000
[    0.309307] share in base: 0xffffffc0801c1000, share out base: 0xffffffc08005d000
[    0.310240] phy_in_base: 0x50f9000, phy_out_base: 0x50ff000
[    0.334035] Loading compiled-in X.509 certificates for regulatory database
[    0.338563] Loaded X.509 cert 'wens: 61c038651aabdcf94bd0ac7ff06c7248db18c600'
[    0.339398] Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    0.339860] clk: Disabling unused clocks
[    0.341172] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    0.342122] failed to load regulatory.db
[    0.368855]     scramble_reg=0xfe02e030
[    0.368862]     vout=1080p60hz,enable
[    0.368865]     panel_type=rgb_0
[    0.368877]     jtag=disable
[    0.368879]     reboot_mode=cold_boot
[    0.424894] fe078000.serial: ttyS1 at MMIO 0xfe078000 (irq = 21, base_baud = 1500000) is a meson_uart
[    0.429429] meson_mbox_fifo fe006000.mbox_fifo: set mbox irq_nums to default value
[    0.450635] build info: 2024.08.14-13.01.17, common_drivers:  6.6.18
[    0.452032] serial = 400b010100000000cb875264d61c293c
[    0.466203] fail to obtain phy addr of shared mem
[    0.551170] probing for conduit method.
[    0.559293] scramble_reg=fe02e030
[    0.577634] meson-gxbb-wdt fe002100.watchdog: pretimeout is enabled
[    0.577915] meson-gxbb-wdt fe002100.watchdog: feeding watchdog mode: [kernel]
[    0.621617] cmd-best-c:18, cmd-best-size:34
[    0.694576] mmcblk0: mmc0:0001 8GTF4R 7.28 GiB
[    0.696504]  mmcblk0: p1 p2 p3 p4 p5 p6 p7 p8
[    0.697791] mmcblk0boot0: mmc0:0001 8GTF4R 4.00 MiB
[    0.699648] mmcblk0boot1: mmc0:0001 8GTF4R 4.00 MiB
[    0.701128] mmcblk0rpmb: mmc0:0001 8GTF4R 512 KiB, chardev (244:0)
[    0.708035] amlmmc_dtb_init: register dtb chardev OK
[    0.749523] enable: 1
[    0.749956] lcd: panel_type: rgb_0
[    0.750508] lcd: panel_type: rgb_0
[    0.752631] vdin_get_video_reverse: bootargs is 0.
[    0.753368] vpp_axis_reverse: bootargs is 0
[    0.755537] vpu: vpu_probe OK
[    0.760584] codec_mm_probe ok
[    0.761930] codec_io_probe success, cpu_type=0x40
[    0.762376] vclk: aml_vclk_probe: find mode: 1
[    0.762684] vclk: aml_vclk_probe OK
[    0.763967] canvas_probe ok, reg=fe030048, size=2000 base =ffffffc0803d0048
[    0.768179] register osd enable status func
[    0.768228] aml_media: osd_probe using cma memory
[    0.776707] aml_media: osd probe OK
[    0.779171] amlogic_heap_secure_dma_buf_init: heap-secure not added in dts.
[    0.783676] create amvideo_poll attribute (null) fail
[    0.784736] amdolby_vision_init:module init
[    0.795180] [viuin..]viuin_probe probe ok.
[    0.798494] secure dmaheap:enter amlogic_system_secure_dma_buf_init
[    0.799210] codecmm dmaheap:enter amlogic_codec_mm_dma_buf_init
[    0.810837] adc_keypad adc_keypad: Not find mbox channel byidx
[    0.811036] mbox chan is NULL
[    0.832487] ### usb_main_init() start
[    0.832829] call amlogic_new_c2_usb2_v2_driver_init() success
[    0.833008] call amlogic_new_c2_usb3_v2_driver_init() success
[    0.833261] call amlogic_bc_driver_init() success
[    0.833388] call amlogic_new_usb2_v2_driver_init() success
[    0.833509] call amlogic_new_usb3_v2_driver_init() success
[    0.833619] call amlogic_usb2_m31_drv_init() success
[    0.833725] call amlogic_usb3_m31_drv_init() success
[    0.834521] amlogic-crg-drd-usb2 fe03a020.crgphy20: USB2 phy probe:phy_mem:0xfe03a020, iomap phy_base:0xffffffc0802d9020
[    0.835563] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.836376] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.837969] amlogic-crg-drd-usb2 fe03a000.crgphy21: USB2 phy probe:phy_mem:0xfe03a000, iomap phy_base:0xffffffc0803a3000
[    0.839120] amlogic-crg-drd-usb2 fe03a000.crgphy21: phy trim value= 0x0000007f
[    0.840244] call amlogic_crg_drd_usb2_drv_init() success
[    0.840415] amlogic-crg-drd-usb3 fe03a080.crg3phy20: This phy has no usb port
[    0.841026] amlogic-crg-drd-usb3 fe03a080.crg3phy20: USB3 phy probe:phy_mem:0xfe03a080, iomap phy_base:0xffffffc0803b1080
[    0.842567] amlogic-crg-drd-usb3 fe03a080.crg3phy21: This phy has no usb port
[    0.843527] amlogic-crg-drd-usb3 fe03a080.crg3phy21: USB3 phy probe:phy_mem:0xfe03a080, iomap phy_base:0xffffffc0803c1080
[    0.845194] call amlogic_crg_drd_usb3_drv_init() success
[    0.845601] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.846061] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.847991] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.848356] amlogic-crg-drd-usb2 fe03a020.crgphy20: phy trim value= 0x0000007f
[    0.850360] xhci-hcd-meson xhci-hcd-meson.0.auto: new USB bus registered, assigned bus number 1
[    0.851607] xhci-hcd-meson xhci-hcd-meson.0.auto: Wait for controller to be ready for doorbell rings
[    0.851617] xhci-hcd-meson xhci-hcd-meson.0.auto: Enabling 32-bit DMA addresses.
[    0.851680] xhci-hcd-meson xhci-hcd-meson.0.auto: // Device context base array address = 0x0x0000000008463000 (DMA), 0000000048b85485 (virt)
[    0.851705] xhci-hcd-meson xhci-hcd-meson.0.auto: Allocated command ring at 0000000030085eb5
[    0.851724] xhci-hcd-meson xhci-hcd-meson.0.auto: // Doorbell array is located at offset 0x1c00 from cap regs base addr
[    0.851749] xhci-hcd-meson xhci-hcd-meson.0.auto: // Write event ring dequeue pointer, preserving EHB bit
[    0.851756] xhci-hcd-meson xhci-hcd-meson.0.auto: Allocating 0 scratchpad buffers
[    0.851768] xhci-hcd-meson xhci-hcd-meson.0.auto: Ext Cap 00000000bd69400e, port offset = 1, count = 2, revision = 0x2
[    0.851788] xhci-hcd-meson xhci-hcd-meson.0.auto: USB3 root hub has no ports
[    0.855151] xhci-hcd-meson xhci-hcd-meson.0.auto: Enable interrupts
[    0.855157] xhci-hcd-meson xhci-hcd-meson.0.auto: Enable primary interrupter
[    0.855587] xHCI aml_xhci_add_endpoint called for root hub
[    0.855594] xHCI aml_xhci_check_bandwidth called for root hub
[    0.855700] hub 1-0:1.0: USB hub found
[    0.855748] hub 1-0:1.0: 2 ports detected
[    0.860243] amlogic-crg-otg soc:crg20otg@fe03a000: phy2_mem:0xfe03a000, iomap phy2_base:0xffffffc0803ed000
[    0.861602] amlogic-crg-otg soc:crg20otg@fe03a000: phy3_mem:0xfe03a080, iomap phy3_base:0xffffffc0803f5080
[    0.864010] amlogic-crg-drd-usb2 fe03a000.crgphy21: phy trim value= 0x0000007f
[    0.865174] amlogic-crg-drd-usb2 fe03a000.crgphy21: phy trim value= 0x0000007f
[    0.866502] xhci-hcd-meson xhci-hcd-meson.1.auto: new USB bus registered, assigned bus number 2
[    0.867752] xhci-hcd-meson xhci-hcd-meson.1.auto: Wait for controller to be ready for doorbell rings
[    0.867762] xhci-hcd-meson xhci-hcd-meson.1.auto: Enabling 32-bit DMA addresses.
[    0.867822] xhci-hcd-meson xhci-hcd-meson.1.auto: // Device context base array address = 0x0x0000000007eec000 (DMA), 00000000b7a43a91 (virt)
[    0.867844] xhci-hcd-meson xhci-hcd-meson.1.auto: Allocated command ring at 000000009f9eeb72
[    0.867862] xhci-hcd-meson xhci-hcd-meson.1.auto: // Doorbell array is located at offset 0x1c00 from cap regs base addr
[    0.867885] xhci-hcd-meson xhci-hcd-meson.1.auto: // Write event ring dequeue pointer, preserving EHB bit
[    0.867892] xhci-hcd-meson xhci-hcd-meson.1.auto: Allocating 0 scratchpad buffers
[    0.867921] xhci-hcd-meson xhci-hcd-meson.1.auto: USB3 root hub has no ports
[    0.871288] xhci-hcd-meson xhci-hcd-meson.1.auto: Enable interrupts
[    0.871293] xhci-hcd-meson xhci-hcd-meson.1.auto: Enable primary interrupter
[    0.871763] xHCI aml_xhci_add_endpoint called for root hub
[    0.871769] xHCI aml_xhci_check_bandwidth called for root hub
[    0.871880] hub 2-0:1.0: USB hub found
[    0.871949] hub 2-0:1.0: 1 port detected
[    0.873298] ### usb_main_init() end
[    1.133631] usb usb2: USB disconnect, device number 1
[    1.137259] xHCI aml_xhci_drop_endpoint called for root hub
[    1.137273] xHCI aml_xhci_check_bandwidth called for root hub
[    1.138297] xhci-hcd-meson xhci-hcd-meson.1.auto: Wait for controller to be ready for doorbell rings
[    1.138310] xhci-hcd-meson xhci-hcd-meson.1.auto: // Disabling event ring interrupts
[    1.138711] xhci-hcd-meson xhci-hcd-meson.1.auto: USB bus 2 deregistered
[    1.140639] amlogic-crg-drd-usb2 fe03a000.crgphy21: phy trim value= 0x0000007f
[    1.141271] crg_udc fe320000.crgudc2: disable vbus detect.
[    1.266741] EXT4-fs (mmcblk0p8): recovery complete
[    1.267147] EXT4-fs (mmcblk0p8): mounted filesystem ea1bb23c-3a14-4162-b006-5c0b3fc41b6a r/w with ordered data mode. Quota mode: disabled.
[    1.320446] [wifi_dev_probe] use double channel
[    1.320540] [wifi_dev_probe] buf_level is :0
[    1.321256] [dhd] STATIC-MSG) bcmdhd_init_wlan_mem : 101.10.361.31 (wlan=r892223-20230427-1)
[    1.325488] input_btrcu as /devices/platform/aml_bt/input/input3
[    1.364905] xhci-hcd-meson xhci-hcd-meson.0.auto: aml_xhci_hub_status_data: stopping usb1 port polling
[    1.401429] aml_dvb_extern_init: OK, version: V1.18.
[    1.413350] aml dvb init
[    1.473071] ledring_probe
[    1.474470] aml_ledring: probe of 2-001f failed with error -12
[    1.512997] meson8b-dwmac fdc00000.ethernet: IRQ eth_wake_irq not found
[    1.513296] meson8b-dwmac fdc00000.ethernet: IRQ eth_lpi not found
[    1.514341] meson8b-dwmac fdc00000.ethernet: PTP uses main clock
[    1.515714] meson8b-dwmac fdc00000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    1.516121] meson8b-dwmac fdc00000.ethernet:         DWMAC1000
[    1.516946] meson8b-dwmac fdc00000.ethernet: DMA HW capability register supported
[    1.517980] meson8b-dwmac fdc00000.ethernet: RX Checksum Offload Engine supported
[    1.519052] meson8b-dwmac fdc00000.ethernet: COE Type 2
[    1.519843] meson8b-dwmac fdc00000.ethernet: TX Checksum insertion supported
[    1.520871] meson8b-dwmac fdc00000.ethernet: Wake-Up On Lan supported
[    1.521872] meson8b-dwmac fdc00000.ethernet: Normal descriptors
[    1.522684] meson8b-dwmac fdc00000.ethernet: Ring mode enabled
[    1.523548] meson8b-dwmac fdc00000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    1.524706] meson8b-dwmac fdc00000.ethernet: device MAC address 02:ad:40:01:b6:f0
[    1.527216] cover mc_val as 0x4be0c
[    1.529491] meson8b-dwmac fdc00000.ethernet: Not find mbox channel byidx
[    1.561877] usbcam: usbcam init!
[    1.561955] usbcam: usbcam register class!
[    1.562457] usbcore: registered new interface driver aml_usbcam
[    1.564775] [TEE] E/TC:? 0 ta_open:224 ree system is not ready, ta can not be loaded.
[    1.565228] [TEE] E/LD:  init_elf:453 sys_open_ta_bin(1a658fe8-894e-4403-aea6-5ae691e8a35f)
[    1.581231] tl1_acodec fe01a000.acodec: aml_tl1_acodec_probe
[    1.586575] aml_tl1_acodec_probe over
[    1.598172] tas5707 eq_enable:0, drc_enable:0
[    1.601113] tas5707 eq_enable:0, drc_enable:0
[    1.646755] audio-ddr-manager fe330000.audiobus:ddr_manager: 0, irqs frddr 43
[    1.647148] audio-ddr-manager fe330000.audiobus:ddr_manager: 1, irqs frddr 44
[    1.648181] audio-ddr-manager fe330000.audiobus:ddr_manager: 2, irqs frddr 45
[    1.650046] effect_platform_probe     module:1, lane_mask:1, ch_mask:3
[    1.651334] snd_pdm fe330000.audiobus:pdm: Can't retrieve xtal_clk clock
[    1.651645] snd_pdm fe330000.audiobus:pdm: no clk_src_cd clock for 44k case
[    1.652655] snd_pdm fe330000.audiobus:pdm: supply pdm3v3 not found, using dummy regulator
[    1.655482] snd_spdif fe330000.audiobus:spdif@0: supply spdif3v3 not found, using dummy regulator
[    1.657088] snd_spdif fe330000.audiobus:spdif@0: no clk_src_cd clock for 44k case
[    1.659300] aml_tdm_platform_probe, tdm ID = 0, lane_cnt = 4
[    1.659539] snd_tdm fe330000.audiobus:tdm@0: Can't get clk_src_cd
[    1.660612] meson-a4-pinctrl fe000000.apb4:pinctrl@4000: pin GPIOT_11 already requested by fe050000.spi; cannot claim for fe330000.audiobus:tdm@0
[    1.662185] meson-a4-pinctrl fe000000.apb4:pinctrl@4000: pin-61 (fe330000.audiobus:tdm@0) status -22
[    1.663413] meson-a4-pinctrl fe000000.apb4:pinctrl@4000: could not request pin 61 (GPIOT_11) from group tdm_fs2_t11  on device pinctrl-meson
[    1.665136] snd_tdm fe330000.audiobus:tdm@0: Error applying setting, reverse things back
[    1.666881] snd_tdm fe330000.audiobus:tdm@0: supply tdm3v3 not found, using dummy regulator
[    1.668618] aml_tdm_platform_probe, tdm ID = 1, lane_cnt = 8
[    1.668969] snd_tdm fe330000.audiobus:tdm@1: Can't get clk_src_cd
[    1.670063] TDM id 1 output clk enable:1
[    1.670550] snd_tdm fe330000.audiobus:tdm@1: supply tdm3v3 not found, using dummy regulator
[    1.672054] aml_tdm_platform_probe, tdm ID = 2, lane_cnt = 8
[    1.672501] snd_tdm fe330000.audiobus:tdm@2: Can't get clk_src_cd
[    1.673547] snd_tdm fe330000.audiobus:tdm@2: supply tdm3v3 not found, using dummy regulator
[    1.675926] aud_sram_iomap_probe reg:f7000000, size:100000
[    1.676607] vad_keypad as /devices/platform/soc/fe330000.audiobus/fe330000.audiobus:vad/input/input5
[    1.829316] tl1_acodec_probe
               loopback_dai_set_sysclk, 0, 12288000, 0
[    1.831340] asoc loopback_dai_set_fmt, 0x1010, 00000000629fbdf3
[    1.832963] tl1_acodec_set_toacodec, is_bclk_cap_inv true
[    1.833818] tl1_acodec_set_toacodec, is_bclk_o_inv false
[    2.703903] meson8b-dwmac fdc00000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
[    2.740575] AML_BT: going OFF,btpower_evt=0
[    2.766061] meson8b-dwmac fdc00000.ethernet eth0: PHY [mdio_mux-0.1:08] driver [Meson G12A Internal PHY] (irq=40)
[    2.776752] meson8b-dwmac fdc00000.ethernet eth0: No Safety Features support found
[    2.777184] meson8b-dwmac fdc00000.ethernet eth0: PTP not supported by HW
[    2.779075] meson8b-dwmac fdc00000.ethernet eth0: configuring for phy/rmii link mode
[    2.864763] [usb_power_control] Set WiFi power down
[    2.864874] [usb_power_control] Set WiFi power on !
[    3.140318] r: b_s = e, b_sz = 32, f: b_s = 0, b_sz = 20
[    3.146381] [usb_power_control] Set WiFi power on !
[    3.154631] aml_w1_sdio_probe(793): func->num 1 sdio block size=512,
[    3.155495] aml_w1_sdio_probe(803): func->num 1 sdio_func=00000000a12d1eca,
[    3.156510] aml_w1_sdio_probe(810):func_num=1, last func num=7
[    3.157684] aml_w1_sdio_probe(793): func->num 2 sdio block size=512,
[    3.158324] aml_w1_sdio_probe(803): func->num 2 sdio_func=0000000072d8d9e8,
[    3.159343] aml_w1_sdio_probe(810):func_num=2, last func num=7
[    3.160488] aml_w1_sdio_probe(793): func->num 3 sdio block size=512,
[    3.161238] aml_w1_sdio_probe(803): func->num 3 sdio_func=0000000067da514d,
[    3.162167] aml_w1_sdio_probe(810):func_num=3, last func num=7
[    3.163286] aml_w1_sdio_probe(793): func->num 4 sdio block size=512,
[    3.164046] aml_w1_sdio_probe(803): func->num 4 sdio_func=000000008645e5f5,
[    3.165099] aml_w1_sdio_probe(810):func_num=4, last func num=7
[    3.166269] aml_w1_sdio_probe(793): func->num 5 sdio block size=512,
[    3.167034] aml_w1_sdio_probe(803): func->num 5 sdio_func=000000004769c4b5,
[    3.168057] aml_w1_sdio_probe(810):func_num=5, last func num=7
[    3.169374] aml_w1_sdio_probe(793): func->num 6 sdio block size=512,
[    3.170236] aml_w1_sdio_probe(803): func->num 6 sdio_func=0000000064df0b3d,
[    3.171252] aml_w1_sdio_probe(810):func_num=6, last func num=7
[    3.172370] aml_w1_sdio_probe(793): func->num 7 sdio block size=512,
[    3.173092] aml_w1_sdio_probe(803): func->num 7 sdio_func=000000004fc373a7,
[    3.220926] driver version: v1.6.3_20240426-w1-br driver:ea3eb3c912b3467c59ff+419228+423143+406532
[    3.226707] aml_sdio_calibration right, use this config: i:0, j:0, k:0, l:0
[    3.249722] config_pmu_reg power on: before write A12=0x2a2c, A13=0xc0000006, A14=0x1, A15=0x6, A17=0x700, A18=0x1700, A20=0x0, A22=0x704, A24=0x0
[    3.322513] hal_priv->hal_call_back->dev_probe
[    3.325123] bbpll power on -------------->
[    3.327140] bbpll done !
[    3.327168] bbpll  init ok!
[    3.336881] RG_WIFI_CPU_CTRL = 70b0 redata= 10000
[    3.682083] AML_BT: going ON,btpower_evt=0
[    3.960992] [dhd] STATIC-MSG) bcmdhd_mem_prealloc : section 11, size 459776
[    4.096748] [usb_power_control] Set BT power on !
[    4.124986] btHAL->
[    4.125004] BTAML SDIOBT version:v2.0.2_20220112_sdiobt
[    4.125516] btHAL->
[    4.125519] ++++++sdio bt driver insmod start.++++++
[    4.127701] btHAL->
[    4.128660] btHAL->
[    4.129420] btHAL->
[    4.131179] btHAL->
[    4.131186] BT power on: before write A12=0x2a2c, A13=0xc0000006, A14=0x1, A15=0x6, A16=0x0, A17=0x700, A18=0x1700, A20=0x0, A22=0x704
[    4.132648] btHAL->
[    4.164716] btHAL->
[    4.176759] btHAL->
[    4.178241] btHAL->
[    4.178249] BT power on: config_bt_pmu_reg, line=111
[    4.183818] for uart baudrate0x4c4b400
[    4.185161] set uart baudrate, apb_clk=80000000, addr=0x00004c08 data=0x100010ac
[    4.186182] hal_priv->beaconframeaddress  0xa107b8
[    4.188747] btHAL->
[    4.204661] ======>>>>>> wftx_pwrtbl_en = 1
[    4.206026] ======>>>>>> wftx_power_change_disable = 0
[    4.206806] ======>>>>>> initial_gain_change_disable = 0
[    4.207608] ======>>>>>> digital gain = disable min_2g:0x0 max_2g:0x0 min_5g:0x0 max_5g:0x0
[    4.208735] btHAL->
[    4.208821] ======>>>>>>ce_band_pwr_tbl: 0
[    4.213058] calibration parameter: version 1, config 0, freq_offset 6, tssi_2g 223, tssi_5g 226 241 2 6 tx_en 1
[    4.214424] hal_cfg_cali_param:2204, set calibration parameter
[    4.216015] hal_probe(2002) hal_priv->bhalOpen 0x0
[    4.224949] drv_dev_probe(2382) mac_addr set done.MAC_ADDR=40:80:e1:31:1a:98
[    4.235574] wifi_mac_scan_timeout is 00000000153bce84
[    4.237448] [dhd] STATIC-MSG) bcmdhd_mem_prealloc : section 20, size 245760
[    4.245905] vht cap init: sgi 0x1, ldpc 0x1, tx_stbc 0x0, rx_stbc 0x7
[    4.248715] AML INFO:before register vendor cmd!!!
[    4.255453] <wifi_mac_create_vmac> 4071:wnet_vif->vm_mac_mode=14, wnet_vif:00000000bdb0012f
[    4.259860]  phy_set_mac_bssid:wnet_vif_id= 1 bssid=40:80:f1:31:1a:98
[    4.260776] btHAL->
[    4.266110] vht cap init: sgi 0x1, ldpc 0x1, tx_stbc 0x0, rx_stbc 0x7
[    4.268951] AML INFO:before register vendor cmd!!!
[    4.275655] <wifi_mac_create_vmac> 4071:wnet_vif->vm_mac_mode=14, wnet_vif:00000000252b7428
[    4.277415] wifi_mac_rst_bss, wnet_vif->wnet_vif_id= 0
[    4.279208] alloc_sta_node vid:0, sta:00000000c964fb75
[    4.279987] wifi_mac_rst_bss add vm_mainsta:00000000c964fb75
[    4.281414] wifi_mac_rst_bss, wnet_vif->wnet_vif_id= 1
[    4.283983] wifi_mac_rst_bss add vm_mainsta:000000009c238082
[    4.284871] FUNCTION: phy_set_bmfm_info LINE: 1327:group id null
[    4.285719] phy_set_coexist_en:1367, phy_set_coexist_en, enable 1
[    4.288876] aml_sdio_irq_path: b_gpio=1
[    4.291292] aml_sdio_probe-- ret 0
[    4.292888] btHAL->
[    4.293889] config_bt_pmu_reg bt_pmu_status:0x6
[    4.295804] btHAL->
[    4.297290] btHAL->
[    4.298027] btHAL->
[    4.298032] major number:499
[    4.298922] btHAL->
[    4.301089] btHAL->
[    4.301408] btHAL->
[    4.302427] btHAL->
[    4.302430] ------sdio bt driver insmod end.------
[    4.303752] amlbt_sdio_probe RG_AON_A15:0x0
[    4.305189] hal_open(1805) bhalOpen 0x1
[    4.306518] sdio_bt sdio_bt: Init sdio_bt OK!
[    4.309088] phy_interface_enable:1562, vid 0, enable 1
[    4.313804] vm_cfg80211_init_ht_capab(5721)
[    4.313847] vm_cfg80211_init_vht_capab(5679)
[    4.315154] vm_cfg80211_init_ht_capab(5721)
[    4.315815] vm_cfg80211_init_vht_capab(5679)
[    4.316490] <wlan0> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->SCAN
[    4.317700] <running> drv_bcn_init 414
[    4.317986] vm_cfg80211_set_power_mgmt 2767 <wlan0> enabled=0 timeout=-1
[    4.328914] phy_interface_enable:1562, vid 1, enable 1
[    4.330627] vm_cfg80211_init_ht_capab(5721)
[    4.331288] vm_cfg80211_init_vht_capab(5679)
[    4.332653] vm_cfg80211_init_ht_capab(5721)
[    4.333491] vm_cfg80211_init_vht_capab(5679)
[    4.333991] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->SCAN
[    4.334987] <wlan1> wifi_mac_sub_sm 2940  wifi_mac_sub_sm(2941) sm:ap mode, vm_des_nssid:0
[    4.435121] chandef center_freq:2437, hw_value:6 band:0, at vm_cfg80211_start_ap, 4181
[    4.436251] phy_set_preamble_type(286) 0
[    4.437271] FUNCTION: _iv_cfg80211_add_set_beacon LINE: 3804:no vht cap ie found.
[    4.438285] FUNCTION: _iv_cfg80211_add_set_beacon LINE: 3832:no vht op ie found.
[    4.439343] _iv_cfg80211_add_set_beacon vm_mac_mode 7, offset 0, vm_bandwidth:0, center_chan:6
[    4.443604] _iv_cfg80211_add_set_beacon 3931 change ssid
[    4.446632] _iv_cfg80211_add_set_beacon vm_flags=0x100a510, rsn_mcastcipher=0x3 rsn_ucastcipherset=0x8 rsn_keymgmtset=0x4, rsn_caps=0xc
[    4.448291] vm_p2p_update_beacon_app_ie 1122 total_beacon_app_ie_len=0
[    4.449964] _iv_cfg80211_add_set_beacon set_beacon_flag 1, wm_flags_ext:40184001, wm_flags:00042500, sta_vhtcap:00000000
[    4.456540] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->SCAN
[    4.458251] <wlan1> wifi_mac_sub_sm 2936  wifi_mac_sub_sm(2937)wifi_mac_create_ap channel = 6
[    4.464270] alloc_sta_node vid:1, sta:000000002ab020eb
[    4.465038] wifi_mac_create_wifi(473): pri_chan 6, bw 0, chan_cfreq1 6
[    4.466925] wifi_mac_start_bss_ex ori:000000009c238082, add main_sta:000000002ab020eb
[    4.468911] wifi_mac_start_bss_ex, obss:000000009c238082
[    4.640993] <is_connect_need_set_gain> 526:overlapping:0, is_connect_set_gain:0, low_chan:3, up_chan:7, bw:0, center:6
[    4.643273] start bss ok!!! AP CHANNEL:6, BW:0, SSID:amlogic-audio-4080f1311a98, BSSID:40:80:f1:31:1a:98
[    4.645497] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state SCAN->CONNECTED
[    4.646536] wifi_mac_top_sm(3243) wm_running=1, wnet_vif_mode 7 vm_bandwidth:0
[    4.652944] vm_cfg80211_change_bss 3523 <wlan1>
[    4.654492] key is 44:83:e6:63:bc:89:08:63:76:76:a5:d7:29:16:77:19:
[    4.839906] wifi_mac_beacon_alloc_ex 726
[    4.841510] wifi_mac_beacon_init(27)
[    4.843176] wifi_mac_beacon_alloc 699 Put beacon to HW;  wnet_vif_id 1 len 226 Bcn init rate 0x80 flag 0
[    4.845796] <running> drv_set_bcn_start 423
[    5.389205] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state CONNECTED->INIT
[    5.390251] wifi_mac_rst_bss, wnet_vif->wnet_vif_id= 1
[    5.394397] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->INIT
[    5.398046] phy_interface_enable:1562, vid 1, enable 0
[    5.910395] phy_interface_enable:1562, vid 1, enable 1
[    5.912210] vm_cfg80211_init_ht_capab(5721)
[    5.912922] vm_cfg80211_init_vht_capab(5679)
[    5.914235] vm_cfg80211_init_ht_capab(5721)
[    5.914896] vm_cfg80211_init_vht_capab(5679)
[    5.917151] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->SCAN
[    5.918094] <wlan1> wifi_mac_sub_sm 2940  wifi_mac_sub_sm(2941) sm:ap mode, vm_des_nssid:0
[    5.921509] key is 44:83:e6:63:bc:89:08:63:76:76:a5:d7:29:16:77:19:
[    5.926644] chandef center_freq:2437, hw_value:6 band:0, at vm_cfg80211_start_ap, 4181
[    5.927775] phy_set_preamble_type(286) 0
[    5.928765] FUNCTION: _iv_cfg80211_add_set_beacon LINE: 3804:no vht cap ie found.
[    5.929806] FUNCTION: _iv_cfg80211_add_set_beacon LINE: 3832:no vht op ie found.
[    5.930877] _iv_cfg80211_add_set_beacon vm_mac_mode 6, offset 0, vm_bandwidth:0, center_chan:6
[    5.935222] _iv_cfg80211_add_set_beacon 3931 change ssid
[    5.937560] vm_p2p_update_beacon_app_ie 1122 total_beacon_app_ie_len=0
[    5.939210] _iv_cfg80211_add_set_beacon set_beacon_flag 1, wm_flags_ext:40104001, wm_flags:00042500, sta_vhtcap:00000000
[    5.944766] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state INIT->SCAN
[    5.945693] <wlan1> wifi_mac_sub_sm 2936  wifi_mac_sub_sm(2937)wifi_mac_create_ap channel = 6
[    5.948231] alloc_sta_node vid:1, sta:00000000e23063bd
[    5.949032] wifi_mac_create_wifi(473): pri_chan 6, bw 0, chan_cfreq1 6
[    6.141447] wifi_mac_start_bss_ex ori:000000002ab020eb, add main_sta:00000000e23063bd
[    6.142480] wifi_mac_start_bss_ex, obss:000000002ab020eb
[    6.143282] wifi_mac_free_sta sta:000000002ab020eb, new:1
[    6.145286] <is_connect_need_set_gain> 526:overlapping:0, is_connect_set_gain:0, low_chan:3, up_chan:7, bw:0, center:6
[    6.147645] start bss ok!!! AP CHANNEL:6, BW:0, SSID:amlogic-audio-4080f1311a98, BSSID:40:80:f1:31:1a:98
[    6.149856] <wlan1> wifi_mac_sub_sm 2837  wifi_mac_sub_sm state SCAN->CONNECTED
[    6.150909] wifi_mac_top_sm(3243) wm_running=1, wnet_vif_mode 6 vm_bandwidth:0
[    6.188850] vm_cfg80211_change_bss 3523 <wlan1>
[    6.340412] wifi_mac_beacon_alloc_ex 726
[    6.340996] wifi_mac_beacon_init(27)
[    6.341569] wifi_mac_beacon_alloc 699 Put beacon to HW;  wnet_vif_id 1 len 220 Bcn init rate 0x80 flag 0
[    6.342921] <running> drv_set_bcn_start 423
[   11.230386] nsta_free free 000000002ab020eb
[   62.428806] aml_media: mem_free_work, free fb-memory size:400000
```