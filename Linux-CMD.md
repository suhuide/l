[memo.md](memo.md)
```c
mkfs [-V] [-t fstype][fs-options]
mkfs.vfat

fdisk /dev/hdb
mkfs.vfat /dev/hdb1
mount /dev/hdb1 /data

//查看分区
cat /proc/partitions
```
```c
//文件夹下的文件个数
ls -lR|grep "^-"|wc -l

//文件数
find . -name "*.c"|wc -l
//行数
find . -name "*.c" -or  -name "*.h" | xargs cat|wc -l
//行数(除空白行)
find . -name "*.c" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
find . -name "*.cpp" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
```
```c
uname -srm
```
```c
//在当前目录及其子目录的php文件中查找include字符串
find -name '*.php'|xargs grep 'include'
find -name '*.html'|xargs grep 'EMU_DCDCInit '
find . -name '*.php' -exec grep -i -nH "include" {} \
find -name '*.c'|xargs grep 'CRYPTO_AES_CTRx'
find -name '*.c'|xargs grep 'TUM'
find -name '*.c'|xargs grep 'halGetStandaloneBootloaderVersion'
find -name "*.sh" -o -name "*.mk" | xargs grep -l "linaro"
find -name "*.sh" -o -name "*.mk" | xargs grep -l "useradd"
```
```c
fdisk -l

sudo umount /dev/sda1
sudo mkfs.vfat -F 32 /dev/sda1
sudo mkfs.ext4 /dev/sda1
```
```c
ls /dev/sd*
/dev/sdb /dev/sdb1
dd if=/dev/urandom of=/dev/sdb bs=4k status=progress
```
```c
sudo apt-get install libssl-dev

(initramfs) fsck /dev/sda1 -y
(initramfs) reboot
```
```c
top
ps aux | less
pstree

grep -o '@' documentERROR.txt | wc -l
grep 'LFXO' *.txt #显示在*.txt文件中包含LFXO的行

tar -xvf archive.tar.xz
```
```c
1、查看串口是否可用
   可以对串口发送数据比如对com1口，echo /dev/ttyS0
2、查看串口名称使用
   ls -l /dev/ttyS*
  一般情况下串口的名称全部在dev下面，如果你没有外插串口卡的话默认是dev下的ttyS*,一般ttyS0对应com1，   ttyS1对应com2，当然也不一定是必然的；
3、查看串口驱动
   cat/proc/tty/drivers/serial
4、查看串口设备
   dmesg | grep ttyS*
5、查一下板子上的串口有没有设备
   grep tty/proc/devices
```
```c
lsusb | grep -i bluetooth 

Bluetooth Debuging 
暴力探测蓝牙设备工具 redfang
$ sudo hcidump -i hci0
$ sudo btmon
$ sudo btattach -B /dev/ttyACM0 -S 1000000 //Maybe it is for Zephyr only
hciattach -t 30 -s 115200 /dev/ttyS0 any



$ bluetoothctl -v
hciconfig
hcitool
```
```c
Win11和Ubuntu实现Samba共享文件

一、Ubuntu开启Samba服务器 
sudo apt-get install samba samba-common
二、Ubuntu配置共享目录和用户权限 
	1.创建用于共享的Samba目录 
	mkdir -p ~/share
	2.给创建的待共享目录设置权限
	chmod -R 777~/share
	3.配置Samba的配置文件
	# 打开配置文件
	sudo vim /etc/samba/smb.conf
	# 在配置文件smb.conf最后添加下面的内容（[]中是待共享目录的文件名，path是带共享目录的绝对路径）
	[share]
	comment = share folder
	browseable = yes
	path = /home/{username}/share
	create mask = 0700
	directory mask = 0700
	valid user = ls
	force user = ls
	force group = ls
	public = yes
	available = yes
	writable = yes
 
	4.重启Samba服务器
	sudo service smbd restart
	# 或者/etc/init.d/samba restart

三、访问
Ubuntu, ifconifg 看IP
Windows ,直接访问ip地址即可
```

