[memo](memo.md)  
[AR01A](AR01A.md)  

# GPS
GPS: Global Position System
GNSS: Global Navigation Satellite System,GPS(US),GLONASS(Russia),Galileo (EU),BeiDou(CN)  
<div align="center">
  <img src="files/gps/band.png" width="720">
</div>

# LC29H
## QGNSS
<div align="center">
  <img src="files/gps/1.png" width="1080">
</div>

## Pin map
<div align="center">
  <img src="files/gps/lc29h.png" width="720">
</div>

## GPS Pins
|   Name       | Pin | Pin No. | Other |
|    ----         |     -----    |     -----    |     -----    |
| GPS_PWR         |    GPIO1_A6  | 38 | R3317,C3311 |
| GPS_VBKP        |    GPIO1_A5  | 37 | R3315,C3313 |
| GPS_RESET       |    GPIO0_A4  | 4 | R3308,Q3300 |
| GPS_WAKEUP      |    GPIO4_D1  | 153 | R3300  |
| GPS_PPS_TRIG    |    GPIO3_C0  | |   |
| GPS_PPS_CLK     |    GPIO3_C1  | |   |
| GPS_UART_EN     |    GPIO4_A7  | 135 | R3316  |
| uart5_m0        |    GPIO4_D5->TX,GPIO4_D4->RX  |  |  |
```c
./kernel/arch/arm64/boot/dts/rockchip/rk3588s-pinctrl.dtsi
	uart5 {
		/omit-if-no-ref/
		uart5m0_xfer: uart5m0-xfer {
			rockchip,pins =
				/* uart5_rx_m0 */
				<4 RK_PD4 10 &pcfg_pull_up>,
				/* uart5_tx_m0 */
				<4 RK_PD5 10 &pcfg_pull_up>;
		};

		/omit-if-no-ref/
		uart5m0_ctsn: uart5m0-ctsn {
			rockchip,pins =
				/* uart5m0_ctsn */
				<4 RK_PD2 10 &pcfg_pull_none>;
		};

		/omit-if-no-ref/
		uart5m0_rtsn: uart5m0-rtsn {
			rockchip,pins =
				/* uart5m0_rtsn */
				<4 RK_PD3 10 &pcfg_pull_none>;
		};
	};

./kernel/arch/arm64/boot/dts/rockchip/rk3588s_evb4_lp4x.dtsi
	gnss {
		gnss_pwr_gpio: gnss-pwr-gpio {
			rockchip,pins = <1 RK_PA6 RK_FUNC_GPIO &pcfg_pull_none>;
		};
		gnss_vbkp_gpio: gnss-vbkp-gpio {
			rockchip,pins = <1 RK_PA5 RK_FUNC_GPIO &pcfg_pull_none>;
		};	
		gnss_rst_gpio: gnss-rst-gpio {
			rockchip,pins = <1 RK_PA4 RK_FUNC_GPIO &pcfg_pull_none>;
		};
		gnss_wakeup_gpio: gnss-wakeup-gpio {
			rockchip,pins = <1 RK_PD1 RK_FUNC_GPIO &pcfg_pull_none>;
		};							
	};

	&uart5 {
		status = "okay";		
		pinctrl-names = "default";
    	pinctrl-0 = <&uart5m0_xfer &uart5m0_ctsn>;
	}  

```
## [Hot Startup](https://forumschinese.quectel.com/t/topic/6112)
```c
$PAIR650,0*25
1. 断电前发送指令“$PAIR650,0*25\r\n”指令，使模块进入Backup模式。
2. 保持备份电池有电，断掉VCC电源。
3. 唤醒时，首先给模块VCC上点，然后WAKEUP(PIN1)引脚拉高10ms以上，模块就可以实现热启动。
```
### Backup mode Entry
- 1,Send the command "$PAIR650,0*25\r\n" to the module.
- 2,Power off the module VCC and keep the backup battery V_BCKP powered.
### Backup mode Exit
- 1,First power on the module, 
- 2,Pull up the WAKEUP pin for 10ms or more, the module can be implemented hot startup.

