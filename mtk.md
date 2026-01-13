[memo.md](memo.md)

[P02K Build](http://10.5.103.101:5080/p02k/p02k_doc/-/blob/main/09_%E7%BC%96%E8%AF%91/P02K_6225%E7%BC%96%E8%AF%91.md)


[PYO同步QCOM代码仓库](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/PYO%E5%90%8C%E6%AD%A5QCOM%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93.md)   

[SEL代码同步](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/SEL%E4%BB%A3%E7%A0%81%E5%90%8C%E6%AD%A5.md)  

# MTK log
```c
*#*#365001#*#*
```
log @ /storage/emulated/0/debugger

# SEL
[原理图](http://10.5.103.101:5080/sel/sel_doc/-/tree/main/05_key_component/%E7%A1%AC%E4%BB%B6%E5%8E%9F%E7%90%86%E5%9B%BE)
 
[刷机工具](http://10.5.103.101:8082/artifactory/tools_open/MTK_TOOLS/SP_Flash_Tool_Selector_exe_Windows_v1.2404.00.000.zip)  

# E01K
[Pull Code](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/%E5%90%8C%E6%AD%A5MTK6761%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93.md)
```c
//alps
cd ${workspace}
mkdir -p mtk/alps && cd mtk/alps
repo init -u ssh://gerrit/lens/manifest -b E01K -m E01K_EVT1_alps.xml --repo-url=ssh://gerrit/lens/git_repo --no-repo-verify -c
repo sync -j8

//modem
cd ${workspace}
mkdir -p mtk/modem && cd mtk/modem
repo init -u ssh://gerrit/lens/manifest -b E01K -m E01K_EVT1_modem.xml --repo-url=ssh://gerrit/lens/git_repo --no-repo-verify -c
repo sync -j8

// modem link
cd ${workspace}/mtk/modem/TK_MD_BASIC_MOLY.LR12A.R3.MP-xthink-s0.mp1.rc-bsp-kr-modem-x50

ln -s ../../tools/NDK apps/NDK
ln -s  ../../../../tools/GCC mcu/common/tools/GCC
ln -s  TK_MD_BASIC_MOLY.LR12A.R3.MP-xthink-s0.mp1.rc-bsp-kr-modem-x50 ../x050_k61v1_32_bsp_1g

//modem build
cd ${WORKSPACE}/mtk/alps
./xbuild_scripts/build_modem.sh -d x050_k61v1_32_bsp_1g -k "TK_MD_BASIC(LWCTG_6177M_R3_6761).mak" -c GEN93_USER -m Yes
```
```c
cd ${WORKSPACE}/mtk/alps
cp -rf vendor/hnlens/proprietary/ls_aosp/aosp/* .
./APK_CONFIG.sh SZ000087:APADtuFkJ2xneMconWiT39DtZ54
./APK_CONFIG.sh SZ000016:AP67rv8nrtb9PDLFSHoKtjxktin
./apk_sign_encrypt.sh "SideButton,LS_FACTORYTEST,LS_CQR,LS_PLATFORM,OP01SoundRecorder" platform
source build/envsetup.sh
lunch full_x050_k61v1_32_bsp_1g-userdebug 
make -j32
```
# PYO 
[原理图](http://10.5.103.101:5080/p02k/pyo_doc/-/tree/main/05_Key_Component/%E7%A1%AC%E4%BB%B6%E5%8E%9F%E7%90%86%E5%9B%BE)

[工具路径](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool)  
    . [下载工具及驱动](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool/qpst.win.2.7_installer_00496.2.zip)   
    . [下载工具SOP](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/qcom_tool/QFIL.docx)  
    . [写号工具](http://10.5.103.101:8082/ui/repos/tree/General/tools_open/others/%E9%AB%98%E9%80%9A%E5%86%99%E5%8F%B7%E5%B7%A5%E5%85%B7%2020130305.zip)  
# Fastboot
```c
cd alps
source build/envsetup.sh;lunch sys_mssi_32_ago_h_ww-userdebug;make Bluetooth
```
```c
./out/target/product/mssi_32_ago_h_ww/apex/com.android.btservices/app/Bluetooth@UP1A.231005.007/Bluetooth.apk
```
```c
cd out/target/product/mssi_32_ago_h_ww/apex/com.android.btservices/app/Bluetooth@UP1A.231005.007/  
```
```c
adb disable-verity&&adb reboot
adb root&&adb remount
adb push Bluetooth.apk /apex/com.android.btservices/app/Bluetooth@UP1A.231005.007/
adb push Bluetooth.apk /apex/com.android.btservices@340090000/app/Bluetooth@UP1A.231005.007/
```
Device must be bootloader unlocked
Navigate to Setting->System->Developper Option-> OEM unlock enable
```c
adb reboot bootloader
fastboot flashing unlock
```
```c
thor2:/ # find -name Bluetooth.apk 2>/dev/null
./apex/com.android.btservices/app/Bluetooth@UP1A.231005.007/Bluetooth.apk
./apex/com.android.btservices@340090000/app/Bluetooth@UP1A.231005.007/Bluetooth.apk
```
## SEL
```c
git push mtk HEAD:refs/for/android14/mt6765/sel%r=SZ000008
git push mtk HEAD:refs/for/android14/mt6765/sel/alps%r=SZ000008
```
```c
#在根目录运行脚本
rm -rfv build_images&&./build_scripts/build_modem.sh&&./build_scripts/build_android.sh all
```
[Prop](./mtk-prop.md)  
[bt](../sel/bt/bt.md)  
[BQB](../sel/bt/BQB/QDID.md)   
[HCI](./files/mtk/hcidefs.h)

```c
MT6765+MT6631N/B
- Host: 5.4, QDID[214253](https://qualification.bluetooth.com/ICSDetails/214253)
- Controller: 5.4, QDID[207299](https://qualification.bluetooth.com/ICSDetails/207299)
```

[android/app/AndroidManifest.xml](http://10.5.103.101:8010/c/mtk/alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/+/34987/1/android/app/AndroidManifest.xml)  
[android/app/src/com/android/bluetooth/opp/](http://10.5.103.101:8010/c/mtk/alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/+/34987/1/android/app/src/com/android/bluetooth/opp/BluetoothOppObexServerSession.java)  
[android/app/src/com/android/bluetooth/opp/Constants.java](http://10.5.103.101:8010/c/mtk/alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/+/34987/1/android/app/src/com/android/bluetooth/opp/Constants.java)  

[BUG_12345](http://10.5.103.101:9080/bug-view-12345.html)  
[[TASK_11241]modify bluetooth certs](http://10.5.103.101:8010/c/mtk/alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/+/35725)
```
project alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/
commit 5459500bc14fdf9ee481c5887ea31bc355de36ec
Author: sdev39 <sdev39.sz@hnlens.com>
Date:   Wed Aug 21 15:54:19 2024 +0800

    [TASK_11241]modify bluetooth certs
    
    Change-Id: Ibe57c87346b90b2a8473273477a9d26327b9597c
```
### TX power
```c
/sel/alps_vendor/device/mediatek/mt6765/WMT_SOC.cfg
ls@ls-VirtualBox:/sel/alps_vendor/device/mediatek/mt6765$ git diff
diff --git a/WMT_SOC.cfg b/WMT_SOC.cfg
index 1a84588..c15484e 100644
--- a/WMT_SOC.cfg
+++ b/WMT_SOC.cfg
@@ -6,7 +6,7 @@ wmt_gps_lna_enable=0
 co_clock_flag=1
 
 bt_tssi_from_wifi=3
-bt_tssi_target=3776
+bt_tssi_target=3719




thor2:/ # cat ./vendor/firmware/WMT_SOC.cfg
coex_wmt_ant_mode=1

wmt_gps_lna_pin=0
wmt_gps_lna_enable=0

co_clock_flag=1

bt_tssi_from_wifi=3
bt_tssi_target=3719
```
```c
/sel/alps_vendor/vendor/mediatek/proprietary/hardware/connectivity/bluetooth/driver/mt66xx/bluedroid/radiomod.c
@line1560
VOID *GORM_FW_Init_Thread(UNUSED_ATTR VOID *ptr)
{
    INT32 i = 0;
    bt_vendor_op_result_t ret = BT_VND_OP_RESULT_FAIL;
    char bt_ssp_debug_val[PROPERTY_VALUE_MAX];
    char bt_pip_val[PROPERTY_VALUE_MAX];

    LOG_DBG("FW init thread starts\n");
    parse_fw_cfg_para();

    /* preload init script */
    switch (btinit->chip_id) {
      //...
      case 0x6765:
      case 0x3967:
      case 0x6761:
      case 0x8168:
      case 0x6768:
      case 0x6785:
        btinit->cur_script = bt_init_preload_script_connac;
        btinit->chip_type = BT_CONNAC;
        memcpy(ucDefaultAddr, stBtDefault_connac_soc_1_0.addr, 6);
        break;
      //...
    }

}
```

```c
/sel/alps_vendor/vendor/mediatek/proprietary/custom/common/cgen/cfgdefault/CFG_BT_Default.h
@line206
static ap_nvram_btradio_struct stBtDefault_connac_soc_1_0 =
{
    {0x00, 0x00, 0x46, 0x00, 0x00, 0x01},
    {0x60, 0x00}, // not used
    {0x23, 0x10, 0x00, 0x00}, // not used
    {0x07, 0x00, 0x00, 0x00, 0x06, 0x07}, // Radio[0-5]
}
```

[mtk-opp.md](mtk-opp.md)
```c
./alps_vendor/packages/apps/Bluetooth/src/com/android/bluetooth/avrcpcontroller/AvrcpControllerService.java
./alps_vendor/vendor/mediatek/proprietary/packages/apps/Bluetooth/src/com/android/bluetooth/avrcpcontroller/AvrcpControllerService.java
./alps/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/avrcpcontroller/AvrcpControllerService.java
./alps/vendor/mediatek/proprietary/packages/modules/Bluetooth/android/app/src/com/android/bluetooth/avrcpcontroller/AvrcpControllerService.java
```
        intentFilter.addAction(BluetoothHeadset.ACTION_CONNECTION_STATE_CHANGED);
        registerReceiver(receiver, intentFilter);

public class HeadphoneReceiver extends BroadcastReceiver {
 
    @Override
    public void onReceive(Context context, Intent intent) {
 
        String action = intent.getAction();
        if (Intent.ACTION_HEADSET_PLUG.equals(action)) {
            int state = intent.getIntExtra("state", -1);
            if (state == 0) {
                // 耳机拔出
            } else if (state == 1) {
                // 耳机插入
            }
        } else if (BluetoothHeadset.ACTION_CONNECTION_STATE_CHANGED.equals(action)) {
 
            BluetoothAdapter adapter = BluetoothAdapter.getDefaultAdapter();
            /* 申请权限
            if (ActivityCompat.checkSelfPermission(context, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                return;
            }
            */
            //如果应用运行的Android系统版本大于等于12，获取蓝牙状态需要动态申请权限
            int state = adapter.getProfileConnectionState(BluetoothProfile.HEADSET);
            if (state == BluetoothAdapter.STATE_DISCONNECTED) {
                //Bluetooth headset is now disconnected
            }
        }
    }
}


```c
ls@ls-VirtualBox:/sel/alps/frameworks$ grep -rn "setDeviceConnectionStateInt"
av/services/audiopolicy/managerdefault/AudioPolicyManager.cpp:159:    MTK_ALOGI("[MTK_APM_Route]setDeviceConnectionStateInt() device: 0x%X, state %d, name %s format 0x%X",       
```