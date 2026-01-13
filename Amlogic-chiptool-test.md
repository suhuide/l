[Amlogic.md](Amlogic.md)  
# Test Guideline
[Working with the CHIP Tool](https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/chip_tool_guide.md)  
## Setup Command
```c
$ ./chip-tool pairing ble-wifi <node_id> <ssid> <password> <pin_code> <discriminator>
```
# [Matter bulb](https://detail.tmall.com/item.htm?spm=a21n57.1.item.7.3b03523cSSiza3&priceTId=215045ff17246643987338000e00b4&utparam=%7B%22aplus_abtest%22:%22d6146710853b76aa3f073ff6a9cd4791%22%7D&id=744896042532&ns=1&abbucket=11&xxc=taobaoSearch&skuId=5306521562336&pisk=fMcEt_YHSBdUyIHublNz7-JXa-NLsSKXTbZ7r40uRkq3A44uacmWJkgkv0lzj4HBJ8tdzwhZ0_1Bvp3la7NkcnOXG2LLw7xbe3TfUMUYlzA7q6AMANVy1nOXGVJ3J7gMcUnvBFZYP743EJjM7zauqTmuE5XgXzUlxzfH7VqTr74lKz4GSraFtg2nCVVuMia0KE7bXg45oB23m2qnRblGDJ6KRll-Zf4E7u3He_fo_yyENXAG4i2IEqexO4OP6WgqI54rwEXz4-koO5cHjI2TEYDbUAsHRmmrS0FIsUX3mviQsXDVr_0aTly78-SebocKSjFgCIYqSfnIJfu5rQ4scl0Kt7RDkWP3x5ztNhC34ADoOJFRx3r-_VcnUgo52PXivbHFqTy3WPrX7FAM6n_D5OTcDTB8pNUaceeleTe3WPrX7FWReJKY7oTLE)
QR code
```c
//Buld A
MT:S6SA2.DB00YCIH74E00
//Buld B
MT:S6SA2F0S02PMYA2OR10
```
# Preparatory step
Configure and verify the network.
```c
wpa_cli -iwlan0 remove_network 0
wpa_cli -iwlan0 add_network 0
wpa_cli -iwlan0 set_network 0 ssid '"lensgms"' 
wpa_cli -iwlan0 set_network 0 key_mgmt WPA-PSK
wpa_cli -iwlan0 set_network 0 psk '"Lensgms@2023.."'
wpa_cli -iwlan0 set_network 0 pairwise CCMP
wpa_cli -iwlan0 set_network 0 group CCMP
wpa_cli -iwlan0 set_network 0 proto RSN
wpa_cli -iwlan0 enable_network 0
wpa_cli -iwlan0 status
wpa_cli -iwlan0 save
dhcpcd wlan0
```
```c
wpa_cli -iwlan0 remove_network 0
wpa_cli -iwlan0 add_network 0
wpa_cli -iwlan0 set_network 0 ssid '"lh"' 
wpa_cli -iwlan0 set_network 0 key_mgmt WPA-PSK
wpa_cli -iwlan0 set_network 0 psk '"56781234"'
wpa_cli -iwlan0 set_network 0 pairwise CCMP
wpa_cli -iwlan0 set_network 0 group CCMP
wpa_cli -iwlan0 set_network 0 proto RSN
wpa_cli -iwlan0 enable_network 0
wpa_cli -iwlan0 status
wpa_cli -iwlan0 save
dhcpcd wlan0
```
```c
wpa_cli -iwlan0 remove_network 0
wpa_cli -iwlan0 add_network 0
wpa_cli -iwlan0 set_network 0 ssid '"Eip8"' 
wpa_cli -iwlan0 set_network 0 key_mgmt WPA-PSK
wpa_cli -iwlan0 set_network 0 psk '"05161234"'
wpa_cli -iwlan0 set_network 0 pairwise CCMP
wpa_cli -iwlan0 set_network 0 group CCMP
wpa_cli -iwlan0 set_network 0 proto RSN
wpa_cli -iwlan0 enable_network 0
wpa_cli -iwlan0 status
wpa_cli -iwlan0 save
dhcpcd wlan0
```
Verify by check the ip address.
```c
/ # ifconfig
wlan0     Link encap:Ethernet  HWaddr 40:80:E1:31:13:2B
          inet addr:172.20.10.2  Bcast:172.20.10.15  Mask:255.255.255.240
          inet6 addr: fe80::65ef:ce50:7ce3:9faa/64 Scope:Link
          inet6 addr: 2409:895b:3242:ddfc:458e:56cf:93b6:f6bc/64 Scope:Global
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:121 errors:0 dropped:0 overruns:0 frame:0
          TX packets:251 errors:1 dropped:7 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:12423 (12.1 KiB)  TX bytes:35708 (34.8 KiB)
```
Verify by ping the network.  
OK response.
```c
/ # ping www.baidu.com
PING www.baidu.com (183.240.98.198): 56 data bytes
64 bytes from 183.240.98.198: seq=0 ttl=51 time=63.690 ms
64 bytes from 183.240.98.198: seq=1 ttl=51 time=51.368 ms
```
NG response.
```c
/ # ping www.baidu.com
ping: bad address 'www.baidu.com'
```
# Setup
## Bulb A
### Get setup payload from QR code.
```c
/ # chip-tool payload parse-setup-payload MT:S6SA2.DB00YCIH74E00
[1569.853751][10685:10685] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1569.853932][10685:10685] CHIP:DL: writing settings to file (/tmp/chip_tool_kvs-L9Sim9)
[1569.854020][10685:10685] CHIP:DL: renamed tmp file to file (/tmp/chip_tool_kvs)
[1569.854078][10685:10685] CHIP:SPL: Parsing base38Representation: MT:S6SA2.DB00YCIH74E00
[1569.854144][10685:10685] CHIP:SPL: Version:             0
[1569.854156][10685:10685] CHIP:SPL: VendorID:            5136
[1569.854166][10685:10685] CHIP:SPL: ProductID:           1001
[1569.854176][10685:10685] CHIP:SPL: Custom flow:         0    (STANDARD)
[1569.854187][10685:10685] CHIP:SPL: Discovery Bitmask:   0x02 (BLE)
[1569.854198][10685:10685] CHIP:SPL: Long discriminator:  1488   (0x5d0)
[1569.854208][10685:10685] CHIP:SPL: Passcode:            17594029
```
### Setup by ble-wifi
```c
rm -rf /tmp/chip_* && chip-tool pairing ble-wifi 0x1 "Eip8" "05161234" 17594029 1488 --paa-trust-store-path /etc/matter_credentials/paa-root-certs/
```
### Setup by code-wifi
```c
rm -rf /tmp/chip_* && chip-tool pairing code-wifi 1 "Eip8" "05161234" 13038110737 --paa-trust-store-path /etc/matter_credentials/paa-root-certs/  --timeout 100
```
### Verify
```c
chip-tool onoff toggle 0x1 0x1
```
[Amlogic-matter-test-pair-failed-network-issue.log](Amlogic-matter-test-pair-failed-network-issue.log)  
[Amlogic-matter-test-pair-successed-bulbA.log](Amlogic-matter-test-pair-successed-bulbA.log)  

