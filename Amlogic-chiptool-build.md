[Amlogic.md](Amlogic.md)  
[Amlogic-matter.md](Amlogic-matter.md)   

# Build Amlogic base matter
```c
source setenv.sh a4_ba400_spk_a64_release
source setenv.sh a4_ba400_spk_a64_k66_release
make matter-rebuild
make
```
# Add matter config in buildroot
Add and edit some files in buildroot directory.
```c
./buildroot/configs/amlogic/a4_ba400_spk.config
./buildroot/configs/amlogic/matter.config
./buildroot/package/amlogic/Config.in
./buildroot/package/amlogic/matter/Config.in
./buildroot/package/amlogic/matter/matter.mk
```
Detail refer to this diff file.
```c
eric@ubuntu:/aml/dock/buildroot$ git diff
diff --git a/configs/amlogic/a4_ba400_spk.config b/configs/amlogic/a4_ba400_spk.config
index ad8b5c43..d7118c62 100644
--- a/configs/amlogic/a4_ba400_spk.config
+++ b/configs/amlogic/a4_ba400_spk.config
@@ -54,5 +54,7 @@ BR2_PACKAGE_AML_CUSTOMIZE_KERNEL_ENABLE_OPT_LIST="CONFIG_NLS_UTF8"
 BR2_PACKAGE_AML_CUSTOMIZE_KERNEL_DISABLE_OPT_LIST=""
 BR2_PACKAGE_AML_CUSTOMIZE_KERNEL_SET_OPT_LIST="CONFIG_FAT_DEFAULT_IOCHARSET=\"utf8\""
 
-
+#---------Enable Matter SDK -----------------#
+#-----Add #include "matter.config" on the end------#
+#include "matter.config"
 
diff --git a/configs/amlogic/matter.config b/configs/amlogic/matter.config
index 67125a5a..21eba19b 100644
--- a/configs/amlogic/matter.config
+++ b/configs/amlogic/matter.config
@@ -1,8 +1,21 @@
-BR2_PACKAGE_CONNECTEDHOMEIP=y
+# Matter common config
+BR2_PACKAGE_MATTER=y
 BR2_PACKAGE_WPA_SUPPLICANT_DBUS=y
 BR2_PACKAGE_WPA_SUPPLICANT_DBUS_INTROSPECTION=y
+BR2_PACKAGE_WPA_SUPPLICANT_WPA3=y
 BR2_PACKAGE_BIND_TOOLS=y
 BR2_PACKAGE_DHCP=y
 BR2_PACKAGE_DHCP_CLIENT=y
 BR2_PACKAGE_AML_BRCM_BSA=n
 BR2_PACKAGE_BRCM_PATCHRAM_PLUS=y
+
+# Specific matter apps that need to be compiled
+BR2_PACKAGE_MATTER_CHIP_TOOL=y
+BR2_PACKAGE_MATTER_CHIP_SHELL=n
+BR2_PACKAGE_MATTER_ALL_CLUSTERS_APP=n
+BR2_PACKAGE_MATTER_LIGHTING_APP=n
+BR2_PACKAGE_MATTER_SOUNDBAR_APP=n
+BR2_PACKAGE_MATTER_WIFI_SETUP_APP=n
+
+# Amlogic matter specific configuration
+BR2_PACKAGE_AML_MATTER_SECURITY=n
diff --git a/package/amlogic/Config.in b/package/amlogic/Config.in
index 45682986..a70c19c0 100644
--- a/package/amlogic/Config.in
+++ b/package/amlogic/Config.in
@@ -189,7 +189,7 @@ menu "amlogic"
 # source "package/amlogic/ffmpeg-aml/Config.in"
 
 #AIoT Matter
-    source "package/amlogic/connectedhomeip/Config.in"
+    source "package/amlogic/matter/Config.in"
 
 #lvmedia_tsplayer src
     source "package/amlogic/lvmedia_tsplayer/Config.in"
diff --git a/package/amlogic/matter/Config.in b/package/amlogic/matter/Config.in
new file mode 100644
index 00000000..e1eb6c11
--- /dev/null
+++ b/package/amlogic/matter/Config.in
@@ -0,0 +1,81 @@
+menuconfig BR2_PACKAGE_MATTER
+       bool "Amlogic Matter"
+       select BR2_PACKAGE_OPENSSL
+       help
+               It's for Matter
+
+if BR2_PACKAGE_MATTER
+
+config BR2_PACKAGE_AML_MATTER_CLIENT
+       bool "Aml Matter Client Demo and Library"
+       default n
+       select BR2_PACKAGE_AML_LOG
+       select BR2_PACKAGE_CJSON
+       select BR2_PACKAGE_LIBWEBSOCKETS
+       depends on BR2_PACKAGE_MATTER
+       help
+               Enable Aml Matter Client Library
+
+config BR2_PACKAGE_AML_MATTER_USING_THREAD
+       bool "Aml Matter Using Thread"
+       default n
+       depends on BR2_PACKAGE_MATTER
+       help
+               Enable Aml Matter Thread
+
+config BR2_PACKAGE_MATTER_CHIP_TOOL
+    bool "Build Matter Chip Tool"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter Chip Tool application.
+
+config BR2_PACKAGE_MATTER_CHIP_SHELL
+    bool "Build Matter Chip Shell"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter Chip Shell application.
+
+config BR2_PACKAGE_MATTER_ALL_CLUSTERS_APP
+    bool "Build Matter All Clusters App"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter All Clusters application.
+
+config BR2_PACKAGE_MATTER_LIGHTING_APP
+    bool "Build Matter Lighting App"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter Lighting application.
+
+config BR2_PACKAGE_AML_EXTRA_MATTER_PATCH
+    string "input project matter extra patches"
+    default ""
+    help
+      set project matter extra patches path.
+
+config BR2_PACKAGE_AML_MATTER_SECURITY
+    bool "Enable Amlogic security crypto for Matter"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Enable Amlogic security crypto  for Matter.
+
+config BR2_PACKAGE_MATTER_SOUNDBAR_APP
+    bool "Build Matter Soundbar App"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter Soundbar application.
+
+config BR2_PACKAGE_MATTER_WIFI_SETUP_APP
+    bool "Build Matter WIFI SETUP App"
+    default n
+    depends on BR2_PACKAGE_MATTER
+    help
+        Build the Matter WIFI SETUP application.
+
+endif
diff --git a/package/amlogic/matter/matter.mk b/package/amlogic/matter/matter.mk
new file mode 100644
index 00000000..b06fd2f6
--- /dev/null
+++ b/package/amlogic/matter/matter.mk
@@ -0,0 +1,224 @@
+################################################################################
+#
+# Matter(CHIP)
+#
+# Supported Official Matter Version: 1.3
+# Download Address: https://github.com/project-chip/connectedhomeip.git
+# Tag: v1.3.0.0
+#
+################################################################################
+
+MATTER_SITE = $(TOPDIR)/../vendor/amlogic/matter
+MATTER_SITE_METHOD = local
+MATTER_DEPENDENCIES = openssl
+
+export MATTER_SYSROOT_DIR = $(STAGING_DIR)
+MATTER_SOURCE = $(MATTER_SITE)
+BOARD_NAME = $(BR2_PACKAGE_AML_SOC_BOARD_NAME)
+STORAGE_DIRECT = /etc/matter
+IS_DEBUG = false
+BUILD_OUT_DIR = amlogic_build_out
+ENABLE_AMLOGIC_CHIP_TOOL = false
+ENABLE_AMLOGIC_CREDENTIAL = false
+DEFAULT_AMLOGIC_CREDENTIAL = false
+
+TOOLCHAIN_PATH = $(TARGET_CROSS)
+
+# Avoid unnecessary file copying to speed up compilation
+MATTER_OVERRIDE_SRCDIR_RSYNC_EXCLUSIONS += --exclude .environment --exclude docs
+
+define MATTER_PREPARE_SUBMODULE
+       cd $(MATTER_SOURCE)/ && \
+       git submodule update --init --depth=1 --recursive \
+       third_party/nlassert/repo \
+       third_party/nlio/repo \
+       third_party/nlunit-test/repo \
+       examples/common/QRCode/repo \
+       third_party/pigweed/repo \
+       third_party/openthread/repo \
+       third_party/ot-br-posix/repo \
+       third_party/jsoncpp/repo \
+       third_party/editline/repo \
+       third_party/boringssl/repo/src \
+       third_party/libwebsockets/repo \
+       third_party/perfetto/repo
+endef
+
+MATTER_POST_RSYNC_HOOKS += MATTER_PREPARE_SUBMODULE
+
+ifdef BR2_PACKAGE_AML_EXTRA_MATTER_PATCH
+define MATTER_APPLY_COMMON_PATCHES
+  if [ -d $(BR2_PACKAGE_AML_EXTRA_MATTER_PATCH) ]; then \
+               echo patch for extra matter; \
+               $(APPLY_PATCHES) $(@D) $(BR2_PACKAGE_AML_EXTRA_MATTER_PATCH) *.patch; \
+  fi
+endef
+MATTER_POST_PATCH_HOOKS += MATTER_APPLY_COMMON_PATCHES
+endif
+
+IS_ACTIVATE_ENV = true
+
+ifeq ($(BR2_PACKAGE_AML_MATTER_SECURITY),y)
+# Enable amlogic credential for matter security
+ENABLE_AMLOGIC_CREDENTIAL = true
+#if you need to update security library and source code,
+#please enter matter/third_party/amlogic_sdk/security_crypto/
+#run ./build.sh script to compile and update new library.
+endif
+# Configuration of matter client
+ifeq ($(BR2_PACKAGE_AML_MATTER_CLIENT),y)
+MATTER_DEPENDENCIES += cjson aml-commonlib libwebsockets
+
+# Determine need to compile the test client bin
+IS_BUILD_TEST_CLIENT = false
+
+define AML_MATTER_CLIENT_BUILD_CMDS
+       echo "Building Matter Client..."
+       $(MAKE) CC=$(TARGET_CC) CXX=$(TARGET_CXX) -C $(@D)/third_party/amlogic_sdk/aml_matter_client all IS_BUILD_TEST_CLIENT=$(IS_BUILD_TEST_CLIENT)
+endef
+define AML_MATTER_CLIENT_INSTALL_TARGET_CMDS
+       $(MAKE) -C $(@D)/third_party/amlogic_sdk/aml_matter_client install
+endef
+endif
+
+# Configuration for Matter Chip Tool
+ifeq ($(BR2_PACKAGE_MATTER_CHIP_TOOL),y)
+ifeq ($(ENABLE_AMLOGIC_CHIP_TOOL),true)
+CHIP_TOOL_APP_NAME = amlogic-chip-tool
+else
+CHIP_TOOL_APP_NAME = chip-tool
+endif
+define MATTER_CHIP_TOOL_BUILD_CMDS
+       echo "Building Matter Chip Tool..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_TOOL_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(DEFAULT_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_CHIP_TOOL_INSTALL_TARGET_CMDS
+       echo "Installing Matter Chip Tool..."
+       mkdir -p $(TARGET_DIR)/etc/matter_credentials/paa-root-certs/
+       cp -r $(MATTER_SOURCE)/credentials/development/paa-root-certs/Chip-Test-PAA-* $(TARGET_DIR)/etc/matter_credentials/paa-root-certs/
+       cp -r $(MATTER_SOURCE)/credentials/production/paa-root-certs/* $(TARGET_DIR)/etc/matter_credentials/paa-root-certs/
+       $(INSTALL) -D -m 755 $(MATTER_SITE)/third_party/amlogic_sdk/scripts/S91matter \
+               $(TARGET_DIR)/etc/init.d/S91matter
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_TOOL_APP_NAME)/chip-tool \
+               $(TARGET_DIR)/usr/bin/chip-tool
+endef
+endif
+
+# Configuration for Matter Chip Shell
+ifeq ($(BR2_PACKAGE_MATTER_CHIP_SHELL),y)
+CHIP_SHELL_APP_NAME = chip-shell
+define MATTER_CHIP_SHELL_BUILD_CMDS
+       echo "Building Matter Chip Shell..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_SHELL_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(DEFAULT_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_CHIP_SHELL_INSTALL_TARGET_CMDS
+       echo "Installing Matter Chip Shell..."
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_SHELL_APP_NAME)/chip-shell \
+               $(TARGET_DIR)/usr/bin/chip-shell
+endef
+endif
+
+# Configuration for Matter All Clusters App
+ifeq ($(BR2_PACKAGE_MATTER_ALL_CLUSTERS_APP),y)
+CHIP_ALL_CLUSTERS_APP_NAME = all-clusters-app
+define MATTER_ALL_CLUSTERS_APP_BUILD_CMDS
+       echo "Building Matter All Clusters App..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_ALL_CLUSTERS_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(ENABLE_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_ALL_CLUSTERS_APP_INSTALL_TARGET_CMDS
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_ALL_CLUSTERS_APP_NAME)/chip-all-clusters-app \
+               $(TARGET_DIR)/usr/bin/chip-all-clusters-app
+endef
+endif
+
+# Configuration for Matter Lighting App
+ifeq ($(BR2_PACKAGE_MATTER_LIGHTING_APP),y)
+CHIP_LIGHTING_APP_NAME = lighting-app
+define MATTER_LIGHTING_APP_BUILD_CMDS
+       echo "Building Matter Lighting App..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_LIGHTING_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(ENABLE_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_LIGHTING_APP_INSTALL_TARGET_CMDS
+       echo "Installing Matter Lighting App..."
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_LIGHTING_APP_NAME)/chip-lighting-app \
+               $(TARGET_DIR)/usr/bin/chip-lighting-app
+endef
+endif
+
+# Configuration for Matter Soundbar App
+ifeq ($(BR2_PACKAGE_MATTER_SOUNDBAR_APP),y)
+CHIP_SOUNDBAR_APP_NAME = soundbar-app
+define MATTER_SOUNDBAR_APP_BUILD_CMDS
+       echo "Building Matter Soundbar App..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_SOUNDBAR_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(ENABLE_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_SOUNDBAR_APP_INSTALL_TARGET_CMDS
+       echo "Installing Matter Soundbar App..."
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_SOUNDBAR_APP_NAME)/chip-soundbar-app \
+               $(TARGET_DIR)/usr/bin/chip-soundbar-app
+endef
+endif
+
+# Configuration for Matter WiFi Setup App
+ifeq ($(BR2_PACKAGE_MATTER_WIFI_SETUP_APP),y)
+CHIP_WIFI_SETUP_APP_NAME = wifi-setup-app
+define MATTER_WIFI_SETUP_APP_BUILD_CMDS
+       echo "Building Matter WiFi Setup App..."; \
+       $(@D)/scripts/examples/gn_amlogic_example.sh $(BOARD_NAME) $(CHIP_WIFI_SETUP_APP_NAME) $(MATTER_SYSROOT_DIR) $(BUILD_OUT_DIR) $(TOOLCHAIN_PATH) $(IS_DEBUG) $(IS_ACTIVATE_ENV) $(ENABLE_AMLOGIC_CREDENTIAL);
+endef
+define MATTER_WIFI_SETUP_APP_INSTALL_TARGET_CMDS
+       echo "Installing Matter WiFi Setup App..."
+       $(INSTALL) -D -m 755 \
+               $(@D)/$(BUILD_OUT_DIR)/$(BOARD_NAME)/$(CHIP_WIFI_SETUP_APP_NAME)/chip-wifi-setup-app \
+               $(TARGET_DIR)/usr/bin/chip-wifi-setup-app
+endef
+endif
+
+# Configuration for thread
+ifeq ($(BR2_PACKAGE_AML_MATTER_USING_THREAD),y)
+define AML_MATTER_USING_THREAD_INSTALL_TARGET_CMDS
+       $(INSTALL) -D -m 755 $(MATTER_SITE)/third_party/amlogic_sdk/scripts/S93thread \
+               $(TARGET_DIR)/etc/init.d/S93thread
+endef
+endif
+
+# Amlogic Security Mechanism
+ifeq ($(BR2_PACKAGE_AML_MATTER_SECURITY),y)
+define AML_MATTER_SECURITY_INSTALL_TARGET_CMDS
+       $(INSTALL) -D -m 644 $(MATTER_SITE)/src/platform/Linux/amlogic/libmatter_keypair.so \
+               $(TARGET_DIR)/usr/lib/libmatter_keypair.so
+endef
+endif
+# build action
+define MATTER_BUILD_CMDS
+       cd $(@D); \
+       source $(MATTER_SOURCE)/scripts/activate.sh; \
+       $(MATTER_CHIP_TOOL_BUILD_CMDS) \
+       $(MATTER_CHIP_SHELL_BUILD_CMDS) \
+       $(MATTER_ALL_CLUSTERS_APP_BUILD_CMDS) \
+       $(MATTER_LIGHTING_APP_BUILD_CMDS) \
+       $(MATTER_SOUNDBAR_APP_BUILD_CMDS) \
+       $(MATTER_WIFI_SETUP_APP_BUILD_CMDS) \
+       $(AML_MATTER_CLIENT_BUILD_CMDS)
+endef
+
+# install action
+define MATTER_INSTALL_INIT_SYSV
+       mkdir -p $(TARGET_DIR)$(STORAGE_DIRECT)
+       $(MATTER_CHIP_TOOL_INSTALL_TARGET_CMDS)
+       $(MATTER_CHIP_SHELL_INSTALL_TARGET_CMDS)
+       $(MATTER_ALL_CLUSTERS_APP_INSTALL_TARGET_CMDS)
+       $(MATTER_LIGHTING_APP_INSTALL_TARGET_CMDS)
+       $(MATTER_SOUNDBAR_APP_INSTALL_TARGET_CMDS)
+       $(MATTER_WIFI_SETUP_APP_INSTALL_TARGET_CMDS)
+       $(AML_MATTER_CLIENT_INSTALL_TARGET_CMDS)
+       $(AML_MATTER_USING_THREAD_INSTALL_TARGET_CMDS)
+       $(AML_MATTER_SECURITY_INSTALL_TARGET_CMDS)
+endef
+
+$(eval $(generic-package))
(END)

```
# Copy matter source code
Put code under directory ./vendor/amlogic/
```c
matter.git.tar.gz
unzip to .repo/project-objects/aiot/matter.git

matter.git_projects.tar.gz
unzip to .repo/projects/vendor/amlogic/matter.git
```
```c
eric@ubuntu:/aml/dock/vendor/amlogic/matter$ ls 
amlogic_build_out  build_overrides                config           data_model  gn_build.sh   kotlin-detect-config.yaml  NOTICE        ruff.toml              src
build              cipd-20240719-17-35-42.tar.gz  CONTRIBUTING.md  docs        integrations  lgtm.yml                   README.md     scripts                third_party
BUILD.gn           CODE_OF_CONDUCT.md             credentials      examples    iwyu.imp      LICENSE                    REVIEWERS.md  SPECIFICATION_VERSION  zzz_generated
```
# Build command
```c
rm -rf build* .devcontainer .environment examples
git submodule update --init
git checkout .
source setenv.sh a4_ba400_spk_a64_release;make matter-rebuild;make 
```
# Build log
```c
/aml/dock/output/a4_ba400_spk_a64_release
/aml/dock/vendor/amlogic/matter
gn gen --check --fail-on-unused-args --root=/aml/dock/vendor/amlogic/matter/scripts/examples/../../examples/chip-tool amlogic_build_out/BA400_SBR/chip-tool '--args=
target_os="linux"
target_cpu="arm"
treat_warnings_as_errors=false
import("//build_overrides/build.gni")
sysroot="/aml/dock/output/a4_ba400_spk_a64_release/host/aarch64-linux-gnu/sysroot"
custom_toolchain="${build_root}/toolchain/custom"
target_cc="/aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-gcc"
target_cxx="/aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-g++"
target_ar="/aml/dock/output/a4_ba400_spk_a64_release/host/bin/aarch64-none-linux-gnu-ar"
is_debug=true
amlogic_board_name = "BA400_SBR"'

ninja -v -C amlogic_build_out/BA400_SBR/chip-tool -j10
```
# Re-sync the submodule
```c
git submodule update --init --depth=1 --recursive \
third_party/nlassert/repo \
third_party/nlio/repo \
third_party/nlunit-test/repo \
examples/common/QRCode/repo \
third_party/pigweed/repo \
third_party/openthread/repo \
third_party/ot-br-posix/repo \
third_party/jsoncpp/repo \
third_party/editline/repo \
third_party/boringssl/repo/src \
third_party/libwebsockets/repo \
third_party/perfetto/repo
```
[Amlogic-share-code](https://drive.google.com/drive/folders/1tSQbU5EDhmBI1bgs9ftFdc0KyElgtl-P?usp=sharing) may not able to compile success.
Due to it has link to github, so we neet to issue command for re-sync the remote repo again.  
Option --recursive ensures that the command applies not just the top-level files but to every level of the directory tree. This can be helpfull for submodule.
```c
git submodule update --init --depth=1 --recursive
```
Onec compile successed, we will get a bin file name <font color="#dd00dd">chip-tool</font>.  
# Usage example
```c
$ ./chip-tool pairing ble-wifi <node_id> <ssid> <password> <pin_code> <discriminator>
```


```c
$ make matter-rebuild
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_rsynced
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_staging_installed
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_target_installed
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_images_installed
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_host_installed
rm -f /chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_built
/usr/bin/make -j1 O=/chef/dock/output/a4_ba400_spk_a64_release HOSTCC="/usr/bin/gcc" HOSTCXX="/usr/bin/g++" syncconfig
  GEN     /chef/dock/output/a4_ba400_spk_a64_release/Makefile
package/amlogic/aml-nn-dncnn/Config.in:2:warning: leading whitespace ignored
package/amlogic/wpe/wpeframework-plugins/Config.in:1000:warning: defaults for choice values not supported
package/ffmpeg/Config.in:118:warning: config symbol 'BR2_PACKAGE_FFMPEG_DEMUXERS' uses select, but is not bool or tristate
>>> matter  Syncing from source dir /chef/dock/buildroot/../vendor/amlogic/matter
rsync -au --chmod=u=rwX,go=rX --exclude .environment --exclude docs --exclude .svn --exclude .git --exclude .hg --exclude .bzr --exclude CVS /chef/dock/buildroot/../vendor/amlogic/matter/ /chef/dock/output/a4_ba400_spk_a64_release/build/matter
cd /chef/dock/buildroot/../vendor/amlogic/matter/ && git submodule update --init --depth=1 --recursive third_party/nlassert/repo third_party/nlio/repo third_party/nlunit-test/repo examples/common/QRCode/repo third_party/pigweed/repo third_party/openthread/repo third_party/ot-br-posix/repo third_party/jsoncpp/repo third_party/editline/repo third_party/boringssl/repo/src third_party/libwebsockets/repo third_party/perfetto/repo
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
package/pkg-generic.mk:208: recipe for target '/chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_rsynced' failed
make[1]: *** [/chef/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_rsynced] Error 128
/chef/dock/output/a4_ba400_spk_a64_release/Makefile:23: recipe for target '_all' failed
make: *** [_all] Error 2

```
```c
Command: python3 /chef/dock/vendor/amlogic/matter/build/config/linux/pkg-config.py glib-2.0 gio-unix-2.0
Returned 1.
stderr:

Could not run pkg-config.

```
sudo apt-get install pkg-config

sudo apt-get install libglib2.0-dev 

Command: python3 /chef/dock/vendor/amlogic/matter/build/config/linux/pkg-config.py glib-2.0 gio-unix-2.0
Returned 1.
stderr:

Package glib-2.0 was not found in the pkg-config search path.


[Amlogic.md](Amlogic.md)  
[Amlogic-matter.md](Amlogic-matter.md)   

# Ubuntu update error
```c
$ sudo apt-get update
[sudo] password for ls: 
Hit:1 https://dl.google.com/linux/chrome/deb stable InRelease                                                                         
Hit:2 http://cn.archive.ubuntu.com/ubuntu bionic InRelease                                                                            
Hit:3 http://cn.archive.ubuntu.com/ubuntu bionic-updates InRelease                                                                    
Hit:4 http://cn.archive.ubuntu.com/ubuntu bionic-backports InRelease                                                                  
Hit:5 http://security.ubuntu.com/ubuntu bionic-security InRelease                         
Ign:6 https://www.scootersoftware.com bcompare4 InRelease                                 
Hit:7 https://www.scootersoftware.com bcompare4 Release
Traceback (most recent call last):
  File "/usr/lib/cnf-update-db", line 8, in <module>
    from CommandNotFound.db.creator import DbCreator
ModuleNotFoundError: No module named 'CommandNotFound'
Reading package lists... Done
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code
```
Try these command for resovle.
```c
sudo apt-get remove --purge python3-apt
sudo apt autoremove
sudo apt-get install python3-apt
```
```c
//# Import the key from Ubuntu keyserver
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EC34ED227AFAE3F2
```
```c
$ sudo apt install git gcc g++ pkg-config libssl-dev libdbus-1-dev
libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev 
python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev

sudo apt list --installed | grep gcc
```
```c
Installing pip requirements for all...
ERROR: Cannot install pandas because these package versions have conflicting dependencies.
ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts

[notice] A new release of pip is available: 23.2.1 -> 24.2
[notice] To update, run: pip install --upgrade pip
/aml/dock/vendor/amlogic/matter/scripts/helpers/bash-completion.sh: line 42: syntax error near unexpected token `<'
/aml/dock/vendor/amlogic/matter/scripts/helpers/bash-completion.sh: line 42: `            readarray -t COMPREPLY < <(compgen -W "alpha beta gamma 4 5 6 7 8 9" -- "$cur")'
package/pkg-generic.mk:266: recipe for target '/aml/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_built' failed
make[1]: *** [/aml/dock/output/a4_ba400_spk_a64_release/build/matter/.stamp_built] Error 2
/aml/dock/output/a4_ba400_spk_a64_release/Makefile:23: recipe for target '_all' failed
make: *** [_all] Error 2


```
```c
gn_out/python-venv/bin/yapf:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/ptipython:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/ptipython3.11:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/black:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/rst2man.py:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/pyserial-ports:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/dmypy:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/humanfriendly:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/pyrsa-sign:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/pyjson5:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/python-venv/bin/pip3:1:#!/aml/dock/vendor/amlogic/matter/.environment/gn_out/python-venv/bin/python
gn_out/relative_path_transformations.json:2:  "/aml/dock/vendor/amlogic/matter/.environment/gn_out/=out/",
gn_out/relative_path_transformations.json:3:  "/aml/dock/vendor/amlogic/matter/.environment/gn_out=",
gn_out/relative_path_transformations.json:4:  "/aml/dock/vendor/amlogic/matter/=",
gn_out/relative_path_transformations.json:8:  "/aml/dock/vendor/amlogic/matter/=",
gn_out/relative_path_transformations.json:9:  "/aml/dock/vendor/amlogic/matter/.environment/gn_out=",
gn_out/relative_path_transformations.json:10:  "/aml/dock/vendor/amlogic/matter/.environment/gn_out/=out/"
actions.json:6:                "/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin",
actions.json:7:                "/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools"
actions.json:13:        "_PW_ENVIRONMENT_CONFIG_FILE": "/aml/dock/vendor/amlogic/matter/scripts/setup/environment.json",
actions.json:15:        "PW_PROJECT_ROOT": "/aml/dock/vendor/amlogic/matter",
actions.json:16:        "PW_ROOT": "/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo",
actions.json:17:        "_PW_ACTUAL_ENVIRONMENT_ROOT": "/aml/dock/vendor/amlogic/matter/.environment",
actions.json:18:        "VIRTUAL_ENV": "/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv",
actions.json:21:        "PW_PACKAGE_ROOT": "/aml/dock/vendor/amlogic/matter/.environment/packages"
activate.sh:1:_PW_ENVIRONMENT_CONFIG_FILE="/aml/dock/vendor/amlogic/matter/scripts/setup/environment.json"
activate.sh:7:PW_PROJECT_ROOT="/aml/dock/vendor/amlogic/matter"
activate.sh:10:PW_ROOT="/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo"
activate.sh:13:_PW_ACTUAL_ENVIRONMENT_ROOT="/aml/dock/vendor/amlogic/matter/.environment"
activate.sh:58:#   /aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin
activate.sh:89:#   /aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools
activate.sh:116:PATH="$(echo "$PATH" | sed "s|:/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin:|:|g;" | sed "s|^/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin:||g;" | sed "s|:/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin$||g;")"
activate.sh:119:PATH="$(echo "$PATH" | sed "s|:/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools:|:|g;" | sed "s|^/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools:||g;" | sed "s|:/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools$||g;")"

env_root.txt:1:/aml/dock/vendor/amlogic/matter/.environment
deactivate.sh:6:PATH="$(echo "$PATH" | sed "s|:/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin:|:|g;" | sed "s|^/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin:||g;" | sed "s|:/aml/dock/vendor/amlogic/matter/.environment/pigweed-venv/bin$||g;")"
deactivate.sh:9:PATH="$(echo "$PATH" | sed "s|:/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools:|:|g;" | sed "s|^/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools:||g;" | sed "s|:/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo/out/host/host_tools$||g;")"
pigweed-venv/gn-gen-python_packages_install-20241008-143601.log:2:['gn', 'gen', '/aml/dock/vendor/amlogic/matter/.environment/gn_out', '--args=chip_crypto="boringssl" dir_pigweed="/aml/dock/vendor/amlogic/matter/third_party/pigweed/repo"']

pigweed-venv/lib/python3.8/site-packages/chip_rpc-0.0.1+20241008143718.dist-info/direct_url.json:1:{"dir_info": {}, "url": "file:///aml/dock/vendor/amlogic/matter/.environment/gn_out/python/obj/examples/common/pigweed/rpc_console/chip_rpc_distribution"}
pigweed-venv/lib/python3.8/site-packages/chip_mobly-0.0.1.dist-info/direct_url.json:1:{"dir_info": {"editable": true}, "url": "file:///aml/dock/vendor/amlogic/matter/integrations/mobly"}
pigweed-venv/lib/python3.8/site-packages/__editable___chip_mobly_0_0_1_finder.py:8:MAPPING = {'chip_mobly': '/aml/dock/vendor/amlogic/matter/integrations/mobly/chip_mobly'}
pigweed-venv/lib/python3.8/site-packages/pigweed-0.0.15+20241008143718.dist-info/direct_url.json:1:{"dir_info": {}, "url": "file:///aml/dock/vendor/amlogic/matter/.environment/gn_out/python/obj/third_party/pigweed/repo/pw_env_setup/generate_pigweed_python_package"}
pigweed-venv/lib/python3.8/site-packages/chef-0.0.1.dist-info/direct_url.json:1:{"dir_info": {"editable": true}, "url": "file:///aml/dock/vendor/amlogic/matter/examples/chef"}
pigweed-venv/lib/python3.8/site-packages/__editable___chef_0_0_1_finder.py:8:MAPPING = {'sample_app_util': '/aml/dock/vendor/amlogic/matter/examples/chef/sample_app_util'}
```