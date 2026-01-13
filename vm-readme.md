```c
一、 虚拟机.ova文件说明：

ubuntu18.04.20230922.ova           : 可编译 rk3566 sm8350 sm8475 sm6225 MTK6761 MTK6789 AOSP
ubuntu1804_sm6225.ova              : 可编译        sm8350 sm8475 sm6225 MTK6761 MTK6789 AOSP
ubuntu1804_sm6225-private.zip      : 可编译        sm8350 sm8475 sm6225 MTK6761 MTK6789 AOSP       |   VMWare 文件 —— 解压即可用

二、 安装虚拟工具
工具版本及获取：
统一开发工具及版本.md： http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/70_%E7%BC%96%E8%AF%91%E9%9B%86%E6%88%90/%E7%BB%9F%E4%B8%80%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7%E5%8F%8A%E7%89%88%E6%9C%AC.md  —— 章节：3、Virtual 虚拟工具

三、 安装虚拟机：
1、ubuntu1804_sm6225-private.zip
   WMware 解压后，open 即可用
2、ubuntu1804_*.ova
   需按照向导导入


四、 虚拟机使用 —— 初始配置：
1、虚拟机账号|密码： ls | android

2、虚拟机使用请先配置：
1）、git account
2）、~/.ssh 密钥对 & ~/.ssh/config 文件

     如上2个配置可见文档：git操作指南.md：http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/10_%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B/git%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97.md
     也可copy其他环境下文件|文件夹：~/.gitconfig     ~/.git_template/       ~/.ssh/  至相同位置。

3）、硬盘(数据盘)新增&挂载等，启动自挂载配置 ：/etc/fstab

     请将所有用户数据放到自己新增的数据盘内；
     导入.ova文件自带硬盘仅作系统盘，和编译环境配置。
     如上，便于虚拟机升级：备份git用户文件；卸载数据盘（虚拟机配置setting页面，存储配置选项卡，进行删除）；删除待升级虚拟机；导入新的虚拟机ova文件，挂载数据盘...

4）、根据宿主机情况，配置虚拟机CPU,内存等
5）、配置网络


五、 其他：  

1、P02K项目数据盘： qcom android13 sm6225 已编译通过的 整套代码， 已共享在：10.5.103.102 | 10.5.103.103 samba 公用账号 sw 目录下：virtual_files/P02K/sm6225_dataxxxxxxxx.vdi

获取方法见：
服务器公用账号及管理规范.md，地址如下：
http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/10_%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B/%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%AC%E7%94%A8%E8%B4%A6%E5%8F%B7%E5%8F%8A%E7%AE%A1%E7%90%86%E8%A7%84%E8%8C%83.md

硬盘说明：
当前大小：600G 左右
硬盘最大容量：1T
硬盘非固化容量，实际大小随使用增长。


```
[virtualbox虚拟机ubuntu18.04网络配置--虚拟机和宿主机互通且联网](https://www.cnblogs.com/muyuequzhi/p/12259797.html)
```c
思路：添加两张网卡，分别为“网络地址转换（NAT）”和“仅主机（Host-only）网络”。虚拟机安装完成后默认是“网络地址转换（NAT）”一张网卡，这时虚拟机能上网但是不能和宿主# 机互通，所以再添加一张“仅主机（Host-only）网络”网卡让虚拟机和宿主机之间互通
虚拟机ip：192.168.5.6，宿主机ip：192.168.5.1。这两个要同一网段

因为虚拟机安装之后网卡一默认为“网络地址转换（NAT）”，所以就只添加网卡二

1、VirtualBox添加第二张网卡


2、更改网络适配器
点击这个网卡配置下ip地址

我这里的ip为192.168.5.1


3、Ubuntu虚拟机配置ip，注意address的配置和192.168.5.1同一网段
we@we-VirtualBox:~$ cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
auto lo
iface lo inet loopback

auto enp0s8
iface enp0s8 inet static
address 192.168.5.6
netmask 255.255.255.0

配置完成之后重启虚拟机即可
```