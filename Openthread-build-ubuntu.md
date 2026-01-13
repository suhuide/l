```c
eric@ubuntu:/rk356x$ cd openthread/
eric@ubuntu:/rk356x/openthread$ git clone https://github.com/openthread/ot-br-posix.git --depth 1
Cloning into 'ot-br-posix'...
remote: Enumerating objects: 448, done.
remote: Counting objects: 100% (448/448), done.
remote: Compressing objects: 100% (396/396), done.
remote: Total 448 (delta 148), reused 161 (delta 35), pack-reused 0 (from 0)
Receiving objects: 100% (448/448), 1.05 MiB | 642.00 KiB/s, done.
Resolving deltas: 100% (148/148), done.
eric@ubuntu:/rk356x/openthread$ ls
ot-br-posix
eric@ubuntu:/rk356x/openthread$ cd ot-br-posix/
eric@ubuntu:/rk356x/openthread/ot-br-posix$ ./script/bootstrap
+++ dirname ./script/bootstrap
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
++ STAGE_DIR=/rk356x/openthread/ot-br-posix/stage
++ BUILD_DIR=/rk356x/openthread/ot-br-posix/build
++ [[ -d /rk356x/openthread/ot-br-posix/stage ]]
++ mkdir -v -p /rk356x/openthread/ot-br-posix/stage
mkdir: created directory '/rk356x/openthread/ot-br-posix/stage'
++ [[ -d /rk356x/openthread/ot-br-posix/build ]]
++ mkdir -v -p /rk356x/openthread/ot-br-posix/build
mkdir: created directory '/rk356x/openthread/ot-br-posix/build'
++ export PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
++ PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
+++ basename ./script/bootstrap
++ TASKNAME=bootstrap
++ BEFORE_HOOK=examples/platforms/ubuntu/before_bootstrap
++ AFTER_HOOK=examples/platforms/ubuntu/after_bootstrap
++ [[ ! -f examples/platforms/ubuntu/before_bootstrap ]]
++ BEFORE_HOOK=/dev/null
++ [[ ! -f examples/platforms/ubuntu/after_bootstrap ]]
++ AFTER_HOOK=/dev/null
+ NAT64_SERVICE=openthread
+ FIREWALL=1
+ OTBR_MDNS=mDNSResponder
+ OT_BACKBONE_CI=0
+ REFERENCE_DEVICE=0
+ main
+ . /dev/null
+ git submodule update --init --recursive --depth 1
Submodule 'third_party/cJSON/repo' (https://github.com/DaveGamble/cJSON.git) registered for path 'third_party/cJSON/repo'
Submodule 'third_party/http-parser/repo' (https://github.com/nodejs/http-parser.git) registered for path 'third_party/http-parser/repo'
Submodule 'third_party/openthread/repo' (https://github.com/openthread/openthread.git) registered for path 'third_party/openthread/repo'
Cloning into '/rk356x/openthread/ot-br-posix/third_party/cJSON/repo'...
Cloning into '/rk356x/openthread/ot-br-posix/third_party/http-parser/repo'...
Cloning into '/rk356x/openthread/ot-br-posix/third_party/openthread/repo'...
remote: Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Enumerating objects: 63, done.
remote: Counting objects: 100% (63/63), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 32 (delta 26), reused 5 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (32/32), done.
From https://github.com/DaveGamble/cJSON
 * branch            cf97c6f066d81fdbba4ef722cfd327bbbba2365c -> FETCH_HEAD
Submodule path 'third_party/cJSON/repo': checked out 'cf97c6f066d81fdbba4ef722cfd327bbbba2365c'
remote: Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 1 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/nodejs/http-parser
 * branch            4f15b7d510dc7c6361a26a7c6d2f7c3a17f8d878 -> FETCH_HEAD
Submodule path 'third_party/http-parser/repo': checked out '4f15b7d510dc7c6361a26a7c6d2f7c3a17f8d878'
remote: Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Enumerating objects: 63, done.
remote: Counting objects: 100% (63/63), done.
remote: Compressing objects: 100% (32/32), done.
remote: Total 32 (delta 29), reused 2 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (32/32), done.
From https://github.com/openthread/openthread
 * branch            e19c775ce3740331069c78899908db0a3a3d29da -> FETCH_HEAD
Submodule path 'third_party/openthread/repo': checked out 'e19c775ce3740331069c78899908db0a3a3d29da'
+ install_packages
+ have apt-get
+ command -v apt-get
+ install_packages_apt
+ sudo apt-get update
[sudo] password for eric: 
Hit:1 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                       
Hit:2 http://us.archive.ubuntu.com/ubuntu bionic InRelease                                                              
Hit:3 http://us.archive.ubuntu.com/ubuntu bionic-updates InRelease                        
Hit:4 http://us.archive.ubuntu.com/ubuntu bionic-backports InRelease                                     
Ign:5 https://www.scootersoftware.com bcompare4 InRelease                         
Get:6 https://www.scootersoftware.com bcompare4 Release [1,717 B]
Get:7 https://www.scootersoftware.com bcompare4 Release.gpg [836 B]
Ign:7 https://www.scootersoftware.com bcompare4 Release.gpg
Hit:8 https://www.scootersoftware.com bcompare4/non-free i386 Packages
Hit:9 https://www.scootersoftware.com bcompare4/non-free amd64 Packages
Fetched 2,553 B in 3s (849 B/s)
Reading package lists... Done
W: GPG error: https://www.scootersoftware.com bcompare4 Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY EC34ED227AFAE3F2
W: The repository 'https://www.scootersoftware.com bcompare4 Release' is not signed.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
+ sudo apt-get install --no-install-recommends -y wget iproute2 iputils-ping libreadline-dev libncurses-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'libncurses5-dev' instead of 'libncurses-dev'
libreadline-dev is already the newest version (7.0-3).
iproute2 is already the newest version (4.15.0-2ubuntu1.3).
iputils-ping is already the newest version (3:20161105-1ubuntu3).
libncurses5-dev is already the newest version (6.1-1ubuntu1.18.04.1).
wget is already the newest version (1.19.4-1ubuntu2.2).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ sudo apt-get install --no-install-recommends -y build-essential ninja-build cmake
Reading package lists... Done
Building dependency tree       
Reading state information... Done
build-essential is already the newest version (12.4ubuntu1).
ninja-build is already the newest version (1.8.2-1).
cmake is already the newest version (3.10.2-1ubuntu2.18.04.2).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ sudo apt-get install --no-install-recommends -y rsyslog
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rsyslog is already the newest version (8.32.0-1ubuntu4.2).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ sudo apt-get install --no-install-recommends -y dbus libdbus-1-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
dbus is already the newest version (1.12.2-1ubuntu1.4).
libdbus-1-dev is already the newest version (1.12.2-1ubuntu1.4).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ sudo apt-get install --no-install-recommends -y libavahi-client3 libavahi-common-dev libavahi-client-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libavahi-client-dev is already the newest version (0.7-3.1ubuntu1.3).
libavahi-client3 is already the newest version (0.7-3.1ubuntu1.3).
libavahi-common-dev is already the newest version (0.7-3.1ubuntu1.3).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ [[ mDNSResponder == \a\v\a\h\i ]]
+ [[ 0 == 1 ]]
+ [[ 0 == 1 ]]
+ MDNS_RESPONDER_SOURCE_NAME=mDNSResponder-1790.80.10
+++ dirname ./script/bootstrap
++ realpath ./script/../third_party/mDNSResponder
+ MDNS_RESPONDER_PATCH_PATH=/rk356x/openthread/ot-br-posix/third_party/mDNSResponder
+ cd /tmp
+ wget --no-check-certificate https://github.com/apple-oss-distributions/mDNSResponder/archive/refs/tags/mDNSResponder-1790.80.10.tar.gz
--2024-09-04 18:21:00--  https://github.com/apple-oss-distributions/mDNSResponder/archive/refs/tags/mDNSResponder-1790.80.10.tar.gz
Resolving github.com (github.com)... 20.205.243.166
Connecting to github.com (github.com)|20.205.243.166|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/apple-oss-distributions/mDNSResponder/tar.gz/refs/tags/mDNSResponder-1790.80.10 [following]
--2024-09-04 18:21:01--  https://codeload.github.com/apple-oss-distributions/mDNSResponder/tar.gz/refs/tags/mDNSResponder-1790.80.10
Resolving codeload.github.com (codeload.github.com)... 20.205.243.165
Connecting to codeload.github.com (codeload.github.com)|20.205.243.165|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2989629 (2.9M) [application/x-gzip]
Saving to: ‘mDNSResponder-1790.80.10.tar.gz’

mDNSResponder-1790.80.10.tar.gz                    100%[================================================================================================================>]   2.85M  1.89MB/s    in 1.5s    

2024-09-04 18:21:03 (1.89 MB/s) - ‘mDNSResponder-1790.80.10.tar.gz’ saved [2989629/2989629]

+ mkdir -p mDNSResponder-1790.80.10
+ tar xvf mDNSResponder-1790.80.10.tar.gz -C mDNSResponder-1790.80.10 --strip-components=1
mDNSResponder-mDNSResponder-1790.80.10/Clients/
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/BonjourExample.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/BonjourExample.sln
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/BonjourExample.vcproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/stdafx.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/BonjourExample/stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ClientCommon.c
mDNSResponder-mDNSResponder-1790.80.10/Clients/ClientCommon.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/DNS-SD.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/DNS-SD64.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/dns-sd.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/dns-sd.sdk.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/dns-sd.sdk.vcproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/dns-sd.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/dns-sd.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.VisualStudio/resource.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.xcodeproj/
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNS-SD.xcodeproj/project.pbxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/App.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/AssemblyInfo.cs
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/DNSServiceBrowser.NET.csproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/DNSServiceBrowser.cs
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.NET/DNSServiceBrowser.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/DNSServiceBrowser.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/DNSServiceBrowser.VB.vbproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/DNSServiceBrowser.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/DNSServiceBrowser.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Application.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Application.myapp
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/AssemblyInfo.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Resources.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Resources.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Settings.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/DNSServiceBrowser.VB/My Project/Settings.settings
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/About.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/About.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ClassFactory.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ClassFactory.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerBar.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerBar.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerBarWindow.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerBarWindow.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.def
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPlugin.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginLocRes.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginLocRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginLocRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginRes.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ExplorerPluginRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/LoginDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/LoginDialog.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/Resource.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/StdAfx.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/StdAfx.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/ExplorerPlugin.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/ExplorerPlugin64.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/about.bmp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/button-2k.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/button-xp.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/cold.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/hot.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/res/logo.bmp
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/resource_dll.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/resource_loc_res.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ExplorerPlugin/resource_res.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/BrowserApp.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/BrowserApp.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/DNSSDUnitTest.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/JavaSamples.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/SimpleChat.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/SimpleChat.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/SwingBrowseListener.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/SwingDomainListener.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/SwingQueryListener.java
mDNSResponder-mDNSResponder-1790.80.10/Clients/Java/nmakefile
mDNSResponder-mDNSResponder-1790.80.10/Clients/Makefile
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/About.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/About.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/FirstPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/FirstPage.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/FourthPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/FourthPage.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/Logger.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/Logger.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizard.ncb
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizard.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizard.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizard.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardApp.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardApp.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardLocRes.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardLocRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardLocRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardRes.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardSheet.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/PrinterSetupWizardSheet.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/SecondPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/SecondPage.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/ThirdPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/ThirdPage.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/UtilTypes.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/Info.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/NetworkPrinter.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/Print.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizard.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizard.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizard.rc2
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizard64.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizardLocRes.rc2
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/PrinterSetupWizardRes.rc2
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/Thumbs.db
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/about.bmp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/banner_icon.bmp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/res/watermark.bmp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/resource.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/resource_exe.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/resource_loc_res.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/resource_res.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/stdafx.cpp
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/PrinterSetupWizard/tcpxcv.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/App.ico
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/AssemblyInfo.cs
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/SimpleChat.NET.csproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/SimpleChat.cs
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.NET/SimpleChat.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Application.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Application.myapp
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/AssemblyInfo.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Resources.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Resources.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Settings.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/My Project/Settings.settings
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/SimpleChat.Designer.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/SimpleChat.VB.vbproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/SimpleChat.resx
mDNSResponder-mDNSResponder-1790.80.10/Clients/SimpleChat.VB/SimpleChat.vb
mDNSResponder-mDNSResponder-1790.80.10/Clients/dns-sd.c
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/DNSServerDNSSEC.c
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/DNSServerDNSSEC.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/TestUtils.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/TestUtils.m
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/dns-rcode-func-autogen
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/dns-rr-func-autogen
mDNSResponder-mDNSResponder-1790.80.10/Clients/dnssdutil/dnssdutil.c
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/mDNSNetMonitor.manifest
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/mDNSNetMonitor.rc
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/mDNSNetMonitor.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/mDNSNetMonitor.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/Clients/mDNSNetMonitor.VisualStudio/resource.h
mDNSResponder-mDNSResponder-1790.80.10/Clients/srputil/
mDNSResponder-mDNSResponder-1790.80.10/Clients/srputil/srputil.c
mDNSResponder-mDNSResponder-1790.80.10/DSO/
mDNSResponder-mDNSResponder-1790.80.10/DSO/dso-transport.c
mDNSResponder-mDNSResponder-1790.80.10/DSO/dso-transport.h
mDNSResponder-mDNSResponder-1790.80.10/DSO/dso.c
mDNSResponder-mDNSResponder-1790.80.10/DSO/dso.h
mDNSResponder-mDNSResponder-1790.80.10/Documents/
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/52D711AF-4055-4867-A494-7E31552BB9E1.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/Screen Shot 2015-09-16 at 3.36.23 PM.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/Screen Shot 2015-09-16 at 3.46.14 PM.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/TXT.rtf
mDNSResponder-mDNSResponder-1790.80.10/Documents/Attach mDNSResponder to Xcode.rtfd/unknown.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Automatic Discovery of DNS Push Zones.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/ServiceRegistrationConventions.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/Start mDNSResponder in Xcode.rtfd/
mDNSResponder-mDNSResponder-1790.80.10/Documents/Start mDNSResponder in Xcode.rtfd/A944EB40-AEFD-4CA1-BF10-E8F52835CA8C.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Start mDNSResponder in Xcode.rtfd/Screen Shot 2015-09-16 at 4.22.37 PM.png
mDNSResponder-mDNSResponder-1790.80.10/Documents/Start mDNSResponder in Xcode.rtfd/TXT.rtf
mDNSResponder-mDNSResponder-1790.80.10/Documents/advertising-proxy.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/discovery-proxy.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/dns-sd.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/dnssd-client-library.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/mDNSResponder.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/openthread-border-router.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/relative-time-in-mDNSResponder.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/srp-client.md
mDNSResponder-mDNSResponder-1790.80.10/Documents/srp-update-proxy.md
mDNSResponder-mDNSResponder-1790.80.10/LICENSE
mDNSResponder-mDNSResponder-1790.80.10/PrivateDNS.txt
mDNSResponder-mDNSResponder-1790.80.10/README.md
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/.gitignore
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/Makefile
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/README.md
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/adv-ctl-common.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/adv-ctl-server.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/adv-ctl-server.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/advertising_proxy_services.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/advertising_proxy_services.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/config-parse.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/config-parse.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-common.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-openthread.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-openthread.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-proto.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-proto.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-server.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-server.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-services.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/cti-services.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dns-msg.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dnssd-proxy.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dnssd-proxy.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dnssd-relay.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dso-utils.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/dso-utils.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/fromwire.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/hmac-macos.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/hmac-mbedtls.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/hmac-openssl.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/interface-monitor-macos.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/interface-monitor-macos.m
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/ioloop-common.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/ioloop-common.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/ioloop.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/ioloop.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/keydump.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/log/
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/log/log_srp.m
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/macos-ioloop.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/nat64-macos.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/nat64-macos.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/posix.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/ra-tester.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/route.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/route.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/sign-macos.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/sign-mbedtls.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-api.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-client.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-crypto.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-dns-proxy.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-features.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-filedata.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-gw.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-ioloop.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-log.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-log.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-mdns-proxy.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-mdns-proxy.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-parse.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-proxy.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-replication.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-replication.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-thread.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-thread.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp-tls.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/srp.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/tls-macos.h
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/tls-mbedtls.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/towire.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/verify-macos.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/verify-mbedtls.c
mDNSResponder-mDNSResponder-1790.80.10/ServiceRegistration/wireutils.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/DNSCommon.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/DNSCommon.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/DNSDigest.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/Implementer Notes.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/mDNS.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/mDNSDebug.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/mDNSEmbeddedAPI.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/mdns_strict.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/uDNS.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSCore/uDNS.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/ApplePlatformFeatures.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/Base.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/Base.lproj/SafariExtensionViewController.xib
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/BonjourSafariExtension.entitlements
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/CNServiceBrowserView.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/CNServiceBrowserView.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/Localizable.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/SafariExtensionHandler.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/SafariExtensionHandler.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/SafariExtensionViewController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/SafariExtensionViewController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/ToolbarItemIcon.png
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Extension/script.js
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/AppDelegate.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/AppDelegate.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Assets.xcassets/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Assets.xcassets/AppIcon.appiconset/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Assets.xcassets/AppIcon.appiconset/Contents.json
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Base.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Base.lproj/Main.storyboard
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/BonjourSafariMenu.entitlements
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/ViewController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/ViewController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Bonjour Safari Menu/main.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourEvents-Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourEvents.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/BonjourTop.xcodeproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/BonjourTop.xcodeproj/project.pbxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/BonjourTop.xcodeproj/project.xcworkspace/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/BonjourTop.xcodeproj/project.xcworkspace/contents.xcworkspacedata
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/BonjourTop.1
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/BonjourTop.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/BonjourTop.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/CaptureFile.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/CaptureFile.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/CollectBy.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/CollectBy.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/DNSFrame.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/DNSFrame.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/Frame.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/Frame.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/LLRBTree.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/LLRBTree.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjIPAddr.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjIPAddr.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjMACAddr.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjMACAddr.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjStringtoStringMap.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjStringtoStringMap.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjsocket.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjsocket.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjstring.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjstring.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/bjtypes.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/BonjourTop/source/main.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/D2D.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/D2D.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DNS64.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DNS64.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DNS64State.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DNSProxySupport.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/Shared/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/Shared/CNDomainBrowserPathUtils.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/Shared/CNDomainBrowserPathUtils.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/Shared/_CNDomainBrowser.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/Shared/_CNDomainBrowser.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/CNDomainBrowserViewController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/CNDomainBrowserViewController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/DomainBrowser.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/DomainBrowser.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/iOS/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/macOS/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/macOS/CNDomainBrowserView.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/macOS/CNDomainBrowserView.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/macOS/DomainBrowser.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/DomainBrowser/macOS/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/LegacyNATTraversal.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Artwork/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Artwork/failure.tiff
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Artwork/inprogress.tiff
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Artwork/success.tiff
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Base.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Base.lproj/DNSServiceDiscoveryPref.xib
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPref.icns
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPref.tiff
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/BonjourPrefTool-Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/BonjourPrefTool.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/BonjourPrefTool.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/BonjourPrefToolProtocol.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/entitlements.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/BonjourPrefTool/main.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/DNSServiceDiscoveryPref.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/DNSServiceDiscoveryPref.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/Info-PreferencePane.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/BonjourPrefRemoteViewService-Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/BonjourPrefRemoteViewService.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/BonjourPrefRemoteViewService.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/InfoPlist.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/entitlements.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/RemoteViewService/main.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/en.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/PreferencePane/en.lproj/InfoPlist.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/QuerierSupport.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/QuerierSupport.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/README.privsep
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Scripts/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Scripts/bonjour-mcast-diagnose
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Scripts/bonjour-start-mdns-tcpdump
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Scripts/com.apple.mDNSResponder.mdns-tcpdump.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/Contents.json
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/UIPreferencesBlueCheck.imageset/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/UIPreferencesBlueCheck.imageset/Contents.json
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/UIPreferencesBlueCheck.imageset/UIPreferencesBlueCheck.png
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Assets.xcassets/UIPreferencesBlueCheck.imageset/UIPreferencesBlueCheck@2x.png
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/BonjourConstants.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/BonjourSCStore.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/BonjourSCStore.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/BonjourSettingsController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/BonjourSettingsController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/CNBrowseDomainsController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/CNBrowseDomainsController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/HostnameController.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/HostnameController.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SettingsBundle/Localizable.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SymptomReporter.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/SymptomReporter.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/BATS Scripts/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/BATS Scripts/bats_test_proxy.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/BATS Scripts/bats_test_state_dump.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/DNSMessageToString.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/DNSMessageToString.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/DNSMessageToString.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/README.md
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/build-all.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_message_received.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_message_received.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_message_received.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_wire_parse.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_wire_parse.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/dns_wire_parse.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/fuzzer.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/icmp_callback.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/icmp_callback.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/icmp_callback.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/mDNS_snprintf.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/mDNS_snprintf.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/mDNS_snprintf.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/setrdata.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/setrdata.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/setrdata.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Fuzzing/upload.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/CNameRecordTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/CacheOrderTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/DNSDigestTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/DNSHeuristicsTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/DNSMessageTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/HelperFunctionTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/Info.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/LocalOnlyTimeoutTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/LocalOnlyWithInterfacesTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/PathEvaluationTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/ResourceRecordTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/Unit Tests/mDNSCoreReceiveTest.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/Tests/mDNSResponder.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/build_scripts/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/build_scripts/project_version_string_to_integer
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/build_scripts/update_dns_sd_h_version
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/clientstub/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/clientstub/dnssd_clientstub_apple.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/clientstub/dnssd_clientstub_apple.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/com.apple.dnsextd.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/com.apple.mDNSResponder.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/com.apple.mDNSResponderHelper.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/com.apple.srp-mdns-proxy.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/command_line_client_entitlements/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/command_line_client_entitlements/dns-sd-entitlements.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/daemon.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnsproxy.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnsproxy.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_analytics.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_analytics.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_descriptions.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_object.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_object.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_server.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_server.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_svcb.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_svcb.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_xpc.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/dnssd_xpc.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helper-main.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helper-server.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helper-stubs.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helper.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helper.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/helpermsg-types.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/mrc/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/mrc/dns_proxy.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/mrc/object.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/mrc/object_members.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/mrc/private.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc_object.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc_objects.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc_objects.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc_xpc.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrc_xpc.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_cf_support.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_cf_support.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_dns_proxy.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_dns_proxy.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_object.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_object.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_object_members.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_objects.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_objects.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_server.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_server.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/libmrc/src/mrcs_server_internal.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/log/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/log/liblog_mdnsresponder.m
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/log/pseudo-OSLogCopyFormattedString.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSMacOSX.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSMacOSX.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSNetMonitor/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSNetMonitor/mDNSNetMonitor.8
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/Resources/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/Resources/English.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/Resources/English.lproj/Localizable.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/Resources/French.lproj/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-bundle/Resources/French.lproj/Localizable.strings
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder-xcodeproj-explanation.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponder.order
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponderHelper.8
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/mDNSResponderHelper.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/ra-tester-entitlements.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/secure_coding/
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/secure_coding/lintrc
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/secure_coding/secure-coding.xcconfig
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/secure_coding/strict.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/srp-mdns-proxy.plist
mDNSResponder-mDNSResponder-1790.80.10/mDNSMacOSX/uDNSPathEvaluation.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/Client.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/ExampleClientApp.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/ExampleClientApp.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/Identify.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/Makefile
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/NetMonitor.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/PosixDaemon.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/ProxyResponder.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/Responder.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/Services.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/libnss_mdns.8
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mDNSPosix.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mDNSPosix.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mDNSUNP.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mDNSUNP.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mbedtls.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/mdnsd.sh
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/nss_ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/nss_mdns.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/nss_mdns.conf
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/nss_mdns.conf.5
mDNSResponder-mDNSResponder-1790.80.10/mDNSPosix/parselog.py
mDNSResponder-mDNSResponder-1790.80.10/mDNSResponder.proj
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/ClientRequests.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/ClientRequests.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/CommonServices.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/DebugServices.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/DebugServices.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/GenLinkedList.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/GenLinkedList.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/BaseListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/BrowseListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSRecord.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSSD.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSSDException.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSSDRecordRegistrar.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSSDRegistration.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DNSSDService.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/DomainListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/JNISupport.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/QueryListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/RegisterListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/RegisterRecordListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/ResolveListener.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/Java/TXTRecord.java
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/PlatformCommon.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/PlatformCommon.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/discover_resolver.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/discover_resolver.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dns-sd.1
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dns_sd.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dns_sd_internal.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dns_sd_private.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd.8
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd.conf
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd_lexer.l
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnsextd_parser.y
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_clientlib.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_clientshim.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_clientstub.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_clientstub.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_errstring.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_ipc.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/dnssd_ipc.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/mDNSDebug.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/mDNSFeatures.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/mDNSResponder.8
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/tls-keychain.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/uds_daemon.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/uds_daemon.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/bsd_queue.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/mdns_addr_tailq.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/mdns_addr_tailq.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/misc_utilities.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/misc_utilities.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSShared/utilities/nullability.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/BonjourQuickLooks.sln
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/BonjourQuickLooksInstaller/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/BonjourQuickLooksInstaller/BonjourQuickLooksInstaller.wixproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/BonjourQuickLooksInstaller/Product.wxs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/BrowsingPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/BrowsingPage.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ConfigDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ConfigDialog.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ConfigPropertySheet.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ConfigPropertySheet.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.def
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanel.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelDll.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelExe.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelExe.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelExe.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelLocRes.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelLocRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelLocRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelRes.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelRes.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ControlPanelRes.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/FourthPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/FourthPage.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/RegistrationPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/RegistrationPage.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/SecondPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/SecondPage.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ServicesPage.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/ServicesPage.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/SharedSecret.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/SharedSecret.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/ControlPanel.dll.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/ControlPanel.exe.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/ControlPanel.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/ControlPanel.rc2
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/ControlPanel64.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/EnergySaver.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/controlpanel.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/failure.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/res/success.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/stdafx.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/ControlPanel/stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/AssemblyInfo.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/PString.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/Stdafx.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/Stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/dnssd_NET.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/dnssd_NET.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/dnssd_NET.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/dnssd_NET.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/dnssd_NET.vcproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL.NET/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/dll.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/dllmain.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/dnssd.def
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/dnssd.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/dnssd.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLL/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLStub/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLStub/DLLStub.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLStub/DLLStub.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLStub/DLLStub.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLStub/DLLStub.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.def
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.idl
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.rgs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DLLX.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSD.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDEventManager.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDEventManager.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDEventManager.rgs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDRecord.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDRecord.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDRecord.rgs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDService.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDService.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/DNSSDService.rgs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/StringServices.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/StringServices.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/TXTRecord.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/TXTRecord.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/TXTRecord.rgs
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/_IDNSSDEvents_CP.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/dlldatax.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/dlldatax.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DLLX/stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/ApplicationVS2002.sln
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/ApplicationVS2002.vcproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/ApplicationVS2003.sln
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/ApplicationVS2003.vcproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Resources/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Resources/Application.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Resources/Application.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Resources/Application.rc2
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Resources/Resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/AboutDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/AboutDialog.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/Application.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/Application.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/ChooserDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/ChooserDialog.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/LoginDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/LoginDialog.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/StdAfx.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/Windows/Sources/StdAfx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Application.vcc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Application.vcp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Application.vcw
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/Application.ico
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/Application.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/Application.rc2
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/newres.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Resources/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/Application.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/Application.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/BrowserDialog.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/BrowserDialog.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/StdAfx.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/DNSServiceBrowser/WindowsCE/Sources/StdAfx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Java/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Java/Java.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Java/jdns_sd.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Java/makefile
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Java/makefile64
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/NSPTool.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/NSPTool.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/NSPTool.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/NSPTool.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/Prefix.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/NSPTool/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Poll.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Poll.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/PosixCompat.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/PosixCompat.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/README.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/RegNames.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Secret.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/Secret.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/EventLog.mc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Firewall.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Firewall.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Prefix.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Service.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Service.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Service.mcp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/Service.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/dllmain.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/exports.def
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/mDNSResponder.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/mDNSResponder.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/mDNSResponderDLL.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/mDNSResponderDLL.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/mDNSResponderLib.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/main.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/res/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/res/mDNSResponder.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/res/mDNSResponder64.manifest
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/resource.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/resrc1.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/stdafx.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/stdafx.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/SystemService/targetver.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/VPCDetect.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/VPCDetect.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/VisualStudioSupport.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/VisualStudioSupport.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/WinServices.cpp
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/WinServices.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/WinVersRes.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/XBS.targets
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/isocode.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/loclibrary.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/loclibrary.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mDNSResponder.sln
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mDNSWin32.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mDNSWin32.h
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/ReadMe.txt
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/mdnsNSP.c
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/mdnsNSP.def
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/mdnsNSP.rc
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/mdnsNSP.vcxproj
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/mdnsNSP.vcxproj.filters
mDNSResponder-mDNSResponder-1790.80.10/mDNSWindows/mdnsNSP/resource.h
mDNSResponder-mDNSResponder-1790.80.10/unittests/
mDNSResponder-mDNSResponder-1790.80.10/unittests/daemon_ut.c
mDNSResponder-mDNSResponder-1790.80.10/unittests/mdns_macosx_ut.c
mDNSResponder-mDNSResponder-1790.80.10/unittests/mdns_ut.c
mDNSResponder-mDNSResponder-1790.80.10/unittests/uds_daemon_ut.c
mDNSResponder-mDNSResponder-1790.80.10/unittests/unittest.h
mDNSResponder-mDNSResponder-1790.80.10/unittests/unittest_common.c
mDNSResponder-mDNSResponder-1790.80.10/unittests/unittest_common.h
+ cd /tmp/mDNSResponder-1790.80.10
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSShared/uds_daemon.c
Hunk #1 succeeded at 2913 (offset 1 line).
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
patching file mDNSPosix/mDNSPosix.h
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ for patch in "$MDNS_RESPONDER_PATCH_PATH"/*.patch
+ patch -p1
patching file mDNSPosix/mDNSPosix.c
+ cd mDNSPosix
+ make os=linux tls=no
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/PosixDaemon.c.o PosixDaemon.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/mDNSPosix.c.o mDNSPosix.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/mDNSUNP.c.o mDNSUNP.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/mDNS.c.o ../mDNSCore/mDNS.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/DNSDigest.c.o ../mDNSCore/DNSDigest.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/uDNS.c.o ../mDNSCore/uDNS.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/DNSCommon.c.o ../mDNSCore/DNSCommon.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/uds_daemon.c.o ../mDNSShared/uds_daemon.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/mDNSDebug.c.o ../mDNSShared/mDNSDebug.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/dnssd_ipc.c.o ../mDNSShared/dnssd_ipc.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/GenLinkedList.c.o ../mDNSShared/GenLinkedList.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/PlatformCommon.c.o ../mDNSShared/PlatformCommon.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/ClientRequests.c.o ../mDNSShared/ClientRequests.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/dso.c.o ../DSO/dso.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/dso-transport.c.o ../DSO/dso-transport.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/dnssd_clientshim.c.o ../mDNSShared/dnssd_clientshim.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/mdns_addr_tailq.c.o ../mDNSShared/utilities/mdns_addr_tailq.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/misc_utilities.c.o ../mDNSShared/utilities/misc_utilities.c
cc -o build/prod/mdnsd objects/prod/PosixDaemon.c.o objects/prod/mDNSPosix.c.o objects/prod/mDNSUNP.c.o objects/prod/mDNS.c.o objects/prod/DNSDigest.c.o objects/prod/uDNS.c.o objects/prod/DNSCommon.c.o objects/prod/uds_daemon.c.o objects/prod/mDNSDebug.c.o objects/prod/dnssd_ipc.c.o objects/prod/GenLinkedList.c.o objects/prod/PlatformCommon.c.o objects/prod/ClientRequests.c.o objects/prod/dso.c.o objects/prod/dso-transport.c.o objects/prod/dnssd_clientshim.c.o objects/prod/mdns_addr_tailq.c.o objects/prod/misc_utilities.c.o 
strip -S build/prod/mdnsd
Responder daemon done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -fPIC -o objects/prod/dnssd_clientlib.c.so.o ../mDNSShared/dnssd_clientlib.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -fPIC -o objects/prod/dnssd_clientstub.c.so.o ../mDNSShared/dnssd_clientstub.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -fPIC -o objects/prod/dnssd_ipc.c.so.o ../mDNSShared/dnssd_ipc.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -fPIC -o objects/prod/dnssd_errstring.c.so.o ../mDNSShared/dnssd_errstring.c
cc -shared  -o build/prod/libdns_sd.so objects/prod/dnssd_clientlib.c.so.o objects/prod/dnssd_clientstub.c.so.o objects/prod/dnssd_ipc.c.so.o objects/prod/dnssd_errstring.c.so.o
strip -S build/prod/libdns_sd.so
Client library done
make -C ../Clients DEBUG= SUPMAKE_CFLAGS=" -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0"
make[1]: Entering directory '/tmp/mDNSResponder-1790.80.10/Clients'
mkdir build
cc -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE="/var/run/mdnsd.pid" -DMDNS_UDS_SERVERPATH="/var/run/mdnsd" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 dns-sd.c ClientCommon.c -L../mDNSPosix/build/prod/ -ldns_sd -I../mDNSShared -Wall -o build/dns-sd
make[1]: Leaving directory '/tmp/mDNSResponder-1790.80.10/Clients'
Clients done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/ExampleClientApp.c.o ExampleClientApp.c
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/Client.c.o Client.c
cc objects/prod/mDNSPosix.c.o objects/prod/mDNSUNP.c.o objects/prod/mDNSDebug.c.o objects/prod/GenLinkedList.c.o objects/prod/DNSDigest.c.o objects/prod/uDNS.c.o objects/prod/DNSCommon.c.o objects/prod/PlatformCommon.c.o objects/prod/dso.c.o objects/prod/dso-transport.c.o objects/prod/dnssd_clientshim.c.o objects/prod/mdns_addr_tailq.c.o objects/prod/misc_utilities.c.o objects/prod/mDNS.c.o objects/prod/ExampleClientApp.c.o objects/prod/Client.c.o -o build/prod/mDNSClientPosix 
Embedded Standalone Client done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/Responder.c.o Responder.c
cc objects/prod/mDNSPosix.c.o objects/prod/mDNSUNP.c.o objects/prod/mDNSDebug.c.o objects/prod/GenLinkedList.c.o objects/prod/DNSDigest.c.o objects/prod/uDNS.c.o objects/prod/DNSCommon.c.o objects/prod/PlatformCommon.c.o objects/prod/dso.c.o objects/prod/dso-transport.c.o objects/prod/dnssd_clientshim.c.o objects/prod/mdns_addr_tailq.c.o objects/prod/misc_utilities.c.o objects/prod/mDNS.c.o objects/prod/Responder.c.o -o build/prod/mDNSResponderPosix 
Embedded Standalone Responder done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/ProxyResponder.c.o ProxyResponder.c
cc objects/prod/mDNSPosix.c.o objects/prod/mDNSUNP.c.o objects/prod/mDNSDebug.c.o objects/prod/GenLinkedList.c.o objects/prod/DNSDigest.c.o objects/prod/uDNS.c.o objects/prod/DNSCommon.c.o objects/prod/PlatformCommon.c.o objects/prod/dso.c.o objects/prod/dso-transport.c.o objects/prod/dnssd_clientshim.c.o objects/prod/mdns_addr_tailq.c.o objects/prod/misc_utilities.c.o objects/prod/mDNS.c.o objects/prod/ProxyResponder.c.o -o build/prod/mDNSProxyResponderPosix 
Embedded Standalone ProxyResponder done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -o objects/prod/NetMonitor.c.o NetMonitor.c
cc objects/prod/mDNSPosix.c.o objects/prod/mDNSUNP.c.o objects/prod/mDNSDebug.c.o objects/prod/GenLinkedList.c.o objects/prod/DNSDigest.c.o objects/prod/uDNS.c.o objects/prod/DNSCommon.c.o objects/prod/PlatformCommon.c.o objects/prod/dso.c.o objects/prod/dso-transport.c.o objects/prod/dnssd_clientshim.c.o objects/prod/mdns_addr_tailq.c.o objects/prod/misc_utilities.c.o objects/prod/NetMonitor.c.o -o build/prod/mDNSNetMonitor 
NetMonitor done
cc  -I../mDNSCore -I../mDNSShared -I../mDNSShared/utilities -I../DSO -I../ServiceRegistration -Iobjects/prod -fwrapv -W -Wall -DPOSIX_BUILD -DPID_FILE=\"/var/run/mdnsd.pid\" -DMDNS_UDS_SERVERPATH=\"/var/run/mdnsd\" -D_GNU_SOURCE -DHAVE_IPV6 -DNOT_HAVE_SA_LEN -DUSES_NETLINK -DHAVE_LINUX -DTARGET_OS_LINUX -ftabstop=4 -Wno-expansion-to-defined -g -DMDNS_DEBUGMSGS=0 -c -fPIC -o objects/prod/nss_mdns.c.so.o nss_mdns.c
cc -shared  -o build/prod/libnss_mdns-0.2.so objects/prod/dnssd_clientlib.c.so.o objects/prod/dnssd_clientstub.c.so.o objects/prod/dnssd_ipc.c.so.o objects/prod/dnssd_errstring.c.so.o objects/prod/nss_mdns.c.so.o
strip -S build/prod/libnss_mdns-0.2.so
Name Service Switch module done
+ sudo make install os=linux tls=no
cp mdnsd.sh /etc/init.d/mdns
chmod ugo+x /etc/init.d/mdns
ln -s -f /etc/init.d/mdns /etc/rc2.d/S52mdns
ln -s -f /etc/init.d/mdns /etc/rc3.d/S52mdns
ln -s -f /etc/init.d/mdns /etc/rc4.d/S52mdns
ln -s -f /etc/init.d/mdns /etc/rc5.d/S52mdns
ln -s -f /etc/init.d/mdns /etc/rc0.d/K16mdns
ln -s -f /etc/init.d/mdns /etc/rc6.d/K16mdns
/etc/init.d/mdns  installed
if test -x /usr/sbin/mdnsd; then /etc/init.d/mdns stop; fi
[....] Stopping mdns (via systemctl): mdns.serviceWarning: The unit file, source configuration file or drop-ins of mdns.service changed on disk. Run 'systemctl daemon-reload' to reload units.
. ok 
cp build/prod/mdnsd /usr/sbin/mdnsd
/etc/init.d/mdns start
[....] Starting mdns (via systemctl): mdns.serviceWarning: The unit file, source configuration file or drop-ins of mdns.service changed on disk. Run 'systemctl daemon-reload' to reload units.
. ok 
/usr/sbin/mdnsd  installed
cp build/prod/libdns_sd.so /usr/lib/libdns_sd.so.1
ln -s -f /usr/lib/libdns_sd.so.1 /usr/lib/libdns_sd.so
/usr/lib/libdns_sd.so.1 /usr/include/dns_sd.h  installed
/usr/share/man/man8/mdnsd.8  installed
cp ../Clients/build/dns-sd /usr/bin/dns-sd
/usr/bin/dns-sd  installed
cp build/prod/libnss_mdns-0.2.so /lib/libnss_mdns-0.2.so
chmod 444 /lib/libnss_mdns-0.2.so
ln -s -f /lib/libnss_mdns-0.2.so /lib/libnss_mdns.so.2
ldconfig
/lib/libnss_mdns.so.2 /etc/nss_mdns.conf /usr/share/man/man5/nss_mdns.conf.5 /usr/share/man/man8/libnss_mdns.8  installed
+ sudo apt-get install --no-install-recommends -y libboost-dev libboost-filesystem-dev libboost-system-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libboost-dev is already the newest version (1.65.1.0ubuntu1).
libboost-filesystem-dev is already the newest version (1.65.1.0ubuntu1).
libboost-system-dev is already the newest version (1.65.1.0ubuntu1).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ without NAT64
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ '[' openthread '!=' tayga ']'
+ sudo apt-get install --no-install-recommends -y iptables
Reading package lists... Done
Building dependency tree       
Reading state information... Done
iptables is already the newest version (1.6.1-2ubuntu2.1).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ without DNS64
+ with DNS64
+ local value
++ printenv DNS64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DNS64-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ without NETWORK_MANAGER
+ with NETWORK_MANAGER
+ local value
++ printenv NETWORK_MANAGER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NETWORK_MANAGER-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ without DHCPV6_PD
+ with DHCPV6_PD
+ local value
++ printenv DHCPV6_PD
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DHCPV6_PD-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ sudo apt-get install --no-install-recommends -y libjsoncpp-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libjsoncpp-dev is already the newest version (1.7.4-3).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ without REFERENCE_DEVICE
+ with REFERENCE_DEVICE
+ local value
++ printenv REFERENCE_DEVICE
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${REFERENCE_DEVICE-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ without BACKBONE_ROUTER
+ with BACKBONE_ROUTER
+ local value
++ printenv BACKBONE_ROUTER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BACKBONE_ROUTER-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo apt-get install --no-install-recommends -y libnetfilter-queue1 libnetfilter-queue-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libnetfilter-queue-dev is already the newest version (1.0.2-2).
libnetfilter-queue1 is already the newest version (1.0.2-2).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ without WEB_GUI
+ with WEB_GUI
+ local value
++ printenv WEB_GUI
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${WEB_GUI-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ command -v npm
/usr/bin/npm
+ sudo apt-get install -y iptables ipset
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ipset is already the newest version (6.34-1).
iptables is already the newest version (1.6.1-2ubuntu2.1).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ sudo apt-get install -y libprotobuf-dev protobuf-compiler
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libprotobuf-dev is already the newest version (3.0.0-9.1ubuntu1.1).
protobuf-compiler is already the newest version (3.0.0-9.1ubuntu1.1).
The following packages were automatically installed and are no longer required:
  fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-iostreams1.65.1 libboost-locale1.65.1 libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common
  liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libxapian30 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 39 not upgraded.
+ . /dev/null
eric@ubuntu:/rk356x/openthread/ot-br-posix$ INFRA_IF_NAME=enp2s0 ./script/setup
+++ dirname ./script/setup
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
++ STAGE_DIR=/rk356x/openthread/ot-br-posix/stage
++ BUILD_DIR=/rk356x/openthread/ot-br-posix/build
++ [[ -d /rk356x/openthread/ot-br-posix/stage ]]
++ [[ -d /rk356x/openthread/ot-br-posix/build ]]
++ export PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
++ PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
+++ basename ./script/setup
++ TASKNAME=setup
++ BEFORE_HOOK=examples/platforms/ubuntu/before_setup
++ AFTER_HOOK=examples/platforms/ubuntu/after_setup
++ [[ ! -f examples/platforms/ubuntu/before_setup ]]
++ BEFORE_HOOK=/dev/null
++ [[ ! -f examples/platforms/ubuntu/after_setup ]]
++ AFTER_HOOK=/dev/null
+ . script/_border_routing
++ INFRA_IF_NAME=enp2s0
++ readonly INFRA_IF_NAME
++ SYSCTL_ACCEPT_RA_FILE=/etc/sysctl.d/60-otbr-accept-ra.conf
++ readonly SYSCTL_ACCEPT_RA_FILE
++ DHCPCD_CONF_FILE=/etc/dhcpcd.conf
++ readonly DHCPCD_CONF_FILE
++ DHCPCD_CONF_BACKUP_FILE=/etc/dhcpcd.conf.orig
++ readonly DHCPCD_CONF_BACKUP_FILE
+ . script/_otbr
++ OTBR_TOP_BUILDDIR=/rk356x/openthread/ot-br-posix/build/otbr
++ readonly OTBR_TOP_BUILDDIR
++ OTBR_OPTIONS=
++ readonly OTBR_OPTIONS
++ REFERENCE_DEVICE=0
++ readonly REFERENCE_DEVICE
+ . script/_ipforward
++ SYSCTL_IP_FORWARD=/etc/sysctl.d/60-otbr-ip-forward.conf
+ . script/_nat64
++ NAT64_SERVICE=openthread
++ TAYGA_DEFAULT=/etc/default/tayga
++ TAYGA_CONF=/etc/tayga.conf
++ TAYGA_IPV4_ADDR=192.168.255.1
++ TAYGA_IPV6_ADDR=fdaa:bb:1::1
++ TAYGA_TUN_V6_ADDR=fdaa:bb:1::2
++ NAT64_PREFIX=64:ff9b::/96
++ DYNAMIC_POOL=192.168.255.0/24
++ NAT44_SERVICE=/etc/init.d/otbr-nat44
++ WLAN_IFNAMES=enp2s0
++ THREAD_IF=wpan0
+ . script/_dns64
++ BIND_CONF_OPTIONS=/etc/bind/named.conf.options
++ NAT64_PREFIX=64:ff9b::/96
++ DNS64_NAMESERVER_ADDR=127.0.0.1
+++ echo 64:ff9b::/96
+++ tr '"/"' '"/"'
++ DNS64_CONF='dns64 64:ff9b::/96 { clients { thread; }; recursive-only yes; };'
++ without NAT64
++ with NAT64
++ local value
+++ printenv NAT64
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
+++ eval echo '${NAT64-}'
++++ echo 1
++ value=1
++ [[ 1 == 1 ]]
++ without DNS64
++ with DNS64
++ local value
+++ printenv DNS64
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
+++ eval echo '${DNS64-}'
++++ echo 0
++ value=0
++ [[ 0 == 1 ]]
++ '[' ubuntu = raspbian ']'
++ '[' ubuntu = beagleboneblack ']'
++ '[' ubuntu = ubuntu ']'
++ RESOLV_CONF_HEAD=/etc/resolvconf/resolv.conf.d/head
+ . script/_dhcpv6_pd
++ '[' ubuntu = ubuntu ']'
++ WAN_INTERFACE=enp0s3
++ WLAN_INTERFACE=wlan0
++ WPAN_INTERFACE=wpan0
++ DHCPCD_CONF=/etc/dhcpcd.conf
++ DHCPCD_CONF_BACKUP=/etc/dhcpcd.conf.orig
++ NCP_STATE_NOTIFIER=/usr/sbin/ncp_state_notifier
++ NCP_STATE_DISPATCHER=/etc/ncp_state_notifier/dispatcher.d
++ NCP_STATE_NOTIFIER_SERVICE_NAME=ncp_state_notifier.service
++ NCP_STATE_NOTIFIER_SERVICE=/etc/systemd/system/ncp_state_notifier.service
++ DHCPCD_RELOADER=/etc/ncp_state_notifier/dispatcher.d/dhcpcd_reloader
++ without DHCPV6_PD
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
+ . script/_network_manager
++ AP_CONN=BorderRouter-AP
++ ETH_CONN=BorderRouter-Eth
++ AP_HELPER_SCRIPT=/etc/NetworkManager/dispatcher.d/ap-helper
++ DHCPV6_HELPER_SCRIPT=/etc/NetworkManager/dispatcher.d/dhcpv6-helper
+ . script/_rt_tables
+ . script/_swapfile
++ SWAP_REQUIRED=false
++ SWAP_FILENAME=/swapfile
++ SWAP_BLOCK_SIZE=1M
++ SWAP_BLOCK_CNT=1024
+ . script/_sudo_extend
++ ETC_SUDOERS=/etc/sudoers
++ SUDO_EXTEND_TIME=false
++ SUDO_EXTEND_TIME_AMOUNT=120
+ . script/_disable_services
+ . script/_firewall
++ FIREWALL_SERVICE=/etc/init.d/otbr-firewall
++ sudo modprobe ip6table_filter
++ FIREWALL=1
+ main
+ . /dev/null
+ extend_sudo_timeout
+ local _why
+ _why=Disabled
+ false
+ false
+ echo 'sudo-timeout: Not extending, Disabled'
sudo-timeout: Not extending, Disabled
+ setup_swapfile
+ false
+ echo 'Swapfile: not required'
Swapfile: not required
+ disable_services
+ case $PLATFORM in
+ echo 'Nothing to disable'
+ otbr_uninstall
+ have systemctl
+ command -v systemctl
+ sudo systemctl stop otbr-web
+ sudo systemctl stop otbr-agent
+ sudo systemctl disable otbr-web
Removed /etc/systemd/system/multi-user.target.wants/otbr-web.service.
Removed /etc/systemd/system/otbr-web.service.
+ sudo systemctl disable otbr-agent
Removed /etc/systemd/system/otbr-agent.service.
Removed /etc/systemd/system/multi-user.target.wants/otbr-agent.service.
+ sudo systemctl is-enabled otbr-web
disabled
+ sudo systemctl is-enabled otbr-agent
disabled
+ sudo killall otbr-web otbr-agent
otbr-web: no process found
otbr-agent: no process found
+ true
+ cd /rk356x/openthread/ot-br-posix/build/otbr
script/_otbr: line 52: cd: /rk356x/openthread/ot-br-posix/build/otbr: No such file or directory
+ have systemctl
+ command -v systemctl
+ sudo systemctl daemon-reload
+ border_routing_uninstall
+ with BORDER_ROUTING
+ local value
++ printenv BORDER_ROUTING
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BORDER_ROUTING-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ accept_ra_uninstall
+ test '!' -f /etc/sysctl.d/60-otbr-accept-ra.conf
+ sudo rm -v /etc/sysctl.d/60-otbr-accept-ra.conf
removed '/etc/sysctl.d/60-otbr-accept-ra.conf'
+ dhcpcd_enable_ipv6
+ '[' -f /etc/dhcpcd.conf.orig ']'
+ network_manager_uninstall
+ with NETWORK_MANAGER
+ local value
++ printenv NETWORK_MANAGER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NETWORK_MANAGER-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ dhcpv6_pd_uninstall
+ with DHCPV6_PD
+ local value
++ printenv DHCPV6_PD
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DHCPV6_PD-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ nat64_uninstall
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ nat64_stop
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ '[' openthread = tayga ']'
+ nat44_stop
+ with DOCKER
+ local value
++ printenv DOCKER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DOCKER-}'
+++ echo
+ value=
+ [[ '' == 1 ]]
+ have systemctl
+ command -v systemctl
+ sudo systemctl stop otbr-nat44
+ '[' openthread = tayga ']'
+ nat44_uninstall
+ have systemctl
+ command -v systemctl
+ sudo systemctl disable otbr-nat44
otbr-nat44.service is not a native service, redirecting to systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install disable otbr-nat44
+ have update-rc.d
+ command -v update-rc.d
+ sudo update-rc.d otbr-nat44 remove
+ test '!' -f /etc/init.d/otbr-nat44
+ sudo rm /etc/init.d/otbr-nat44
+ dns64_uninstall
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ with DNS64
+ local value
++ printenv DNS64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DNS64-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ rt_tables_uninstall
+ with BACKBONE_ROUTER
+ local value
++ printenv BACKBONE_ROUTER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BACKBONE_ROUTER-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo sed -i.bak '/88\s\+openthread/d' /etc/iproute2/rt_tables
+ ipforward_uninstall
+ test '!' -f /etc/sysctl.d/60-otbr-ip-forward.conf
+ sudo rm -v /etc/sysctl.d/60-otbr-ip-forward.conf
removed '/etc/sysctl.d/60-otbr-ip-forward.conf'
+ firewall_uninstall
+ with FIREWALL
+ local value
++ printenv FIREWALL
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${FIREWALL-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ firewall_stop
+ with FIREWALL
+ local value
++ printenv FIREWALL
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${FIREWALL-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ with DOCKER
+ local value
++ printenv DOCKER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DOCKER-}'
+++ echo
+ value=
+ [[ '' == 1 ]]
+ have systemctl
+ command -v systemctl
+ sudo systemctl stop otbr-firewall
+ have systemctl
+ command -v systemctl
+ sudo systemctl disable otbr-firewall
otbr-firewall.service is not a native service, redirecting to systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install disable otbr-firewall
+ have update-rc.d
+ command -v update-rc.d
+ sudo update-rc.d otbr-firewall remove
+ test '!' -f /etc/init.d/otbr-firewall
+ sudo rm /etc/init.d/otbr-firewall
+ firewall_install
+ with FIREWALL
+ local value
++ printenv FIREWALL
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${FIREWALL-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo cp script/otbr-firewall /etc/init.d/otbr-firewall
+ sudo chmod a+x /etc/init.d/otbr-firewall
+ have systemctl
+ command -v systemctl
+ sudo systemctl enable otbr-firewall
otbr-firewall.service is not a native service, redirecting to systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable otbr-firewall
+ sudo systemctl start otbr-firewall
+ ipforward_install
+ sudo tee /etc/sysctl.d/60-otbr-ip-forward.conf
net.ipv6.conf.all.forwarding = 1
net.ipv4.ip_forward = 1
+ without DOCKER
+ with DOCKER
+ local value
++ printenv DOCKER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DOCKER-}'
+++ echo
+ value=
+ [[ '' == 1 ]]
+ ipforward_enable
+ echo 1
+ sudo tee /proc/sys/net/ipv6/conf/all/forwarding
1
+ echo 1
+ sudo tee /proc/sys/net/ipv4/ip_forward
1
+ rt_tables_install
+ with BACKBONE_ROUTER
+ local value
++ printenv BACKBONE_ROUTER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BACKBONE_ROUTER-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ rt_tables_uninstall
+ with BACKBONE_ROUTER
+ local value
++ printenv BACKBONE_ROUTER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BACKBONE_ROUTER-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo sed -i.bak '/88\s\+openthread/d' /etc/iproute2/rt_tables
+ sudo sh -c 'echo "88 openthread" >>/etc/iproute2/rt_tables'
+ without DOCKER
+ with DOCKER
+ local value
++ printenv DOCKER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DOCKER-}'
+++ echo
+ value=
+ [[ '' == 1 ]]
+ sudo sh -c 'echo "" >>/etc/sysctl.conf'
+ sudo sh -c 'echo "# OpenThread configuration" >>/etc/sysctl.conf'
+ sudo sh -c 'echo "net.core.optmem_max=65536" >>/etc/sysctl.conf'
+ sudo sh -c 'sysctl -p /etc/sysctl.conf'
net.core.optmem_max = 65536
net.core.optmem_max = 65536
+ nat64_install
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ '[' openthread = tayga ']'
+ nat44_install
+ sudo tee /etc/init.d/otbr-nat44
#! /bin/sh
#
#  Copyright (c) 2017, The OpenThread Authors.
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the
#     names of its contributors may be used to endorse or promote products
#     derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
### BEGIN INIT INFO
# Provides:          otbr-nat44
# Required-Start:
# Required-Stop:
# Should-Start:
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: iptables NAT44
# Description:       NAT44 is require for OpenThread border router
#                    to connect to arbitrary IPv4 endpoints.
### END INIT INFO

. /lib/lsb/init-functions
. /lib/init/vars.sh

case "$1" in
    start)
+ '[' openthread = tayga ']'
+ echo '        iptables -t mangle -A PREROUTING -i wpan0 -j MARK --set-mark 0x1001'
+ sudo tee -a /etc/init.d/otbr-nat44
        iptables -t mangle -A PREROUTING -i wpan0 -j MARK --set-mark 0x1001
+ echo '        iptables -t nat -A POSTROUTING -m mark --mark 0x1001 -j MASQUERADE'
+ sudo tee -a /etc/init.d/otbr-nat44
        iptables -t nat -A POSTROUTING -m mark --mark 0x1001 -j MASQUERADE
+ for IFNAME in $WLAN_IFNAMES
+ echo '        iptables -t filter -A FORWARD -o enp2s0 -j ACCEPT'
+ sudo tee -a /etc/init.d/otbr-nat44
        iptables -t filter -A FORWARD -o enp2s0 -j ACCEPT
+ echo '        iptables -t filter -A FORWARD -i enp2s0 -j ACCEPT'
+ sudo tee -a /etc/init.d/otbr-nat44
        iptables -t filter -A FORWARD -i enp2s0 -j ACCEPT
+ sudo tee -a /etc/init.d/otbr-nat44
        ;;
    restart|reload|force-reload)
        echo "Error: argument '$1' not supported" >&2
        exit 3
        ;;
    stop|status)
        # No-op
        ;;
    *)
        echo "Usage: $0 start|stop" >&2
        exit 3
        ;;
esac
+ sudo chmod a+x /etc/init.d/otbr-nat44
+ have systemctl
+ command -v systemctl
+ sudo systemctl enable otbr-nat44
otbr-nat44.service is not a native service, redirecting to systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable otbr-nat44
+ sudo systemctl start otbr-nat44
+ dns64_install
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ with DNS64
+ local value
++ printenv DNS64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DNS64-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ network_manager_install
+ with NETWORK_MANAGER
+ local value
++ printenv NETWORK_MANAGER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NETWORK_MANAGER-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ dhcpv6_pd_install
+ with DHCPV6_PD
+ local value
++ printenv DHCPV6_PD
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DHCPV6_PD-}'
+++ echo 0
+ value=0
+ [[ 0 == 1 ]]
+ return 0
+ border_routing_install
+ with BORDER_ROUTING
+ local value
++ printenv BORDER_ROUTING
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BORDER_ROUTING-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ dhcpcd_disable_ipv6
+ '[' -f /etc/dhcpcd.conf ']'
+ accept_ra_install
+ sudo tee /etc/sysctl.d/60-otbr-accept-ra.conf
net.ipv6.conf.enp2s0.accept_ra = 2
net.ipv6.conf.enp2s0.accept_ra_rt_info_max_plen = 64
+ without DOCKER
+ with DOCKER
+ local value
++ printenv DOCKER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${DOCKER-}'
+++ echo
+ value=
+ [[ '' == 1 ]]
+ accept_ra_enable
+ with BORDER_ROUTING
+ local value
++ printenv BORDER_ROUTING
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BORDER_ROUTING-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ '[' -f /proc/sys/net/ipv6/conf/enp2s0/accept_ra ']'
+ '[' -f /proc/sys/net/ipv6/conf/enp2s0/accept_ra_rt_info_max_plen ']'
+ otbr_install
+ otbr_options=()
+ local otbr_options
+ [[ -n '' ]]
+ otbr_options=("-DBUILD_TESTING=OFF" "-DCMAKE_INSTALL_PREFIX=/usr" "-DOTBR_DBUS=ON" "-DOTBR_DNSSD_DISCOVERY_PROXY=ON" "-DOTBR_SRP_ADVERTISING_PROXY=ON" "-DOTBR_INFRA_IF_NAME=${INFRA_IF_NAME}" "-DOTBR_MDNS=${OTBR_MDNS:=mDNSResponder}" "-DOTBR_VERSION=" "-DOT_PACKAGE_VERSION=" "${otbr_options[@]}")
+ with WEB_GUI
+ local value
++ printenv WEB_GUI
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${WEB_GUI-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOTBR_WEB=ON")
+ with BORDER_ROUTING
+ local value
++ printenv BORDER_ROUTING
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BORDER_ROUTING-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOTBR_BORDER_ROUTING=ON")
+ with REST_API
+ local value
++ printenv REST_API
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${REST_API-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOTBR_REST=ON")
+ with BACKBONE_ROUTER
+ local value
++ printenv BACKBONE_ROUTER
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${BACKBONE_ROUTER-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOTBR_BACKBONE_ROUTER=ON")
+ [[ 0 == \1 ]]
+ [[ 0 == \1 ]]
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ [[ openthread == \o\p\e\n\t\h\r\e\a\d ]]
+ otbr_options+=("-DOTBR_NAT64=ON" "-DOT_POSIX_NAT64_CIDR=${NAT64_DYNAMIC_POOL:-192.168.255.0/24}")
+ with NAT64
+ local value
++ printenv NAT64
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${NAT64-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOTBR_DNS_UPSTREAM_QUERY=ON")
+ with FIREWALL
+ local value
++ printenv FIREWALL
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${FIREWALL-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ otbr_options+=("-DOT_FIREWALL=ON")
+ ./script/cmake-build -DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=/usr -DOTBR_DBUS=ON -DOTBR_DNSSD_DISCOVERY_PROXY=ON -DOTBR_SRP_ADVERTISING_PROXY=ON -DOTBR_INFRA_IF_NAME=enp2s0 -DOTBR_MDNS=mDNSResponder -DOTBR_VERSION= -DOT_PACKAGE_VERSION= -DOTBR_WEB=ON -DOTBR_BORDER_ROUTING=ON -DOTBR_REST=ON -DOTBR_BACKBONE_ROUTER=ON -DOTBR_NAT64=ON -DOT_POSIX_NAT64_CIDR=192.168.255.0/24 -DOTBR_DNS_UPSTREAM_QUERY=ON -DOT_FIREWALL=ON
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
++ STAGE_DIR=/rk356x/openthread/ot-br-posix/stage
++ BUILD_DIR=/rk356x/openthread/ot-br-posix/build
++ [[ -d /rk356x/openthread/ot-br-posix/stage ]]
++ [[ -d /rk356x/openthread/ot-br-posix/build ]]
++ export PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
++ PATH=/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/rk356x/openthread/ot-br-posix/stage/usr/bin:/rk356x/openthread/ot-br-posix/stage/usr/sbin:/usr/bin:/home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/gcc-linaro-7.3.1-2018.05-i686_aarch64-elf/bin
+++ basename ./script/cmake-build
++ TASKNAME=cmake-build
++ BEFORE_HOOK=examples/platforms/ubuntu/before_cmake-build
++ AFTER_HOOK=examples/platforms/ubuntu/after_cmake-build
++ [[ ! -f examples/platforms/ubuntu/before_cmake-build ]]
++ BEFORE_HOOK=/dev/null
++ [[ ! -f examples/platforms/ubuntu/after_cmake-build ]]
++ AFTER_HOOK=/dev/null
+ OTBR_TOP_SRCDIR=/rk356x/openthread/ot-br-posix
+ readonly OTBR_TOP_SRCDIR
+ OTBR_TOP_BUILD_DIR=/rk356x/openthread/ot-br-posix/build/otbr
+ readonly OTBR_TOP_BUILD_DIR
+ OTBR_TARGET=
+ main -DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=/usr -DOTBR_DBUS=ON -DOTBR_DNSSD_DISCOVERY_PROXY=ON -DOTBR_SRP_ADVERTISING_PROXY=ON -DOTBR_INFRA_IF_NAME=enp2s0 -DOTBR_MDNS=mDNSResponder -DOTBR_VERSION= -DOT_PACKAGE_VERSION= -DOTBR_WEB=ON -DOTBR_BORDER_ROUTING=ON -DOTBR_REST=ON -DOTBR_BACKBONE_ROUTER=ON -DOTBR_NAT64=ON -DOT_POSIX_NAT64_CIDR=192.168.255.0/24 -DOTBR_DNS_UPSTREAM_QUERY=ON -DOT_FIREWALL=ON
+ local builddir=/rk356x/openthread/ot-br-posix/build/otbr
+ mkdir -p /rk356x/openthread/ot-br-posix/build/otbr
+ cd /rk356x/openthread/ot-br-posix/build/otbr
+ cmake -GNinja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON /rk356x/openthread/ot-br-posix -DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=/usr -DOTBR_DBUS=ON -DOTBR_DNSSD_DISCOVERY_PROXY=ON -DOTBR_SRP_ADVERTISING_PROXY=ON -DOTBR_INFRA_IF_NAME=enp2s0 -DOTBR_MDNS=mDNSResponder -DOTBR_VERSION= -DOT_PACKAGE_VERSION= -DOTBR_WEB=ON -DOTBR_BORDER_ROUTING=ON -DOTBR_REST=ON -DOTBR_BACKBONE_ROUTER=ON -DOTBR_NAT64=ON -DOT_POSIX_NAT64_CIDR=192.168.255.0/24 -DOTBR_DNS_UPSTREAM_QUERY=ON -DOT_FIREWALL=ON
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'dbus-1'
--   Found dbus-1, version 1.12.2
-- OTBR package name: OpenThread_BorderRouter
-- Version: 0.3.0-9f86725
-- Checking for module 'systemd'
--   Found systemd, version 237
-- OpenThread Source Directory: /rk356x/openthread/ot-br-posix/third_party/openthread/repo
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- OT_APP_CLI=ON
-- OT_APP_NCP=ON
-- OT_APP_RCP=ON
-- OT_FTD=ON
-- OT_MTD=ON
-- OT_RCP=ON
-- - - - - - - - - - - - - - - - - 
-- OpenThread ON/OFF/Unspecified Configs
-- OT_15_4=ON --> OPENTHREAD_CONFIG_RADIO_LINK_IEEE_802_15_4_ENABLE=1
-- OT_ANDROID_NDK=""
-- OT_ANYCAST_LOCATOR=ON --> OPENTHREAD_CONFIG_TMF_ANYCAST_LOCATOR_ENABLE=1
-- OT_ASSERT=""
-- OT_BACKBONE_ROUTER=ON --> OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE=1
-- OT_BACKBONE_ROUTER_DUA_NDPROXYING=OFF --> OPENTHREAD_CONFIG_BACKBONE_ROUTER_DUA_NDPROXYING_ENABLE=0
-- OT_BACKBONE_ROUTER_MULTICAST_ROUTING=""
-- OT_BLE_TCAT=""
-- OT_BORDER_AGENT=ON --> OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE=1
-- OT_BORDER_AGENT_EPSKC=ON --> OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE=1
-- OT_BORDER_AGENT_ID=ON --> OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE=1
-- OT_BORDER_ROUTER=ON --> OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE=1
-- OT_BORDER_ROUTING=ON --> OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE=1
-- OT_BORDER_ROUTING_DHCP6_PD=OFF --> OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE=0
-- OT_BORDER_ROUTING_COUNTERS=ON --> OPENTHREAD_CONFIG_IP6_BR_COUNTERS_ENABLE=1
-- OT_CHANNEL_MANAGER=""
-- OT_CHANNEL_MANAGER_CSL=""
-- OT_CHANNEL_MONITOR=""
-- OT_COAP=ON --> OPENTHREAD_CONFIG_COAP_API_ENABLE=1
-- OT_COAP_BLOCK=""
-- OT_COAP_OBSERVE=""
-- OT_COAPS=ON --> OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE=1
-- OT_COMMISSIONER=ON --> OPENTHREAD_CONFIG_COMMISSIONER_ENABLE=1
-- OT_CSL_AUTO_SYNC=""
-- OT_CSL_DEBUG=""
-- OT_CSL_RECEIVER=""
-- OT_CSL_RECEIVER_LOCAL_TIME_SYNC=""
-- OT_DATASET_UPDATER=ON --> OPENTHREAD_CONFIG_DATASET_UPDATER_ENABLE=1
-- OT_DEVICE_PROP_LEADER_WEIGHT=""
-- OT_DHCP6_CLIENT=""
-- OT_DHCP6_SERVER=""
-- OT_DIAGNOSTIC=""
-- OT_DNS_CLIENT=ON --> OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE=1
-- OT_DNS_CLIENT_OVER_TCP=OFF --> OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE=0
-- OT_DNS_DSO=""
-- OT_DNS_UPSTREAM_QUERY=ON --> OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE=1
-- OT_DNSSD_DISCOVERY_PROXY=""
-- OT_DNSSD_SERVER=ON --> OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE=1
-- OT_DUA=""
-- OT_ECDSA=ON --> OPENTHREAD_CONFIG_ECDSA_ENABLE=1
-- OT_EXTERNAL_HEAP=ON --> OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE=1
-- OT_FIREWALL=ON --> OPENTHREAD_POSIX_CONFIG_FIREWALL_ENABLE=1
-- OT_HISTORY_TRACKER=ON --> OPENTHREAD_CONFIG_HISTORY_TRACKER_ENABLE=1
-- OT_IP6_FRAGM=""
-- OT_JAM_DETECTION=""
-- OT_JOINER=ON --> OPENTHREAD_CONFIG_JOINER_ENABLE=1
-- OT_LINK_METRICS_INITIATOR=OFF --> OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE=0
-- OT_LINK_METRICS_MANAGER=OFF --> OPENTHREAD_CONFIG_LINK_METRICS_MANAGER_ENABLE=0
-- OT_LINK_METRICS_SUBJECT=ON --> OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE=1
-- OT_LINK_RAW=""
-- OT_LOG_LEVEL_DYNAMIC=ON --> OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE=1
-- OT_MAC_FILTER=ON --> OPENTHREAD_CONFIG_MAC_FILTER_ENABLE=1
-- OT_MDNS=""
-- OT_MESH_DIAG=""
-- OT_MESSAGE_USE_HEAP=""
-- OT_MLE_LONG_ROUTES=""
-- OT_MLR=ON --> OPENTHREAD_CONFIG_MLR_ENABLE=1
-- OT_MULTIPAN_RCP=""
-- OT_MULTIPLE_INSTANCE=""
-- OT_NAT64_BORDER_ROUTING=ON --> OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE=1
-- OT_NAT64_TRANSLATOR=ON --> OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE=1
-- OT_NEIGHBOR_DISCOVERY_AGENT=""
-- OT_NETDATA_PUBLISHER=ON --> OPENTHREAD_CONFIG_NETDATA_PUBLISHER_ENABLE=1
-- OT_NETDIAG_CLIENT=ON --> OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE=1
-- OT_NETDIAG_VENDOR_INFO=""
-- OT_OPERATIONAL_DATASET_AUTO_INIT=""
-- OT_OTNS=""
-- OT_PING_SENDER=ON --> OPENTHREAD_CONFIG_PING_SENDER_ENABLE=1
-- OT_PLATFORM_BOOTLOADER_MODE=""
-- OT_PLATFORM_KEY_REF=""
-- OT_PLATFORM_LOG_CRASH_DUMP=""
-- OT_PLATFORM_NETIF=ON --> OPENTHREAD_CONFIG_PLATFORM_NETIF_ENABLE=1
-- OT_PLATFORM_POWER_CALIBRATION=""
-- OT_PLATFORM_UDP=ON --> OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE=1
-- OT_REFERENCE_DEVICE=""
-- OT_SERVICE=ON --> OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE=1
-- OT_SETTINGS_RAM=""
-- OT_SLAAC=ON --> OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE=1
-- OT_SNTP_CLIENT=""
-- OT_SRP_ADV_PROXY=""
-- OT_SRP_CLIENT=ON --> OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE=1
-- OT_SRP_SERVER=ON --> OPENTHREAD_CONFIG_SRP_SERVER_ENABLE=1
-- OT_TCP=OFF --> OPENTHREAD_CONFIG_TCP_ENABLE=0
-- OT_TIME_SYNC=""
-- OT_TREL=OFF --> OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE=0
-- OT_TX_BEACON_PAYLOAD=""
-- OT_TX_QUEUE_STATS=""
-- OT_UDP_FORWARD=OFF --> OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE=0
-- OT_UPTIME=ON --> OPENTHREAD_CONFIG_UPTIME_ENABLE=1
-- OT_VERHOEFF_CHECKSUM=""
-- - - - - - - - - - - - - - - - - 
-- OT_PLATFORM="posix"
-- OT_THREAD_VERSION="1.3" -> OPENTHREAD_CONFIG_THREAD_VERSION=OT_THREAD_VERSION_1_3
-- OT_LOG_LEVEL="INFO" --> OPENTHREAD_CONFIG_LOG_LEVEL=OT_LOG_LEVEL_INFO
-- OT_LOG_OUTPUT=""
-- OT_VENDOR_NAME=""
-- OT_VENDOR_MODEL=""
-- OT_VENDOR_SW_VERSION=""
-- OT_POWER_SUPPLY=""
-- OT_MAC_CSL_REQUEST_AHEAD_US=""
-- OT_MLE_MAX_CHILDREN=""
-- OT_RCP_RESTORATION_MAX_COUNT=""
-- OT_RCP_TX_WAIT_TIME_SECS=""
-- Package Name: OPENTHREAD
-- Setting default package version: e19c775
-- Package Version: e19c775
-- OT_PLATFORM_CONFIG="openthread-core-posix-config.h"
-- OT_PLATFORM_POSIX_CONFIG_FILE=""
-- Readline: readline
You have called ADD_LIBRARY for library openthread-cli-ftd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-cli-mtd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-cli-radio without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-ftd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-mtd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-radio without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-radio-cli without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-radio-spinel without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-spinel-ncp without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-spinel-rcp without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-ncp-ftd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-ncp-mtd without any source files. This typically indicates a problem with your CMakeLists.txt file
You have called ADD_LIBRARY for library openthread-rcp without any source files. This typically indicates a problem with your CMakeLists.txt file
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "3") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Performing Test C_COMPILER_SUPPORTS_WFORMAT_SIGNEDNESS
-- Performing Test C_COMPILER_SUPPORTS_WFORMAT_SIGNEDNESS - Success
CMake Warning (dev) at third_party/cJSON/repo/CMakeLists.txt:4 (project):
  Policy CMP0048 is not set: project() command manages VERSION variables.
  Run "cmake --help-policy CMP0048" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The following variable(s) would be set to empty:

    PROJECT_VERSION
    PROJECT_VERSION_MAJOR
    PROJECT_VERSION_MINOR
    PROJECT_VERSION_PATCH
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Performing Test FLAG_SUPPORTED_fvisibilityhidden
-- Performing Test FLAG_SUPPORTED_fvisibilityhidden - Success
-- Checking for module 'libsystemd'
--   No package 'libsystemd' found
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread (found version "3.0.0") 
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread;-pthread (found version "3.0.0") 
-- Checking for module 'jsoncpp'
--   Found jsoncpp, version 1.7.4
-- Boost version: 1.65.1
-- Found the following Boost libraries:
--   filesystem
--   system
-- Configuring done
-- Generating done
-- Build files have been written to: /rk356x/openthread/ot-br-posix/build/otbr
+ [[ -n '' ]]
+ ninja
[80/529] cd /rk356x/openthread/ot-br-posix/build/otbr/third_party/openthread/repo && /usr/bin/cmake ...XY_MLR_ENABLE=1" -P /rk356x/openthread/ot-br-posix/third_party/openthread/repo/etc/cmake/print.cmake
OPENTHREAD_CONFIG_RADIO_LINK_IEEE_802_15_4_ENABLE=1
OPENTHREAD_CONFIG_TMF_ANYCAST_LOCATOR_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_DUA_NDPROXYING_ENABLE=0
OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE=0
OPENTHREAD_CONFIG_IP6_BR_COUNTERS_ENABLE=1
OPENTHREAD_CONFIG_COAP_API_ENABLE=1
OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE=1
OPENTHREAD_CONFIG_COMMISSIONER_ENABLE=1
OPENTHREAD_CONFIG_DATASET_UPDATER_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE=0
OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE=1
OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE=1
OPENTHREAD_CONFIG_ECDSA_ENABLE=1
OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FIREWALL_ENABLE=1
OPENTHREAD_CONFIG_HISTORY_TRACKER_ENABLE=1
OPENTHREAD_CONFIG_JOINER_ENABLE=1
OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE=0
OPENTHREAD_CONFIG_LINK_METRICS_MANAGER_ENABLE=0
OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE=1
OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE=1
OPENTHREAD_CONFIG_MAC_FILTER_ENABLE=1
OPENTHREAD_CONFIG_MLR_ENABLE=1
OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE=1
OPENTHREAD_CONFIG_NETDATA_PUBLISHER_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_PING_SENDER_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_NETIF_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE=1
OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE=1
OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_SRP_SERVER_ENABLE=1
OPENTHREAD_CONFIG_TCP_ENABLE=0
OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE=0
OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE=0
OPENTHREAD_CONFIG_UPTIME_ENABLE=1
OPENTHREAD_CONFIG_THREAD_VERSION=OT_THREAD_VERSION_1_3
OPENTHREAD_CONFIG_LOG_LEVEL=OT_LOG_LEVEL_INFO
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS=1
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS_MANAGEMENT=0
OPENTHREAD_CONFIG_POSIX_SETTINGS_PATH=/var/lib/thread
PACKAGE_NAME=OPENTHREAD
OPENTHREAD_PLATFORM_POSIX=1
OPENTHREAD_PLATFORM_CORE_CONFIG_FILE=openthread-core-posix-config.h
OPENTHREAD_POSIX_CONFIG_DAEMON_ENABLE=1
OPENTHREAD_CONFIG_NCP_HDLC_ENABLE=1
OPENTHREAD_CONFIG_LOG_CLI=1
OPENTHREAD_CONFIG_MAX_STATECHANGE_HANDLERS=3
OPENTHREAD_CONFIG_MLE_STEERING_DATA_SET_OOB_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FILE=/rk356x/openthread/ot-br-posix/build/otbr/src/agent/openthread-otbr-posix-config.h
OPENTHREAD_CONFIG_TMF_PROXY_DUA_ENABLE=1
OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE=1
[524/529] Generating node_modules/angular-material/angular-material.min.css, node_modules/material-d...angular/angular.min.js, node_modules/d3/d3.min.js, node_modules/material-design-lite/material.min.js
npm WARN deprecated angular-aria@1.8.3: For the actively supported Angular, see https://www.npmjs.com/package/@angular/core. AngularJS support has officially ended. For extended AngularJS support options, see https://goo.gle/angularjs-path-forward.
npm WARN deprecated angular@1.8.3: For the actively supported Angular, see https://www.npmjs.com/package/@angular/core. AngularJS support has officially ended. For extended AngularJS support options, see https://goo.gle/angularjs-path-forward.
npm WARN deprecated angular-animate@1.8.3: For the actively supported Angular, see https://www.npmjs.com/package/@angular/core. AngularJS support has officially ended. For extended AngularJS support options, see https://goo.gle/angularjs-path-forward.
npm WARN deprecated angular-material@1.2.5: For the actively supported Angular Material, see https://www.npmjs.com/package/@angular/material. AngularJS support has officially ended. For extended AngularJS support options, see https://goo.gle/angularjs-path-forward.
otbr-web@1.0.0 /rk356x/openthread/ot-br-posix/build/otbr/src/web/web-service/frontend
├── angular@1.8.3 
├── angular-animate@1.8.3 
├── angular-aria@1.8.3 
├── angular-material@1.2.5 
├── angular-messages@1.8.3 
├── d3@3.5.17 
└── material-design-lite@1.3.0 

npm WARN otbr-web@1.0.0 No repository field.
[529/529] Linking CXX executable src/web/otbr-web
+ cd /rk356x/openthread/ot-br-posix/build/otbr
+ ninja
[2/3] cd /rk356x/openthread/ot-br-posix/build/otbr/third_party/openthread/repo && /usr/bin/cmake -DL...XY_MLR_ENABLE=1" -P /rk356x/openthread/ot-br-posix/third_party/openthread/repo/etc/cmake/print.cmake
OPENTHREAD_CONFIG_RADIO_LINK_IEEE_802_15_4_ENABLE=1
OPENTHREAD_CONFIG_TMF_ANYCAST_LOCATOR_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_DUA_NDPROXYING_ENABLE=0
OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE=0
OPENTHREAD_CONFIG_IP6_BR_COUNTERS_ENABLE=1
OPENTHREAD_CONFIG_COAP_API_ENABLE=1
OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE=1
OPENTHREAD_CONFIG_COMMISSIONER_ENABLE=1
OPENTHREAD_CONFIG_DATASET_UPDATER_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE=0
OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE=1
OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE=1
OPENTHREAD_CONFIG_ECDSA_ENABLE=1
OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FIREWALL_ENABLE=1
OPENTHREAD_CONFIG_HISTORY_TRACKER_ENABLE=1
OPENTHREAD_CONFIG_JOINER_ENABLE=1
OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE=0
OPENTHREAD_CONFIG_LINK_METRICS_MANAGER_ENABLE=0
OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE=1
OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE=1
OPENTHREAD_CONFIG_MAC_FILTER_ENABLE=1
OPENTHREAD_CONFIG_MLR_ENABLE=1
OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE=1
OPENTHREAD_CONFIG_NETDATA_PUBLISHER_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_PING_SENDER_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_NETIF_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE=1
OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE=1
OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_SRP_SERVER_ENABLE=1
OPENTHREAD_CONFIG_TCP_ENABLE=0
OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE=0
OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE=0
OPENTHREAD_CONFIG_UPTIME_ENABLE=1
OPENTHREAD_CONFIG_THREAD_VERSION=OT_THREAD_VERSION_1_3
OPENTHREAD_CONFIG_LOG_LEVEL=OT_LOG_LEVEL_INFO
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS=1
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS_MANAGEMENT=0
OPENTHREAD_CONFIG_POSIX_SETTINGS_PATH=/var/lib/thread
PACKAGE_NAME=OPENTHREAD
OPENTHREAD_PLATFORM_POSIX=1
OPENTHREAD_PLATFORM_CORE_CONFIG_FILE=openthread-core-posix-config.h
OPENTHREAD_POSIX_CONFIG_DAEMON_ENABLE=1
OPENTHREAD_CONFIG_NCP_HDLC_ENABLE=1
OPENTHREAD_CONFIG_LOG_CLI=1
OPENTHREAD_CONFIG_MAX_STATECHANGE_HANDLERS=3
OPENTHREAD_CONFIG_MLE_STEERING_DATA_SET_OOB_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FILE=/rk356x/openthread/ot-br-posix/build/otbr/src/agent/openthread-otbr-posix-config.h
OPENTHREAD_CONFIG_TMF_PROXY_DUA_ENABLE=1
OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE=1
[3/3] Generating node_modules/angular-material/angular-material.min.css, node_modules/material-desig...angular/angular.min.js, node_modules/d3/d3.min.js, node_modules/material-design-lite/material.min.js
npm WARN otbr-web@1.0.0 No repository field.
+ sudo ninja install
[2/6] cd /rk356x/openthread/ot-br-posix/build/otbr/third_party/openthread/repo && /usr/bin/cmake -DL...XY_MLR_ENABLE=1" -P /rk356x/openthread/ot-br-posix/third_party/openthread/repo/etc/cmake/print.cmake
OPENTHREAD_CONFIG_RADIO_LINK_IEEE_802_15_4_ENABLE=1
OPENTHREAD_CONFIG_TMF_ANYCAST_LOCATOR_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BACKBONE_ROUTER_DUA_NDPROXYING_ENABLE=0
OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE=1
OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE=0
OPENTHREAD_CONFIG_IP6_BR_COUNTERS_ENABLE=1
OPENTHREAD_CONFIG_COAP_API_ENABLE=1
OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE=1
OPENTHREAD_CONFIG_COMMISSIONER_ENABLE=1
OPENTHREAD_CONFIG_DATASET_UPDATER_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE=0
OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE=1
OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE=1
OPENTHREAD_CONFIG_ECDSA_ENABLE=1
OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FIREWALL_ENABLE=1
OPENTHREAD_CONFIG_HISTORY_TRACKER_ENABLE=1
OPENTHREAD_CONFIG_JOINER_ENABLE=1
OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE=0
OPENTHREAD_CONFIG_LINK_METRICS_MANAGER_ENABLE=0
OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE=1
OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE=1
OPENTHREAD_CONFIG_MAC_FILTER_ENABLE=1
OPENTHREAD_CONFIG_MLR_ENABLE=1
OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE=1
OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE=1
OPENTHREAD_CONFIG_NETDATA_PUBLISHER_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_PING_SENDER_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_NETIF_ENABLE=1
OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE=1
OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE=1
OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE=1
OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE=1
OPENTHREAD_CONFIG_SRP_SERVER_ENABLE=1
OPENTHREAD_CONFIG_TCP_ENABLE=0
OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE=0
OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE=0
OPENTHREAD_CONFIG_UPTIME_ENABLE=1
OPENTHREAD_CONFIG_THREAD_VERSION=OT_THREAD_VERSION_1_3
OPENTHREAD_CONFIG_LOG_LEVEL=OT_LOG_LEVEL_INFO
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS=1
OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS_MANAGEMENT=0
OPENTHREAD_CONFIG_POSIX_SETTINGS_PATH=/var/lib/thread
PACKAGE_NAME=OPENTHREAD
OPENTHREAD_PLATFORM_POSIX=1
OPENTHREAD_PLATFORM_CORE_CONFIG_FILE=openthread-core-posix-config.h
OPENTHREAD_POSIX_CONFIG_DAEMON_ENABLE=1
OPENTHREAD_CONFIG_NCP_HDLC_ENABLE=1
OPENTHREAD_CONFIG_LOG_CLI=1
OPENTHREAD_CONFIG_MAX_STATECHANGE_HANDLERS=3
OPENTHREAD_CONFIG_MLE_STEERING_DATA_SET_OOB_ENABLE=1
OPENTHREAD_POSIX_CONFIG_FILE=/rk356x/openthread/ot-br-posix/build/otbr/src/agent/openthread-otbr-posix-config.h
OPENTHREAD_CONFIG_TMF_PROXY_DUA_ENABLE=1
OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE=1
[5/6] Install the project...
-- Install configuration: ""
-- Installing: /usr/sbin/otbr-agent
-- Installing: /usr/sbin/ot-ctl
-- Installing: /etc/dbus-1/system.d/otbr-agent.conf
-- Installing: /lib/systemd/system/otbr-agent.service
-- Installing: /etc/default/otbr-agent
-- Installing: /usr/sbin/otbr-web
-- Installing: /lib/systemd/system/otbr-web.service
-- Installing: /usr/share/otbr-web/frontend/index.html
-- Installing: /usr/share/otbr-web/frontend/join.dialog.html
-- Up-to-date: /usr/share/otbr-web/frontend/res
-- Up-to-date: /usr/share/otbr-web/frontend/res/img
-- Installing: /usr/share/otbr-web/frontend/res/img/borderrouter.png
-- Installing: /usr/share/otbr-web/frontend/res/img/icon-info.png
-- Installing: /usr/share/otbr-web/frontend/res/img/android-desktop.png
-- Installing: /usr/share/otbr-web/frontend/res/img/openthread_logo.png
-- Installing: /usr/share/otbr-web/frontend/res/img/ios-desktop.png
-- Installing: /usr/share/otbr-web/frontend/res/img/favicon.png
-- Up-to-date: /usr/share/otbr-web/frontend/res/css
-- Installing: /usr/share/otbr-web/frontend/res/css/styles.css
-- Up-to-date: /usr/share/otbr-web/frontend/res/js
-- Installing: /usr/share/otbr-web/frontend/res/js/app.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/angular-animate.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/angular-aria.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/angular-material.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/angular-messages.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/angular.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/d3.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/js/material.min.js
-- Up-to-date: /usr/share/otbr-web/frontend/res/css/angular-material.min.css
-- Up-to-date: /usr/share/otbr-web/frontend/res/css/material.min.css
+ have systemctl
+ command -v systemctl
+ sudo systemctl reload dbus
+ sudo systemctl daemon-reload
+ without WEB_GUI
+ with WEB_GUI
+ local value
++ printenv WEB_GUI
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${WEB_GUI-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo systemctl enable otbr-web
Created symlink /etc/systemd/system/otbr-web.service → /lib/systemd/system/otbr-web.service.
Created symlink /etc/systemd/system/multi-user.target.wants/otbr-web.service → /lib/systemd/system/otbr-web.service.
+ sudo systemctl enable otbr-agent
Created symlink /etc/systemd/system/otbr-agent.service → /lib/systemd/system/otbr-agent.service.
Created symlink /etc/systemd/system/multi-user.target.wants/otbr-agent.service → /lib/systemd/system/otbr-agent.service.
+ sudo systemctl is-enabled otbr-agent
enabled
+ without WEB_GUI
+ with WEB_GUI
+ local value
++ printenv WEB_GUI
+ value=
+ [[ -z '' ]]
+ [[ -f examples/platforms/ubuntu/default ]]
++ . examples/platforms/ubuntu/default
+++ NAT64=1
+++ DNS64=0
+++ DHCPV6_PD=0
+++ NETWORK_MANAGER=0
+++ BACKBONE_ROUTER=1
+++ BORDER_ROUTING=1
+++ WEB_GUI=1
+++ REST_API=1
++ eval echo '${WEB_GUI-}'
+++ echo 1
+ value=1
+ [[ 1 == 1 ]]
+ sudo systemctl is-enabled otbr-web
enabled
+ [[ 0 == \1 ]]
+ . /dev/null
eric@ubuntu:/rk356x/openthread/ot-br-posix$ find -name 'otbr-agent'
./build/otbr/src/agent/otbr-agent
eric@ubuntu:/rk356x/openthread/ot-br-posix$ find -name 'ot-ctl'
./build/otbr/third_party/openthread/repo/src/posix/ot-ctl
```