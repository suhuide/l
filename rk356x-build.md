[memo.md](memo.md)

[weekly_report](http://10.5.103.101:5080/iotteam/iotteam_doc/-/tree/main/2024weekly_report)

```c
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
source build/envsetup.sh; lunch rk3566_r-userdebug; make Bluetooth
```
```c
cd kernel
make ARCH=arm64 rockchip_defconfig rk356x_evb.config android-11.config; make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img rk3566-evb2-lp4x-v10.img -j24
make ARCH=arm64 rockchip_defconfig android-11.config; make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img rk3566-evb2-lp4x-v10.img -j24
```
```c
repo forall  "platform/mkcombinedroot" -c 'echo $REPO_PATH'
git push rk HEAD:refs/for/android11/rk3566%r=SZ000008
git push aosp HEAD:refs/for/android11/rk3566%r=SZ000008
repo forall -p -c "git log --branches HEAD -p --stat  --no-merges --since=2023-12-13 --until=2023-12-22"
repo forall -p -c "git log --branches HEAD --no-merges --since=2024-01-08 --until=2024-01-12" > 74.txt

repo start <b> --all
repo checkout <b>
repo abandon <b>
```
```c
//删除空白行
^\s*(?=\r?$)\n
//只保留commit开头的行
^((?!commit ).)*$
^((?!(TASK|task|BUG|bug)).)*$
```
```c
sudo /etc/init.d/network-manager restart
```
```c
[  338.664005] init: starting service 'filecopy'...
[  338.668833] init: cannot execv('/system/bin/zigbee/filecopy.sh'). See the 'Debugging init' section of init's README.md for tips: Permission denied
[  338.669591] type=1400 audit(1706086991.593:96): avc: denied { entrypoint } for comm="init" path="/system/bin/zigbee/filecopy.sh" dev="dm-0" ino=1852 scontext=u:r:shell:s0 tcontext=u:object_r:system_file:s0 tclass=file permissive=0
```