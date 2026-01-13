
```c
查看
sudo swapon --show
关闭
sudo swapoff -a
移除
sudo rm /swapfile
创建
sudo fallocate -l 60G /swapfile
修改权限
sudo chown 600 /swapfile
打开
sudo swapon /swapfile
查看
sudo swapon --show
```