## Bulb B
### Get setup payload from QR code.
```c
/ # chip-tool payload parse-setup-payload MT:S6SA2F0S02PMYA2OR10
[1357.569232][9365:9365] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1357.569389][9365:9365] CHIP:SPL: Parsing base38Representation: MT:S6SA2F0S02PMYA2OR10
[1357.569442][9365:9365] CHIP:SPL: Version:             0
[1357.569458][9365:9365] CHIP:SPL: VendorID:            5136
[1357.569466][9365:9365] CHIP:SPL: ProductID:           1001
[1357.569481][9365:9365] CHIP:SPL: Custom flow:         0    (STANDARD)
[1357.569509][9365:9365] CHIP:SPL: Discovery Bitmask:   0x02 (BLE)
[1357.569520][9365:9365] CHIP:SPL: Long discriminator:  1450   (0x5aa)
[1357.569530][9365:9365] CHIP:SPL: Passcode:            81732706
```
### Setup by ble-wifi
```c
rm -rf /tmp/chip_* && chip-tool pairing ble-wifi 0x1 "Eip8" "05161234" 81732706 1450 --paa-trust-store-path /etc/matter_credentials/paa-root-certs/
```
### Setup by code-wifi
```c
rm -rf /tmp/chip_* && chip-tool pairing code-wifi 1 "Eip8" "05161234" 12569849880 --paa-trust-store-path /etc/matter_credentials/paa-root-certs/ --timeout 200
```
[Amlogic-matter-test-pair-successed-bulbA.log](Amlogic-matter-test-pair-successed-bulbA.log)    

### Setup on Amlogic end device, image from Amlogic
```c
date 091112302024
//Controller
adb -s ap222bc9165d66452cb14 shell
rm -rf /tmp/chip_* && chip-tool pairing ble-wifi 0x1 "lensgms" "Lensgms@2023.." 20202021 3840
rm -rf /tmp/chip_* && chip-tool pairing ble-wifi 0x1 "Eip8" "05161234" 20202021 3840 --timeout 100
//End device
adb -s ap2226c0665d664529620 shell
rm -rf /tmp/chip_* && chip-lighting-app --wifi
```
# Issue and debug
## DAC Certificate outdate
```c
[60.946476][1042:1044] CHIP:CTL: Verifying attestation
[60.970694][1042:1044] CHIP:CTL: Failed in verifying 'Attestation Information' command received from the device: err 300. Look at AttestationVerificationResult enum to understand the errors
```
[Amlogic-matter-test-fail.log](Amlogic-matter-test-fail.log)  

Countermeasure:
Configure WiFi, make sure network accessible.
Or set datetime up to date.
## WiFi enable fail
At commissioning step 'WiFiNetworkEnable', WiFi enable fail.
```c
[1726040109.175679][30638:30640] CHIP:DMG: Time out! failed to receive invoke command response from Exchange: 31354i
[1726040109.175741][30638:30640] CHIP:CTL: Received failure response src/app/CommandSender.cpp:328: CHIP Error 0x00000032: Timeout

[1726040109.175762][30638:30640] CHIP:CTL: Error on commissioning step 'WiFiNetworkEnable': 'src/app/CommandSender.cpp:328: CHIP Error 0x00000032: Timeout'
[1726040109.175774][30638:30640] CHIP:CTL: Going from commissioning step 'WiFiNetworkEnable' with lastErr = 'src/app/CommandSender.cpp:328: CHIP Error 0x00000032: Timeout' -> 'Cleanup'
[1726040109.175789][30638:30640] CHIP:CTL: Performing next commissioning step 'Cleanup' with completion status = 'src/app/CommandSender.cpp:328: CHIP Error 0x00000032: Timeout'
[1726040109.175800][30638:30640] CHIP:CTL: Successfully finished commissioning step 'Cleanup'
```
[Amlogic-matter-test-fail2.log](Amlogic-matter-test-fail2.log)   
Countermeasure:  
1, Check WiFi antenna connection.  
2, Reset the set and WiFi AP  
3, Reconfig WiFi  
4, Retry.  

[Amlogic.md](Amlogic.md)