```c
du -sh
ls@ls-VirtualBox:/s06g$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev             16G     0   16G   0% /dev
tmpfs           3.2G  3.2M  3.2G   1% /run
/dev/sda1       295G  116G  164G  42% /
tmpfs            16G     0   16G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs            16G     0   16G   0% /sys/fs/cgroup
/dev/sdb        570G  170G  372G  32% /s06g
/dev/loop1       41M   41M     0 100% /snap/snapd/20671
/dev/loop2      219M  219M     0 100% /snap/gnome-3-34-1804/72
/dev/loop3      486M  486M     0 100% /snap/gnome-42-2204/126
/dev/loop4       92M   92M     0 100% /snap/gtk-common-themes/1535
/dev/loop5      497M  497M     0 100% /snap/gnome-42-2204/141
/dev/loop6      2.3M  2.3M     0 100% /snap/gnome-calculator/955
/dev/loop7       56M   56M     0 100% /snap/core18/2823
/dev/loop0       39M   39M     0 100% /snap/snapd/21759
/dev/loop8      350M  350M     0 100% /snap/gnome-3-38-2004/143
/dev/loop9      896K  896K     0 100% /snap/gnome-logs/123
/dev/loop10      75M   75M     0 100% /snap/core22/1380
/dev/loop11     219M  219M     0 100% /snap/gnome-3-34-1804/93
/dev/loop12     2.2M  2.2M     0 100% /snap/gnome-calculator/950
/dev/loop13      64M   64M     0 100% /snap/core20/2318
/dev/loop14      64M   64M     0 100% /snap/core20/2182
/dev/loop15      56M   56M     0 100% /snap/core18/2812
/dev/loop16     640K  640K     0 100% /snap/gnome-characters/797
/dev/loop17     1.5M  1.5M     0 100% /snap/gnome-system-monitor/184
/dev/loop18      66M   66M     0 100% /snap/gtk-common-themes/1515
/dev/loop19     1.7M  1.7M     0 100% /snap/gnome-system-monitor/186
/dev/loop20     896K  896K     0 100% /snap/gnome-logs/121
/dev/loop21      74M   74M     0 100% /snap/core22/864
/dev/loop22     512K  512K     0 100% /snap/gnome-characters/795
/dev/loop23     242M  242M     0 100% /snap/gnome-3-38-2004/70
/dev/loop24     128K  128K     0 100% /snap/bare/5
tmpfs           3.2G   28K  3.2G   1% /run/user/121
tmpfs           3.2G   44K  3.2G   1% /run/user/1000

```
```c
eric@ubuntu:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens33: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:b3:92:39 brd ff:ff:ff:ff:ff:ff
eric@ubuntu:~$ sudo ip link set ens33 up
eric@ubuntu:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:b3:92:39 brd ff:ff:ff:ff:ff:ff
eric@ubuntu:~$ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::20c:29ff:feb3:9239  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:b3:92:39  txqueuelen 1000  (Ethernet)
        RX packets 6  bytes 1282 (1.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 20  bytes 3397 (3.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 235884  bytes 16749997 (16.7 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 235884  bytes 16749997 (16.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
Reset network
```c
eric@ubuntu:~$ sudo ifconfig ens33 192.168.1.100 netmask 255.255.255.0 up
eric@ubuntu:~$ sudo systemctl restart networking
eric@ubuntu:~$ ifconfig

sudo service network-manager stop
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service network-manager start
```
查看网卡支持频段
```c

ubuntu@ubuntu:~$ iwlist wlan0 freq
wlan0     22 channels in total; available frequencies :
          Channel 01 : 2.412 GHz
          Channel 02 : 2.417 GHz
          Channel 03 : 2.422 GHz
          Channel 04 : 2.427 GHz
          Channel 05 : 2.432 GHz
          Channel 06 : 2.437 GHz
          Channel 07 : 2.442 GHz
          Channel 08 : 2.447 GHz
          Channel 09 : 2.452 GHz
          Channel 10 : 2.457 GHz
          Channel 11 : 2.462 GHz
          Channel 12 : 2.467 GHz
          Channel 13 : 2.472 GHz
          Channel 36 : 5.18 GHz
          Channel 40 : 5.2 GHz
          Channel 44 : 5.22 GHz
          Channel 48 : 5.24 GHz
          Channel 149 : 5.745 GHz
          Channel 153 : 5.765 GHz
          Channel 157 : 5.785 GHz
          Channel 161 : 5.805 GHz
          Channel 165 : 5.825 GHz
          Current Frequency:2.437 GHz (Channel 6)
```