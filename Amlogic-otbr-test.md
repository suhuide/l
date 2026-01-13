[Amlogic.md](Amlogic.md)  

QR code
```c
MT:6FCJ142C00KA0648G00
```
```c
chip-tool payload parse-setup-payload MT:6FCJ142C00KA0648G00
eric@ubuntu:~$ chip-tool payload parse-setup-payload MT:6FCJ142C00KA0648G00
[1726309686.781121][3018:3018] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /home/eric/snap/chip-tool/common/chip_tool_kvs
[1726309686.781171][3018:3018] CHIP:SPL: Parsing base38Representation: MT:6FCJ142C00KA0648G00
[1726309686.782238][3018:3018] CHIP:SPL: Version:             0
[1726309686.782253][3018:3018] CHIP:SPL: VendorID:            65521
[1726309686.782255][3018:3018] CHIP:SPL: ProductID:           32773
[1726309686.782256][3018:3018] CHIP:SPL: Custom flow:         0    (STANDARD)
[1726309686.782259][3018:3018] CHIP:SPL: Discovery Bitmask:   0x02 (BLE)
[1726309686.782260][3018:3018] CHIP:SPL: Long discriminator:  3840   (0xf00)
[1726309686.782261][3018:3018] CHIP:SPL: Passcode:            20202021

eric@ubuntu:~$ chip-tool pairing ble-thread 110 hex:0e080000000000000000000300000b35060004001fffe00208dead00beef00cafe0708fddead00beef000005100f57099e74d1249f13151f0b3c38fe39030a4f70656e5468726561640102dc5304108a088834b967b81f767705fe72732d000c0402a0f7f8 20202021 3840
```

