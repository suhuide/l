


# Install docker
May meet error, some can resolve by modity .sh, change python version to 3.6, the original one.  
```c
sudo apt-get install apt-transport-https ca-certificates curl gnupg software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#sudo add-apt-repository "deb [arch=amd64] #https://download.docker.com/linux/ubuntu ${lsb_release -cs} stable"
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt-get update

sudo apt install docker-ce | sudo apt install docker.io

sudo systemctl status docker

// Looks like can be ingrone below script.
sudo groupadd docker
sudo usermod -aG docker ${whoami}
```
# Config
更换docker home目录到数据盘，避免系统盘不够用，且不影响系统盘升级。 
查看docker 默认目录
```c
$ sudo docker info
Docker Root Dir: /var/lib/docker
```
停止docker服务
```c
$ sudo systemctl disable docker.service
$ sudo systemctl disable docker.socket
```
备份原 docker home 目录
```c
$ sudo mv /var/lib/docker /var/lib/docker_back
```
采用软连接方式，将 docker home 目录 指向到数据盘，比如/data/docker_home目录
```c
$ sudo ln -s /data/docker_home /var/lib/docker
```
启动docker
```c
$ sudo systemctl restart docker
```

# 导入镜像
## download 镜像文件（from配置管理）到数据盘（i.e: $path/$imagesName），导入后即可删除。
docker load -i $path/$imagesName
```c
$ docker load -i ls_ubuntu22.04.rk3588.250411.tar 
270a1170e7e3: Loading layer [==================================================>]  80.41MB/80.41MB
a8ad863da20d: Loading layer [==================================================>]  883.1MB/883.1MB
5c30c915e695: Loading layer [==================================================>]  4.742MB/4.742MB
4539cc91c761: Loading layer [==================================================>]  8.192kB/8.192kB
092573d11e0e: Loading layer [==================================================>]  12.39MB/12.39MB
32b92e507904: Loading layer [==================================================>]  26.21MB/26.21MB
af9f54993e5f: Loading layer [==================================================>]  7.843MB/7.843MB
48dbfb3c51a9: Loading layer [==================================================>]  7.168kB/7.168kB
90c5b3c9fa3d: Loading layer [==================================================>]  13.82kB/13.82kB
515b741d4c72: Loading layer [==================================================>]  8.192kB/8.192kB
dd406445957a: Loading layer [==================================================>]  3.584kB/3.584kB
cae5801e1831: Loading layer [==================================================>]   2.56kB/2.56kB
772f09a2b3fa: Loading layer [==================================================>]   2.56kB/2.56kB
c46285680149: Loading layer [==================================================>]  5.632kB/5.632kB
e6c1f27891c9: Loading layer [==================================================>]  835.6MB/835.6MB
Loaded image: ls/ubuntu22.04:rk3588.250411
```
```c
$ docker images
REPOSITORY       TAG             IMAGE ID       CREATED       SIZE
ls/ubuntu22.04   rk3588.250411   42107067b7e2   3 weeks ago   1.81GB
```
```c
ls@ls-VirtualBox:/data/docker01$ docker run -td --name ls_ubuntu2204 --restart always -v /data/docker01:/data ls/ubuntu22.04:rk3588.250411 
c2f86d73bd21e627f6431b8c30191611b521492ccd48cb2cabdeb41a75876fa6
ls@ls-VirtualBox:/data/docker01$ docker ps -a
CONTAINER ID   IMAGE                          COMMAND       CREATED          STATUS          PORTS     NAMES
c2f86d73bd21   ls/ubuntu22.04:rk3588.250411   "/bin/bash"   39 seconds ago   Up 38 seconds   22/tcp    ls_ubuntu2204
ls@ls-VirtualBox:/data/docker01$ docker exec -it ls_ubuntu2204 bash
```

# 启动镜像示例 —— 即容器
```c
docker run -td --name ${userName} --restart always -v /data/docker/data/${e01k}:/data 
-p 222x:22 -p 445x:445 -p 139x:139 ls/sm8550_rk3566_sm6225_sm8475_mtk67616789:20240223
i.e:
docker run -td --name docker03 --restart always -v /data/docker/data/docker03:/data 
-p 22222:22 -p 44522:445 -p 13922:139 ls/sm8550_rk3566_sm6225_sm8475_mtk67616789:20240223
```
## 说明：
```c
-it ：后台运行
--name docker03 : 容器命名为 docker03
--restart always : 主机重启时，容器自动重启
-v /data/docker/data/docker03:/data ： 将 主机 /data/docker/data/docker03目录，映射到  容器/data目录；可双向修改
-p 22222:22 -p 44522:445 -p 13922:139 : 将容器 22端口映射到 主机 22222端口（ssh）； 
   445端口映射到主机44522端口, 139端口映射到主机13922（samba）
ls/sm8550_rk3566_sm6225_sm8475_mtk67616789:20240223  : 实例此镜像
```
4、容器数据持久化 文件夹 赋权, 主机中进行：
sudo chown lens:lens /data/docker/data/docker03  -R


安装docker工具：http://10.5.103.101:8082/ui/repos/tree/General/tools/dockerImages/docker_info.txt

下载镜像：public.ecr.aws_k5o4b3u5_thundercomm_turbox-sdkmanager-18.04.3.2.3.tar

