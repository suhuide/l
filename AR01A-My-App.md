[memo](memo.md)  
[AR01A](AR01A.md)  

开发过程中，Buildroot自带的软件包有时可能无法满足我们的需求，为此我们需要添加自定义的软件包。

Buildroot支持多种格式的软件包，包括generic-package、cmake-package、autotools-package等，我们以generic-package举例说明。

要添加自己的本地源码包，：

首先创建工程目录，比如这里演示使用的helloworld目录；
接着helloworld里面添加Config.in和helloworld.mk；
最后在package/Config.in中添加指向新增helloworld目录的Config.in。
# 创建工程目录
```c
$ sudo mkdir buildroot/package/helloworld
```
# helloworld目录
## Config.in
在helloworld目录新建Config.in，内容如下：
```c
config BR2_PACKAGE_HELLOWORLD
    bool "helloworld"
    help
      This is a demo to add local app.
```      
只有在BR2_PACKAGE_HELLOWORLD=y条件下，才会调用helloworld.mk进行编译。

## helloworld.mk
buildroot编译helloworld所需要的设置helloworld.mk，包括源码位置、安装目录、权限设置等。

在helloworld目录新建helloworld.mk，内容如下：
```c
################################################################################
#
# helloworld
#
################################################################################
ifeq ($(BR2_PACKAGE_HELLOWORLD), y)

        HELLOWORLD_VERSION:=1.0.0
        HELLOWORLD_SITE=$(TOPDIR)/../external/helloworld
        HELLOWORLD_SITE_METHOD=local

define HELLOWORLD_BUILD_CMDS
        $(TARGET_MAKE_ENV) $(MAKE) CC=$(TARGET_CC) CXX=$(TARGET_CXX) -C $(@D)
endef

define HELLOWORLD_CLEAN_CMDS
        $(TARGET_MAKE_ENV) $(MAKE) -C $(@D) clean
endef

define HELLOWORLD_INSTALL_TARGET_CMDS
        $(TARGET_MAKE_ENV) $(MAKE) -C $(@D) install
endef

define HELLOWORLD_UNINSTALL_TARGET_CMDS
        $(TARGET_MAKE_ENV) $(MAKE) -C $(@D) uninstall
endef

$(eval $(generic-package))
endif
```
注意：上面的HELLOWORLD的开头也是必须的。

## 创建源码目录
上文的helloworld.mk文件里已经指定了源码目录 external/helloworld。

$ sudo mkdir -p external/helloworld
在external/helloworld目录下简单的编写一个helloworld.c文件：
```c
#include <stdio.h>

void main(void)
{
    printf("Hello world.\n");
}
```
然后编写Makefile文件：
```c
CPPFLAGS += 
LDLIBS += 

all: helloworld

analyzestack: helloworld.o
        $(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)

clean:
        rm -f *.o helloworld
    
.PHONY: install
install:
        cp -f helloworld $(TARGET_DIR)/usr/bin/

.PHONY: uninstall
uninstall:
        rm -f $(TARGET_DIR)/usr/bin/helloworld

.PHONY: all clean
```
由于在helloworld.mk中指定了命令CLEAN、INSTALL、UNINSTALL，因此这里需要配置目标install、clean、uninstall。

## 添加package/Config.in入口
在 package/Config.in 末尾添加一行：
```c
$sudo gedit buildroot/package/Config.in

menu "Target packages"

......
menu "helloworld package"
       source "package/helloworld/Config.in"
endmenu

endmenu
```
# 配置软件包
在配置文件末尾添加 BR2_PACKAGE_HELLOWORLD=y。 重新lunch与build就可以了。
```c
./buildroot/configs/rockchip_3588_defconfig
#include "base/base.config"
#include "chips/rk3588_aarch64.config"
#include "font/chinese.config"
#include "fs/exfat.config"
#include "fs/ntfs.config"
#include "fs/vfat.config"
#include "gpu/gpu.config"
#include "multimedia/audio.config"
#include "multimedia/camera.config"
#include "multimedia/gst/audio.config"
#include "multimedia/gst/camera.config"
#include "multimedia/gst/rtsp.config"
#include "multimedia/gst/video.config"
#include "multimedia/mpp.config"
#include "wifibt/bt.config"
#include "wifibt/wireless.config"
#include "tools/benchmark.config"
#include "tools/common.config"
#include "tools/test.config"
#include "network/chromium.config"
#include "npu2.config"
#include "powermanager.config"
#include "weston.config"

BR2_PACKAGE_HELLOWORLD=y
```