# Test Guideline
[Working with the CHIP Tool](https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/chip_tool_guide.md)   
[How to set up OpenThread Border Router on Ubuntu](https://canonical-matter.readthedocs-hosted.com/en/latest/how-to/otbr-on-ubuntu/)   
[How to commission and control Matter devices with Chip Tool](https://canonical-matter.readthedocs-hosted.com/en/latest/how-to/chip-tool-commission-and-control/)   
## Setup Command
```c
$ ./chip-tool pairing ble-wifi <node_id> <ssid> <password> <pin_code> <discriminator>
```
```c
ot-ctl dataset networkkey 00112233445566778899aabbccddeeff
ot-ctl dataset networkname GRL
ot-ctl dataset extpanid 000db80000000000
ot-ctl dataset pskc -p THREADJPAKETEST
ot-ctl dataset activetimestamp 1
ot-ctl dataset securitypolicy 3600 onrc
ot-ctl dataset meshlocalprefix fd00:db9::
ot-ctl dataset panid 0xface
ot-ctl dataset channel 17
ot-ctl dataset channelmask 0x07fff800
ot-ctl dataset commit active
ot-ctl ifconfig up
ot-ctl thread start

ot-ctl state
```
# RasPi
```c
Build Standalone OTBR on RPi 4 
> git clone https://github.com/openthread/ot-br-posix
> cd ot-br-posix
> ./script/bootstrap
> sudo BACKBONE_ROUTER=1 INFRA_IF_NAME=eth0 ./script/setup

Update OTBR-Agent:
> sudo nano /etc/default/otbr-agent
Replace OTBR_AGENT_OPTS as following
> OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyACM0?uart-baudrate=460800“
```
## Edit otbr-agent config file for perpor interface
### Check RCP interface
```c
ubuntu@ubuntu:~$ ls /dev/ttyAC*
/dev/ttyACM0
```

```c
ubuntu@ubuntu:~$ cat /etc/default/otbr-agent
# Default settings for otbr-agent. This file is sourced by systemd

# Options to pass to otbr-agent
OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyACM0 trel://eth0"
OTBR_NO_AUTO_ATTACH=0
```
Executable bin files
```c
ubuntu@ubuntu:/$ ls -1 /usr/sbin/ot*
/usr/sbin/ot-ctl  
/usr/sbin/otbr-agent  
/usr/sbin/otbr-web
```
All otbr relevant in the Raspi.
```c
ubuntu@ubuntu:/$ find -name otbr* 2>/dev/null
./usr/lib/systemd/system/otbr-web.service
./usr/lib/systemd/system/otbr-agent.service
./usr/share/otbr-web
./usr/sbin/otbr-agent
./usr/sbin/otbr-web
./run/systemd/generator.late/otbr-nat44.service
./run/systemd/generator.late/otbr-firewall.service
./run/systemd/generator.late/graphical.target.wants/otbr-nat44.service
./run/systemd/generator.late/graphical.target.wants/otbr-firewall.service
./run/systemd/generator.late/multi-user.target.wants/otbr-nat44.service
./run/systemd/generator.late/multi-user.target.wants/otbr-firewall.service
./sys/fs/cgroup/system.slice/otbr-web.service
./sys/fs/cgroup/system.slice/otbr-agent.service
./etc/systemd/system/otbr-web.service
./etc/systemd/system/multi-user.target.wants/otbr-web.service
./etc/systemd/system/multi-user.target.wants/otbr-agent.service
./etc/systemd/system/otbr-agent.service
./etc/dbus-1/system.d/otbr-agent.conf
./etc/default/otbr-agent
./etc/init.d/otbr-firewall
./etc/init.d/otbr-nat44
```
Start a browser and use http://ip-of-raspberry-pi-border-router to access to web page of OpenThread Border Router.
```c
http://ip-of-raspberry-pi-border-router
```
### otbr-agent service on/off
```c
sudo systemctl start otbr-agent.service
sudo systemctl stop otbr-agent.service
```
```c
ubuntu@ubuntu:~$ mattertool startThread
Starting a new thread network
Done
Done
Done
Done
Done
Done
Done
Done
New ThreadDataset: 0e080000000000010000000300001835060004001fffe00208d730c4e31abb9fb90708fd63080c3351d66c0510349311f1ffcf05ba0e2c0a2b63d180ba030f4f70656e5468726561642d30306263010200bc0410481228613d92ad174a4df2dc5dcb70bb0c0402a0f7f8
```
```c
ubuntu@ubuntu:~$ mattertool bleThread
[1726296138.608185][1483:1483] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_kvs
[1726296138.608676][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_kvs-wHpJjs)
[1726296138.609076][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_kvs)
[1726296138.615665][1483:1483] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1726296138.615983][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_factory.ini-D3uwMI)
[1726296138.616213][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_factory.ini)
[1726296138.616348][1483:1483] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1726296138.616488][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_config.ini-yIBrxM)
[1726296138.616641][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_config.ini)
[1726296138.616748][1483:1483] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1726296138.616870][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_counters.ini-4HxqvW)
[1726296138.617012][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_counters.ini)
[1726296138.617266][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_factory.ini-9ajgt9)
[1726296138.617833][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_factory.ini)
[1726296138.617894][1483:1483] CHIP:DL: NVS set: chip-factory/unique-id = "1B399D89AFD856DD"
[1726296138.618048][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_factory.ini-qNnajW)
[1726296138.622729][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_factory.ini)
[1726296138.622786][1483:1483] CHIP:DL: NVS set: chip-factory/vendor-id = 65521 (0xFFF1)
[1726296138.622926][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_factory.ini-FgoYLY)
[1726296138.628810][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_factory.ini)
[1726296138.628863][1483:1483] CHIP:DL: NVS set: chip-factory/product-id = 32769 (0x8001)
[1726296138.629003][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_counters.ini-YBDVEr)
[1726296138.629354][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_counters.ini)
[1726296138.629399][1483:1483] CHIP:DL: NVS set: chip-counters/reboot-count = 1 (0x1)
[1726296138.629516][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_counters.ini-bBQegb)
[1726296138.632943][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_counters.ini)
[1726296138.633064][1483:1483] CHIP:DL: NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1726296138.633426][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_counters.ini-yfdgmW)
[1726296138.634544][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_counters.ini)
[1726296138.634657][1483:1483] CHIP:DL: NVS set: chip-counters/boot-reason = 0 (0x0)
[1726296138.634977][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_config.ini-TQu3qE)
[1726296138.635957][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_config.ini)
[1726296138.636067][1483:1483] CHIP:DL: NVS set: chip-config/regulatory-location = 0 (0x0)
[1726296138.636340][1483:1483] CHIP:DL: writing settings to file (/tmp/chip_config.ini-6Gl2LQ)
[1726296138.637495][1483:1483] CHIP:DL: renamed tmp file to file (/tmp/chip_config.ini)
[1726296138.637605][1483:1483] CHIP:DL: NVS set: chip-config/location-capability = 2 (0x2)
[1726296138.640208][1483:1483] CHIP:DL: Failed to get Ethernet interface
[1726296138.641358][1483:1483] CHIP:DL: Failed to reset Ethernet statistic counts
[1726296138.641852][1483:1483] CHIP:DL: Got WiFi interface: wlan0
[1726296138.643848][1483:1483] CHIP:DL: Found the primary WiFi interface:wlan0
[1726296138.651319][1483:1483] CHIP:IN: UDP::Init bind&listen port=0
[1726296138.651642][1483:1483] CHIP:IN: UDP::Init bound to port=60233
[1726296138.651690][1483:1483] CHIP:IN: UDP::Init bind&listen port=0
[1726296138.651840][1483:1483] CHIP:IN: UDP::Init bound to port=49776
[1726296138.651876][1483:1483] CHIP:IN: BLEBase::Init - setting/overriding transport
[1726296138.651907][1483:1483] CHIP:IN: TransportMgr initialized
[1726296138.651986][1483:1483] CHIP:FP: Initializing FabricTable from persistent storage
[1726296138.652897][1483:1483] CHIP:TS: Last Known Good Time: [unknown]
[1726296138.652944][1483:1483] CHIP:TS: Setting Last Known Good Time to firmware build time 2022-11-01T16:49:03
[1726296138.659230][1483:1483] CHIP:ZCL: Using ZAP configuration...
[1726296138.663961][1483:1483] CHIP:DL: MDNS failed to join multicast group on wpan0 for address type IPv4: ../../examples/chip-tool/third_party/connectedhomeip/src/inet/UDPEndPointImplSockets.cpp:761: Inet Error 0x00000110: Address not found
[1726296138.664416][1483:1483] CHIP:CTL: System State Initialized...
[1726296138.664497][1483:1483] CHIP:CTL: Stopping commissioning discovery over DNS-SD
[1726296138.669215][1483:1483] CHIP:CTL: Setting attestation nonce to random value
[1726296138.669304][1483:1483] CHIP:CTL: Setting CSR nonce to random value
[1726296138.669434][1483:1483] CHIP:IN: UDP::Init bind&listen port=5550
[1726296138.669591][1483:1483] CHIP:IN: UDP::Init bound to port=5550
[1726296138.669627][1483:1483] CHIP:IN: UDP::Init bind&listen port=5550
[1726296138.669744][1483:1483] CHIP:IN: UDP::Init bound to port=5550
[1726296138.669775][1483:1483] CHIP:IN: TransportMgr initialized
[1726296138.670197][1483:1488] CHIP:DL: CHIP task running
[1726296138.671056][1483:1488] CHIP:CTL: Stopping commissioning discovery over DNS-SD
[1726296138.671122][1483:1488] CHIP:CTL: Setting attestation nonce to random value
[1726296138.671349][1483:1488] CHIP:CTL: Setting CSR nonce to random value
[1726296138.671605][1483:1488] CHIP:CTL: Couldn't get ExampleOpCredsCAKey from storage: ../../examples/chip-tool/config/PersistentStorage.cpp:85: CHIP Error 0x000000A0: Value not found in the persisted storage
[1726296138.673221][1483:1488] CHIP:CTL: Couldn't get ExampleOpCredsICAKey from storage: ../../examples/chip-tool/config/PersistentStorage.cpp:85: CHIP Error 0x000000A0: Value not found in the persisted storage
[1726296138.676308][1483:1488] CHIP:CTL: Generating RCAC
[1726296138.679143][1483:1488] CHIP:CTL: Generating ICAC
[1726296138.685416][1483:1488] CHIP:CTL: Generating NOC
[1726296138.686527][1483:1488] CHIP:FP: Validating NOC chain
[1726296138.689017][1483:1488] CHIP:FP: NOC chain validation successful
[1726296138.693023][1483:1488] CHIP:FP: Added new fabric at index: 0x1
[1726296138.693070][1483:1488] CHIP:FP: Assigned compressed fabric ID: 0x508046A4FD710914, node ID: 0x000000000001B669
[1726296138.693100][1483:1488] CHIP:TS: Last Known Good Time: 2022-11-01T16:49:03
[1726296138.693122][1483:1488] CHIP:TS: New proposed Last Known Good Time: 2021-01-01T00:00:00
[1726296138.693143][1483:1488] CHIP:TS: Retaining current Last Known Good Time
[1726296138.696590][1483:1488] CHIP:FP: Metadata for Fabric 0x1 persisted to storage.
[1726296138.703315][1483:1488] CHIP:TS: Committing Last Known Good Time to storage: 2022-11-01T16:49:03
[1726296138.709895][1483:1488] CHIP:CTL: Joined the fabric at index 1. Compressed fabric ID is: 0x0000000000000000
[1726296138.709968][1483:1488] CHIP:IN: UDP::Init bind&listen port=5550
[1726296138.710147][1483:1488] CHIP:IN: UDP::Init bound to port=5550
[1726296138.710186][1483:1488] CHIP:IN: UDP::Init bind&listen port=5550
[1726296138.710308][1483:1488] CHIP:IN: UDP::Init bound to port=5550
[1726296138.710340][1483:1488] CHIP:IN: TransportMgr initialized
[1726296138.758104][1483:1488] CHIP:IN: SecureSession[0xffff70014dd0]: Allocated Type:1 LSID:19697
[1726296138.758171][1483:1488] CHIP:SC: Assigned local session key ID 19697
[1726296138.758246][1483:1488] CHIP:SC: Including MRP parameters in PBKDF param request
[1726296138.758345][1483:1488] CHIP:EM: <<< [E:21201i M:52434248] (U) Msg TX to 0:0000000000000000 [0000] --- Type 0000:20 (SecureChannel:PBKDFParamRequest)
[1726296138.758402][1483:1488] CHIP:IN: (U) Sending msg 52434248 to IP address 'BLE'
[1726296138.758441][1483:1488] CHIP:IN: Message appended to BLE send queue
[1726296138.758473][1483:1488] CHIP:SC: Sent PBKDF param request
[1726296138.758511][1483:1488] CHIP:CTL: Setting thread operational dataset from parameters
[1726296138.758541][1483:1488] CHIP:CTL: Setting attempt thread scan from parameters
[1726296138.758572][1483:1488] CHIP:CTL: Setting attestation nonce to random value
[1726296138.758622][1483:1488] CHIP:CTL: Setting CSR nonce to random value
[1726296138.758670][1483:1488] CHIP:CTL: Commission called for node ID 0x0000000000002A27
[1726296138.759032][1483:1489] CHIP:DL: TRACE: Bluez mainloop starting Thread
[1726296138.759252][1483:1486] CHIP:DL: TRACE: Bus acquired for name C-05cb
[1726296138.767192][1483:1488] CHIP:DL: PlatformBlueZInit init success
[1726296138.773195][1483:1486] CHIP:BLE: BLE removing known devices.
[1726296138.775316][1483:1486] CHIP:BLE: BLE initiating scan.
[1726296138.822311][1483:1486] CHIP:BLE: Device 41:94:D7:2E:82:29 does not look like a CHIP device.
[1726296139.197463][1483:1486] CHIP:BLE: Device 61:1F:D5:06:08:88 does not look like a CHIP device.
[1726296139.234014][1483:1486] CHIP:BLE: Device 66:BD:2F:59:C2:B3 does not look like a CHIP device.
[1726296139.269452][1483:1486] CHIP:BLE: New device scanned: 8C:6F:B9:68:8E:2F
[1726296139.269703][1483:1486] CHIP:BLE: Device discriminator match. Attempting to connect.
[1726296139.274926][1483:1486] CHIP:BLE: Scan complete notification without an active scan.
[1726296140.185839][1483:1486] CHIP:DL: FAIL: ConnectDevice : GDBus.Error:org.bluez.Error.Failed: le-connection-abort-by-local (36)
[1726296148.107532][1483:1486] CHIP:DL: FAIL: ConnectDevice : GDBus.Error:org.bluez.Error.Failed: le-connection-abort-by-local (36)
[1726296149.270291][1483:1488] CHIP:DL: HandlePlatformSpecificBLEEvent 16386
[1726296149.270385][1483:1488] CHIP:IN: Clearing BLE pending packets.
[1726296149.270459][1483:1488] CHIP:IN: BleConnection Error: ../../examples/chip-tool/third_party/connectedhomeip/src/platform/Linux/BLEManagerImpl.cpp:63: CHIP Error 0x00000032: Timeout
[1726296149.270633][1483:1486] CHIP:DL: FAIL: ConnectDevice : Operation was cancelled (19)
[1726296149.270892][1483:1488] CHIP:DL: HandlePlatformSpecificBLEEvent 16386
```

The Raspberry Pi running the chip tool must have WiFi turned off, otherwise it will cause serious interference to the BLE. You can discover the matter device, but cannot successfully establish the BLE connection. The error log is as you can see.

If your Raspberry Pi‘s Wi-Fi is indeed on, please use nmcli or rfkill to turn it off, and then try to commission some matter device , you may see the success rate is almost 100%.

[Amlogic.md](Amlogic.md)


```c
./connectedhomeip/out/standalone/chip-tool pairing code-wifi 1 "lensgms" "Lensgms@2023.." 12569849880
```
|   Command       | Usage |
|    ----      |   ----  |
| mattertool startThread|Starts the thread network on the OTBR|
|mattertool bleThread|Starts commissioning of a MAD using chip-tool|
|mattertool on|Sends an on command to the MAD using chip-tool|
|mattertool off|Sends an off command to the MAD using chip-tool|

```c
# sudo snap set openthread-border-router infra-if="eth0"
# sudo snap get openthread-border-router
# sudo snap start --enable openthread-border-router
Started.
# sudo openthread-border-router.ot-ctl dataset init new
# sudo openthread-border-router.ot-ctl dataset commit active
# sudo openthread-border-router.ot-ctl ifconfig up
# sudo openthread-border-router.ot-ctl thread start
# sudo openthread-border-router.ot-ctl dataset init new;sudo openthread-border-router.ot-ctl dataset commit active;sudo openthread-border-router.ot-ctl ifconfig up;sudo openthread-border-router.ot-ctl thread start
# sudo openthread-border-router.ot-ctl dataset active -x
0e080000000000000000000300000b35060004001fffe00208dead00beef00cafe0708fddead00beef000005100f57099e74d1249f13151f0b3c38fe39030a4f70656e5468726561640102dc5304108a088834b967b81f767705fe72732d000c0402a0f7f8
Done

# chip-tool pairing ble-thread 110 hex:0e080000000000000000000300000b35060004001fffe00208dead00beef00cafe0708fddead00beef000005100f57099e74d1249f13151f0b3c38fe39030a4f70656e5468726561640102dc5304108a088834b967b81f767705fe72732d000c0402a0f7f8 20202021 3840

# chip-tool pairing ble-thread 110 hex:0e080000000000010000000300001935060004001fffe00208f9c52173bceb49a50708fd52913316c5aaed05101f4cd227125b48c541002fe3554d67c1030f4f70656e5468726561642d3163666601021cff04100ff4bb9166d4feac4b491bf533dbaa5f0c0402a0f7f8 20202021 3840

# chip-tool onoff toggle 110 1
```

## 验证 RCP
```c
sudo systemctl start otbr-agent.service
sudo systemctl stop otbr-agent.service

sudo ot-ctl state

sudo ot-ctl version

sudo ot-ctl rcp version

```
## 配置网络
```c
sudo ot-ctl dataset init new
sudo ot-ctl dataset networkkey 0123456789abcdef0123456789abcdef
sudo ot-ctl dataset extpanid 1234567812345678
sudo ot-ctl dataset panid 0x1234
sudo ot-ctl dataset channel 15
sudo ot-ctl dataset commit active
```

## 打开IPV6接口
```c
sudo ot-ctl ifconfig up
```

## 启动Thread协议
```c
sudo ot-ctl thread start
```

## 查看网络参数
```c
sudo ot-ctl dataset active -x
```
sudo snap start --enable openthread-border-router
tx
[16:52:56.240]收←◆
7E 80 01 02 EA F0 7E 
7E 81 02 01 C5 B2 7E 
7E 82 02 02 3A 6F 7E 
7E 83 02 08 BC 9A 7E 
7E 84 02 05 5C CD 7E 
7E 85 02 B0 01 B8 21 7E 

[16:52:56.564]收←◆7E 80 01 02 EA F0 7E 7E 81 02 01 C5 B2 7E 7E 82 02 02 3A 6F 7E 7E 83 02 08 BC 9A 7E 7E 84 02 05 5C CD 7E 7E 85 02 B0 01 B8 21 7E 
[16:52:56.806]收←◆7E 80 01 02 EA F0 7E 7E 81 02 01 C5 B2 7E 7E 82 02 02 3A 6F 7E 7E 83 02 08 BC 9A 7E 7E 84 02 05 5C CD 7E 7E 85 02 B0 01 B8 21 7E 
[16:52:57.052]收←◆7E 80 01 02 EA F0 7E 7E 81 02 01 C5 B2 7E 7E 82 02 02 3A 6F 7E 7E 83 02 08 BC 9A 7E 7E 84 02 05 5C CD 7E 7E 85 02 B0 01 B8 21 7E 
[16:52:57.311]收←◆7E 80 01 02 EA F0 7E 7E 81 02 01 C5 B2 7E 7E 82 02 02 3A 6F 7E 7E 83 02 08 BC 9A 7E 7E 84 02 05 5C CD 7E 7E 85 02 B0 01 B8 21 7E 

rx
[16:54:58.616]收←◆
7E 80 06 00 70 EE 74 7E 
7E 81 06 01 04 03 DB 0A 7E 
7E 82 06 02 53 4C 2D 4F 50 45 4E 54 48 52 45 41 44 2F 32 2E 34 2E 33 2E 30 5F 47 69 74 48 75 62 2D 37 30 37 34 61 34 33 65 34 3B 20 45 46 52 33 32 3B 20 4F 63 74 20 32 33 20 32 30 32 34 20 31 35 3A 30 34 3A 33 33 00 1A 19 7E 
7E 83 06 08 8C 6F B9 FF FE 68 8E 2B 25 38 7E 
7E 84 06 05 05 0C 18 22 81 04 40 41 42 86 04 CC 41 7E 
7E 85 06 B0 01 09 B7 26 7E 

[16:54:59.062]收←◆7E 80 06 00 70 EE 74 7E 7E 81 06 01 04 03 DB 0A 7E 7E 82 06 02 53 4C 2D 4F 50 45 4E 54 48 52 45 41 44 2F 32 2E 34 2E 33 2E 30 5F 47 69 74 48 75 62 2D 37 30 37 34 61 34 33 65 34 3B 20 45 46 52 33 32 3B 20 4F 63 74 20 32 33 20 32 30 32 34 20 31 35 3A 30 34 3A 33 33 00 1A 19 7E 7E 83 06 08 8C 6F B9 FF FE 68 8E 2B 25 38 7E 7E 84 06 05 05 0C 18 22 81 04 40 41 42 86 04 CC 41 7E 7E 85 06 B0 01 09 B7 26 7E 
[16:54:59.305]收←◆7E 80 06 00 70 EE 74 7E 7E 81 06 01 04 03 DB 0A 7E 7E 82 06 02 53 4C 2D 4F 50 45 4E 54 48 52 45 41 44 2F 32 2E 34 2E 33 2E 30 5F 47 69 74 48 75 62 2D 37 30 37 34 61 34 33 65 34 3B 20 45 46 52 33 32 3B 20 4F 63 74 20 32 33 20 32 30 32 34 20 31 35 3A 30 34 3A 33 33 00 1A 19 7E 7E 83 06 08 8C 6F B9 FF FE 68 8E 2B 25 38 7E 7E 84 06 05 05 0C 18 22 81 04 40 41 42 86 04 CC 41 7E 7E 85 06 B0 01 09 B7 26 7E 
[16:54:59.550]收←◆7E 80 06 00 70 EE 74 7E 7E 81 06 01 04 03 DB 0A 7E 7E 82 06 02 53 4C 2D 4F 50 45 4E 54 48 52 45 41 44 2F 32 2E 34 2E 33 2E 30 5F 47 69 74 48 75 62 2D 37 30 37 34 61 34 33 65 34 3B 20 45 46 52 33 32 3B 20 4F 63 74 20 32 33 20 32 30 32 34 20 31 35 3A 30 34 3A 33 33 00 1A 19 7E 7E 83 06 08 8C 6F B9 FF FE 68 8E 2B 25 38 7E 7E 84 06 05 05 0C 18 22 81 04 40 41 42 86 04 CC 41 7E 7E 85 06 B0 01 09 B7 26 7E 
[16:54:59.810]收←◆7E 80 06 00 70 EE 74 7E 7E 81 06 01 04 03 DB 0A 7E 7E 82 06 02 53 4C 2D 4F 50 45 4E 54 48 52 45 41 44 2F 32 2E 34 2E 33 2E 30 5F 47 69 74 48 75 62 2D 37 30 37 34 61 34 33 65 34 3B 20 45 46 52 33 32 3B 20 4F 63 74 20 32 33 20 32 30 32 34 20 31 35 3A 30 34 3A 33 33 00 1A 19 7E 7E 83 06 08 8C 6F B9 FF FE 68 8E 2B 25 38 7E 7E 84 06 05 05 0C 18 22 81 04 40 41 42 86 04 CC 41 7E 7E 85 06 B0 01 09 B7 26 7E

sdk4.1
tx
[17:09:22.731]收←◆7E 80 06 00 77 51 00 7E
rx
[17:14:47.060]收←◆7E 81 03 71 3F 00 41 D8 A2 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 02 F0 4D 4C 4D 4C 57 60 00 15 E1 5F 00 00 00 00 00 00 01 1E 4A 25 F3 0E C6 8A 99 78 35 E9 5A CA FD 14 FF C0 45 44 3E 2E 76 47 62 8F 00 00 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 76 DD 7E 
[17:14:48.311]收←◆7E 82 03 71 3F 00 41 D8 A3 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 02 F0 4D 4C 4D 4C 12 45 00 15 E2 5F 00 00 00 00 00 00 01 6D D9 5B A4 53 98 20 0E 41 8A 39 D7 D0 B6 E7 85 2E 45 8D 33 66 E1 7D 5E AE 32 00 00 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 E0 77 7E 
[17:14:49.566]收←◆7E 83 03 35 00 B0 BB 77 7E 
[17:14:49.591]收←◆7E 84 03 71 4B 00 41 D8 A4 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C E4 50 00 15 E3 5F 00 00 00 00 00 00 01 79 E3 D9 BF 79 34 7C F6 06 FE A4 A4 B1 EB BA 8F 17 61 5E 0B 83 1B 93 5B 78 28 95 07 AB 1B 87 61 58 50 3D 2A 5E 00 00 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 C4 BC 7E 
[17:14:50.107]收←◆7E 85 03 71 66 00 41 D8 A5 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C 97 AE 00 15 E4 5F 00 00 00 00 00 00 01 A3 62 AB 43 92 D5 4F 89 49 9A DE 9D 8F 20 9D 7B 97 EE 0A 0A 3E FF 91 B4 14 41 CD 3B 5C 39 29 D7 B7 1F A8 E9 A2 22 8A 77 7D 5E 94 B2 F9 76 FB 9E 02 FB 8E A1 1A 20 A9 F6 C2 B2 C3 CA 72 D7 14 51 9F 00 00 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 A9 6E 7E 
[17:14:50.387]收←◆7E 86 03 71 45 00 41 D8 A6 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C CF 14 00 15 E5 5F 00 00 00 00 00 00 01 03 D4 C5 2B C6 43 0A 99 28 4F 3B 6A 5B 00 85 F6 84 9D 04 7D 31 16 7C 46 82 6D DA F3 0E 74 E7 CF D7 B7 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 A4 F2 7E 
[17:14:50.581]收←◆7E 87 03 71 76 00 41 D8 A7 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C 07 C4 00 15 E6 5F 00 00 00 00 00 00 01 DD EF 07 FB 9A 0E A1 BE 0E 42 04 FC 0C D7 5B 5D 1B 80 FE E9 34 F0 C1 D3 3E D7 BA A8 97 EC EA FF 23 75 5B 24 4D 77 25 92 82 A1 7D 5E 7D 5D AB CB 0E 9E A4 0C 93 93 34 A6 33 98 FF DB 23 58 24 32 F7 E7 48 77 25 D6 9B 81 DB 1C 80 48 15 C0 EC 7B 39 43 00 00 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 1A 2B 7E 
[17:14:52.257]收←◆7E 88 03 71 45 00 41 D8 A8 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C FB 58 00 15 E7 5F 00 00 00 00 00 00 01 7D 31 3D 37 79 34 22 24 D9 24 2E 1C BC AA D6 84 49 FE BB B0 C9 0F 3D 9E 0B 85 BB 73 50 2E 46 8F FF 23 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 6E A6 7E 
[17:14:55.174]收←◆7E 89 03 71 45 00 41 D8 A9 FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C 9D B2 00 15 E8 5F 00 00 00 00 00 00 01 42 F3 47 00 BF 70 AE 7C 14 44 93 20 12 8A 77 D8 14 0E 83 B2 EA 91 A2 12 42 D9 00 A9 40 A9 F9 FF 23 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 65 CD 7E 
[17:15:01.917]收←◆7E 8A 03 71 45 00 41 D8 AA FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C 1F 9F 00 15 E9 5F 00 00 00 00 00 00 01 E8 15 83 64 26 A3 DD C3 DE F2 1A 12 94 55 62 16 C2 74 C6 72 AD 2A A0 D1 D6 CF 9A 30 3D 7F FA FF 23 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 C7 D5 7E 
[17:15:16.770]收←◆7E 8B 03 71 45 00 41 D8 AB FF 1C FF FF 7D 5E 36 A7 91 5A 85 FA 5A 7F 3B 01 F0 4D 4C 4D 4C 93 24 00 15 EA 5F 00 00 00 00 00 00 01 1D EA 56 52 D7 7D 31 84 B1 7D 33 DD 53 74 A7 35 98 08 FE 70 2A 14 C5 DC 93 02 5B F2 97 07 D3 53 9B FF 23 19 04 0F 01 00 00 00 00 00 00 00 00 00 00 00 08 6A 7E 

sudo openthread-border-router.ot-ctl rcp version
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl rcp version
OPENTHREAD/7a567da; EFR32; Jul 15 2022 17:49:53
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl version
OPENTHREAD/thread-reference-20230119; POSIX; Apr  9 2024 09:21:20
Done

# My project
```c
eric@eric-pi:~$ sudo snap start --enable openthread-border-router
Started.
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl version
OPENTHREAD/thread-reference-20230119; POSIX; Apr  9 2024 09:21:20
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl rcp version
SL-OPENTHREAD/2.1.6.0_GitHub-2ce3d3bf0; EFR32; Oct 23 2024 17:31:36
Done


eric@eric-pi:~$ sudo snap start --enable openthread-border-router
Started.
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl rcp version
SL-OPENTHREAD/2.1.6.0_GitHub-2ce3d3bf0; EFR32; Oct 24 2024 09:44:05
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl dataset init new
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl dataset commit active
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl ifconfig up
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl thread start
Done
eric@eric-pi:~$ sudo openthread-border-router.ot-ctl state
leader
Done
```
```c
C:\Users\huide\Desktop>adb shell
/ # ./usr/bin/otbr-agent -d7 -v /dev/ttyS2 115200
otbr-agent[10390]: [NOTE]-AGENT---: Running 0.3.0
otbr-agent[10390]: [NOTE]-AGENT---: Thread version: 1.3.0
otbr-agent[10390]: [NOTE]-AGENT---: Thread interface: wpan0
otbr-agent[10390]: [NOTE]-AGENT---: Backbone interface is not specified
otbr-agent[10390]: [NOTE]-AGENT---: Radio URL: /dev/ttyS2
otbr-agent[10390]: [NOTE]-AGENT---: Radio URL: 115200
otbr-agent[10390]: [NOTE]-ILS-----: Infra link selected:
otbr-agent[10390]: [INFO]-RCP_HOS-: OpenThread log level changed to 5
otbr-agent[10390]: 49d.17:33:37.829 [C] Platform------: Init() at radio_url.cpp:146: Failure

```
# Silabs image
```c
ubuntu@ubuntu:/$ find -name ot-ctl 2>/dev/null
./usr/sbin/ot-ctl
./home/ubuntu/ot-br-posix/build/otbr/third_party/openthread/repo/src/posix/ot-ctl
ubuntu@ubuntu:/$ find -name otbr-agent 2>/dev/null
./usr/sbin/otbr-agent
./etc/default/otbr-agent
./home/ubuntu/ot-br-posix/build/otbr/src/agent/otbr-agent
ubuntu@ubuntu:/$ sudo ./usr/sbin/ot-ctl state
disabled
Done
ubuntu@ubuntu:/$ sudo ./usr/sbin/ot-ctl rcp version
OPENTHREAD/7a567da; EFR32; Jul 15 2022 17:49:53
Done
ubuntu@ubuntu:/$
```
```c

ubuntu@ubuntu:/$ find -name ot* 2>/dev/null
./usr/lib/systemd/system/otbr-agent.service
./usr/lib/systemd/system/otbr-web.service
./usr/share/otbr-web
./usr/sbin/otbr-web
./usr/sbin/ot-ctl
./usr/sbin/otbr-agent
./etc/dbus-1/system.d/otbr-agent.conf
./etc/systemd/system/otbr-agent.service
./etc/systemd/system/multi-user.target.wants/otbr-agent.service
./etc/systemd/system/multi-user.target.wants/otbr-web.service
./etc/systemd/system/otbr-web.service
./etc/init.d/otbr-nat44
./etc/init.d/otbr-firewall
./etc/default/otbr-agent
./run/systemd/generator.late/otbr-firewall.service
./run/systemd/generator.late/graphical.target.wants/otbr-firewall.service
./run/systemd/generator.late/graphical.target.wants/otbr-nat44.service
./run/systemd/generator.late/multi-user.target.wants/otbr-firewall.service
./run/systemd/generator.late/multi-user.target.wants/otbr-nat44.service
./run/systemd/generator.late/otbr-nat44.service
./sys/fs/cgroup/system.slice/otbr-web.service
./sys/fs/cgroup/system.slice/otbr-agent.service
```