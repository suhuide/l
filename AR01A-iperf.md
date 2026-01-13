

# TCP
## Server on Raspi(10.5.17.228)
```c
iperf -s -i 1 -w 1M
//-s: work as a server 
//-i 1: 1s interval 
//-w 1M: 1M window size
```
```c
eric@eric-pi:~$ sudo apt install iperf
[sudo] password for eric:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  iperf
0 upgraded, 1 newly installed, 0 to remove and 266 not upgraded.
Need to get 130 kB of archives.
After this operation, 367 kB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 iperf arm64 2.1.9+dfsg-1 [130 kB]
Fetched 130 kB in 2s (66.8 kB/s)
Selecting previously unselected package iperf.
(Reading database ... 148356 files and directories currently installed.)
Preparing to unpack .../iperf_2.1.9+dfsg-1_arm64.deb ...
Unpacking iperf (2.1.9+dfsg-1) ...
Setting up iperf (2.1.9+dfsg-1) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for ufw (0.36.2-6) ...
eric@eric-pi:~$ which iperf
/usr/bin/iperf
eric@eric-pi:~$ iperf --version
iperf version 2.1.9 (14 March 2023) pthreads
eric@eric-pi:~$ iperf -s -i 1 -w 1M
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size:  416 KByte (WARNING: requested 1.00 MByte)
------------------------------------------------------------
[  1] local 10.5.17.228 port 5001 connected with 10.5.17.111 port 53594 (icwnd/mss/irtt=14/1448/451
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec   112 MBytes   940 Mbits/sec
[  1] 1.0000-2.0000 sec   112 MBytes   941 Mbits/sec
[  1] 2.0000-3.0000 sec   112 MBytes   941 Mbits/sec
[  1] 3.0000-4.0000 sec   112 MBytes   941 Mbits/sec
[  1] 4.0000-5.0000 sec   112 MBytes   941 Mbits/sec
[  1] 5.0000-6.0000 sec   112 MBytes   941 Mbits/sec
[  1] 6.0000-7.0000 sec   112 MBytes   941 Mbits/sec
[  1] 7.0000-8.0000 sec   112 MBytes   941 Mbits/sec
[  1] 8.0000-9.0000 sec   112 MBytes   941 Mbits/sec
[  1] 9.0000-10.0000 sec   112 MBytes   941 Mbits/sec
[  1] 0.0000-10.0035 sec  1.10 GBytes   941 Mbits/sec
```

