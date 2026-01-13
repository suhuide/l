function burn_qssi()
{
    qssi_dir=LA.QSSI.14.0.r1/LINUX/android/out/target/product/qssi
    echo "img dir : $qssi_dir"
    #"system system_ext product vbmeta_system"
    list="system system_ext product vbmeta_system"
    for i in $list; do
        fastboot flash $i ${qssi_dir}/$i.img;
    done
}

function burn_vendor()
{
    vendor_dir=LA.VENDOR.13.2.1.r1/LINUX/android/out/target/product/bengal_515
    echo "img dir : $vendor_dir"
    # "boot dtbo init_boot metadata odm recovery  vendor vbmeta vendor_dlkm system_dlkm userdata"
    list="boot dtbo init_boot metadata odm recovery  vendor vbmeta vendor_dlkm system_dlkm userdata"
    for i in $list; do
        fastboot flash $i ${vendor_dir}/$i.img;
    done
    fastboot flash vendor_boot ${vendor_dir}/vendor_boot-debug.img;
}

function main(){
    echo "wait add connect ..."
    adb wait-for-device reboot fastboot

    if [ $1 == "qssi" ];then
        echo "burn qssi ..."
        burn_qssi
    elif [ $1 == "vendor" ];then
        echo "burn vendor ..."
        burn_vendor
    elif [ $1 == "all" ];then
        echo "burn all ..."
        burn_qssi
        burn_vendor
    else
        echo "burn error ..."
    fi

    fastboot reboot
    date
}

main $1

