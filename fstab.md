[memo.md](memo.md)
```c
sudo gedit /etc/fstab

# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=b05913c7-f4d9-47eb-8019-43b2cbf9de9f /               ext4    errors=remount-ro 0       1
/swapfile                                 none            swap    sw              0       0
/mnt/swap                                 swap            swap    defaults        0       0
/dev/sdb                                  /pyo           ext4    auto            0       0
/dev/sdc                                  /sel           ext4    auto            0       0
/dev/sdd                                  /chef          ext4    auto            0       0
/dev/sde                                  /s06g          ext4    auto            0       0
/dev/sdf                                  /p02k          ext4    auto            0       0
```