# Client on AR01A(10.5.17.111)
```c
iperf -c 10.5.17.228 -i 1 -w 1M
//-c: ????? 
```
```c
root@linaro-alip:/# ifconfig eth0 10.5.17.111
root@linaro-alip:/# ping 10.5.17.228
PING 10.5.17.228 (10.5.17.228) 56(84) bytes of data
.
64 bytes from 10.5.17.228: icmp_seq=1 ttl=64 time=0
.783 ms
64 bytes from 10.5.17.228: icmp_seq=2 ttl=64 time=0
.397 ms
^C
--- 10.5.17.228 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss,
time 1027ms
rtt min/avg/max/mdev = 0.397/0.590/0.783/0.193 ms
root@linaro-alip:/#
root@linaro-alip:/# iperf -c 10.5.17.228 -i 1 -w 1M
---------------------------------------------------
---------
Client connecting to 10.5.17.228, TCP port 5001
TCP window size:  416 KByte (WARNING: requested 1.0
0 MByte)
------------------------------------------------------------
[  3] local 10.5.17.111 port 53594 connected with 10.5.17.228 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3] 0.0000-1.0000 sec   112 MBytes   942 Mbits/sec
[  3] 1.0000-2.0000 sec   112 MBytes   942 Mbits/sec
[  3] 2.0000-3.0000 sec   112 MBytes   941 Mbits/sec
[  3] 3.0000-4.0000 sec   112 MBytes   942 Mbits/sec
[  3] 4.0000-5.0000 sec   112 MBytes   941 Mbits/sec
[  3] 5.0000-6.0000 sec   112 MBytes   941 Mbits/sec
[  3] 6.0000-7.0000 sec   112 MBytes   941 Mbits/sec
[  3] 7.0000-8.0000 sec   112 MBytes   942 Mbits/sec
[  3] 8.0000-9.0000 sec   112 MBytes   942 Mbits/sec
[  3] 9.0000-10.0000 sec   112 MBytes   940 Mbits/sec
[  3] 10.0000-10.0002 sec   256 KBytes  9.89 Gbits/sec
[  3] 0.0000-10.0002 sec  1.10 GBytes   941 Mbits/sec
root@linaro-alip:/#
```
## Server on AR01A(10.5.17.111)
```c
iperf -s -i 1 -w 1M
```
```c
root@linaro-alip:/# iperf -s -i 1 -w 1M
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size:  416 KByte (WARNING: requested 1.00 MByte)
------------------------------------------------------------
[  4] local 10.5.17.111 port 5001 connected with 10.5.17.228 port 48318
[ ID] Interval       Transfer     Bandwidth
[  4] 0.0000-1.0000 sec   112 MBytes   936 Mbits/sec
[  4] 1.0000-2.0000 sec   112 MBytes   936 Mbits/sec
[  4] 2.0000-3.0000 sec   112 MBytes   936 Mbits/sec
[  4] 3.0000-4.0000 sec   112 MBytes   937 Mbits/sec
[  4] 4.0000-5.0000 sec   112 MBytes   936 Mbits/sec
[  4] 5.0000-6.0000 sec   112 MBytes   936 Mbits/sec
[  4] 6.0000-7.0000 sec   112 MBytes   937 Mbits/sec
[  4] 7.0000-8.0000 sec   112 MBytes   937 Mbits/sec
[  4] 8.0000-9.0000 sec   112 MBytes   936 Mbits/sec
[  4] 9.0000-10.0000 sec   111 MBytes   935 Mbits/sec
[  4] 10.0000-10.0018 sec   195 KBytes   913 Mbits/sec
[  4] 0.0000-10.0018 sec  1.09 GBytes   936 Mbits/sec
```
# Client on Raspi(10.5.17.228)
```c
iperf -c 10.5.17.111 -i 1 -w 1M
```
```c
eric@eric-pi:~iperf -c 10.5.17.111 -i 1 -w 1M
------------------------------------------------------------
Client connecting to 10.5.17.111, TCP port 5001
TCP window size:  416 KByte (WARNING: requested 1.00 MByte)
------------------------------------------------------------
[  1] local 10.5.17.228 port 48318 connected with 10.5.17.111 port 5001 (icwnd/mss/irtt=14/1448/495)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec   112 MBytes   937 Mbits/sec
[  1] 1.0000-2.0000 sec   112 MBytes   936 Mbits/sec
[  1] 2.0000-3.0000 sec   112 MBytes   937 Mbits/sec
[  1] 3.0000-4.0000 sec   112 MBytes   935 Mbits/sec
[  1] 4.0000-5.0000 sec   112 MBytes   936 Mbits/sec
[  1] 5.0000-6.0000 sec   112 MBytes   936 Mbits/sec
[  1] 6.0000-7.0000 sec   112 MBytes   937 Mbits/sec
[  1] 7.0000-8.0000 sec   112 MBytes   935 Mbits/sec
[  1] 8.0000-9.0000 sec   112 MBytes   936 Mbits/sec
[  1] 9.0000-10.0000 sec   111 MBytes   934 Mbits/sec
[  1] 0.0000-10.0319 sec  1.09 GBytes   933 Mbits/sec
```

# UDP
## Server on Raspi(10.5.17.228)
```c
iperf -u -s
```
```c
eric@eric-pi:~$ iperf -u -s
------------------------------------------------------------
Server listening on UDP port 5001
UDP buffer size:  208 KByte (default)
------------------------------------------------------------
[  1] local 10.5.17.228 port 5001 connected with 10.5.17.111 port 60811
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  1] 0.0000-60.0015 sec  6.59 GBytes   944 Mbits/sec   0.018 ms 0/4814894 (0%)
```

