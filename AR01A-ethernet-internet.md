```c
C:\Users\huide\Desktop>adb shell
* daemon not running; starting now at tcp:5037
* daemon started successfully

root@linaro-alip:/# ifconfig eth_to_adu 172.20.10.11 netmask 255.255.255.0
root@linaro-alip:/# ifconfig
eth0.101: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b2:39:7b:42:0e:6c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0.102: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 6e:ee:89:70:73:e7  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth_to_adu: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.20.10.11  netmask 255.255.255.0  broadcast 172.20.10.255
        inet6 2409:895a:326c:a049:34c0:7fff:febe:53f7  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::34c0:7fff:febe:53f7  prefixlen 64  scopeid 0x20<link>
        ether 36:c0:7f:be:53:f7  txqueuelen 1000  (Ethernet)
        RX packets 4027  bytes 420376 (410.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2668  bytes 185194 (180.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 73

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 3496  bytes 283112 (276.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3496  bytes 283112 (276.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

root@linaro-alip:/# ip route add 172.20.10.0/24 dev eth_to_adu
RTNETLINK answers: File exists
root@linaro-alip:/# ip route add default via 172.20.10.1 dev eth_to_adu
root@linaro-alip:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         172.20.10.1     0.0.0.0         UG    0      0        0 eth_to_adu
172.20.10.0     0.0.0.0         255.255.255.0   U     0      0        0 eth_to_adu
root@linaro-alip:/# ping 172.20.10.1
PING 172.20.10.1 (172.20.10.1) 56(84) bytes of data.
64 bytes from 172.20.10.1: icmp_seq=1 ttl=64 time=11.2 ms
64 bytes from 172.20.10.1: icmp_seq=2 ttl=64 time=12.0 ms
64 bytes from 172.20.10.1: icmp_seq=3 ttl=64 time=4.55 ms
64 bytes from 172.20.10.1: icmp_seq=4 ttl=64 time=4.80 ms
^C
--- 172.20.10.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 4.552/8.128/11.950/3.465 ms

root@linaro-alip:/# ping 101.42.128.234
PING 101.42.128.234 (101.42.128.234) 56(84) bytes of data.
64 bytes from 101.42.128.234: icmp_seq=1 ttl=48 time=93.2 ms
64 bytes from 101.42.128.234: icmp_seq=2 ttl=48 time=100 ms
64 bytes from 101.42.128.234: icmp_seq=3 ttl=48 time=80.0 ms
64 bytes from 101.42.128.234: icmp_seq=4 ttl=48 time=92.7 ms
64 bytes from 101.42.128.234: icmp_seq=5 ttl=48 time=87.3 ms
64 bytes from 101.42.128.234: icmp_seq=6 ttl=48 time=97.0 ms
64 bytes from 101.42.128.234: icmp_seq=7 ttl=48 time=92.0 ms
64 bytes from 101.42.128.234: icmp_seq=8 ttl=48 time=91.6 ms
64 bytes from 101.42.128.234: icmp_seq=9 ttl=48 time=97.5 ms
64 bytes from 101.42.128.234: icmp_seq=10 ttl=48 time=89.6 ms
^C
--- 101.42.128.234 ping statistics ---
11 packets transmitted, 10 received, 9.09091% packet loss, time 10015ms
rtt min/avg/max/mdev = 79.977/92.139/100.482/5.487 ms
root@linaro-alip:/# ping www.baidu.com
PING www.baidu.com(2409:8c00:6c21:11eb:0:ff:b0bf:59ca) 56 data bytes
64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=1 ttl=50 time=101 ms
64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=2 ttl=50 time=65.5 ms
64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=3 ttl=50 time=57.7 ms
64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=4 ttl=50 time=91.7 ms
64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=5 ttl=50 time=81.1 ms
^C64 bytes from 2409:8c00:6c21:11eb:0:ff:b0bf:59ca: icmp_seq=6 ttl=50 time=89.0 ms

--- www.baidu.com ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 9909ms
rtt min/avg/max/mdev = 57.653/80.950/100.739/15.012 ms
root@linaro-alip:/#
```