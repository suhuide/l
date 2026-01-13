# Profile Version
HFP我扫描出来是1.6，1.6版本目前只能用参考列名的方式来做，但是你们的 QDID是1.8的，所以你们产品需要修改版本为1.7或1.8
AVRCP扫描出来是1.3，1.3版本目前已经撤销不能用了，产品需要修改为1.5或者1.6
SAP扫描出来是1.2，目前我查询官网没有1.2这个版本，产品需要修改为1.1
MAP扫描出来是1.2，1.2版本目前只能参考列名，但你们QDID是1.4，产品需要修改为1.3或1.4

1. turn off BT
2. set the following ADB command
```c
adb shell setprop persist.bluetooth.pts true
adb shell setprop vendor.bt.pts.certification true
adb shell setprop vendor.bt.pts.avrcp true
adb shell setprop vendor.bt.pts.pbap true
adb shell setprop vendor.bt.pts.map true
adb shell setprop bt.sap.pts true
```
3. reboot the device
4. turn on BT
5. Start BQB test
