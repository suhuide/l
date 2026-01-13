
# Configure compile environment
## gcc
按Amlogic要求配置。
Copy compiler(gcc-linaro-7.3.1-2018.05-i686_aarch64-elf.tar.gz) to <font color="#dd00dd">Linux host /opt</font><br />
```c
sudo mv gcc-linaro-7.3.1-2018.05-i686_aarch64-elf.tar.gz /opt

cd /opt
sudo tar -xzvf gcc-linaro-7.3.1-2018.05-i686_aarch64-elf.tar.gz
```
```c
gedit ~/.bashrc
Add below line in the end of file.

export PATH=$PATH:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
```
```c
echo 'export PATH=$PATH:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin' >> ~/.bashrc
```

Run,
```c
source ~/.bashrc
```
Check,
```c
aarch64-elf-gcc -v
```
## matter
直接参照官网的
```c
$ sudo apt install git gcc g++ pkg-config libssl-dev libdbus-1-dev
libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev 
python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev
```
## cmake
再看Openthread 编译用cmake, 版本要求3.14以上， 如已安装了低版本要先清除，再用snap安装，snap是为了得到高版本。
```c
ls@ls-VirtualBox:/aml/dock/vendor/amlogic$ cmake --version
cmake version 3.10.2
```

```c
sudo apt remove cmake
```

```c
sudo snap install cmake --classic 
```

```c
ls@ls-VirtualBox:/aml/dock/vendor/amlogic$ which cmake
/snap/bin/cmake
```

```c

echo 'export PATH=/snap/bin:$PATH' >> ~/.bashrc
```

```c
source ~/.bashrc
```

```c
ls@ls-VirtualBox:/aml/dock/vendor/amlogic$ cmake --version
cmake version 3.30.4

```