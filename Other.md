[memo.md](memo.md) 
```c
init PW: XT.lens123

http://10.5.103.101:9080
@E.1

http://10.5.113.213:8080
@e.1

Qcom
https://support.qualcomm.com/s/case/Case/Default
sz000062@hnlens.com
Exxxxxx1

MTK
https://online.mediatek.com/
andy.qian@hnlens.com
ZAQ!xsw2
9512083476

```
```c
https://atmosic.com/products_atm33/

Username or Email Address：
gavin.huang@hnlens.com
Password：
Lens20250430@
```
```c
gnome-screenshot -a
```
```c
# remove all working directory(and staged) changes
repo forall -c 'git reset --hard'
# clean untracked files
repo forall -c 'git clean -f -d'
```
```c
# sync
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
repo sync -j8
```
```c
# repo location
repo forall  "platform/mkcombinedroot" -c 'echo $REPO_PATH'

http://10.5.103.101:8010/c/qcom/t_vendor/Turbox_C8550/release/platform/platform_testing/+/46823
repo forall "Turbox_C8550/release/platform/platform_testing" -c 'echo $REPO_PATH'
ls@ls-VirtualBox:/data/sm8550$ repo forall "Turbox_C8550/release/platform/platform_testing" -c 'echo $REPO_PATH'
vendor/LA.VENDOR.13.2.6/LINUX/android/platform_testing

http://10.5.103.101:8010/c/qcom/t_vendor/Turbox_C8550/release/LA.VENDOR.13.2.6/LINUX/android/vendor/qcom/proprietary/+/46820
repo forall "Turbox_C8550/release/LA.VENDOR.13.2.6/LINUX/android/vendor/qcom/proprietary" -c 'echo $REPO_PATH'
ls@ls-VirtualBox:/data/sm8550$ repo forall "Turbox_C8550/release/LA.VENDOR.13.2.6/LINUX/android/vendor/qcom/proprietary" -c 'echo $REPO_PATH'
vendor/LA.VENDOR.13.2.6/LINUX/android/vendor/qcom/proprietary

```
```c
git reset --hard HEAD
# push
git push rk HEAD:refs/for/android11/rk3566%r=SZ000008
git push aosp HEAD:refs/for/android11/rk3566%r=SZ000008
```
```c
# log
repo forall -p -c "git log --branches HEAD -p --stat  --no-merges --since=2023-12-13 --until=2023-12-22"
repo forall -p -c "git log --branches HEAD --no-merges --since=2025-08-15 --until=2025-09-20" > 41.txt
repo forall -p -c "git log --branches HEAD --no-merges --since=2025-09-19 --until=2025-09-26" > 42.txt
```
```c
# rollback
repo forall -c 'commitID=`git log --before "2024-02-27 23:59" -1 --pretty=format:"%H"`; git reset --hard $commitID'
```
```c
repo start <b> --all
repo checkout <b>
repo abandon <b>
```
Check SELinux status
```c
adb shell getenforce
```
Disk mapping on Windows
```c
net use Z: /delete
net use Z: \\192.168.133.184\aml
```
```c
script -f output.txt

Ctrl+D cancel
```
```c
git reset --hard HEAD^
git fetch --tags
```
```c
$ git tag
v2024.12.0
v2024.12.1-0
v2024.12.2
v2024.12.3
v2024.6.0
v2024.6.1-0
v2024.6.2
v2024.6.3
v2025.6.0
v2025.6.1
v2025.6.2
```
```c
$ git checkout v2025.6.0 -f
```
```c
//文件数
find . -name "*.c"|wc -l
//行数
find . -name "*.c" -or  -name "*.h" | xargs cat|wc -l
//行数(除空白行)
find . -name "*.c" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
find . -name "*.cpp" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
```
```c
//wildcard
.+?
```
```c
//每行前8个字符
.{8}
//包含0x00000044的所有行
.*0x00000044.*
```
```c
//删除空白行
^\s*(?=\r?$)\n
//只保留commit开头的行
^((?!commit ).)*$
^((?!(TASK|task|BUG|bug|JENKINS_JOB)).)*$
^(?!(.*(TASK|task|BUG|bug|JENKINS_JOB))).*$

//BDADDR, AC:86:D1:54:07:2D
\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b
\b(?!00:00:00:00:00:00\b)([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b
\b(?!00:00:00:00:00:00\b)([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b(?![:0-9A-Fa-f])
```
Victor2102 Oscilloscope
```c
//time
Press [HOR] then [return], then [up] key slow down for ecah X grid, [down] key speed up for ecah X grid.
//voltage
Press [CH1/2] then [return], then [left] higher voltage for each Y grid,[right] lower voltage for each Y grid
//Cursor
Press [Measure] then [Fn]
```

