ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio4 RK_PA2'
./rk3588-evb7-v11.dtsi:		spk-con-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588s.dtsi:		i2s-lrck-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>; /* i2s1m0_lrck */
./rk3588s-evb2-lp5.dtsi:	enable-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb.dtsi:		spk-con-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-x0.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-edp-x0.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-evb5-lp4.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-nvr-demo.dtsi:	snps,reset-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-evb-rkserdes-rk682-dcphy0-ar0330.dtsi:		irq-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-rkserdes-rk682-dcphy0-ox03j10.dtsi:		irq-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96722-dcphy0.dtsi:		lock-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-evb3-lp5.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-lp4.dtsi:		spk-con-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dcphy0.dtsi:		lock-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-adsp-audio-s66.dtsi:	i2s-lrck-gpio = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588s-evb8-lp4x.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:	reset-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio4 RK_PA6'
./rk3588-evb4-lp4.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb2-lp5.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-x0.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-edp-x0.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96722-dphy3-dummy.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dphy3-os04a10.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dphy3-dummy.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb6-lp4.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96722-dphy3.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb2-imx415.dtsi:		ircut-open-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712.dtsi:		power-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb3-lp5.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet.dtsi:		otg-mode-en-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dphy3.dtsi:		gpio = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x-v10-nvp6158-ahd-to-bt1120.dts:		// pwdn2-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-pcie-ep-demo.dtsi:	sbu1-dc-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb3-imx415.dtsi:		ircut-open-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-rk806-single-camera.dtsi:		reset-gpios = <&gpio4 RK_PA6 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio0 RK_PC5'
./rk3588-nvr-demo1-v21.dtsi:		enable-gpios = <&gpio0 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-v11.dtsi:		BT,wake_gpio     = <&gpio0 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-lp4.dtsi:		BT,wake_gpio     = <&gpio0 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-single.dtsi:		BT,wake_host_irq = <&gpio0 RK_PC5 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PC5'
./rk3588s-evb1-lp4x-v10-camera.dtsi:		// hpd-ctl-gpios = <&gpio3 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x-v10-camera.dtsi:		reset-gpios = <&gpio3 RK_PC5 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-evb-v22.dts:		himax,irq-gpio = <&gpio3 RK_PC5 IRQ_TYPE_EDGE_FALLING>;
./rk3588-evb2-lp4.dtsi:	enable-gpios = <&gpio3 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-v21.dts:		himax,irq-gpio = <&gpio3 RK_PC5 IRQ_TYPE_EDGE_FALLING>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:		himax,irq-gpio = <&gpio3 RK_PC5 IRQ_TYPE_EDGE_FALLING>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:		//himax,irq-gpio = <&gpio3 RK_PC5 IRQ_TYPE_EDGE_FALLING>;
./rk3588-vehicle-serdes-mfd-display-rohm.dtsi:		himax,irq-gpio = <&gpio3 RK_PC5 IRQ_TYPE_EDGE_FALLING>;
./rk3588s-evb1-lp4x.dtsi:		reset-gpio = <&gpio3 RK_PC5 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet.dtsi:		reset-gpios = <&gpio3 RK_PC5 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PC6'
./rk3588-evb7-v11.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-evb4-lp4.dtsi:	snps,reset-gpio = <&gpio3 RK_PC6 GPIO_ACTIVE_LOW>;
./rk3588s-evb2-lp5.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588s-tablet-rk806-single.dtsi:		irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-evb2-lp4.dtsi:	snps,reset-gpio = <&gpio3 RK_PC6 GPIO_ACTIVE_LOW>;
./rk3588-evb1-lp4-v10-edp-8lanes-M280DCA.dts:		gpio = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-x0.dtsi:		rst_gpio_number = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-edp-x0.dtsi:		rst_gpio_number = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-v20.dts:		/*power-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;*/
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:	//enable-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display-v20.dtsi:	enable-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-rohm.dtsi:	enable-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-mipi-nvp6188.dtsi:		/*power-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;*/
./rk3588s-evb1-lp4x.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588s-tablet.dtsi:		reset-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_LOW>;
./rk3588-evb7-lp4.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-vehicle-evb-thine_thcv244.dtsi:		/*power-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;*/
./rk3588s-evb8-lp4x.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-vehicle-serdes-display-v21.dtsi:	enable-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:		//irq-gpio = <&gpio3 RK_PC6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-vehicle-serdes-display.dtsi:	enable-gpios = <&gpio3 RK_PC6 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PA6'
./rk3588-evb7-v11.dtsi:		gpio = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4.dtsi:		BT,reset_gpio    = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-x0.dtsi:		BT,reset_gpio    = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-edp-x0.dtsi:		BT,reset_gpio    = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-rkserdes-rk682-dcphy0-ar0330.dtsi:		enable-gpios = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-rkserdes-rk682-dcphy0-ox03j10.dtsi:		enable-gpios = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96722-dcphy0.dtsi:		gpio = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-lp4.dtsi:	hpd-gpios = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dcphy0.dtsi:		gpio = <&gpio3 RK_PA6 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PB2'
./rk3588-nvr-demo1-v21.dtsi:		gpio = <&gpio3 RK_PB2 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PB7'
./rk3588-toybrick.dtsi:			gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-v11.dtsi:	snps,reset-gpio = <&gpio3 RK_PB7 GPIO_ACTIVE_LOW>;
./rk3588s-tablet-rk806-single.dtsi:		BT,reset_gpio    = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle.dtsi:			gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb.dtsi:	snps,reset-gpio = <&gpio3 RK_PB7 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-evb-maxim-max96722.dtsi:		lock-gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-nvr-demo.dtsi:			gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96756-dphy0.dtsi:		lock-gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:		BT,reset_gpio    = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:	snps,reset-gpio = <&gpio3 RK_PB7 GPIO_ACTIVE_LOW>;
./rk3588-evb7-lp4.dtsi:	snps,reset-gpio = <&gpio3 RK_PB7 GPIO_ACTIVE_LOW>;
./rk3588s-tablet-single.dtsi:		reset-gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-evb.dtsi:			gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96712-dphy0.dtsi:		lock-gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588s-evb8-lp4x.dtsi:		BT,reset_gpio    = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:		BT,reset_gpio    = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-evb-maxim-max96722-dphy0.dtsi:		lock-gpios = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PC7'
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PD0'
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio4 RK_PD1'
./rk3588-vehicle-evb-maxim-max96712-dcphy1.dtsi:		gpio = <&gpio4 RK_PD1 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio1 RK_PA6'
./rk3588-toybrick.dtsi:	 *in TB-RK3588 gpio1 RK_PA6 for edp tp
./rk3588-toybrick.dtsi:		gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x-v10-camera.dtsi:		power-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4-v10-lt6911uxe.dts:		// power-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4-v10-lt6911uxe.dts:		// power-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-toybrick-x0.dtsi:		irq_gpio_number = <&gpio1 RK_PA6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-toybrick-edp-x0.dtsi:		irq_gpio_number = <&gpio1 RK_PA6 IRQ_TYPE_LEVEL_LOW>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:	//enable-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display-v20.dtsi:	enable-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-rohm.dtsi:	enable-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-single.dtsi:		elan,rst-gpio = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x.dtsi:		gpio = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4-v10-lt6911uxc-dual-mipi.dts:		// power-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-lp4-v10-lt6911uxc-dual-mipi.dts:		// power-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x-v10-nvp6158-ahd-to-bt1120.dts:		// pwr-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display-v21.dtsi:	enable-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-maxim-serdes.dtsi:			lock-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:		gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display.dtsi:		reset-gpios = <&gpio1 RK_PA6 GPIO_ACTIVE_LOW>,
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio1 RK_PA5'
./rk3588s-tablet-rk806-single.dtsi:		gpio = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-rk806-single.dtsi:			/*enable = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;*/
./rk3588-toybrick-edp-x0.dtsi:		gpio = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:		himax,irq-gpio = <&gpio1 RK_PA5 IRQ_TYPE_EDGE_FALLING>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:		//himax,irq-gpio = <&gpio1 RK_PA5 IRQ_TYPE_EDGE_FALLING>;
./rk3588s-evb1-lp4x.dtsi:		gpio = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:		reset-gpio = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x-v10-nvp6158-ahd-to-bt1120.dts:		pwr2-gpios = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588s-evb8-lp4x.dtsi:		gpio = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-maxim.dtsi:			lock-gpios = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display-v21.dtsi:		reset-gpios = <&gpio1 RK_PA5 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-maxim-serdes.dtsi:			lock-gpios = <&gpio1 RK_PA5 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display.dtsi:		reset-gpios = <&gpio1 RK_PA5 GPIO_ACTIVE_LOW>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio1 RK_PA4'
./rk3588s-evb2-lp5.dtsi:		gpio = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-maxim-serdes-display-s66.dtsi:			lock-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-rk806-single.dtsi:	reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588s-tablet-rk806-single.dtsi:	//reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588-evb2-lp4.dtsi:		hp-det-gpio = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588-nvr-demo-v10-cam-4x.dtsi:		reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-maxim-split.dtsi:		lock-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588-evb3-lp5.dtsi:		hp-det-gpio = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588-evb7-cam-8x.dtsi:		pwdn-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-single.dtsi:		gpio = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x-v10-nvp6158-ahd-to-bt1120.dts:		// pwdn-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-mfd-display-maxim.dtsi:		lock-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588-vehicle-serdes-display-v21.dtsi:		reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-maxim-serdes.dtsi:			lock-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:	reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588s-evb4-lp4x.dtsi:	//reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
./rk3588-vehicle-serdes-display.dtsi:		reset-gpios = <&gpio1 RK_PA4 GPIO_ACTIVE_LOW>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PC0'
./rk3588-evb7-v11.dtsi:		goodix,irq-gpio = <&gpio3 RK_PC0 IRQ_TYPE_LEVEL_LOW>;
./rk3588s-tablet-rk806-single.dtsi:		BT,wake_host_irq = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-imx415.dtsi:		ircut-close-gpios  = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
./rk3588-nvr-demo.dtsi:			gpios = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:		BT,wake_host_irq = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-lp4.dtsi:		goodix,irq-gpio = <&gpio3 RK_PC0 IRQ_TYPE_LEVEL_LOW>;
./rk3588s-evb8-lp4x.dtsi:		BT,wake_host_irq = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:		BT,wake_host_irq = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio3 RK_PC1'
./rk3588-evb7-v11.dtsi:		goodix,rst-gpio = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588s-tablet-rk806-single.dtsi:		BT,wake_gpio     = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588-evb1-imx415.dtsi:		ircut-open-gpios = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588-nvr-demo.dtsi:			gpios = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588s-evb1-lp4x.dtsi:		BT,wake_gpio     = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588-evb7-lp4.dtsi:		goodix,rst-gpio = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588s-evb3-lp4x-v10-nvp6158-ahd-to-bt1120.dts:		// rst2-gpios = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588s-evb8-lp4x.dtsi:		BT,wake_gpio     = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
./rk3588s-evb4-lp4x.dtsi:		BT,wake_gpio     = <&gpio3 RK_PC1 GPIO_ACTIVE_HIGH>;
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio4 RK_PD4'
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ find -name 'rk3588*.dts*' | xargs grep 'gpio4 RK_PD5'
ls@ls-VirtualBox:/data/ar01a/kernel/arch/arm64/boot/dts/rockchip$ 