# RTK
```c
域名:vrs.sixents.com
IP:101.42.128.234

账号:smrns064
密码:e87FGsTP

账号:smrns065
密码:IzJ27hch

端口:
端口8001	对应坐标框架ITRF2014 参考历元2020.0
端口8002	对应坐标框架WGS84    参考历元2010.0
端口8003	对应坐标框架CGCS2000 参考历元2000.0
端口8004	对应坐标框架ITRF2014 参考历元2018.0
端口8005	对应坐标框架WGS84	 参考历元2005.0


挂载点：
RTCM32_GNSS2		(4星13频)
RTCM32_GRECJ2		(5星16频)

端口没有特殊要求，一般用8002，挂载点用 RTCM32_GRECJ2
```
```c
./ntripclient -s 101.42.128.234 -r 8002 -u lfcs300 -p 7HDte3pD -m RTCM32_GRECJ2 -D /dev/ttyS5 -B 115200 -n GNGGA | grep RMC
./ntripclient -s 101.42.128.234 -r 8002 -u lfcs300 -p 7HDte3pD -m RTCM32_GRECJ2 -D /dev/ttyACM0 -B 115200 -n GNGGA | grep RMC
./ntripclient --server 101.42.128.234 --port 8002 --mountpoint RTCM32_GRECJ2 -u lfcs300 -p 7HDte3pD -D /dev/ttyS5 -B 115200 --mode n --nmea "\$GNGGA,034458.00,2810.79928,N,11256.54467,E,2,12,0.64,36.0,M,-12.7,M,1.0,0773*7D" -l logfile.serial
./ntripclient --server 101.42.128.234 --port 8002 --mountpoint RTCM32_GRECJ2 -u lfcs300 -p 7HDte3pD -D /dev/ttyACM0 -B 115200 --mode n --nmea "\$GNGGA,034458.00,2810.79928,N,11256.54467,E,2,12,0.64,36.0,M,-12.7,M,1.0,0773*7D" -l logfile.serial
```
```c
sudo python3 ntrip.py -s 101.42.128.234 -p 8002 -m RTCM32_GRECJ2 -u smrns064 -w e87FGsTP -d /dev/ttyACM0 -b 115200
sudo python3 ntrip.py -s 101.42.128.234 -p 8002 -m RTCM32_GRECJ2 -u smrns065 -w IzJ27hch -d /dev/ttyACM0 -b 115200
```
```c
eric@u24:~/rtk$ curl -v --http0.9 -H "Ntrip-Version: Ntrip/2.0" -H "User-Agent: NTRIP BNC1.14.0" -H "Connection: keep-alive" -H "Ntrip-GGA: $GNGGA,081952.000,2233.017012,N,11358.822674,E,1,14,1.74,49.290,M,-2.409,M,,*50" -u smrns064:e87FGsTP "http://101.42.128.234:8002/RTCM32_GRECJ2"
*   Trying 101.42.128.234:8002...
* Connected to 101.42.128.234 (101.42.128.234) port 8002
* Server auth using Basic with user 'smrns064'
> GET /RTCM32_GRECJ2 HTTP/1.1
> Host: 101.42.128.234:8002
> Authorization: Basic c21ybnMwNjQ6ZTg3RkdzVFA=
> Accept: */*
> Ntrip-Version: Ntrip/2.0
> User-Agent: NTRIP BNC1.14.0
> Connection: keep-alive
> Ntrip-GGA: ,081952.000,2233.017012,N,11358.822674,E,1,14,1.74,49.290,M,-2.409,M,,*50
> 
ICY 200 OK
* Closing connection

```
```c
curl -v --http0.9 -H "Ntrip-Version: Ntrip/2.0" -H "User-Agent: NTRIP BNC1.14.0" -H "Connection: keep-alive" -H "Ntrip-GGA: $GNGGA,145844.000,2238.485545,N,11410.819115,E,1,11,1.92,117.311,M,-1.636,M,,*6D" -u smrns064:e87FGsTP "http://101.42.128.234:8002/RTCM32_GRECJ2"

```
先测试连通性：
curl -I http:/101.42.128.234:8002
如果返回 200 或 401，说明服务器在线。
curl --http0.9 -u smrns064:e87FGsTP -v http://101.42.128.234:8002/RTCM32_GRECJ2
```c
eric@u24:~/rtk$ curl --http0.9 -v http://101.42.128.234:8002/
*   Trying 101.42.128.234:8002...
* Connected to 101.42.128.234 (101.42.128.234) port 8002
> GET / HTTP/1.1
> Host: 101.42.128.234:8002
> User-Agent: curl/8.5.0
> Accept: */*
> 
SOURCETABLE 200 OK
Server: NI Caster
Date: 2025-09-05T22:43:45.773664
Connection: close
Content-Type: text/plain
Content-Length: 555

STR;RTCM32_GRECJ2;RTCM32_GRECJ2;RTCM3.2;1005-1033(10),1074-1084-1094-1114-1124(1);2;GNSS;POPNET;CHN;0.0;0.0;1;1;POP Platform;none;B;N;500;POP
STR;RTCM32_GRECJ_S1;RTCM32_GRECJ_S1;RTCM3.2;1005-1033(10),1074-1084-1094-1114-1124(1);2;GNSS;POPNET;CHN;0.0;0.0;1;1;POP Platform;none;B;N;500;POP
STR;RTCM32_GNSS2;RTCM32_GNSS2;RTCM3.2;1005-1033(10),1074-1084-1094-1124(1);2;GNSS;POPNET;CHN;0.0;0.0;1;1;POP Platform;none;B;N;500;POP
STR;RTCM32_GRC4;RTCM32_GRC4;RTCM3.2;1005-1033(10),1074-1084-1124(1);2;GNSS;POPNET;CHN;0.0;0.0;1;1;POP Platform;none;B;N;500;POP

ENDSOURCETABLE
* Closing connection
```
再测试认证和获取列表：
curl -u "user:pass" http://ntrip.example.com:2101/
这是最关键的一步。如果成功返回源列表，说明你的账号有效，并且服务器功能正常。