# Client on AR01A(10.5.17.111)
```c
iperf -u -c 10.5.17.228 -b 900M  -i 1  -w 1M  -t 60 
```
```c
root@linaro-alip:/# iperf -u -c 10.5.17.228 -b 900M  -i 1  -w 1M  -t 60
------------------------------------------------------------
Client connecting to 10.5.17.228, UDP port 5001
UDP buffer size:  416 KByte (WARNING: requested 1.00 MByte)
------------------------------------------------------------
[  3] local 10.5.17.111 port 60811 connected with 10.5.17.228 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3] 0.0000-1.0000 sec   113 MBytes   944 Mbits/sec
[  3] 1.0000-2.0000 sec   112 MBytes   944 Mbits/sec
[  3] 2.0000-3.0000 sec   112 MBytes   944 Mbits/sec
[  3] 3.0000-4.0000 sec   113 MBytes   944 Mbits/sec
[  3] 4.0000-5.0000 sec   112 MBytes   944 Mbits/sec
[  3] 5.0000-6.0000 sec   113 MBytes   944 Mbits/sec
[  3] 6.0000-7.0000 sec   112 MBytes   944 Mbits/sec
[  3] 7.0000-8.0000 sec   113 MBytes   944 Mbits/sec
[  3] 8.0000-9.0000 sec   112 MBytes   944 Mbits/sec
[  3] 9.0000-10.0000 sec   113 MBytes   944 Mbits/sec
[  3] 10.0000-11.0000 sec   112 MBytes   944 Mbits/sec
[  3] 11.0000-12.0000 sec   113 MBytes   944 Mbits/sec
[  3] 12.0000-13.0000 sec   113 MBytes   944 Mbits/sec
[  3] 13.0000-14.0000 sec   112 MBytes   944 Mbits/sec
[  3] 14.0000-15.0000 sec   113 MBytes   944 Mbits/sec
[  3] 15.0000-16.0000 sec   112 MBytes   944 Mbits/sec
[  3] 16.0000-17.0000 sec   113 MBytes   944 Mbits/sec
[  3] 17.0000-18.0000 sec   113 MBytes   944 Mbits/sec
[  3] 18.0000-19.0000 sec   112 MBytes   944 Mbits/sec
[  3] 19.0000-20.0000 sec   113 MBytes   944 Mbits/sec
[  3] 20.0000-21.0000 sec   112 MBytes   944 Mbits/sec
[  3] 21.0000-22.0000 sec   112 MBytes   944 Mbits/sec
[  3] 22.0000-23.0000 sec   113 MBytes   944 Mbits/sec
[  3] 23.0000-24.0000 sec   113 MBytes   944 Mbits/sec
[  3] 24.0000-25.0000 sec   112 MBytes   944 Mbits/sec
[  3] 25.0000-26.0000 sec   113 MBytes   944 Mbits/sec
[  3] 26.0000-27.0000 sec   113 MBytes   944 Mbits/sec
[  3] 27.0000-28.0000 sec   113 MBytes   944 Mbits/sec
[  3] 28.0000-29.0000 sec   112 MBytes   944 Mbits/sec
[  3] 29.0000-30.0000 sec   112 MBytes   944 Mbits/sec
[  3] 30.0000-31.0000 sec   113 MBytes   944 Mbits/sec
[  3] 31.0000-32.0000 sec   112 MBytes   944 Mbits/sec
[  3] 32.0000-33.0000 sec   113 MBytes   944 Mbits/sec
[  3] 33.0000-34.0000 sec   112 MBytes   944 Mbits/sec
[  3] 34.0000-35.0000 sec   113 MBytes   944 Mbits/sec
[  3] 35.0000-36.0000 sec   112 MBytes   944 Mbits/sec
[  3] 36.0000-37.0000 sec   113 MBytes   944 Mbits/sec
[  3] 37.0000-38.0000 sec   112 MBytes   944 Mbits/sec
[  3] 38.0000-39.0000 sec   113 MBytes   944 Mbits/sec
[  3] 39.0000-40.0000 sec   112 MBytes   944 Mbits/sec
[  3] 40.0000-41.0000 sec   113 MBytes   944 Mbits/sec
[  3] 41.0000-42.0000 sec   112 MBytes   944 Mbits/sec
[  3] 42.0000-43.0000 sec   112 MBytes   944 Mbits/sec
[  3] 43.0000-44.0000 sec   113 MBytes   944 Mbits/sec
[  3] 44.0000-45.0000 sec   113 MBytes   944 Mbits/sec
[  3] 45.0000-46.0000 sec   112 MBytes   944 Mbits/sec
[  3] 46.0000-47.0000 sec   112 MBytes   944 Mbits/sec
[  3] 47.0000-48.0000 sec   113 MBytes   944 Mbits/sec
[  3] 48.0000-49.0000 sec   113 MBytes   944 Mbits/sec
[  3] 49.0000-50.0000 sec   112 MBytes   944 Mbits/sec
[  3] 50.0000-51.0000 sec   112 MBytes   944 Mbits/sec
[  3] 51.0000-52.0000 sec   113 MBytes   944 Mbits/sec
[  3] 52.0000-53.0000 sec   113 MBytes   944 Mbits/sec
[  3] 53.0000-54.0000 sec   112 MBytes   944 Mbits/sec
[  3] 54.0000-55.0000 sec   112 MBytes   944 Mbits/sec
[  3] 55.0000-56.0000 sec   113 MBytes   944 Mbits/sec
[  3] 56.0000-57.0000 sec   113 MBytes   944 Mbits/sec
[  3] 57.0000-58.0000 sec   112 MBytes   944 Mbits/sec
[  3] 58.0000-59.0000 sec   113 MBytes   944 Mbits/sec
[  3] 59.0000-60.0000 sec   113 MBytes   944 Mbits/sec
[  3] 0.0000-60.0001 sec  6.59 GBytes   944 Mbits/sec
[  3] Sent 4814895 datagrams
[  3] Server Report:
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3] 0.0000-60.0015 sec  6.59 GBytes   944 Mbits/sec   0.017 ms    0/4814894 (0%)
root@linaro-alip:/#
```
## Server on AR01A(10.5.17.111)
```c
iperf -u -s
```
```c
root@linaro-alip:/# iperf -u -s
------------------------------------------------------------
Server listening on UDP port 5001
UDP buffer size:  208 KByte (default)
------------------------------------------------------------
[  3] local 10.5.17.111 port 5001 connected with 10.5.17.228 port 52178
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3] 0.0000-59.9971 sec  6.59 GBytes   944 Mbits/sec   0.022 ms  441/4814890 (0.0092%)
```
# Client on Raspi(10.5.17.228)
```c
iperf -u -c 10.5.17.111 -b 900M  -i 1  -w 1M  -t 60 
```
```c
eric@eric-pi:~iperf -u -c 10.5.17.111 -b 900M  -i 1  -w 1M  -t 60
------------------------------------------------------------
Client connecting to 10.5.17.111, UDP port 5001
Sending 1470 byte datagrams, IPG target: 12.46 us (kalman adjust)
UDP buffer size:  416 KByte (WARNING: requested 1.00 MByte)
------------------------------------------------------------
[  1] local 10.5.17.228 port 52178 connected with 10.5.17.111 port 5001
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec   113 MBytes   944 Mbits/sec
[  1] 1.0000-2.0000 sec   112 MBytes   944 Mbits/sec
[  1] 2.0000-3.0000 sec   113 MBytes   944 Mbits/sec
[  1] 3.0000-4.0000 sec   112 MBytes   944 Mbits/sec
[  1] 4.0000-5.0000 sec   112 MBytes   944 Mbits/sec
[  1] 5.0000-6.0000 sec   113 MBytes   944 Mbits/sec
[  1] 6.0000-7.0000 sec   112 MBytes   944 Mbits/sec
[  1] 7.0000-8.0000 sec   113 MBytes   944 Mbits/sec
[  1] 8.0000-9.0000 sec   113 MBytes   944 Mbits/sec
[  1] 9.0000-10.0000 sec   113 MBytes   944 Mbits/sec
[  1] 10.0000-11.0000 sec   112 MBytes   944 Mbits/sec
[  1] 11.0000-12.0000 sec   112 MBytes   944 Mbits/sec
[  1] 12.0000-13.0000 sec   113 MBytes   944 Mbits/sec
[  1] 13.0000-14.0000 sec   112 MBytes   944 Mbits/sec
[  1] 14.0000-15.0000 sec   113 MBytes   944 Mbits/sec
[  1] 15.0000-16.0000 sec   113 MBytes   944 Mbits/sec
[  1] 16.0000-17.0000 sec   112 MBytes   944 Mbits/sec
[  1] 17.0000-18.0000 sec   113 MBytes   944 Mbits/sec
[  1] 18.0000-19.0000 sec   112 MBytes   944 Mbits/sec
[  1] 19.0000-20.0000 sec   113 MBytes   944 Mbits/sec
[  1] 20.0000-21.0000 sec   113 MBytes   944 Mbits/sec
[  1] 21.0000-22.0000 sec   112 MBytes   944 Mbits/sec
[  1] 22.0000-23.0000 sec   112 MBytes   944 Mbits/sec
[  1] 23.0000-24.0000 sec   113 MBytes   944 Mbits/sec
[  1] 24.0000-25.0000 sec   113 MBytes   944 Mbits/sec
[  1] 25.0000-26.0000 sec   112 MBytes   944 Mbits/sec
[  1] 26.0000-27.0000 sec   113 MBytes   944 Mbits/sec
[  1] 27.0000-28.0000 sec   112 MBytes   944 Mbits/sec
[  1] 28.0000-29.0000 sec   112 MBytes   944 Mbits/sec
[  1] 29.0000-30.0000 sec   113 MBytes   944 Mbits/sec
[  1] 30.0000-31.0000 sec   112 MBytes   944 Mbits/sec
[  1] 31.0000-32.0000 sec   113 MBytes   944 Mbits/sec
[  1] 32.0000-33.0000 sec   112 MBytes   944 Mbits/sec
[  1] 33.0000-34.0000 sec   113 MBytes   944 Mbits/sec
[  1] 34.0000-35.0000 sec   113 MBytes   944 Mbits/sec
[  1] 35.0000-36.0000 sec   112 MBytes   944 Mbits/sec
[  1] 36.0000-37.0000 sec   112 MBytes   944 Mbits/sec
[  1] 37.0000-38.0000 sec   113 MBytes   944 Mbits/sec
[  1] 38.0000-39.0000 sec   113 MBytes   944 Mbits/sec
[  1] 39.0000-40.0000 sec   112 MBytes   944 Mbits/sec
[  1] 40.0000-41.0000 sec   113 MBytes   944 Mbits/sec
[  1] 41.0000-42.0000 sec   113 MBytes   944 Mbits/sec
[  1] 42.0000-43.0000 sec   112 MBytes   944 Mbits/sec
[  1] 43.0000-44.0000 sec   113 MBytes   944 Mbits/sec
[  1] 44.0000-45.0000 sec   112 MBytes   944 Mbits/sec
[  1] 45.0000-46.0000 sec   112 MBytes   944 Mbits/sec
[  1] 46.0000-47.0000 sec   112 MBytes   944 Mbits/sec
[  1] 47.0000-48.0000 sec   113 MBytes   944 Mbits/sec
[  1] 48.0000-49.0000 sec   113 MBytes   944 Mbits/sec
[  1] 49.0000-50.0000 sec   113 MBytes   944 Mbits/sec
[  1] 50.0000-51.0000 sec   112 MBytes   944 Mbits/sec
[  1] 51.0000-52.0000 sec   112 MBytes   944 Mbits/sec
[  1] 52.0000-53.0000 sec   113 MBytes   944 Mbits/sec
[  1] 53.0000-54.0000 sec   113 MBytes   944 Mbits/sec
[  1] 54.0000-55.0000 sec   112 MBytes   944 Mbits/sec
[  1] 55.0000-56.0000 sec   113 MBytes   944 Mbits/sec
[  1] 56.0000-57.0000 sec   112 MBytes   944 Mbits/sec
[  1] 57.0000-58.0000 sec   113 MBytes   944 Mbits/sec
[  1] 58.0000-59.0000 sec   113 MBytes   944 Mbits/sec
[  1] 59.0000-60.0000 sec   112 MBytes   944 Mbits/sec
[  1] 0.0000-60.0000 sec  6.59 GBytes   944 Mbits/sec
[  1] Sent 4814891 datagrams
[  1] Server Report:
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  1] 0.0000-59.9971 sec  6.59 GBytes   944 Mbits/sec   0.022 ms 441/4814890 (0.0092%)
```

