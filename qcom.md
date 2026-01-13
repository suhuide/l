[memo.md](memo.md)

[P02K Build](http://10.5.103.101:5080/p02k/p02k_doc/-/blob/main/09_%E7%BC%96%E8%AF%91/P02K_6225%E7%BC%96%E8%AF%91.md)


[PYO同步QCOM代码仓库](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/PYO%E5%90%8C%E6%AD%A5QCOM%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93.md)   

[SEL代码同步](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/SEL%E4%BB%A3%E7%A0%81%E5%90%8C%E6%AD%A5.md)  

# SEL
[原理图](http://10.5.103.101:5080/sel/sel_doc/-/tree/main/05_key_component/%E7%A1%AC%E4%BB%B6%E5%8E%9F%E7%90%86%E5%9B%BE)
 
[刷机工具](http://10.5.103.101:8082/artifactory/tools_open/MTK_TOOLS/SP_Flash_Tool_Selector_exe_Windows_v1.2404.00.000.zip)  


# PYO 
[原理图](http://10.5.103.101:5080/p02k/pyo_doc/-/tree/main/05_Key_Component/%E7%A1%AC%E4%BB%B6%E5%8E%9F%E7%90%86%E5%9B%BE)

[工具路径](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool)  
    . [下载工具及驱动](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool/qpst.win.2.7_installer_00496.2.zip)   
    . [下载工具SOP](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool/QFIL.docx)  
    . [写号工具](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/others/%E9%AB%98%E9%80%9A%E5%86%99%E5%8F%B7%E5%B7%A5%E5%85%B7%2020130305.zip)  
# [Fastboot](./files/fastboot.sh)
```c
source build/envsetup.sh;lunch qssi-userdebug;./build.sh -j12 dist --qssi_only
```
```c
cd out/target/product/qssi
adb reboot fastboot
fastboot flash system system.img
fastboot flash system_ext system_ext.img
fastboot flash product product.img
fastboot flash vbmeta_system vbmeta_system.img
```
Build and replace Bluetooth.apk
```c
cd ./LA.QSSI.14.0.r1/LINUX/android
source build/envsetup.sh;lunch qssi-userdebug;make Bluetooth
source build/envsetup.sh;lunch qssi-userdebug;make out/target/product/qssi/system/app/Bluetooth/Bluetooth.apk

//Find and replace the apk on the phone
odin2:/ # find -name Bluetooth.apk 2>/dev/null
./system/app/Bluetooth/Bluetooth.apk

cd out/target/product/qssi/system/app/Bluetooth/
adb root&&adb disable-verity&&adb reboot
adb root&&adb remount
adb push Bluetooth.apk /system/app/Bluetooth/
```
# prop
[qcom-prop.md](qcom-prop.md)

# Dock
[sm8550](sm8550.md)  
[S08G-A_chef5](S08G-A_chef5.md)

## PYO
```
git push clo HEAD:refs/for/android14/sm6225/pyo%r=SZ000008
```
[bt](../pyo/bt/bt.md)  
HCI log
```c
/data/misc/bluetooth/logs
```
```c
adb shell dumpsys bluetooth_manager
```
[BQB](../pyo/bt/BQB/QDID.md)  
```c
SM6225+WCN3988
- Host: 5.4, QDID[222137](https://qualification.bluetooth.com/ICSDetails/222137)
- Controller: 5.1, QDID[133994](https://qualification.bluetooth.com/ICSDetails/133994)
```

```c
/pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android$ source .build/envsetup.sh && lunch bengal_515-userdebug
source build/envsetup.sh && lunch bengal_515-userdebug

source build/envsetup.sh && lunch qssi-userdebug

./build_scipt_odin2.sh -c True --full True --adsp False
```
```c
source build/envsetup.sh
export IS_BUILD_GMS_VERSION=true
export DISPLAY_BUILD_NUMBER=AT-M120S$(date +%Y%m%d)S_L
export IMG_OUT_DIR=AT-M120S$(date +%Y%m%d)S_L
lunch qssi-userdebug
./build.sh -j12 dist --qssi_only

```

```c
./LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/android/app/AndroidManifest.xml
./LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/opp/BluetoothOppObexServerSession.java
./LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/opp/Constants.java
```
```c
./LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/packages/apps/Bluetooth/AndroidManifest.xml
./LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/packages/apps/Bluetooth/src/com/android/bluetooth/opp/BluetoothOppObexServerSession.java
./LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/packages/apps/Bluetooth/src/com/android/bluetooth/opp/Constants.java
```
TX
```
08-19 07:00:15.601 11333 13668 D ShortcutLoader: querying direct share targets for user UserHandle{0}
08-19 07:00:15.614 11333 13982 I APSResolverComparator: handleSortedAppTargets, sortedAppTargets #1: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}
08-19 07:00:15.624 11333 11333 I ResolverListAdapter: Add DisplayResolveInfo component: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}, intent component: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}
```
```
08-19 07:01:23.399 11333 11361 D ShortcutLoader: querying direct share targets for user UserHandle{0}
08-19 07:01:23.414 11333 14016 I APSResolverComparator: handleSortedAppTargets, sortedAppTargets #1: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}
08-19 07:01:23.414 11333 14016 I APSResolverComparator: handleSortedAppTargets, sortedAppTargets #8: ComponentInfo{com.skt.nugu.apollo/com.skt.nugu.visual.keep.ui.share.KeepShareActivity}
08-19 07:01:23.422 11333 11333 I ResolverListAdapter: Add DisplayResolveInfo component: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}, intent component: ComponentInfo{com.google.android.apps.docs/com.google.android.apps.docs.common.shareitem.UploadMenuActivity}
08-19 07:01:23.423 11333 11333 I ResolverListAdapter: Add DisplayResolveInfo component: ComponentInfo{com.skt.nugu.apollo/com.skt.nugu.visual.keep.ui.share.KeepShareActivity}, intent component: ComponentInfo{com.skt.nugu.apollo/com.skt.nugu.visual.keep.ui.share.KeepShareActivity}
```

```
thor2:/ $ logcat | grep BtOppObex
08-13 06:47:39.177  8141  8695 D BtOppObexClient: Start!
08-13 06:47:39.303  8141  8718 D BtOppObexClient: Create ClientSession with transport com.android.bluetooth.BluetoothObexTransport@ff3787
08-13 06:47:39.346  8141  8718 D BtOppObexClient: OBEX session created
08-13 06:47:46.184  8141  8718 D BtOppObexClient: Remote accept
08-13 06:47:46.200  8141  8718 D BtOppObexClient: Client thread waiting for next share, sleep for 500
08-13 06:47:46.201  8141  8695 D BtOppObexClient: Stop!
08-13 06:47:46.213  8141  8718 D BtOppObexClient: OBEX session disconnected
08-13 06:47:46.249  8141  8742 D BtOppObexClient: Stop!


thor2:/ $ logcat | grep BtOppObex
08-23 02:40:50.705 12231 16510 D BtOppObexClient: Start!
08-23 02:40:50.808 12231 16529 D BtOppObexClient: Create ClientSession with transport com.android.bluetooth.BluetoothObexTransport@8de52d5
08-23 02:40:50.853 12231 16529 D BtOppObexClient: OBEX session created
08-23 02:40:54.487 12231 16529 I BtOppObexClient: Remote reject, Response code is 0
08-23 02:40:54.503 12231 16529 D BtOppObexClient: Client thread waiting for next share, sleep for 500
08-23 02:40:54.508 12231 16510 D BtOppObexClient: Stop!
08-23 02:40:54.509 12231 16529 W BtOppObexClient: OBEX session disconnect errorjava.io.IOException: Broken pipe
08-23 02:40:54.511 12231 16529 D BtOppObexClient: OBEX session close mCs
08-23 02:40:54.512 12231 16529 D BtOppObexClient: OBEX session closed
08-23 02:40:55.538 12231 16564 D BtOppObexClient: Stop!
```
RX
```
odin2:/ $ logcat | grep BtOppObex
08-22 18:46:44.462  3935  3935 D BtOppObexServer: Create ServerSession with transport com.android.bluetooth.BluetoothObexTransport@600e26e
08-22 18:46:44.612  3935 18335 D BtOppObexServer: onConnect
08-22 18:46:44.615  3935 18335 D BtOppObexServer: isHandover :false
08-22 18:46:44.697  3935 18335 D BtOppObexServer: onPut com.android.obex.ServerOperation@ba307a5
08-22 18:46:44.706  3935 18335 D BtOppObexServer: onPut mimeType: application/vnd.android.package-archive,isAcceptlisted:false,mimeTypeMatches:true
08-22 18:46:44.725  3935 18335 V BtOppObexServer: insert contentUri: content://com.android.bluetooth.opp/btopp/2
08-22 18:46:44.726  3935 18335 V BtOppObexServer: mLocalShareInfoId = 2
08-22 18:46:44.737  3935 18336 D BtOppObexServer: Start!
08-22 18:46:44.737  3935 18336 D BtOppObexServer: addShare for id 2
08-22 18:46:44.737  3935 18336 D BtOppObexServer: processShareInfo() 2
08-22 18:46:51.834  3935 18335 D BtOppObexServer: Server unblocked
08-22 18:46:51.834  3935 18335 V BtOppObexServer: after confirm: userAccepted=1
08-22 18:46:56.687  3935 18335 D BtOppObexServer: Receiving file completed for 1MB_064644.apk
08-22 18:46:56.742  3935 18335 D BtOppObexServer: onDisconnect
08-22 18:46:56.778  3935 18335 D BtOppObexServer: onClose isHandover :false
08-22 18:46:56.778  3935 18335 D BtOppObexServer: releasing partial wakelock
08-22 18:46:56.783  3935 19490 D BtOppObexServer: Stop!
```
```
odin2:/ $ logcat | grep BtOppObex
08-23 20:42:24.900  2837 29819 D BtOppObexClient: Start!
08-23 20:42:25.004  2837 29909 D BtOppObexClient: Create ClientSession with transport com.android.bluetooth.BluetoothObexTransport@57aea09
08-23 20:42:25.182  2837 29909 D BtOppObexClient: OBEX session created
08-23 20:42:32.538  2837 29909 V BtOppObexClient: Remote accept
08-23 20:42:45.593  2837 29909 I BtOppObexClient: SendFile finished send out file LOG.TXT length 2190011
08-23 20:42:46.404  2837 29909 V BtOppObexClient: Get response code 160
08-23 20:42:46.415  2837 29909 D BtOppObexClient: Client thread waiting for next share, sleep for 500
08-23 20:42:46.418  2837 29819 D BtOppObexClient: Stop!
08-23 20:42:46.456  2837 29909 D BtOppObexClient: OBEX session disconnected
08-23 20:42:46.472  2837 31666 D BtOppObexClient: Stop!
08-23 20:43:18.013  2837  3074 D BtOppObexClient: Start!
08-23 20:43:18.120  2837  3228 D BtOppObexClient: Create ClientSession with transport com.android.bluetooth.BluetoothObexTransport@26985b7
08-23 20:43:18.318  2837  3228 D BtOppObexClient: OBEX session created
08-23 20:43:18.363  2837  3228 I BtOppObexClient: Remote reject, Response code is 207
08-23 20:43:18.364  2837  3228 I BtOppObexClient: Remote reject file type null
08-23 20:43:18.366  2837  3228 V BtOppObexClient: Get response code 207
08-23 20:43:18.366  2837  3228 I BtOppObexClient: Response error code is 207
08-23 20:43:18.380  2837  3228 D BtOppObexClient: Client thread waiting for next share, sleep for 500
08-23 20:43:18.386  2837  3074 D BtOppObexClient: Stop!
08-23 20:43:18.422  2837  3228 D BtOppObexClient: OBEX session disconnected
08-23 20:43:19.437  2837  3468 D BtOppObexClient: Stop!
```
## TASK BTS Fail
```c
ls@ls-VirtualBox:/pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android$ find -name "libbluetooth_qti.so"
./out/target/product/qssi/system_ext/lib64/libbluetooth_qti.so
./out/target/product/qssi/system_ext/lib/libbluetooth_qti.so
./out/target/product/qssi/symbols/system_ext/lib64/libbluetooth_qti.so
./out/target/product/qssi/symbols/system_ext/lib/libbluetooth_qti.so
./out/target/product/qssi/obj/SHARED_LIBRARIES/libbluetooth_qti_intermediates/libbluetooth_qti.so
./out/target/product/qssi/obj_arm/SHARED_LIBRARIES/libbluetooth_qti_intermediates/libbluetooth_qti.so
./out/soong/.intermediates/vendor/qcom/opensource/commonsys/system/bt/main/libbluetooth_qti/android_arm64_armv8-a-branchprot_shared_scs_cfi/libbluetooth_qti.so
./out/soong/.intermediates/vendor/qcom/opensource/commonsys/system/bt/main/libbluetooth_qti/android_arm64_armv8-a-branchprot_shared_scs_cfi/unstripped/libbluetooth_qti.so
./out/soong/.intermediates/vendor/qcom/opensource/commonsys/system/bt/main/libbluetooth_qti/android_arm_armv8-2a_cortex-a9_shared_cfi/libbluetooth_qti.so
./out/soong/.intermediates/vendor/qcom/opensource/commonsys/system/bt/main/libbluetooth_qti/android_arm_armv8-2a_cortex-a9_shared_cfi/unstripped/libbluetooth_qti.so
```
```c
ls@ls-VirtualBox:/pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android$ ls -l ./out/target/product/qssi/system_ext/lib64/libbluetooth_qti.so
-rwxrwxr-x 1 ls ls 7371952 9月   3 04:33 ./out/target/product/qssi/system_ext/lib64/libbluetooth_qti.so

```
```c
cd /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/
source build/envsetup.sh && lunch qssi-userdebug
cd /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/system/bt
mm
```
@12248
```c
https://android.googlesource.com/platform/packages/modules/Bluetooth/+/de53890aaca2ae08b3ee2d6e3fd25f702fdfa661

gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/system/stack/gatt/att_protocol.cc
gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/system/bt/stack/gatt/att_protocol.cc
```
@12251
```c
https://android.googlesource.com/platform/packages/modules/Bluetooth/+/17044ccf3a2858633cad8f87926e752edfe0d8d8

gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/system/stack/gatt/att_protocol.cc
gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/system/bt/stack/gatt/att_protocol.cc
```
@12252
```c
https://android.googlesource.com/platform/packages/modules/Bluetooth/+/7d0f696f450241d8ba7a168ba14fa7b75032f0c9

gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/packages/modules/Bluetooth/system/stack/smp/smp_act.cc
gedit /pyo/sm6225/LA.QSSI.14.0.r1/LINUX/android/vendor/qcom/opensource/commonsys/system/bt/stack/smp/smp_act.cc
```


# P02K
[Build](http://10.5.103.101:5080/p02k/p02k_doc/-/blob/main/09_%E7%BC%96%E8%AF%91/P02K_6225%E7%BC%96%E8%AF%91.md)
```
- 如果需要完整的编译Full codebase，直接调用如下的命令
  - ./clean_build_scipt_divar.sh (for full clean build)
  - ./incremental_build_scipt_divar.sh (for full incremental build)

  - ./copy_divar_flat_build.sh     
```


```c
./LA.QSSI.13.0/LINUX/android/packages/modules/Bluetooth/android/app/AndroidManifest.xml
./LA.QSSI.13.0/LINUX/android/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/opp/BluetoothOppObexServerSession.java
./LA.QSSI.13.0/LINUX/android/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/opp/Constants.java
```
```c
1
AS.AudioDeviceBroker: Music stream's unmute delay is increased by500 msfor A2DP/LE/Wired connection changes, msg
2
HeadsetStateMachine: updateAgIndicatorEnableState, no change in indicator state null

3
10-09 12:57:33.331  5411  9916 D AudioTrack: pause(123): 0xec357410, prior state:STATE_ACTIVE
10-09 12:57:33.615  1585  1597 I system_server: NativeAlloc concurrent mark compact GC freed 61944(3078KB) AllocSpace objects, 0(0B) LOS objects, 19% free, 24
MB/30MB, paused 14.614ms,16.376ms total 1.122s
10-09 12:57:34.139 11257 11292 I bluetooth: ack_pause: Client already in paused state

4
10-09 12:59:59.732  1585  2688 D AudioTrack: start(127): 0xa4897010, prior state:STATE_STOPPED
10-09 13:00:01.640 11464 11487 D BluetoothAdapterService: updateAdapterState() - Broadcasting state TURNING_ON to 1 receivers.
10-09 13:00:05.225  1000 11186 I BTAudioHalStream: out_dump: state=DISABLED
10-09 13:00:05.827  1025  9955 D APM_AudioPolicyManager: [MTK_APM_Route]setDeviceConnectionStateInt() device: 0x80, state 1, name JBL T280TWS X2 format 0x4000000
```
