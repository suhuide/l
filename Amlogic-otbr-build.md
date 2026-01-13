[Amlogic.md](Amlogic.md)    
[Amlogic-matter.md](Amlogic-matter.md)   

# Reference

[OpenThread Border Router](https://openthread.io/codelabs/openthread-border-router?hl=zh-cn#1)  
[Build an embedded platform base openthread Border Router](https://blog.csdn.net/m0_46411607/article/details/132468191)  
[Matter over Thread Demo Overview](https://siliconlabs.github.io/matter/latest/thread/DEMO_OVERVIEW.html#matter-over-thread-demo-overview)  
[Matter: Build OpenThread Border Router Manually](https://community.silabs.com/s/article/Build-OpenThread-Border-Router?language=en_US)  

# Build on Ubuntu/RasPi
## Step 1, get OTBR source code 
```c
$ git clone https://github.com/openthread/ot-br-posix.git --depth 1
```
## Step 2, install service dependencies
```c
$ cd ot-br-posix
#install service dependencies
$ ./script/bootstrap
#ignore signature
echo 'Acquire::AllowInsecureRepositories "true";' | sudo tee /etc/apt/apt.conf.d/99disable-verification
```
## Step 3, build
INFRA_IF_NAME=enp2s0(ubuntu)/wlan0(raspberryPi)/eth0(raspberryPi), check from ip addr.
```c
$ INFRA_IF_NAME=wlan0 ./script/setup
```
## Step 4, check the status
```c
$ sudo service otbr-agent status
● otbr-agent.service - Border Router Agent
   Loaded: loaded (/lib/systemd/system/otbr-agent.service; enabled; vendor preset: enabled)
   Active: activating (auto-restart) (Result: exit-code) since Mon 2021-03-01 05:43:38 GMT; 2s ago
  Process: 2444 ExecStart=/usr/sbin/otbr-agent $OTBR_AGENT_OPTS (code=exited, status=2)
 Main PID: 2444 (code=exited, status=2)
```
[Openthread-build-ubuntu.md](Openthread-build-ubuntu.md)  

# Add OTBR in Amlogic SDK
Add and edit some files in buildroot directory.
```c
./buildroot/configs/amlogic/a4_ba400_spk.config
./buildroot/configs/amlogic/otbr.config
./buildroot/package/amlogic/Config.in
./buildroot/package/amlogic/otbr/Config.in
./buildroot/package/amlogic/otbr/amlogic_arm.cmake
./buildroot/package/amlogic/otbr/otbr.mk
```
Detail refer to this diff file.
```c
eric@ubuntu:/aml/dock/buildroot$ git diff
diff --git a/configs/amlogic/a4_ba400_spk.config b/configs/amlogic/a4_ba400_spk.config
index d7118c62..faf78a51 100644
--- a/configs/amlogic/a4_ba400_spk.config
+++ b/configs/amlogic/a4_ba400_spk.config
@@ -57,4 +57,5 @@ BR2_PACKAGE_AML_CUSTOMIZE_KERNEL_SET_OPT_LIST="CONFIG_FAT_DEFAULT_IOCHARSET=\"ut
 #---------Enable Matter SDK -----------------#
 #-----Add #include "matter.config" on the end------#
 #include "matter.config"
+#include "otbr.config"

diff --git a/configs/amlogic/otbr.config b/configs/amlogic/otbr.config
new file mode 100644
index 00000000..b6655ad2
--- /dev/null
+++ b/configs/amlogic/otbr.config
@@ -0,0 +1,2 @@
+# otbr common config
+BR2_PACKAGE_OTBR=y

diff --git a/package/amlogic/Config.in b/package/amlogic/Config.in
index a70c19c0..c807abb9 100644
--- a/package/amlogic/Config.in
+++ b/package/amlogic/Config.in
@@ -190,6 +190,7 @@ menu "amlogic"
 
 #AIoT Matter
     source "package/amlogic/matter/Config.in"
+    source "package/amlogic/otbr/Config.in"
 
 #lvmedia_tsplayer src
     source "package/amlogic/lvmedia_tsplayer/Config.in"
diff --git a/package/amlogic/otbr/Config.in b/package/amlogic/otbr/Config.in
new file mode 100644
index 00000000..f994401b
--- /dev/null
+++ b/package/amlogic/otbr/Config.in
@@ -0,0 +1,6 @@
+menuconfig BR2_PACKAGE_OTBR
+       bool "Amlogic OTBR"
+       help
+       It's for OTBR
+
+
diff --git a/package/amlogic/otbr/amlogic_arm.cmake b/package/amlogic/otbr/amlogic_arm.cmake
new file mode 100644
index 00000000..7e7dc5aa
--- /dev/null
+++ b/package/amlogic/otbr/amlogic_arm.cmake
@@ -0,0 +1,18 @@
+
+set(TOOLPREFIX "${SYSROOT_EXTERNAL_PATH}/../../bin/${TOOLCHAIN_EXTERNAL_PREFIX}-")
+set(CMAKE_SYSTEM_NAME Linux)
+set(CMAKE_SYSTEM_PROCESSOR arm)
+set(CMAKE_C_COMPILER    ${TOOLPREFIX}gcc)
+set(CMAKE_CXX_COMPILER  ${TOOLPREFIX}g++)
+set(CMAKE_C_COMPILER_LAUNCHER)
+set(CMAKE_CXX_COMPILER_LAUNCHER)
+set(CMAKE_ASM_COMPILER  ${TOOLPREFIX}gcc)
+set(CMAKE_AR ${TOOLPREFIX}ar)
+
+set(CMAKE_C_FLAGS   "-mthumb-interwork -mfloat-abi=hard -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -pipe -g -feliminate-unused-debug-types -Wno-psabi -lpthread" CACHE STRING "CFLAGS")
+set(CMAKE_ASM_FLAGS  "-mthumb-interwork -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security " CACHE STRING "ASM FLAGS")
+set(CMAKE_C_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -Wl,-z,relro,-z,now" CACHE STRING "LDFLAGS")
+
+set(CMAKE_CXX_FLAGS  "-mthumb-interwork -mfloat-abi=hard -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wno-psabi -lpthread" CACHE STRING "CXXFLAGS")
+set(CMAKE_CXX_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-z,relro,-z,now" CACHE STRING "LDFLAGS")
+message(STATUS "AMLOGIC TOOLPREFIX: ${TOOLPREFIX}")
diff --git a/package/amlogic/otbr/otbr.mk b/package/amlogic/otbr/otbr.mk
new file mode 100644
index 00000000..db0ddfaa
--- /dev/null
+++ b/package/amlogic/otbr/otbr.mk
@@ -0,0 +1,23 @@
+################################################################################
+#
+# OTBR
+#
+# Supported Official OTBR Version:
+# Download Address: https://github.com/openthread/ot-br-posix.git
+# Tag: 
+#
+################################################################################
+OTBR_SITE = $(TOPDIR)/../vendor/amlogic/otbr
+OTBR_SITE_METHOD = local
+
+export OTBR_STAGING_DIR = $(STAGING_DIR)
+
+define OTBR_BUILD_CMDS
+       mkdir $(@D)/examples/platforms/amlogic; \
+       echo "Copying amlogic_arm.cmake to $(@D)/examples/platforms/amlogic"; \
+       cp $(TOPDIR)/package/amlogic/otbr/amlogic_arm.cmake $(@D)/examples/platforms/amlogic/; \
+    cd $(@D); \
+       ./script/cmake-build -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/amlogic/amlogic_arm.cmake -DOT_DAEMON=ON -DBUILD_TESTING=OFF  -DOTBR_BORDER_ROUTING=ON -DOT_JOINER=ON -DOT_COMMISSIONER=ON -DOTBR_MDNS=mDNSResponder -DSYSROOT_EXTERNAL_PATH=$(CONNECTEDHOMEIP_STAGING_DIR) -DTOOLCHAIN_EXTERNAL_PREFIX=$(BR2_TOOLCHAIN_EXTERNAL_PREFIX);
+endef
+
+$(eval $(generic-package))
(END)
```
Add files list above then run a source and make show-targets, otbr should show in the below list.
```c
source setenv.sh a4_ba400_spk_a64_release&&make show-targets

alsa-lib alsa-plugins alsa-utils alsaplayer aml-audio-player aml-bootloader-message aml-bt 
aml-bt-ct aml-commonlib aml-ubootenv aml-usb-config aml-util aml-wifi android-tools5 avs-sdk 
bind bluez-alsa bluez5-utils boa brcm-patchram-plus busybox bzip2 cast-lite dbus dhcp dhcpcd 
dhd_priv dnsmasq dropbear e2fsprogs ell expat faad2 fdk-aac ffmpeg flac glib-networking gmp 
gnutls gst1-libav gst1-plugins-bad gst1-plugins-base gst1-plugins-good gst1-plugins-ugly 
gst1-rtsp-server gstreamer1 host-acl host-aml_img_packer_new host-attr host-cmake 
host-fakeroot host-libzlib host-lz4 host-lzo host-makedevs host-mkpasswd host-patchelf 
host-pkgconf host-skeleton host-squashfs host-uboot-tools host-xz host-zlib host-zstd 
hostapd htop ifupdown-scripts initscripts iozone iw json-c ledring libarchive libcap 
libconfig libcurl libdvdcss libdvdread libevent libffi libgcrypt libglib2 libgmime 
libgpg-error libical libid3tag libidn2 libmad libmnl libmpeg2 libnetfilter_conntrack 
libnfnetlink libnl libnspr libnss libogg libopenssl libsamplerate libsndfile libsoup 
libtasn1 libtool libtotem libusb libvorbis libxml2 libzlib linux lsof matter mbedtls 
mdnsresponder memstat ncurses netcat netcheck nettle nghttp2 ntp openssl openthread otbr 
pcre pkgconf popt portaudio procrank_linux readline sbc sdl2 skeleton skeleton-init-common 
skeleton-init-sysv sqlite strace swupdate taglib tdk toolchain toolchain-external 
toolchain-external-custom tzdata uboot upnp-app util-linux wavpack web-ui-wifi wifi-fw 
wpa_supplicant zlib rootfs-cpio rootfs-squashfs rootfs-tar
```

Pull source from github.
Clone source code into ./vendor/amlogic/
```c
$ git clone https://github.com/openthread/ot-br-posix.git --depth 1
```
```c
eric@ubuntu:/aml/dock/vendor/amlogic/ot-br-posix$ ls
AUTHORS  CMakeLists.txt  CODE_OF_CONDUCT.md  CONTRIBUTING.md  doc  etc  examples  
include  LICENSE  NOTICE  README.md  script  SECURITY.md  src  STYLE_GUIDE.md  
tests  third_party  tools
```

# Tips for Amlogic base OTBR compile and config
Build OTBR will generate bin file <font color="#dd00dd">otbr-agent</font>, it also build openthread, this will out put <font color="#dd00dd">ot-ctl</font> bin file.
## Cmake version 
It requests version 3.14 or higher. Otherwise, some unreasonable error may pop out.  
Here it means the <font color="#dd00dd">cmake version on host Ubuntu</font>.

```c
OPENTHREAD_CONFIG_NCP_HDLC_ENABLE=1
[155/960] Building CXX object src/core/CMakeFiles/openthread-mtd.dir/api/thread_api.cpp.o
In file included from ../../src/core/thread/link_quality.hpp:44,
                 from ../../src/core/common/message.hpp:61,
                 from ../../src/core/instance/instance.hpp:51,
                 from ../../src/core/common/locator_getters.hpp:42,
                 from ../../src/core/api/thread_api.cpp:42:
../../src/core/thread/mle_types.hpp: In constructor ‘ot::Mle::DeviceMode::DeviceMode(ot::Mle::DeviceMode::ModeConfig)’:
../../src/core/thread/mle_types.hpp:192:14: note: parameter passing for argument of type ‘ot::Mle::DeviceMode::ModeConfig’ {aka ‘otLinkModeConfig’} changed in GCC 9.1
  192 |     explicit DeviceMode(ModeConfig aModeConfig) { Set(aModeConfig); }
      |              ^~~~~~~~~~
../../src/core/api/thread_api.cpp: In function ‘otError otThreadSetLinkMode(otInstance*, otLinkModeConfig)’:
../../src/core/api/thread_api.cpp:100:9: note: parameter passing for argument of type ‘otLinkModeConfig’ changed in GCC 9.1
  100 | otError otThreadSetLinkMode(otInstance *aInstance, otLinkModeConfig aConfig)
      |         ^~~~~~~~~~~~~~~~~~~
[389/960] Building CXX object src/core/CMakeFiles/openthread-ftd.dir/api/thread_api.cpp.o
In file included from ../../src/core/thread/link_quality.hpp:44,
                 from ../../src/core/common/message.hpp:61,
                 from ../../src/core/instance/instance.hpp:51,
                 from ../../src/core/common/locator_getters.hpp:42,
                 from ../../src/core/api/thread_api.cpp:42:
../../src/core/thread/mle_types.hpp: In constructor ‘ot::Mle::DeviceMode::DeviceMode(ot::Mle::DeviceMode::ModeConfig)’:
../../src/core/thread/mle_types.hpp:192:14: note: parameter passing for argument of type ‘ot::Mle::DeviceMode::ModeConfig’ {aka ‘otLinkModeConfig’} changed in GCC 9.1
  192 |     explicit DeviceMode(ModeConfig aModeConfig) { Set(aModeConfig); }
      |              ^~~~~~~~~~
../../src/core/api/thread_api.cpp: In function ‘otError otThreadSetLinkMode(otInstance*, otLinkModeConfig)’:
../../src/core/api/thread_api.cpp:100:9: note: parameter passing for argument of type ‘otLinkModeConfig’ changed in GCC 9.1
  100 | otError otThreadSetLinkMode(otInstance *aInstance, otLinkModeConfig aConfig)
      |         ^~~~~~~~~~~~~~~~~~~
[607/960] Linking CXX static library src/lib/hdlc/libopenthread-hdlc.a
FAILED: src/lib/hdlc/libopenthread-hdlc.a 
: && /usr/bin/cmake -E remove src/lib/hdlc/libopenthread-hdlc.a && "" qc src/lib/hdlc/libopenthread-hdlc.a  src/lib/hdlc/CMakeFiles/openthread-hdlc.dir/hdlc.cpp.o && /aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-ranlib src/lib/hdlc/libopenthread-hdlc.a && :
/bin/sh: 1: : Permission denied
[608/960] Linking C static library src/lib/platform/libopenthread-platform.a
FAILED: src/lib/platform/libopenthread-platform.a 
: && /usr/bin/cmake -E remove src/lib/platform/libopenthread-platform.a && "" qc src/lib/platform/libopenthread-platform.a  src/lib/platform/CMakeFiles/openthread-platform.dir/exit_code.c.o && /aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-ranlib src/lib/platform/libopenthread-platform.a && :
/bin/sh: 1: : Permission denied
[620/960] Building CXX object src/lib/spinel/CMakeFiles/openthread-spinel-ncp.dir/spinel_encoder.cpp.o
ninja: build stopped: subcommand failed.
package/pkg-generic.mk:266: recipe for target '/aml/dock/output/a4_ba400_spk_a64_release/build/openthread/.stamp_built' failed
make[1]: *** [/aml/dock/output/a4_ba400_spk_a64_release/build/openthread/.stamp_built] Error 1
/aml/dock/output/a4_ba400_spk_a64_release/Makefile:23: recipe for target '_all' failed
make: *** [_all] Error 2

```
## Cmake config
Amlogic config
```c
//./buildroot/package/amlogic/otbr/amlogic_arm.cmake
set(TOOLPREFIX "${SYSROOT_EXTERNAL_PATH}/../../bin/${TOOLCHAIN_EXTERNAL_PREFIX}-")
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER    ${TOOLPREFIX}gcc)
set(CMAKE_CXX_COMPILER  ${TOOLPREFIX}g++)
set(CMAKE_C_COMPILER_LAUNCHER)
set(CMAKE_CXX_COMPILER_LAUNCHER)
set(CMAKE_ASM_COMPILER  ${TOOLPREFIX}gcc)
set(CMAKE_AR ${TOOLPREFIX}ar)

set(CMAKE_C_FLAGS   "-mthumb-interwork -mfloat-abi=hard -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -pipe -g -feliminate-unused-debug-types -Wno-psabi -lpthread" CACHE STRING "CFLAGS")
set(CMAKE_ASM_FLAGS  "-mthumb-interwork -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security " CACHE STRING "ASM FLAGS")
set(CMAKE_C_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -Wl,-z,relro,-z,now" CACHE STRING "LDFLAGS")

set(CMAKE_CXX_FLAGS  "-mthumb-interwork -mfloat-abi=hard -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wno-psabi -lpthread" CACHE STRING "CXXFLAGS")
set(CMAKE_CXX_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=hard -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-z,relro,-z,now" CACHE STRING "LDFLAGS")
message(STATUS "AMLOGIC TOOLPREFIX: ${TOOLPREFIX}")
```
Reference from [Build an embedded platform base openthread Border Router](https://blog.csdn.net/m0_46411607/article/details/132468191)  
```c
?examples/platforms ??????????????????????????arm.cmake??
?
examples/platforms/bcm6756/arm.cmake
?????
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER    arm-buildroot-linux-gnueabi-gcc)
set(CMAKE_CXX_COMPILER  arm-buildroot-linux-gnueabi-g++)
set(CMAKE_C_COMPILER_LAUNCHER)
set(CMAKE_CXX_COMPILER_LAUNCHER)
set(CMAKE_ASM_COMPILER  arm-buildroot-linux-gnueabi-gcc)
find_program(CMAKE_AR arm-buildroot-linux-gnueabi-gcc-ar DOC "Archiver" REQUIRED)
set(CMAKE_C_FLAGS   "-mthumb-interwork -mfloat-abi=soft -march=armv7-a+mp+sec -mcpu=cortex-a9 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -pipe -g -feliminate-unused-debug-types -Wno-psabi -lpthread" CACHE STRING "CFLAGS")
set(CMAKE_ASM_FLAGS  "-mthumb-interwork -mfloat-abi=soft -mcpu=cortex-a9 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security " CACHE STRING "ASM FLAGS")
set(CMAKE_C_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=soft -mcpu=cortex-a9 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -Wl,-z,relro,-z,now -L/opt/arm_lib -I/home/lyle/arm_include" CACHE STRING "LDFLAGS")

set(CMAKE_CXX_FLAGS  "-mthumb-interwork -mfloat-abi=soft -march=armv7-a+mp+sec -mcpu=cortex-a9 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wno-psabi -lpthread" CACHE STRING "CXXFLAGS")
set(CMAKE_CXX_LINK_FLAGS  "-mthumb -mfpu=neon -mfloat-abi=soft -mcpu=cortex-a9 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-z,relro,-z,now -L/opt/arm_lib " CACHE STRING "LDFLAGS")

FLAGS???????????

```
## Makefile
Amlogic makefile
```c
//./buildroot/package/amlogic/otbr/otbr.mk
./script/cmake-build posix -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/amlogic/amlogic_arm.cmake -DSYSROOT_EXTERNAL_PATH=$(CONNECTEDHOMEIP_STAGING_DIR) -DTOOLCHAIN_EXTERNAL_PREFIX=$(BR2_TOOLCHAIN_EXTERNAL_PREFIX)

```
Reference from [Build an embedded platform base openthread Border Router](https://blog.csdn.net/m0_46411607/article/details/132468191) 
```c
./script/cmake-build -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/bcm6756/arm.cmake -DOT_DAEMON=ON -DBUILD_TESTING=OFF  -DOTBR_BORDER_ROUTING=ON -DOT_JOINER=ON -DOT_COMMISSIONER=ON -DOTBR_MDNS=mDNSResponder

??????
-DBUILD_TESTING=OFF ????test?????????????????
-DOTBR_MDNS=mDNSResponder otbr??????????avahi??????????AVAHI??????????mdns???????????

```

## Cmake related error
```c
    : && /aml/dock/output/a4_ba400_spk_a64_release/host/aarch64-linux-gnu/sysroot/../../bin/aarch64-none-linux-gnu-gcc -Wno-error -mthumb -mfpu=neon -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -Wl,-z,relro,-z,now  CMakeFiles/cmTC_689bf.dir/testCCompiler.c.o  -o cmTC_689bf   && :
    aarch64-none-linux-gnu-gcc: error: unrecognized command-line option ‘-mthumb’
    aarch64-none-linux-gnu-gcc: error: unrecognized command-line option ‘-mfpu=neon’
    ninja: build stopped: subcommand failed.
## fatal error: dns_sd.h: No such file or directory
```
## File not found
```c
[450/485] Building CXX object src/mdns/CMakeFiles/otbr-mdns.dir/mdns_mdnssd.cpp.o
FAILED: src/mdns/CMakeFiles/otbr-mdns.dir/mdns_mdnssd.cpp.o 
/aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-g++ -DMBEDTLS_CONFIG_FILE=\"/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/mbedtls-config.h\" -DOTBR_ENABLE_BORDER_AGENT=1 -DOTBR_ENABLE_BORDER_ROUTING=1 -DOTBR_ENABLE_BORDER_ROUTING_COUNTERS=1 -DOTBR_ENABLE_DHCP6_PD=0 -DOTBR_ENABLE_EPSKC=1 -DOTBR_ENABLE_LINK_METRICS_TELEMETRY=0 -DOTBR_ENABLE_MDNS_MDNSSD=1 -DOTBR_ENABLE_NAT64=0 -DOTBR_ENABLE_NOTIFY_UPSTART=1 -DOTBR_ENABLE_PUBLISH_MESHCOP_BA_ID=1 -DOTBR_ENABLE_VENDOR_INFRA_LINK_SELECT=0 -DOTBR_MESHCOP_SERVICE_INSTANCE_NAME="\"OpenThread BorderRouter\"" -DOTBR_PACKAGE_NAME=\"OpenThread_BorderRouter\" -DOTBR_PACKAGE_VERSION=\"0.3.0\" -DOTBR_PRODUCT_NAME=\"BorderRouter\" -DOTBR_SYSLOG_FACILITY_ID=LOG_USER -DOTBR_VENDOR_NAME=\"OpenThread\" -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/include -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/src -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build/otbr/third_party/openthread/repo/etc/cmake -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/etc/cmake -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/include -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/src/posix/platform/include -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/src -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/third_party/mbedtls/repo/include -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/third_party/mbedtls/repo/3rdparty/everest/include -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/third_party/mbedtls/repo/3rdparty/p256-m -I/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/third_party/openthread/repo/third_party/mbedtls/repo/3rdparty/p256-m/p256-m -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wno-psabi -lpthread -std=c++11 -Wall -Wextra -Werror -Wfatal-errors -Wuninitialized -Wno-missing-braces -MD -MT src/mdns/CMakeFiles/otbr-mdns.dir/mdns_mdnssd.cpp.o -MF src/mdns/CMakeFiles/otbr-mdns.dir/mdns_mdnssd.cpp.o.d -o src/mdns/CMakeFiles/otbr-mdns.dir/mdns_mdnssd.cpp.o -c /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/src/mdns/mdns_mdnssd.cpp
In file included from /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/src/mdns/mdns_mdnssd.cpp:36:
/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/src/mdns/mdns_mdnssd.hpp:46:10: fatal error: dns_sd.h: No such file or directory
   46 | #include <dns_sd.h>
      |          ^~~~~~~~~~
compilation terminated.
[463/485] Building CXX object src/mdns/CMakeFiles/otbr-mdns.dir/mdns.cpp.o
```
Copy dns_sd.h into src/mdns/, then modify mdns_mdnssd.hpp #include "dns_sd.h"


## Cannot find -ldns_sd
```c
OPENTHREAD_CONFIG_TMF_PROXY_DUA_ENABLE=1
OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE=1
[2/2] Linking CXX executable src/agent/otbr-agent
FAILED: src/agent/otbr-agent 
: && /aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-g++ -march=armv8-a -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wno-psabi -lpthread -mtune=cortex-a55 -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fvisibility-inlines-hidden -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-z,relro,-z,now -rdynamic src/agent/CMakeFiles/otbr-agent.dir/application.cpp.o src/agent/CMakeFiles/otbr-agent.dir/main.cpp.o -o src/agent/otbr-agent  src/border_agent/libotbr-border-agent.a  src/mdns/libotbr-mdns.a  third_party/openthread/repo/src/posix/platform/libopenthread-posix.a  third_party/openthread/repo/src/cli/libopenthread-cli-ftd.a  third_party/openthread/repo/src/core/libopenthread-ftd.a  third_party/openthread/repo/src/lib/spinel/libopenthread-spinel-rcp.a  third_party/openthread/repo/src/lib/spinel/libopenthread-radio-spinel.a  third_party/openthread/repo/src/lib/hdlc/libopenthread-hdlc.a  src/sdp_proxy/libotbr-sdp-proxy.a  src/ncp/libotbr-ncp.a  src/common/libotbr-common.a  src/utils/libotbr-utils.a  src/trel_dnssd/libotbr-trel-dnssd.a  src/mdns/libotbr-mdns.a  -ldns_sd  src/ncp/posix/libotbr-posix.a  src/utils/libotbr-utils.a  src/common/libotbr-common.a  third_party/openthread/repo/src/posix/platform/libopenthread-posix.a  third_party/openthread/repo/src/cli/libopenthread-cli-ftd.a  third_party/openthread/repo/src/lib/spinel/libopenthread-spinel-rcp.a  third_party/openthread/repo/src/lib/spinel/libopenthread-radio-spinel.a  third_party/openthread/repo/src/lib/hdlc/libopenthread-hdlc.a  third_party/openthread/repo/src/lib/platform/libopenthread-platform.a  third_party/openthread/repo/src/lib/url/libopenthread-url.a  -lutil  -lrt  -lanl  third_party/openthread/repo/src/core/libopenthread-ftd.a  third_party/openthread/repo/third_party/tcplp/libtcplp-ftd.a  third_party/openthread/repo/src/core/libopenthread-ftd.a  third_party/openthread/repo/third_party/tcplp/libtcplp-ftd.a  third_party/openthread/repo/third_party/mbedtls/repo/library/libmbedtls.a  third_party/openthread/repo/third_party/mbedtls/repo/library/libmbedx509.a  third_party/openthread/repo/third_party/mbedtls/repo/library/libmbedcrypto.a  third_party/openthread/repo/third_party/mbedtls/repo/3rdparty/everest/libeverest.a  third_party/openthread/repo/third_party/mbedtls/repo/3rdparty/p256-m/libp256m.a && :
/aml/dock/toolchain/gcc/linux-x86/aarch64/gcc-arm-10.2-2020.11-x86_64-aarch64-none-linux-gnu/bin/../lib/gcc/aarch64-none-linux-gnu/10.2.1/../../../../aarch64-none-linux-gnu/bin/ld: cannot find -ldns_sd
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
package/pkg-generic.mk:266: recipe for target '/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_built' failed
make[1]: *** [/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_built] Error 1
/aml/dock/output/a4_ba400_spk_a64_release/Makefile:23: recipe for target '_all' failed
make: *** [_all] Error 2

```
mdns lib libdns_sd.so not found, need to reinstall.
```c
make show-targets
```
We can see <font color="#dd00dd">mdnsresponder</font> on the list.
```c
alsa-lib alsa-plugins alsa-utils alsaplayer aml-audio-player aml-bootloader-message aml-bt 
aml-bt-ct aml-commonlib aml-ubootenv aml-usb-config aml-util aml-wifi android-tools5 avs-sdk 
bind bluez-alsa bluez5-utils boa brcm-patchram-plus busybox bzip2 cast-lite dbus dhcp dhcpcd 
dhd_priv dnsmasq dropbear e2fsprogs ell expat faad2 fdk-aac ffmpeg flac glib-networking gmp 
gnutls gst1-libav gst1-plugins-bad gst1-plugins-base gst1-plugins-good gst1-plugins-ugly 
gst1-rtsp-server gstreamer1 host-acl host-aml_img_packer_new host-attr host-cmake 
host-fakeroot host-libzlib host-lz4 host-lzo host-makedevs host-mkpasswd host-patchelf 
host-pkgconf host-skeleton host-squashfs host-uboot-tools host-xz host-zlib host-zstd 
hostapd htop ifupdown-scripts initscripts iozone iw json-c ledring libarchive libcap 
libconfig libcurl libdvdcss libdvdread libevent libffi libgcrypt libglib2 libgmime 
libgpg-error libical libid3tag libidn2 libmad libmnl libmpeg2 libnetfilter_conntrack 
libnfnetlink libnl libnspr libnss libogg libopenssl libsamplerate libsndfile libsoup 
libtasn1 libtool libtotem libusb libvorbis libxml2 libzlib linux lsof matter mbedtls 
mdnsresponder memstat ncurses netcat netcheck nettle nghttp2 ntp openssl openthread otbr 
pcre pkgconf popt portaudio procrank_linux readline sbc sdl2 skeleton skeleton-init-common 
skeleton-init-sysv sqlite strace swupdate taglib tdk toolchain toolchain-external 
toolchain-external-custom tzdata uboot upnp-app util-linux wavpack web-ui-wifi wifi-fw 
wpa_supplicant zlib rootfs-cpio rootfs-squashfs rootfs-tar
```
Rebuild to get the package.
```c
make mdnsresponde-rebuild
````
Compile successed.
```c
eric@ubuntu:/aml/dock$ find -name 'otbr-agent'
./output/a4_ba400_spk_a64_release/build/otbr/build/otbr/src/agent/otbr-agent
eric@ubuntu:/aml/dock$ find -name 'ot-ctl'
./output/a4_ba400_spk_a64_release/build/otbr/build/otbr/third_party/openthread/repo/src/posix/ot-ctl
eric@ubuntu:/aml/dock$ find -name 'chip-tool'
./vendor/amlogic/matter/amlogic_build_out/BA400_SBR/chip-tool
./vendor/amlogic/matter/amlogic_build_out/BA400_SBR/chip-tool/chip-tool
./vendor/amlogic/matter/amlogic_build_out/BA400_SBR/chip-tool/obj/third_party/connectedhomeip/zzz_generated/chip-tool
./vendor/amlogic/matter/zzz_generated/chip-tool
./vendor/amlogic/matter/examples/chip-tool
./vendor/amlogic/matter/.environment/gn_out/obj/examples/chip-tool
./buildroot/amlogic_build_out/BA400_SBR/chip-tool
eric@ubuntu:/aml/dock$ 

```
```c
[11:52:26.191]ÄÂĹĂ˘ÂÂĂ˘ÂÂhelp

  base64          Base64 encode / decode utilities
  exit            Exit the shell application
  help            List out all top level commands
  version         Output the software version
  ble             BLE transport commands
  config          Manage device configuration. Usage to dump value: config [param_name] and to set some values (discriminator): config [param_name] [param_value].
  device          Device management commands
  onboardingcodes Dump device onboarding codes. Usage: onboardingcodes none|softap|ble|onnetwork [qrcode|qrcodeurl|manualpairingcode]
  dns             Dns client commands
  ota             OTA commands
  stat            Statistics commands
  echo            Echo back provided inputs
  log             Logging utilities
  rand            Random number utilities
  otcli           Dispatch OpenThread CLI command
Done
```

[Amlogic.md](Amlogic.md)  
[Amlogic-matter.md](Amlogic-matter.md)   

```c
ls@ls-VirtualBox:/aml/dock$ make otbr-rebuild
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_rsynced
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_staging_installed
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_target_installed
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_images_installed
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_host_installed
rm -f /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_built
>>> otbr  Syncing from source dir /aml/dock/buildroot/../vendor/amlogic/ot-br-posix
rsync -au --chmod=u=rwX,go=rX  --exclude .svn --exclude .git --exclude .hg --exclude .bzr --exclude CVS /aml/dock/buildroot/../vendor/amlogic/ot-br-posix/ /aml/dock/output/a4_ba400_spk_a64_release/build/otbr
>>> otbr  Patching
>>> otbr  Configuring
>>> otbr  Building
mkdir /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/examples/platforms/amlogic; echo "Copying amlogic_arm.cmake to /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/examples/platforms/amlogic"; cp /aml/dock/buildroot/package/amlogic/otbr/amlogic_arm.cmake /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/examples/platforms/amlogic/; cd /aml/dock/output/a4_ba400_spk_a64_release/build/otbr; ./script/cmake-build -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/amlogic/amlogic_arm.cmake -DOT_DAEMON=ON -DBUILD_TESTING=OFF  -DOTBR_BORDER_ROUTING=ON -DOT_JOINER=ON -DOT_COMMISSIONER=ON -DOTBR_MDNS=mDNSResponder -DSYSROOT_EXTERNAL_PATH=/aml/dock/output/a4_ba400_spk_a64_release/host/aarch64-linux-gnu/sysroot -DTOOLCHAIN_EXTERNAL_PREFIX="aarch64-none-linux-gnu";
Copying amlogic_arm.cmake to /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/examples/platforms/amlogic
+++ dirname ./script/cmake-build
++ cd ./script/..
++ HAVE_SYSTEMCTL=0
++ have systemctl
++ command -v systemctl
++ HAVE_SYSTEMCTL=1
++ HAVE_SERVICE=0
++ have service
++ command -v service
++ HAVE_SERVICE=1
++ [[ ! -n '' ]]
++ grep -s 'BeagleBone Black' /sys/firmware/devicetree/base/model
++ case "${OSTYPE}" in
++ have_or_die lsb_release
++ have lsb_release
++ command -v lsb_release
+++ lsb_release -i
+++ cut -c17-
+++ tr '[:upper:]' '[:lower:]'
++ PLATFORM=ubuntu
++ echo 'Current platform is ubuntu'
Current platform is ubuntu
++ with BORDER_ROUTING
++ local value
+++ printenv BORDER_ROUTING
++ value=
++ [[ -z '' ]]
++ [[ -f examples/platforms/ubuntu/default ]]
+++ . examples/platforms/ubuntu/default
++++ NAT64=1
++++ DNS64=0
++++ DHCPV6_PD=0
++++ NETWORK_MANAGER=0
++++ BACKBONE_ROUTER=1
++++ BORDER_ROUTING=1
++++ WEB_GUI=1
++++ REST_API=1
+++ eval echo '${BORDER_ROUTING-}'
++++ echo 1
++ value=1
++ [[ 1 == 1 ]]
++ with DHCPV6_PD
++ local value
+++ printenv DHCPV6_PD
++ value=
++ [[ -z '' ]]
++ [[ -f examples/platforms/ubuntu/default ]]
+++ . examples/platforms/ubuntu/default
++++ NAT64=1
++++ DNS64=0
++++ DHCPV6_PD=0
++++ NETWORK_MANAGER=0
++++ BACKBONE_ROUTER=1
++++ BORDER_ROUTING=1
++++ WEB_GUI=1
++++ REST_API=1
+++ eval echo '${DHCPV6_PD-}'
++++ echo 0
++ value=0
++ [[ 0 == 1 ]]
++ with BORDER_ROUTING
++ local value
+++ printenv BORDER_ROUTING
++ value=
++ [[ -z '' ]]
++ [[ -f examples/platforms/ubuntu/default ]]
+++ . examples/platforms/ubuntu/default
++++ NAT64=1
++++ DNS64=0
++++ DHCPV6_PD=0
++++ NETWORK_MANAGER=0
++++ BACKBONE_ROUTER=1
++++ BORDER_ROUTING=1
++++ WEB_GUI=1
++++ REST_API=1
+++ eval echo '${BORDER_ROUTING-}'
++++ echo 1
++ value=1
++ [[ 1 == 1 ]]
++ with NETWORK_MANAGER
++ local value
+++ printenv NETWORK_MANAGER
++ value=
++ [[ -z '' ]]
++ [[ -f examples/platforms/ubuntu/default ]]
+++ . examples/platforms/ubuntu/default
++++ NAT64=1
++++ DNS64=0
++++ DHCPV6_PD=0
++++ NETWORK_MANAGER=0
++++ BACKBONE_ROUTER=1
++++ BORDER_ROUTING=1
++++ WEB_GUI=1
++++ REST_API=1
+++ eval echo '${NETWORK_MANAGER-}'
++++ echo 0
++ value=0
++ [[ 0 == 1 ]]
++ STAGE_DIR=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage
++ BUILD_DIR=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build
++ [[ -d /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage ]]
++ mkdir -v -p /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage
mkdir: created directory '/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage'
++ [[ -d /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build ]]
++ mkdir -v -p /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build
mkdir: created directory '/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build'
++ export PATH=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage/usr/bin:/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage/usr/sbin:/home/ls/miniconda3/condabin:/home/ls/.cargo/bin:/data/tools/android/sdk/platform-tools:/data/tools/android/studio/bin:/data/tools/flutter/bin:/pkg/java11/bin:/pkg/java11/jre/bin:/usr/lib/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
++ PATH=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage/usr/bin:/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/stage/usr/sbin:/home/ls/miniconda3/condabin:/home/ls/.cargo/bin:/data/tools/android/sdk/platform-tools:/data/tools/android/studio/bin:/data/tools/flutter/bin:/pkg/java11/bin:/pkg/java11/jre/bin:/usr/lib/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
+++ basename ./script/cmake-build
++ TASKNAME=cmake-build
++ BEFORE_HOOK=examples/platforms/ubuntu/before_cmake-build
++ AFTER_HOOK=examples/platforms/ubuntu/after_cmake-build
++ [[ ! -f examples/platforms/ubuntu/before_cmake-build ]]
++ BEFORE_HOOK=/dev/null
++ [[ ! -f examples/platforms/ubuntu/after_cmake-build ]]
++ AFTER_HOOK=/dev/null
+ OTBR_TOP_SRCDIR=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr
+ readonly OTBR_TOP_SRCDIR
+ OTBR_TOP_BUILD_DIR=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build/otbr
+ readonly OTBR_TOP_BUILD_DIR
+ OTBR_TARGET=
+ main -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/amlogic/amlogic_arm.cmake -DOT_DAEMON=ON -DBUILD_TESTING=OFF -DOTBR_BORDER_ROUTING=ON -DOT_JOINER=ON -DOT_COMMISSIONER=ON -DOTBR_MDNS=mDNSResponder -DSYSROOT_EXTERNAL_PATH=/aml/dock/output/a4_ba400_spk_a64_release/host/aarch64-linux-gnu/sysroot -DTOOLCHAIN_EXTERNAL_PREFIX=aarch64-none-linux-gnu
+ local builddir=/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build/otbr
+ mkdir -p /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build/otbr
+ cd /aml/dock/output/a4_ba400_spk_a64_release/build/otbr/build/otbr
+ cmake -GNinja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON /aml/dock/output/a4_ba400_spk_a64_release/build/otbr -DCMAKE_TOOLCHAIN_FILE=./examples/platforms/amlogic/amlogic_arm.cmake -DOT_DAEMON=ON -DBUILD_TESTING=OFF -DOTBR_BORDER_ROUTING=ON -DOT_JOINER=ON -DOT_COMMISSIONER=ON -DOTBR_MDNS=mDNSResponder -DSYSROOT_EXTERNAL_PATH=/aml/dock/output/a4_ba400_spk_a64_release/host/aarch64-linux-gnu/sysroot -DTOOLCHAIN_EXTERNAL_PREFIX=aarch64-none-linux-gnu
./script/cmake-build: line 78: cmake: command not found
package/pkg-generic.mk:266: recipe for target '/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_built' failed
make[1]: *** [/aml/dock/output/a4_ba400_spk_a64_release/build/otbr/.stamp_built] Error 127
/aml/dock/output/a4_ba400_spk_a64_release/Makefile:23: recipe for target '_all' failed
make: *** [_all] Error 2
```

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
```c
OPENTHREAD_CONFIG_TMF_PROXY_DUA_ENABLE=1
OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE=1
[485/485] Linking CXX executable src/agent/otbr-agent
>>> otbr  Installing to target
ls@ls-VirtualBox:/aml/dock$ find -name otbr-agent
./output/a4_ba400_spk_a64_release/build/otbr/build/otbr/src/agent/otbr-agent
```