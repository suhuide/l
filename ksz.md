
ksz9477驱动，dts 如下，
```c
&i2c5 {
	status = "okay";
	i2c_ksz9477: ksz9477@5f {
		compatible = "microchip,ksz9477";
		reg = <0x5f>;

		interrupt-parent = <&gpio3>;
		interrupts = <28 IRQ_TYPE_LEVEL_LOW>;
		status = "okay";
		ports {
			#address-cells = <1>;
			#size-cells = <0>;
			port@0 {
				reg = <0>;
				label = "lan1";
			};
			port@1 {
				reg = <1>;
				label = "lan2";
			};
			port@2 {
				reg = <2>;
				label = "lan3";
			};
			port@3 {
				reg = <3>;
				label = "lan4";
			};
			port@4 {
				reg = <4>;
				label = "lan5";
			};
			port@5 {
				reg = <5>;
				label = "cpu";
				ethernet = <&gmac1>;
				phy-mode = "rgmii-txid";
				fixed-link {
					speed = <1000>;
					full-duplex;
					pause;
				};
			};
			port@6 {
				reg = <6>;
				label = "lan6";
			};
		};
	};
};
&gmac1 {
	/* Use rgmii-rxid mode to disable rx delay inside Soc */
	phy-mode = "rgmii-rxid";
	clock_in_out = "output";
	snps,reset-gpio = <&gpio3 RK_PB2 GPIO_ACTIVE_LOW>;
	snps,reset-active-low;
	/* Reset time is 20ms, 100ms for rtl8211f */
	snps,reset-delays-us = <0 20000 100000>;
	pinctrl-names = "default";
	pinctrl-0 = <&gmac1_miim
		&gmac1_tx_bus2
		&gmac1_rx_bus2
		&gmac1_rgmii_clk
		&gmac1_rgmii_bus>;
	tx_delay = <0x45>;
	/* rx_delay = <0x43>; */
	phy-handle = <&rgmii_phy1>;
	status = "okay";
};

&mdio1 {
	rgmii_phy1: phy@0 {
		compatible = "ethernet-phy-ieee802.3-c22";
		reg = <0x0>;
	};
};
```
调试log如下
```c
root@rk3588s-buildroot:/# dmesg | grep stm
[    1.540015] rcu: RCU calculated value of scheduler-enlistment delay is 30 jiffies.
[    2.188405] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: stmmac_dvr_probe: MDIO bus (id: 1) registration failed
[    3.075316] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: stmmac_dvr_probe: MDIO bus (id: 1) registration failed
```
```c
root@rk3588s-buildroot:/# dmesg | grep eth
[    1.415698] psci: probing for conduit method from DT.
[    2.187536] rk_gmac-dwmac fe1c0000.ethernet: IRQ eth_lpi not found
[    2.187656] rk_gmac-dwmac fe1c0000.ethernet: supply phy not found, using dummy regulator
[    2.187710] rk_gmac-dwmac fe1c0000.ethernet: clock input or output? (output).
[    2.187715] rk_gmac-dwmac fe1c0000.ethernet: TX delay(0x45).
[    2.187720] rk_gmac-dwmac fe1c0000.ethernet: Can not read property: rx_delay.
[    2.187724] rk_gmac-dwmac fe1c0000.ethernet: set rx_delay to 0xffffffff
[    2.187737] rk_gmac-dwmac fe1c0000.ethernet: integrated PHY? (no).
[    2.187743] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_rx
[    2.187748] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_tx
[    2.187758] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock clk_mac_speed
[    2.187973] rk_gmac-dwmac fe1c0000.ethernet: init for RGMII_RXID
[    2.188072] rk_gmac-dwmac fe1c0000.ethernet: User ID: 0x30, Synopsys ID: 0x51
[    2.188077] rk_gmac-dwmac fe1c0000.ethernet:         DWMAC4/5
[    2.188083] rk_gmac-dwmac fe1c0000.ethernet: DMA HW capability register supported
[    2.188086] rk_gmac-dwmac fe1c0000.ethernet: RX Checksum Offload Engine supported
[    2.188090] rk_gmac-dwmac fe1c0000.ethernet: TX Checksum insertion supported
[    2.188094] rk_gmac-dwmac fe1c0000.ethernet: Wake-Up On Lan supported
[    2.188118] rk_gmac-dwmac fe1c0000.ethernet: TSO supported
[    2.188122] rk_gmac-dwmac fe1c0000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    2.188126] rk_gmac-dwmac fe1c0000.ethernet: Enabled Flow TC (entries=2)
[    2.188130] rk_gmac-dwmac fe1c0000.ethernet: TSO feature enabled
[    2.188134] rk_gmac-dwmac fe1c0000.ethernet: Using 32 bits DMA width
[    2.188398] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: Cannot register the MDIO bus
[    2.188405] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: stmmac_dvr_probe: MDIO bus (id: 1) registration failed
[    2.188600] rk_gmac-dwmac: probe of fe1c0000.ethernet failed with error -16
[    3.042192] optee: probing for conduit method.
[    3.071358] rk_gmac-dwmac fe1c0000.ethernet: IRQ eth_lpi not found
[    3.071506] rk_gmac-dwmac fe1c0000.ethernet: supply phy not found, using dummy regulator
[    3.071568] rk_gmac-dwmac fe1c0000.ethernet: clock input or output? (output).
[    3.071575] rk_gmac-dwmac fe1c0000.ethernet: TX delay(0x45).
[    3.071581] rk_gmac-dwmac fe1c0000.ethernet: Can not read property: rx_delay.
[    3.071585] rk_gmac-dwmac fe1c0000.ethernet: set rx_delay to 0xffffffff
[    3.071609] rk_gmac-dwmac fe1c0000.ethernet: integrated PHY? (no).
[    3.071617] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_rx
[    3.071623] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_tx
[    3.071638] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock clk_mac_speed
[    3.071904] rk_gmac-dwmac fe1c0000.ethernet: init for RGMII_RXID
[    3.074685] rk_gmac-dwmac fe1c0000.ethernet: User ID: 0x30, Synopsys ID: 0x51
[    3.074695] rk_gmac-dwmac fe1c0000.ethernet:         DWMAC4/5
[    3.074702] rk_gmac-dwmac fe1c0000.ethernet: DMA HW capability register supported
[    3.074707] rk_gmac-dwmac fe1c0000.ethernet: RX Checksum Offload Engine supported
[    3.074712] rk_gmac-dwmac fe1c0000.ethernet: TX Checksum insertion supported
[    3.074717] rk_gmac-dwmac fe1c0000.ethernet: Wake-Up On Lan supported
[    3.074722] rk_gmac-dwmac fe1c0000.ethernet: TSO supported
[    3.074728] rk_gmac-dwmac fe1c0000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.074736] rk_gmac-dwmac fe1c0000.ethernet: Enabled Flow TC (entries=2)
[    3.074742] rk_gmac-dwmac fe1c0000.ethernet: TSO feature enabled
[    3.074749] rk_gmac-dwmac fe1c0000.ethernet: Using 32 bits DMA width
[    3.074762] rk_gmac-dwmac fe1c0000.ethernet: Unbalanced pm_runtime_enable!
[    3.075303] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: Cannot register the MDIO bus
[    3.075316] rk_gmac-dwmac fe1c0000.ethernet: error -EBUSY: stmmac_dvr_probe: MDIO bus (id: 1) registration failed
[    3.084343] rk_gmac-dwmac: probe of fe1c0000.ethernet failed with error -16
root@rk3588s-buildroot:/#
```

分析是什么问题，怎么解决？另外串口log看到读出chip ID了，IIC用逻辑分析仪也看过未发现异常。