```c
1、查看cpu个数、核数等
# 总核数 = 物理CPU个数 X 每颗物理CPU的核数
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数
# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq
# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l
 查看CPU信息（型号）
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
2.查看内存
（1）查看内存详情
cat /proc/meminfo
（2）查看内存使用情况
free -g
（3）查看内存进程占用详情
top
3.查看系统位数
getconf LONG_BIT
4、查看硬盘大小
查看硬盘占用情况
df -h
```
```c
sudo dpkg -i bcompare-4.4.6.27483_amd64.deb

— BEGIN LICENSE KEY —
GXN1eh9FbDiX1ACdd7XKMV7hL7x0ClBJLUJ-zFfKofjaj2yxE53xauIfkqZ8FoLpcZ0Ux6McTyNmODDSvSIHLYhg1QkTxjCeSCk6ARz0ABJcnUmd3dZYJNWFyJun14rmGByRnVPL49QH+Rs0kjRGKCB-cb8IT4Gf0Ue9WMQ1A6t31MO9jmjoYUeoUmbeAQSofvuK8GN1rLRv7WXfUJ0uyvYlGLqzq1ZoJAJDyo0Kdr4ThF-IXcv2cxVyWVW1SaMq8GFosDEGThnY7C-SgNXW30jqAOgiRjKKRX9RuNeDMFqgP2cuf0NMvyMrMScnM1ZyiAaJJtzbxqN5hZOMClUTE+++
— END LICENSE KEY -----

=========================================================

dpkg -l | grep -i bcompare

sudo apt purge bcompare

rm -rf ~/.bcompare
rm -rf ~/.config/Beyond\ Compare/
rm -rf ~/.cache/Beyond\ Compare/

sudo rm -rf /etc/bcompare

find ~ -name "bcompare.desktop"
find /usr/share/applications -name "bcompare.desktop"


which bcompare
# 应该没有输出才对

bcompare --version
# 应提示 command not found

dpkg -l | grep -i bcompare
# 不应有任何输出
```
```c
//Check directory size
du -sh
//Check disk status
df -h /dev/sd*

//Check memory status  
free -h
//Check thread
ps aux
//Kill
kill -9 xxxx


htop

sudo /etc/init.d/network-manager restart
```
```c
tar cvzf - myfolder | split -d -b 2G - "myfolder.tar.gz.part"
cat myfolder.tar.gz.part* | tar xvzf -
```

```c
sudo apt-get autoremove open-vm-tools

sudo apt-get install open-vm-tools-desktop
```
```c
sudo apt install openssh-server
```
```c
1. Install adb and fastboot
sudo apt install android-tools-adb
sudo apt install android-tools-fastboot
2. Check if it can find by system.
lsusb
/////////
ls@ls-VirtualBox:/pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/out/target/product/qssi$ lsusb
Bus 001 Device 007: ID 05c6:90db Qualcomm, Inc. 
/////////
3. Enter below directory.
/etc/udev/rules.d/
4. Create and edit .rules file.
sudo gedit /etc/udev/rules.d/51-android.rules
5. Input below context.
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="05c6",ATTRS{idProduc}=="90db", MODE="0666"
6. Replug USB cable.
7. sudo adb kill-server;sudo adb start-server
```
```c
dumpsys suspend_control --wakelocks
```
Net neighbour
```c
//Linux
ip neigh
//Windows
arp -a
```

```c
sudo apt install openssh-server
sudo systemctl enable --now ssh
```
## Set
http://10.5.103.101:9090/execution-all.html  
S06G  
http://10.5.103.101:9090/task-view-7930.html   
PYO  
http://10.5.103.101:9090/task-view-9235.html  
http://10.5.103.101:9090/task-view-9545.html

## VM
[vm-readme](vm-readme.md)

## Python2
```c
# Install build dependencies
sudo apt update
sudo apt install build-essential checkinstall
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

# Download and compile Python 2.7.18
cd /tmp
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
tar xzf Python-2.7.18.tgz
cd Python-2.7.18
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall

# Create symlinks
sudo ln -s /usr/local/bin/python2.7 /usr/bin/python2.7
sudo ln -s /usr/bin/python2.7 /usr/bin/python
```