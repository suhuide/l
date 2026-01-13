[memo.md](memo.md)  

[蓝思科技_LS_MMI指令详细定义_RK3566](http://10.5.103.101:5080/xt002/xt002_doc/-/blob/main/01_%E8%A7%84%E8%8C%83%E6%A0%87%E5%87%86/%E8%93%9D%E6%80%9D%E7%A7%91%E6%8A%80_LS_MMI%E6%8C%87%E4%BB%A4%E8%AF%A6%E7%BB%86%E5%AE%9A%E4%B9%89_RK3655_.md)  
[ITX-3588J](https://www.t-firefly.com/doc/download/160.html)  
[Core-3588J Manual](https://wiki.t-firefly.com/zh_CN/Core-3588J/index.html)  
[ROC-RK3566-PC](https://wiki.t-firefly.com/zh_CN/ROC-RK3566-PC/)  
[PCIe 使用](https://wiki.t-firefly.com/zh_CN/ROC-RK3588-RT/usage_pcie.html)   

| 1 | 2 | 3 | 4 | 5 | 6 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| |[rk3588](rk3588.md)|[rk356x-prop](rk356x-prop.md)  |
|[bt-lib](bt-lib.md)|[s06g-gpio](../S06G/S06G_SCH/gpio.md)|[s06g-bt](../S06G/driver/bt.md)|[s06g-zigbee](../S06G/driver/zigbee.md)|[s06g-pwm](../S06G/driver/pwm.md)|[s06g-uart](../S06G/driver/uart.md)|

```c
adb shell lscmd cmd_setsn,2,1,000044311115PD073012LENS666CS228
adb shell getprop ro.serialno
```

```c
adb disable-verity&&adb reboot
adb root&&adb remount
C:\Users\sz000062\Desktop>adb disable-verity
verity is already disabled

C:\Users\sz000062\Desktop>adb reboot

C:\Users\sz000062\Desktop>adb root
adb: unable to connect for root: no devices/emulators found

C:\Users\sz000062\Desktop>adb root
adb: unable to connect for root: no devices/emulators found

C:\Users\sz000062\Desktop>adb root
restarting adbd as root

C:\Users\sz000062\Desktop>adb remount
remount succeeded
```

```c
cd ${workspace}
mkdir -p s06g && cd s06g

repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo

repo sync -j8

ls@ls-VirtualBox:~$ 
cd /data/
ls
cd s06g/
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
repo sync -j8
source build/envsetup.sh
lunch rk3566_r-userdebug
./build.sh -AUCKu
ls -l
df -h
```c
sudo /etc/init.d/network-manager restart

export IS_BUILD_FACTORY_VERSION=true
export IS_BUILD_FACTORY_VERSION=false
source build/envsetup.sh; lunch rk3566_r-userdebug; ./build.sh -AUCKu
source build/envsetup.sh; lunch rk3566_r-userdebug; ./build.sh -UKAup -J32
```
```c
CPU:
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
interactive
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq
1800000(CPU,1.8GHz)

DDR:
cat /sys/class/devfreq/dmc/governor
dmc_ondemand
cat /sys/class/devfreq/dmc/cur_freq
528000000(DDR,528MHz)

EMMC:
cat /sys/kernel/debug/mmc1/ios
clock:          200000000 Hz
actual clock:   198000000 Hz
vdd:            21 (3.3 ~ 3.4 V)
bus mode:       2 (push-pull)
chip select:    0 (don't care)
power mode:     2 (on)
bus width:      2 (4 bits)
timing spec:    6 (sd uhs SDR104)
signal voltage: 1 (1.80 V)
driver type:    0 (driver type B)
```
```c
cd kernel
make ARCH=arm64 rockchip_defconfig rk356x_evb.config android-11.config; make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img rk3566-evb2-lp4x-v10.img -j24
make ARCH=arm64 rockchip_defconfig android-11.config; make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img rk3566-evb2-lp4x-v10.img -j24
```

```c
[  338.664005] init: starting service 'filecopy'...
[  338.668833] init: cannot execv('/system/bin/zigbee/filecopy.sh'). See the 'Debugging init' section of init's README.md for tips: Permission denied
[  338.669591] type=1400 audit(1706086991.593:96): avc: denied { entrypoint } for comm="init" path="/system/bin/zigbee/filecopy.sh" dev="dm-0" ino=1852 scontext=u:r:shell:s0 tcontext=u:object_r:system_file:s0 tclass=file permissive=0
```

```c
rk3566_r:/data/midea $ logcat | grep filecopy
02-21 06:13:03.240  2081  2081 W ls      : type=1400 audit(0.0:1054): avc: denied { getattr } for path="/vendor/bin/lens/filecopy.sh" dev="dm-2" ino=325 scontext=u:r:shell:s0 tcontext=u:object_r:filecopy_exec:s0 tclass=file permissive=0

C:\Users\sz000062\Desktop>adb shell
adb server version (40) doesn't match this client (41); killing...
* daemon started successfully
rk3566_r:/ $ logcat | grep filecopy
02-21 06:35:57.500  2000  2000 W sh      : type=1400 audit(0.0:1041): avc: denied { execute } for name="filecopy.sh" dev="dm-2" ino=325 scontext=u:r:shell:s0 tcontext=u:object_r:filecopy_exec:s0 tclass=file permissive=0

C:\Users\sz000062\Desktop>adb shell
adb server version (40) doesn't match this client (41); killing...
* daemon started successfully
rk3566_r:/ $ logcat | grep filecopy
02-21 06:53:05.676  2013  2013 W sh      : type=1400 audit(0.0:1049): avc: denied { read open } for path="/vendor/bin/lens/filecopy.sh" dev="dm-2" ino=325 scontext=u:r:shell:s0 tcontext=u:object_r:filecopy_exec:s0 tclass=file permissive=0
```
```c
allow shell filecopy_exec:file { getattr execute read open};
```