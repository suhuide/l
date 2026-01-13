[memo](memo.md)

| 1 | 2 | 3 | 4 | 5 | 6 |
| ---- | ---- | ---- | ---- | ---- | ---- |
|[GNSS](AR01A-gnss.md)|[Ethernet](AR01A-ethernet.md)|[PTP](AR01A-ptp.md) |[AR01A-app-debian](AR01A-app-debian.md)|[AR01A-app-KSZ](AR01A-app-KSZ.md)|[AR01A-My-app](AR01A-My-app.md)|
|[5G](AR01A-5G.md)|

# Pull code from remote repo
## Zip and unzip
```c
tar -cvzf - rk3588_linux_sdk/ | split -d -b 4000M - ar01a.tar.gz.part
cat ar01a.tar.gz.part* | tar -xvzf -
```
# Configure compile environment
- python要求安装python 3.6及以上版本，此处以python 3.6为例。  
- make要求安装 make 4.0及以上版本，此处以 make 4.2为例。  
- lz4要求安装 lz4 1.7.3及以上版本。  
```c
sudo apt-get update && sudo apt-get install git ssh make gcc libssl-dev \
liblz4-tool expect expect-dev g++ patchelf chrpath gawk texinfo chrpath \
diffstat binfmt-support qemu-user-static live-build bison flex fakeroot \
cmake gcc-multilib g++-multilib unzip device-tree-compiler ncurses-dev \
libgucharmap-2-90-dev bzip2 expat gpgv2 cpp-aarch64-linux-gnu libgmp-dev \
libmpc-dev bc python-is-python3 python2
```
## Pull
```c
repo init -u ssh://gerrit/lens/manifest -b AR01A  -m ar01a_debian11_rk3588s2.xml --repo-url=ssh://gerrit/lens/git_repo -c --no-repo-verify&&repo sync -j8 -c
```
### T1
```c
repo init -u ssh://gerrit/lens/manifest -b AR01A  -m ar01a-t1_debian11_rk3588s2.xml --repo-url=ssh://gerrit/lens/git_repo -c --no-repo-verify&&repo sync -j8 -c
```

## Commit
```c
git branch -r
git add 
git commit -m "[TASK_16507][AR01A] xxx"
git push rk HEAD:refs/for/debian11/rk3588s2/ar01a/main%r=SZ000008
```

# Build
## Linux
```c
./build.sh lunch:rockchip_rk3588s_evb4_lp4x_v10_defconfig
./build.sh
```
## Debian
```c
// run only once is OK
sudo dpkg -i debian/ubuntu-build-service/packages/*
sudo apt-get install -f
```
```c
./build.sh debian
```

## package
```c
./build.sh updateimg
```
## clean
```c
./build.sh cleanall
./build.sh clean:kernel
```
## buildroot app
```c
make show-targets
alsa-lib alsa-plugins alsa-ucm-conf alsa-utils android-adbd at-spi2-core bash bluez-alsa bluez5_utils bluez5_utils-headers busybox ca-certificates 
cairo camera-engine-rkaiq can-utils chromium-wayland chrony coreutils dbus dejavu dhcpcd dhrystone dnsmasq dosfstools dropbear e2fsprogs ethtool 
eudev evtest exfat exfat-utils expat faad2 fatresize fio flac fluidsynth font-awesome fontconfig freetype gcc-final gdk-pixbuf gesftpserver glibc 
glmark2 gst1-plugins-bad gst1-plugins-base gst1-plugins-good gst1-plugins-ugly gstreamer1 gstreamer1-rockchip harfbuzz host-acl host-attr 
host-autoconf host-automake host-ccache host-cmake host-e2fsprogs host-environment-setup host-eudev host-fakeroot host-libtool host-libzlib 
host-lz4 host-lzo host-m4 host-makedevs host-mkpasswd host-ntfs-3g host-patchelf host-pkgconf host-python3 host-skeleton host-squashfs host-tar 
host-util-linux host-xz host-zlib host-zstd hostapd i2c-tools ifupdown-scripts initscripts input-event-daemon iozone iperf iperf3 iputils iw jpeg 
jpeg-turbo kmod libbsd libcap libdrm liberation libevdev libffi libfribidi libfuse3 libglib2 libgudev libidn2 libinput liblockfile libmad libmpeg2 
libnl libnspr libnss libogg libopenssl libpcap libpng libpsl libpthread-stubs libsamplerate libsndfile libsoup3 libtheora libtirpc libtool 
libunistring libv4l libv4l-rkmpp libvorbis libvpx libxkbcommon libxml2 libxslt libzlib linux-headers linuxptp lmbench lockfile-progs lrzsz make 
memtester mjpegtools mmc-utils mpg123 mtdev ncurses nghttp2 nmea ntfs-3g numactl openssl opus pango parted pcre2 perl pixman pm-utils procps-ng 
procrank_linux pulseaudio readline rknpu2 rkscript rktoolkit rkwifibt rkwifibt-app rockchip-alsa-config rockchip-mali rockchip-mpp rockchip-rga 
rockchip-test rt-tests rtmpdump sbc skeleton skeleton-init-common skeleton-init-sysv source-han-sans-cn sox sqlite strace stress stress-ng 
stressapptest tcpdump toolchain toolchain-buildroot unixbench urandom-scripts usbmount util-linux util-linux-libs wayland wayland-protocols 
wayland-utils webp weston whetstone wireless_tools wpa_supplicant xkeyboard-config zlib rootfs-cpio rootfs-ext2 rootfs-squashfs rootfs-tar

```
```c
rm -rf ./buildroot/output/rockchip_rk3588/build/nmea-1.0.0
make nmea-rebuild

```