## Server on AR01A(192.168.1.5)
```c
iperf -u -s
```
```c
root@linaro-alip:/# iperf -u -s -w 512k
------------------------------------------------------------
Server listening on UDP port 5001
UDP buffer size:  416 KByte (WARNING: requested 500 KByte)
------------------------------------------------------------
[  3] local 192.168.1.5 port 5001 connected with 192.168.1.100 port 63753
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3] 0.0000-59.9971 sec  3.19 GBytes   456 Mbits/sec   0.128 ms  78/2327723 (0.0034%)
```
# Client on Windows(192.168.1.100)
```c
iperf -u -c 192.168.1.5 -b 1000M  -i 1  -t 60 -l 1472 -w 512k
```
```c
C:\Users\huide\Desktop\iperf>iperf -u -c 192.168.1.5 -b 1000M  -i 1  -t 60 -l 1472 -w 512k
------------------------------------------------------------
Client connecting to 192.168.1.5, UDP port 5001
Sending 1472 byte datagrams
UDP buffer size:  512 KByte
------------------------------------------------------------
[  3] local 192.168.1.100 port 63753 connected with 192.168.1.5 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 1.0 sec  53.4 MBytes   448 Mbits/sec
[  3]  1.0- 2.0 sec  53.4 MBytes   448 Mbits/sec
[  3]  2.0- 3.0 sec  54.4 MBytes   456 Mbits/sec
[  3]  3.0- 4.0 sec  52.5 MBytes   440 Mbits/sec
[  3]  4.0- 5.0 sec  54.5 MBytes   457 Mbits/sec
[  3]  5.0- 6.0 sec  55.3 MBytes   464 Mbits/sec
[  3]  6.0- 7.0 sec  53.7 MBytes   451 Mbits/sec
[  3]  7.0- 8.0 sec  54.1 MBytes   454 Mbits/sec
[  3]  8.0- 9.0 sec  53.7 MBytes   451 Mbits/sec
[  3]  9.0-10.0 sec  55.2 MBytes   463 Mbits/sec
[  3] 10.0-11.0 sec  55.4 MBytes   464 Mbits/sec
[  3] 11.0-12.0 sec  53.9 MBytes   452 Mbits/sec
[  3] 12.0-13.0 sec  54.8 MBytes   459 Mbits/sec
[  3] 13.0-14.0 sec  53.4 MBytes   448 Mbits/sec
[  3] 14.0-15.0 sec  54.6 MBytes   458 Mbits/sec
[  3] 15.0-16.0 sec  55.2 MBytes   463 Mbits/sec
[  3] 16.0-17.0 sec  55.5 MBytes   465 Mbits/sec
[  3] 17.0-18.0 sec  53.5 MBytes   449 Mbits/sec
[  3] 18.0-19.0 sec  54.7 MBytes   459 Mbits/sec
[  3] 19.0-20.0 sec  54.3 MBytes   455 Mbits/sec
[  3] 20.0-21.0 sec  53.1 MBytes   445 Mbits/sec
[  3] 21.0-22.0 sec  53.8 MBytes   451 Mbits/sec
[  3] 22.0-23.0 sec  53.9 MBytes   453 Mbits/sec
[  3] 23.0-24.0 sec  55.1 MBytes   462 Mbits/sec
[  3] 24.0-25.0 sec  54.2 MBytes   454 Mbits/sec
[  3] 25.0-26.0 sec  54.4 MBytes   457 Mbits/sec
[  3] 26.0-27.0 sec  54.4 MBytes   456 Mbits/sec
[  3] 27.0-28.0 sec  55.4 MBytes   465 Mbits/sec
[  3] 28.0-29.0 sec  54.6 MBytes   458 Mbits/sec
[  3] 29.0-30.0 sec  55.6 MBytes   466 Mbits/sec
[  3] 30.0-31.0 sec  53.9 MBytes   452 Mbits/sec
[  3] 31.0-32.0 sec  55.2 MBytes   463 Mbits/sec
[  3] 32.0-33.0 sec  55.2 MBytes   463 Mbits/sec
[  3] 33.0-34.0 sec  54.3 MBytes   456 Mbits/sec
[  3] 34.0-35.0 sec  54.7 MBytes   459 Mbits/sec
[  3] 35.0-36.0 sec  54.4 MBytes   457 Mbits/sec
[  3] 36.0-37.0 sec  54.8 MBytes   460 Mbits/sec
[  3] 37.0-38.0 sec  54.9 MBytes   460 Mbits/sec
[  3] 38.0-39.0 sec  55.1 MBytes   462 Mbits/sec
[  3] 39.0-40.0 sec  54.8 MBytes   460 Mbits/sec
[  3] 40.0-41.0 sec  53.8 MBytes   452 Mbits/sec
[  3] 41.0-42.0 sec  55.0 MBytes   462 Mbits/sec
[  3] 42.0-43.0 sec  54.2 MBytes   454 Mbits/sec
[  3] 43.0-44.0 sec  54.8 MBytes   460 Mbits/sec
[  3] 44.0-45.0 sec  54.3 MBytes   455 Mbits/sec
[  3] 45.0-46.0 sec  54.5 MBytes   457 Mbits/sec
[  3] 46.0-47.0 sec  55.3 MBytes   464 Mbits/sec
[  3] 47.0-48.0 sec  54.5 MBytes   457 Mbits/sec
[  3] 48.0-49.0 sec  54.7 MBytes   459 Mbits/sec
[  3] 49.0-50.0 sec  53.8 MBytes   451 Mbits/sec
[  3] 50.0-51.0 sec  55.6 MBytes   466 Mbits/sec
[  3] 51.0-52.0 sec  52.4 MBytes   440 Mbits/sec
[  3] 52.0-53.0 sec  55.5 MBytes   465 Mbits/sec
[  3] 53.0-54.0 sec  55.3 MBytes   464 Mbits/sec
[  3] 54.0-55.0 sec  54.4 MBytes   456 Mbits/sec
[  3] 55.0-56.0 sec  54.6 MBytes   458 Mbits/sec
[  3] 56.0-57.0 sec  54.4 MBytes   456 Mbits/sec
[  3] 57.0-58.0 sec  54.6 MBytes   458 Mbits/sec
[  3] 58.0-59.0 sec  54.8 MBytes   460 Mbits/sec
[  3] 59.0-60.0 sec  54.0 MBytes   453 Mbits/sec
[  3]  0.0-60.0 sec  3.19 GBytes   457 Mbits/sec
[  3] Sent 2327724 datagrams
```