导入镜像：
$ docker load -i public.ecr.aws_k5o4b3u5_thundercomm_turbox-sdkmanager-18.04.3.2.3.tar

启动docker容器：
```c
$ docker run -td --name S08G-A_thundercomm --restart always -v /data/docker/data/docker03:/home/turbox/workspace  -p 22222:22  -p 44522:445  public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-18.04:v3.2.3
docker run -td --name S08G-A_thundercomm --restart always -v /p02k/sm8550:/home/turbox/workspace  -p 22222:22  -p 44522:445  public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-18.04:v3.2.3.2024.11.08
```
备注：
```c
/data/docker/data/docker03 : 本地目录，映射docker容器中目录：/home/turbox/workspace；  可根据自己Linux系统实际情况配置
```
```c
docker run -td --name docker_turbox --restart always -v /data2/:/data2 -p 22222:22 -p 44522:445 -p 13922:139 public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-20.04:latest
```
```c
sudo docker run --name turbox-sdkmanager-18.04_v3.2.3_1000 -it -d -v /home/b/turbox-sdkmanager-ws:/home/turbox/workspace -v /lib/modules:/lib/modules --privileged -v /dev/:/dev -v /run/udev:/run/udev public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-18.04:v3.2.3 /bin/bash
Unable to find image 'public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-18.04:v3.2.3' locally

v3.2.3: Pulling from k5o4b3u5/thundercomm/turbox-sdkmanager-18.04
Digest: sha256:e5643d75dcfe818767f6b5375c88c59c6c285ae8ac584fd3178fe1ff745bcddc
Status: Downloaded newer image for public.ecr.aws/k5o4b3u5/thundercomm/turbox-sdkmanager-18.04:v3.2.3
8c3593ca56b75f701d25fbee0ca09efe2982bfe8046990fbd38677418897c62b
docker start turbox-sdkmanager-18.04_v3.2.3_1000
turbox-sdkmanager-18.04_v3.2.3_1000
docker exec -it turbox-sdkmanager-18.04_v3.2.3_1000 /bin/create-user.sh 1000 1000
Create group turbox_g(1000) successed.
Create user turbox(1000) successed.
docker exec -it -u 1000:1000 -w /home/turbox turbox-sdkmanager-18.04_v3.2.3_1000  /bin/bash
```
登录docker容器：
```c
$ docker exec -it docker_turbox bash
```
登录成功后，切换用户到turbox
```c
$ su turbox
```
初始化：
```c
$ sdkmanager --init
```
编译：
...

```c
 Files copied to /home/turbox/workspace/vendor/LA.VENDOR.13.2.6/LINUX/android/kernel_platform/out/msm-kernel-kalama_tuivm-debug_defconfig/dist
rsync: failed to connect to 10.0.76.14 (10.0.76.14): Connection refused (111)
rsync error: error in socket IO (code 10) at clientserver.c(125) [Receiver=3.1.2]
export SHELL=/bin/bash
export MACHINE=trustedvm
export DISTRO=qti-distro-base-debug
source poky/qti-conf/set_bb_env.sh
warning: failed to load external entity "/home/turbox/workspace/le/LE.UM.6.3.3/apps_proc/.repo/manifests/default.xml"
This script requires PyYAML.    
Please install pyyaml python package.
This script requires PyYAML.    
Please install pyyaml python package.
This script requires PyYAML.    
Please install pyyaml python package.
poky/qti-conf/set_bb_env.sh: line 243: cd: /home/turbox/workspace/le/LE.UM.6.3.3/apps_proc/.repo/manifests: No such file or directory
/home/turbox/workspace/vendor/LE.UM.6.3.3/apps_proc


### Shell environment ready with following configuration to run bitake commands. ###

DISTRO     = qti-distro-base-debug
MACHINE    = trustedvm

You can now run 'bitbake <target>'




Run 'bitbake <pkg-name>' to build a required package, example:
    bitbake systemd

bitbake qti-vm-image
NOTE: Bitbake server didn't start within 5 seconds, waiting for 90
WARNING: Layer qti-display should set LAYERSERIES_COMPAT_qti-display in its conf/layer.conf file to list the core layer names it is compatible with.
NOTE: Your conf/bblayers.conf has been automatically updated.
WARNING: Layer qti-display should set LAYERSERIES_COMPAT_qti-display in its conf/layer.conf file to list the core layer names it is compatible with.
ERROR:  OE-core's config sanity checker detected a potential misconfiguration.
    Either fix the cause of this error or at your own risk disable the checker (see sanity.conf).
    Following is the list of potential problems / advisories:

    Fetcher failure for URL: 'https://www.example.com/'. URL https://www.example.com/ doesn't work.
    Please ensure your host's network is configured correctly.
    If your ISP or network is blocking the above URL,
    try with another domain name, for example by setting:
    CONNECTIVITY_CHECK_URIS = "https://www.yoctoproject.org/"    You could also set BB_NO_NETWORK = "1" to disable network
    access if all required sources are on local disk.


Summary: There were 2 WARNING messages shown.
Summary: There was 1 ERROR message shown, returning a non-zero exit code.
20241108_17:24:05 [TURBOX BUILD ERROR]: build_hlos Error****
[turbox@sdkmanager-18.04-3.2.3 vendor ]$ 
```