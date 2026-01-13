[memo.md](memo.md) 

Upper level code

# Code

app_utils.c


# PTP
[Linux 使用 PTP 进行时间同步](https://blog.csdn.net/yiyu20180729/article/details/136341012)   
[用ptp4l和phc2sys实现系统时钟同步](https://blog.csdn.net/v6543210/article/details/129090770)   
[linuxptp产生pps相关接口](https://blog.csdn.net/a459688264/article/details/125622833)   
[Linux时间同步(PPS、PTP、chrony)分析笔记](https://blog.csdn.net/u010936265/article/details/135648077)  
[验证时间同步](https://docs.redhat.com/zh-cn/documentation/red_hat_enterprise_linux/7/html/system_administrators_guide/sec-verifying_time_synchronization)
## Ubuntu
在 Linux 系统中，PTP 协议的实际实现称为 LinuxPTP，它是 PTPv2 根据 Linux 的 IEEE 1588 标准实现的。
在 LinuxPTP 软件包包括 ptp4l 和 phc2sys 用于时钟同步的程序，
ptp4l 程序实现了 PTP 边界时钟和普通时钟，支持硬件时钟同步和软件时间同步，
硬件时间戳用于将 PTP 硬件时钟与主时钟同步，软件时间戳用于将系统时钟与主时钟同步。
phc2sys 程序则用于将系统时钟同步到网卡上的 PTP 硬件时钟（PHC）。
```c
sudo ip link set eth0 up
sudo systemctl restart systemd-networkd
ifconfig
```
```c
sudo apt install linuxptp
ptp4l -v
```
```c
sudo ethtool -T eth0
Time stamping parameters for eth0:
Capabilities:
	hardware-transmit     (SOF_TIMESTAMPING_TX_HARDWARE)
	software-transmit     (SOF_TIMESTAMPING_TX_SOFTWARE)
	hardware-receive      (SOF_TIMESTAMPING_RX_HARDWARE)
	software-receive      (SOF_TIMESTAMPING_RX_SOFTWARE)
	software-system-clock (SOF_TIMESTAMPING_SOFTWARE)
	hardware-raw-clock    (SOF_TIMESTAMPING_RAW_HARDWARE)
PTP Hardware Clock: 0
Hardware Transmit Timestamp Modes:
	off                   (HWTSTAMP_TX_OFF)
	on                    (HWTSTAMP_TX_ON)
	one-step-sync         (HWTSTAMP_TX_ONESTEP_SYNC)
Hardware Receive Filter Modes:
	none                  (HWTSTAMP_FILTER_NONE)
	all                   (HWTSTAMP_FILTER_ALL)

//对于软件时间戳支持，参数列表应包括：
SOF_TIMESTAMPING_SOFTWARE
SOF_TIMESTAMPING_TX_SOFTWARE
SOF_TIMESTAMPING_RX_SOFTWARE
//对于硬件时间戳支持，参数列表应包括：
SOF_TIMESTAMPING_RAW_HARDWARE
SOF_TIMESTAMPING_TX_HARDWARE
SOF_TIMESTAMPING_RX_HARDWARE   
```

```c
sudo systemctl status ptp4l
sudo systemctl start ptp4l
sudo systemctl enable ptp4l
sudo systemctl disable ptp4l
```
```c
sudo systemctl status phc2sys
sudo systemctl start phc2sys
sudo systemctl enable phc2sys
sudo systemctl disable phc2sys
```
```c
//HW
sudo ptp4l -m -H -i eth0
sudo ptp4l -m -H -s -i eth0
//SW
sudo ptp4l -m -S -i eth0
sudo ptp4l -m -S -s -i eth0
```
```c
场景 1：将 PHC 同步到系统时钟
假设 PHC 设备为 phc0，将 PHC 时间同步到系统时钟：

bash
sudo phc2sys -s phc0 -c CLOCK_REALTIME -w -m
-s phc0：源时钟为 phc0（硬件时钟）。

-c CLOCK_REALTIME：目标时钟为系统时钟。

-w：等待 PTP 时钟同步完成。

-m：打印同步信息到终端。
```
```c
场景 2：将系统时钟同步到 PHC
反向同步（例如系统时钟作为时间源）：

bash
sudo phc2sys -c phc0 -s CLOCK_REALTIME -w -m
场景 3：通过网卡接口同步
直接使用网卡（如 eth0）的 PHC 同步到系统时钟：

bash
sudo phc2sys -S eth0 -c CLOCK_REALTIME -w -m
```
```c
场景 4：主从模式（Master/Slave）
主节点（Master）同步 PHC 到系统时钟：

bash
sudo phc2sys -s phc0 -c CLOCK_REALTIME -w -m
从节点（Slave）从主节点同步：

bash
sudo phc2sys -s <主节点PHC> -c CLOCK_REALTIME -r -w -m
-r：从模式运行。
```
```c
5. 验证同步状态

sudo hwclock --compare

timedatectl
```
```c
sudo phc_ctl /dev/ptp0 SETTIME "$(date +%s)"
sudo phc_ctl /dev/ptp0 GETTIME
```
```c
timedatectl set-timezone Etc/UTC
timedatectl set-timezone Asia/Shanghai
timedatectl set-timezone America/Chicago
timedatectl set-time "2025-05-22 14:30:40"
date 052214302025.30
```
```c
eric@eric-pi:~$ sudo hwclock --compare
eric@eric-pi:~$ date
Fri May 23 14:28:22 CST 2025
eric@eric-pi:~$ sudo timedatectl set-timezone Etc/UTC
eric@eric-pi:~$ date
Fri May 23 06:29:16 UTC 2025
```