## Server on AR01A(192.168.1.5)
```c
iperf -u -s
```
```c
root@linaro-alip:/# iperf -u -s -w 8M
------------------------------------------------------------
Server listening on UDP port 5001
UDP buffer size:  416 KByte (WARNING: requested 500 KByte)
------------------------------------------------------------
[  3] local 10.5.17.111 port 5001 connected with 10.5.17.100 port 63753
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3] 0.0000-10.0072 sec  643 MBytes   539 Mbits/sec   0.179 ms  50/458837 (0.0011%)
```
# Client on Windows(192.168.1.100)
```c
iperf -u -c 192.168.1.5 -b 1000M  -i 1  -t 60 -l 1472 -w 512k
```
```c
C:\Users\huide\Desktop\iperf>iperf -u -c 10.5.17.111 -b 12000M  -i 1 -l 1470 -w 416k
------------------------------------------------------------
Client connecting to 10.5.17.111, UDP port 5001
Sending 1470 byte datagrams
UDP buffer size:  416 KByte
------------------------------------------------------------
[  3] local 10.5.17.100 port 62131 connected with 10.5.17.111 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 1.0 sec  64.8 MBytes   544 Mbits/sec
[  3]  1.0- 2.0 sec  63.7 MBytes   534 Mbits/sec
[  3]  2.0- 3.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  3.0- 4.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  4.0- 5.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  5.0- 6.0 sec  63.6 MBytes   534 Mbits/sec
[  3]  6.0- 7.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  7.0- 8.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  8.0- 9.0 sec  63.6 MBytes   534 Mbits/sec
[  3]  9.0-10.0 sec  64.6 MBytes   542 Mbits/sec
[  3]  0.0-10.0 sec   643 MBytes   539 Mbits/sec
[  3] Sent 458838 datagrams

```
# UDP test
```c
netstat -s -u

cat /proc/sys/net/core/rmem_max
sudo sysctl -w net.core.rmem_max=67108864 # 设置为 64M
sudo sysctl -w net.core.netdev_max_backlog=6000
sudo sysctl -w net.core.rmem_default = 10485760 # 10MB 默认值也适当增大
```


# Reference
[iperf详细使用方法](https://blog.csdn.net/peijian1998/article/details/26563957)