# Flash
```c
//kernel
./kernel/boot.img
//uboot
./u-boot/uboot.img
//Image location
./rockdev/update.img
```
# OTA
## adb
```c
adb connect 192.168.1.5:5555
adb shell
adb push ....
```
### adb push them update(recommend)
```c
adb push update.img /userdata/
```
```c
adb shell
updateEngine --image_url=/userdata/update.img --misc=update --savepath=/userdata/update.img --reboot &
```
## HTTP 
```c
python3 -m http.server 8080 --bind 192.168.1.111
```
### update from http server
```c
updateEngine image_url=http://192.168.1.111:8080/update.img --misc=update --savepath=/userdata/update.img --reboot
```

## Log
```c
root@rk3588s-buildroot:/# updateEngine --image_url=/userdata/update.img --misc=update --savepath=/userdata/update.img --reboot &
[1] 1708
root@rk3588s-buildroot:/# LOG_INFO: *** update_engine: V1.0.1-g63aaba9-250409 ***.
LOG_INFO: Current Mode is recovery.
LOG_INFO: start RK_ota_url url [/userdata/update.img] save path [/userdata/update.img].
LOG_INFO: save image to /userdata/update.img.
LOG_INFO: url = /userdata/update.img.
LOG_INFO: [MiscUpdate:90] save path: /userdata/update.img
LOG_INFO: update recovery in normal system.
//...
LOG_INFO: RK_ota_start is ok!LOG_INFO: rk ota success.
LOG_INFO: Current Mode is recovery.
LOG_INFO: rk m_status = 0.
LOG_INFO: Current device is not MTD
```

# Coding
## Configuration
```c
./buildroot/configs/rockchip_rk3588_defconfig
./buildroot/package/Config.in
```
```c
//Main dts
./kernel/arch/arm64/boot/dts/rockchip/rk3588s-evb4-lp4x.dtsi
//Customize config
./kernel/arch/arm64/configs/rk3588_linux.config
```
## Ethernet(Switch)
```c
./kernel/drivers/net/ethernet/micrel/
./kernel/drivers/net/ethernet/stmicro/stmmac
```


# Clock
```c
root@linaro-alip:/boot/grub# dmesg | grep -i "clock\|timer\|oscillator\|clk"
[    1.677867] arch_timer: cp15 timer(s) running at 24.00MHz (phys).
[    1.678429] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[    1.679417] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    1.681683] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=80000)
[    1.757746] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 6370867519511994 ns
[    1.827877] PTP clock support registered
[    1.830579] clocksource: Switched to clocksource arch_sys_counter
[    2.126830] rkvdec2_init:1024: No niu aclk reset resource define
[    2.126836] rkvdec2_init:1027: No niu hclk reset resource define
[    2.127400] rkvdec2_init:1024: No niu aclk reset resource define
[    2.127407] rkvdec2_init:1027: No niu hclk reset resource define
[    2.195673] rk_gmac-dwmac fe1c0000.ethernet: clock input or output? (output).
[    2.195708] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_rx
[    2.195713] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock mac_clk_tx
[    2.195723] rk_gmac-dwmac fe1c0000.ethernet: cannot get clock clk_mac_speed
[    2.196078] rk_gmac-dwmac fe1c0000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.863599] es7243l_probe: start to get mclk
[    3.863640] es7243l_probe: got mclk successfully
[    3.864066] es7243l_probe(), read CLK2 before setting
[    3.864714] es7243l_probe(), CLK2=0x00
[    4.094461] Enter into es7243l_set_dai_sysclk(), freq = 12288000
[    4.395057] systemd[1]: System time before build time, advancing clock.
[    5.691013] rk_gmac-dwmac fe1c0000.ethernet eth_to_adu: registered PTP clock
[    7.732199] Enter into es7243l_set_dai_sysclk(), freq = 12288000
[    7.990877] Enter into es7243l_set_dai_sysclk(), freq = 0
[    7.997215] Enter into es7243l_set_dai_sysclk(), freq = 0
[    7.997807] Enter into es7243l_set_dai_sysclk(), freq = 0
[    7.998414] Enter into es7243l_set_dai_sysclk(), freq = 0
[    7.999111] Enter into es7243l_set_dai_sysclk(), freq = 0
[    7.999565] Enter into es7243l_set_dai_sysclk(), freq = 12288000
[    8.245519] Enter into es7243l_set_dai_sysclk(), freq = 0
[    8.256430] Enter into es7243l_set_dai_sysclk(), freq = 12288000
[   13.539632] Enter into es7243l_set_dai_sysclk(), freq = 0

```

主时钟源 arch_timer: cp15 timer(s) running at 24.00MHz (phys).
```c
   1.677867] arch_timer: cp15 timer(s) running at 24.00MHz (phys).
```
这是最核心的一行！

arch_timer：ARM 架构定时器（Generic Timer）
cp15：协处理器 15，ARM 内部定时器接口
24.00MHz：硬件计数器频率
(phys)：物理计数器（Physical Timer）
说明系统有一个 24MHz 的定时器时钟源，作为主时间基准

CLOCK_MONOTONIC_RAW 直接来自 arch_sys_counter(24MHz)

