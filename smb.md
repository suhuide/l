[memo.md](memo.md)
```c
Win11和Ubuntu实现Samba共享文件

一、Ubuntu开启Samba服务器 
sudo apt-get install samba samba-common
二、Ubuntu配置共享目录和用户权限 
1.创建用于共享的Samba目录 
mkdir -p ~/share
2.给创建的待共享目录设置权限
chmod -R 777~/share
3.配置Samba的配置文件
# 打开配置文件

sudo gedit /etc/samba/smb.conf
# 在配置文件smb.conf最后添加下面的内容（[]中是待共享目录的文件名，path是带共享目录的绝对路径）
[share]
comment = share folder
browseable = yes
path = /home/{username}/share
create mask = 0700
directory mask = 0700
valid user = ls
force user = ls
force group = ls
public = yes
available = yes
writable = yes

[s06g]
comment = share folder
browseable = yes
path = /s06g
create mask = 0700
directory mask = 0700
public = yes
available = yes
writable = yes

[p02k]
comment = share folder
browseable = yes
path = /p02k
create mask = 0700
directory mask = 0700
public = yes
available = yes
writable = yes

[s08ga]
comment = share folder
browseable = yes
path = /s08ga
create mask = 0700
directory mask = 0700
public = yes
available = yes
writable = yes

[s08gc]
comment = share folder
browseable = yes
path = /s08gc
create mask = 0700
directory mask = 0700
public = yes
available = yes
writable = yes

4.重启Samba服务器
sudo service smbd restart
# 或者/etc/init.d/samba restart

三、访问
Ubuntu, ifconifg 看IP
Windows ,直接访问ip地址即可
```