最后测试具体数据流（可选）：
curl -u "user:pass" --max-time 5 http://ntrip.example.com:2101/RTCM32
看到乱码输出就意味着大功告成！
# NMEA
[NMEA](NMEA.md)

## Cross-Compile
```c
$ file nmea_app
nmea_app: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2671b2b311972539cb186e3e9461453931b7c736, for GNU/Linux 3.2.0, not stripped

$ file nmea_app
nmea_app_d: ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=28faaca424f039a2c9dffab33063c4010ff82684, for GNU/Linux 3.7.0, not stripped
```
## Factory test
产测中有冷热启动还有都老化，这些都是要操作gpio的。应用操作gpio可以通过/sys/class/gpio 这个节点。
内核里已占用，app操作时会报资源占用，所以我的处理方法是另开GNSS专用的节点。

```mermaid
graph TD
    A[nmea] --> |nmea all| B[rmc,gga,gsv]
	A[nmea] --> |nmea rmc| C[rmc]
    A[nmea] --> |nmea gga| D[gga]
	A[nmea] --> |nmea gsv| E[gsv]
    A[nmea] --> |nmea power on| F[power on]
	A[nmea] --> |nmea power off| G[power off]
    A[nmea] --> |nmea sleep| H[sleep]
	A[nmea] --> |nmea weakup| I[weakup]
	A[nmea] --> |nmea aging| J[aging]
	F[power on] --> K[exit]
	G[power off] --> K[exit]
	H[sleep] --> K[exit]
	I[wakeup] --> K[exit]
	J[aging] --> K[exit]
	style F fill:#f9f,stroke:#333,stroke-width:2px
	style G fill:#09f,stroke:#333,stroke-width:2px
	style H fill:#4f0,stroke:#333,stroke-width:2px
	style I fill:#87f,stroke:#333,stroke-width:2px
	style J fill:#9f0,stroke:#333,stroke-width:2px
	style K fill:#9c0,stroke:#333,stroke-width:2px
```