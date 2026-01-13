[AR01A](AR01A.md) 
```c
root@linaro-alip:/# ls
bin   data  etc   info  lost+found  mnt  opt   rockchip-test  run   sdcard            sha256sum.txt  sys     tmp    userdata  var
boot  dev   home  lib   media       oem  proc  root           sbin  sha256sum.README  srv            system  udisk  usr       vendor
root@linaro-alip:/#
root@linaro-alip:/# ls
root@linaro-alip:/# ls usr/bin/
'['                                     dirmngr-client            kbdinfo                               pinentry                         timedatectl
 aarch64-linux-gnu-addr2line            dirname                   kbd_mode                              pinentry-curses                  timeout
 aarch64-linux-gnu-ar                   disk-helper               kbxutil                               ping                             tload
 aarch64-linux-gnu-as                   dmesg                     kernel-install                        ping4                            toe
 aarch64-linux-gnu-c++filt              dm-tool                   kill                                  ping6                            top
 aarch64-linux-gnu-cpp                  dnsdomainname             killall                               pinky                            touch
 aarch64-linux-gnu-cpp-10               domainname                kmod                                  pkaction                         tput
 aarch64-linux-gnu-dwp                  dpkg                      kmsgrab                               pkcheck                          tr
 aarch64-linux-gnu-elfedit              dpkg-architecture         kmstest                               pkexec                           trace-cmd
 aarch64-linux-gnu-g++                  dpkg-buildflags           koi8rxterm                            pkg-config                       tracker
 aarch64-linux-gnu-g++-10               dpkg-buildpackage         l2ping                                pkgdata                          transset
 aarch64-linux-gnu-gcc                  dpkg-checkbuilddeps       l2test                                pkill                            troff
 aarch64-linux-gnu-gcc-10               dpkg-deb                  last                                  pkttyagent                       true
 aarch64-linux-gnu-gcc-ar               dpkg-distaddfile          lastb                                 pl2pm                            truncate
 aarch64-linux-gnu-gcc-ar-10            dpkg-divert               lastlog                               play                             tset
 aarch64-linux-gnu-gcc-nm               dpkg-genbuildinfo         lcf                                   pldd                             tsort
 aarch64-linux-gnu-gcc-nm-10            dpkg-genchanges           ld                                    plog                             tty
 aarch64-linux-gnu-gcc-ranlib           dpkg-gencontrol           ld.bfd                                pmap                             tzselect
 aarch64-linux-gnu-gcc-ranlib-10        dpkg-gensymbols           ldd                                   pm-is-supported                  ucf
 aarch64-linux-gnu-gcov                 dpkg-maintscript-helper   ld.gold                               pod2html                         ucfq
 aarch64-linux-gnu-gcov-10              dpkg-mergechangelogs      less                                  pod2man                          ucfr
 aarch64-linux-gnu-gcov-dump            dpkg-name                 lessecho                              pod2text                         uconv
 aarch64-linux-gnu-gcov-dump-10         dpkg-parsechangelog       lessfile                              pod2usage                        ucs2any
 aarch64-linux-gnu-gcov-tool            dpkg-query                lesskey                               podchecker                       udevadm
 aarch64-linux-gnu-gcov-tool-10         dpkg-realpath             lesspipe                              poff                             udisksctl
 aarch64-linux-gnu-gold                 dpkg-scanpackages         lexgrog                               pon                              ul
 aarch64-linux-gnu-gprof                dpkg-scansources          libnetcfg                             POST                             ulockmgr_server
 aarch64-linux-gnu-ld                   dpkg-shlibdeps            libpng16-config                       power-key.sh                     umount
 aarch64-linux-gnu-ld.bfd               dpkg-source               libpng-config                         pr                               uname
 aarch64-linux-gnu-ld.gold              dpkg-split                lightdm-gtk-greeter-settings          preconv                          uncompress
 aarch64-linux-gnu-lto-dump-10          dpkg-statoverride         lightdm-gtk-greeter-settings-pkexec   printenv                         unexpand
 aarch64-linux-gnu-nm                   dpkg-trigger              link                                  printf                           unicode_start
 aarch64-linux-gnu-objcopy              dpkg-vendor               linux32                               prlimit                          unicode_stop
 aarch64-linux-gnu-objdump              du                        linux64                               prove                            uniq
 aarch64-linux-gnu-pkg-config           dumpkeys                  linux-check-removal                   prtstat                          unlink
 aarch64-linux-gnu-ranlib               dvb-fe-tool               linux-update-symlinks                 ps                               unlzma
 aarch64-linux-gnu-readelf              dvb-format-convert        linux-version                         psfaddtable                      unmkinitramfs
 aarch64-linux-gnu-size                 dvbv5-daemon              listres                               psfgettable                      unshare
 aarch64-linux-gnu-strings              dvbv5-scan                ln                                    psfstriptable                    unxz
 aarch64-linux-gnu-strip                dvbv5-zap                 lnstat                                psfxtable                        unzip
 aarch64-unknown-linux-gnu-pkg-config   dwp                       loadkeys                              pslog                            unzipsfx
 aconnect                               echo                      loadunimap                            pstree                           update
 acpi_listen                            editor                    locale                                pstree.x11                       update-alternatives
 adbd                                   editres                   localectl                             ptar                             update-desktop-database
 addpart                                egrep                     localedef                             ptardiff                         update-leap
 addr2line                              elfedit                   log2asc                               ptargrep                         update-mime-database
 alsabat                                enc2xs                    log2long                              ptx                              upgrade_tool
 alsaloop                               encguess                  logcat                                pulseaudio                       upower
 alsamixer                              env                       logger                                pwd                              uptime
 alsatplg                               eqn                       log-guardian                          pwdx                             usbdevice
 alsaucm                                evtest                    login                                 py3clean                         usb-devices
 amidi                                  ex                        loginctl                              py3compile                       usbhid-dump
 amixer                                 exo-desktop-item-edit     logname                               py3versions                      usbreset
 aplay                                  exo-open                  look                                  pydoc3                           users
 aplaymidi                              expand                    lowntfs-3g                            pydoc3.9                         users-admin
 appres                                 expiry                    ls                                    pygettext3                       user-setup
 apropos                                expr                      lsattr                                pygettext3.9                     utmpdump
 apt                                    factor                    lsblk                                 python3                          uxterm
 apt-cache                              faillog                   lsb_release                           python3.9                        v4l2-compliance
 apt-cdrom                              fallocate                 lscpu                                 qemu-aarch64-static              v4l2-ctl
 apt-config                             false                     lsinitramfs                           qv4l2                            v4l2-sysfs-path
 apt-extracttemplates                   fc-cache                  lsinput                               ranlib                           vdir
 apt-ftparchive                         fc-cat                    lsipc                                 rbash                            vendor_storage
 apt-get                                fc-conflist               lslocks                               rcconf                           vi
 apt-key                                fc-list                   lslogins                              rcp                              view
 apt-mark                               fc-match                  lsmem                                 rctest                           viewres
 apt-sortpkgs                           fc-pattern                lsmod                                 rdma                             vim
 ar                                     fc-query                  lsns                                  rds-ctl                          vim.basic
 arch                                   fc-scan                   lsof                                  readelf                          vimdiff
 arecord                                fc-validate               lspci                                 readlink                         vim.tiny
 arecordmidi                            fgconsole                 lspgpot                               realpath                         vimtutor
 as                                     fgrep                     lsusb                                 rec                              vmstat
 asc2log                                file                      lto-dump-10                           rendercheck                      vpu_api_test
 aseqdump                               fincore                   luit                                  renice                           w
 aseqnet                                find                      lwp-download                          reset                            wall
 async-commit                           findmnt                   lwp-dump                              resize                           watch
 atobm                                  flock                     lwp-mirror                            resize-helper                    watchgnupg
 awk                                    fmt                       lwp-request                           resizepart                       wayland-scanner
 axfer                                  fold                      lxterm                                resolvectl                       wc
 b2sum                                  fonttosfnt                lzcat                                 restart_rknn.sh                  wdctl
 base32                                 free                      lzcmp                                 rev                              wget
 base64                                 funzip                    lzdiff                                rfcomm                           whatis
 basename                               fuser                     lzegrep                               rgrep                            whereis
 basenc                                 fusermount                lzfgrep                               rhythmbox                        which
 bash                                   g++                       lzgrep                                rhythmbox-client                 whiptail
 bashbug                                g++-10                    lzless                                rkaiq_3A_server                  who
 bccmd                                  gapplication              lzma                                  rkaiq_tool_server                whoami
 bcmserver                              gatttool                  lzmainfo                              rknn_common_test                 wifi_ap6xxx_rftest.sh
 bdftopcf                               gcc                       lzmore                                rknn_server                      wifibt-bus
 bdftruncate                            gcc-10                    make                                  rk_wifibt_init                   wifibt-chip
 bitmap                                 gcc-ar                    makeconv                              rlogin                           wifibt-id
 blueman-adapters                       gcc-ar-10                 make-first-existing-target            rm                               wifibt-info
 blueman-applet                         gcc-nm                    man                                   rmdir                            wifibt-init.sh
 blueman-assistant                      gcc-nm-10                 mandb                                 routef                           wifibt-module
 blueman-manager                        gcc-ranlib                manpath                               routel                           wifibt-util.sh
 blueman-report                         gcc-ranlib-10             man-recode                            rpcgen                           wifibt-vendor
 blueman-sendto                         gcov                      mapscrn                               rsh                              wifi-connect.sh
 blueman-services                       gcov-10                   mawk                                  rstart                           wl
 blueman-tray                           gcov-dump                 mcookie                               rstartd                          wpa_passphrase
 bluemoon                               gcov-dump-10              md5sum                                rtk_hciattach                    write
 bluetoothctl                           gcov-tool                 md5sum.textutils                      rtlbtmp                          write.ul
 bmtoa                                  gcov-tool-10              media-ctl                             rtstat                           X
 bootanim                               gdbus                     memtester                             rtwpriv                          X11
 bootctl                                gdbus-codegen             mesg                                  runcon                           x11perf
 brcm_patchram_plus1                    gdk-pixbuf-csource        migrate-pubring-from-classic-gpg      run-parts                        x11perfcomp
 btattach                               gdk-pixbuf-pixdata        mkdir                                 rview                            xargs
 btmgmt                                 gdk-pixbuf-thumbnailer    mkfifo                                rvim                             xauth
 btmon                                  genbrk                    mkfontdir                             savelog                          xbiff
 bt-tty                                 gencat                    mkfontscale                           scp                              xcalc
 bunzip2                                gencfu                    mk_modmap                             screendump                       xclipboard
 busctl                                 gencnval                  mknod                                 script                           xclock
 busybox                                gendict                   mktemp                                scriptlive                       xcmsdb
 bwrap                                  generate_logs             modetest                              scriptreplay                     xconsole
 bzcat                                  genrb                     more                                  sdiff                            xcursorgen
 bzcmp                                  geqn                      mount                                 sdptool                          xcutsel
 bzdiff                                 GET                       mount-helper                          sed                              xdg-dbus-proxy
 bzegrep                                getconf                   mountpoint                            select-editor                    xdg-desktop-icon
 bzexe                                  get-edid                  mpi_dec_mt_test                       sensible-browser                 xdg-desktop-menu
 bzfgrep                                getent                    mpi_dec_multi_test                    sensible-editor                  xdg-email
 bzgrep                                 getkeycodes               mpi_dec_nt_test                       sensible-pager                   xdg-icon-resource
 bzip2                                  getopt                    mpi_dec_test                          seq                              xdg-mime
 bzip2recover                           gio                       mpi_enc_mt_test                       sessreg                          xdg-open
 bzless                                 gio-querymodules          mpi_enc_test                          setarch                          xdg-screensaver
 bzmore                                 git                       mpi_rc2_test                          setfont                          xdg-settings
 c++                                    git-receive-pack          mpp_info_test                         setkeycodes                      xditview
 c89                                    git-shell                 mpris-proxy                           setleds                          xdpyinfo
 c89-gcc                                git-upload-archive        mt                                    setlogcons                       xdriinfo
 c99                                    git-upload-pack           mt-gnu                                setmetamode                      xedit
 c99-gcc                                glib-compile-resources    multivideoplayer                      setpci                           xev
 cal                                    glib-compile-schemas      mv                                    setpriv                          xeyes
 calc_tickadj                           glib-genmarshal           namei                                 setsid                           xfce4-about
 canbusload                             glib-gettextize           nautilus                              setterm                          xfce4-accessibility-settings
 can-calc-bit-timing                    glib-mkenums              nautilus-autorun-software             setupcon                         xfce4-appearance-settings
 candump                                glmark2                   nawk                                  setvtrgb                         xfce4-appfinder
 canfdtest                              glmark2-drm               ncal                                  setxkbmap                        xfce4-color-settings
 cangen                                 glmark2-es2               neqn                                  sftp                             xfce4-display-settings
 cangw                                  glmark2-es2-drm           netstat                               sg                               xfce4-find-cursor
 canlogserver                           glmark2-es2-wayland       networkctl                            sh                               xfce4-keyboard-settings
 canplayer                              glmark2-wayland           newgrp                                sha1sum                          xfce4-mime-helper
 cansend                                glxdemo                   nice                                  sha224sum                        xfce4-mime-settings
 cansequence                            glxgears                  nisdomainname                         sha256sum                        xfce4-mouse-settings
 cansniffer                             glxheads                  nl                                    sha384sum                        xfce4-panel
 captoinfo                              glxinfo                   nm                                    sha512sum                        xfce4-popup-applicationsmenu
 cat                                    gmake                     nm-applet                             shares-admin                     xfce4-popup-directorymenu
 catchsegv                              gnome-www-browser         nmcli                                 shasum                           xfce4-popup-windowmenu
 catman                                 gobject-query             nm-connection-editor                  showconsolefont                  xfce4-power-manager
 cc                                     gold                      nm-online                             showkey                          xfce4-power-manager-settings
 cec-compliance                         gpasswd                   nmtui                                 showrgb                          xfce4-screenshooter
 cec-ctl                                gpg                       nmtui-connect                         shred                            xfce4-session
 cec-follower                           gpg-agent                 nmtui-edit                            shuf                             xfce4-session-logout
 c++filt                                gpgcompose                nmtui-hostname                        size                             xfce4-session-settings
 chage                                  gpgconf                   nohup                                 skill                            xfce4-settings-editor
 chardet                                gpg-connect-agent         nproc                                 slabtop                          xfce4-settings-manager
 chardetect                             gpgparsemail              npu-image.sh                          slcan_attach                     xfconf-query
 chattr                                 gpgsm                     npu_powerctrl                         slcand                           xfd
 chcon                                  gpgsplit                  npu_powerctrl_combine                 slcanpty                         xfdesktop
 cheese                                 gpgtar                    npu_transfer_proxy                    sleep                            xfdesktop-settings
 chfn                                   gpgv                      npu_upgrade                           slogin                           xfhelp4
 chgrp                                  gpg-wks-server            npu_upgrade_pcie                      smproxy                          xflock4
 chmod                                  gpg-zip                   npu_upgrade_pcie_combine              snice                            xfontsel
 choom                                  gpic                      nroff                                 soelim                           xfrun4
 chown                                  gprof                     nsenter                               sort                             xfsettingsd
 chromium                               grep                      nstat                                 sox                              xfwm4
 chrt                                   gresource                 ntfs-3g                               soxi                             xfwm4-settings
 chsh                                   groff                     ntfs-3g.probe                         speaker-test                     xfwm4-tweaks-settings
 chvt                                   grog                      ntfscat                               splain                           xfwm4-workspace-settings
 ciptool                                grops                     ntfscluster                           split                            xgamma
 cisco-decrypt                          grotty                    ntfscmp                               splitfont                        xgc
 ckbcomp                                groups                    ntfsdecrypt                           ss                               xhost
 cksum                                  gsettings                 ntfsfallocate                         ssh                              xinit
 clear                                  gst-device-monitor-1.0    ntfsfix                               ssh-add                          xkbbell
 clear_console                          gst-discoverer-1.0        ntfsinfo                              ssh-agent                        xkbcomp
 cmake                                  gst-inspect-1.0           ntfsls                                ssh-argv0                        xkbevd
 cmp                                    gst-launch-1.0            ntfsmove                              ssh-copy-id                      xkbprint
 codepage                               gst-play-1.0              ntfsrecover                           ssh-import-id                    xkbvleds
 col                                    gst-stats-1.0             ntfssecaudit                          ssh-import-id-gh                 xkbwatch
 colcrt                                 gst-tester-1.0            ntfstruncate                          ssh-import-id-lp                 xkeystone
 colrm                                  gst-transcoder-1.0        ntfsusermap                           ssh-keygen                       xkill
 column                                 gst-typefind-1.0          ntfswipe                              ssh-keyscan                      xload
 comm                                   gtbl                      ntpdc                                 startpar                         xlogo
 corelist                               gtester                   ntpq                                  start-pulseaudio-x11             xlsatoms
 cp                                     gtester-report            ntpsweep                              start_rknn.sh                    xlsclients
 cpack                                  gtf                       ntptrace                              startx                           xlsfonts
 cpan                                   gtk-builder-convert       numfmt                                startxfce4                       xmag
 cpan5.32-aarch64-linux-gnu             gtk-update-icon-cache     obconf                                stat                             xman
 cpio                                   gunzip                    obexctl                               stdbuf                           xmessage
 cpp                                    gzexe                     objcopy                               strace                           xmlcatalog
 cpp-10                                 gzip                      objdump                               strace-log-merge                 xmllint
 cpufreq-aperf                          h2ph                      oclock                                streamzip                        xmodmap
 cpufreq-info                           h2xs                      od                                    stress                           xmore
 cpufreq-set                            hardinfo                  odbcinst                              stressapptest                    Xorg
 c_rehash                               hciattach                 on_ac_power                           stress-ng                        xprop
 csplit                                 hciconfig                 open                                  strings                          xrandr
 ctest                                  hcitool                   opencv_annotation                     strip                            xrdb
 ctstat                                 hd                        opencv_interactive-calibration        stty                             xrefresh
 curl                                   head                      opencv_version                        su                               x-session-manager
 cut                                    HEAD                      opencv_visualisation                  sudo                             xset
 cvt                                    helpztags                 opencv_waldboost_detector             sudoedit                         xsetmode
 cvtsudoers                             hex2hcd                   openssl                               sudoreplay                       xsetpointer
 cx18-ctl                               hexdump                   openvt                                sum                              xsetroot
 dash                                   hostid                    orc-bugreport                         synaptic-pkexec                  xsm
 date                                   hostname                  orcc                                  sync                             xstdcmap
 dbus-cleanup-sockets                   hostnamectl               pacat                                 systemctl                        xsubpp
 dbus-daemon                            iceauth                   pacmd                                 systemd                          xterm
 dbus-launch                            ico                       pactl                                 systemd-analyze                  x-terminal-emulator
 dbus-monitor                           iconv                     padsp                                 systemd-ask-password             xvidtune
 dbus-run-session                       icuinfo                   pager                                 systemd-cat                      xvinfo
 dbus-send                              id                        pa-info                               systemd-cgls                     xwd
 dbus-update-activation-environment     iecset                    pamon                                 systemd-cgtop                    x-window-manager
 dbus-uuidgen                           infocmp                   pango-list                            systemd-delta                    xwininfo
 dd                                     infotocap                 pango-view                            systemd-detect-virt              xwud
 ddcmon                                 inotifywait               paplay                                systemd-escape                   x-www-browser
 deallocvt                              input-event-daemon        parec                                 systemd-hwdb                     xxd
 debconf                                input-events              parecord                              systemd-id128                    xz
 debconf-apt-progress                   input-kbd                 parse-edid                            systemd-inhibit                  xzcat
 debconf-communicate                    install                   partx                                 systemd-machine-id-setup         xzcmp
 debconf-copydb                         instmodsh                 passwd                                systemd-mount                    xzdiff
 debconf-escape                         io                        paste                                 systemd-notify                   xzegrep
 debconf-set-selections                 ionice                    pasuspender                           systemd-path                     xzfgrep
 debconf-show                           ip                        patch                                 systemd-resolve                  xzgrep
 deb-systemd-helper                     ipcmk                     pathchk                               systemd-run                      xzless
 deb-systemd-invoke                     ipcrm                     pavucontrol                           systemd-socket-activate          xzmore
 decode-dimms                           ipcs                      pax11publish                          systemd-stdio-bridge             yes
 decode-edid                            iperf                     pcf2vpnc                              systemd-sysusers                 ypdomainname
 decode_tm6000                          iptables-xml              pcre2-config                          systemd-tmpfiles                 zathura
 decode-vaio                            ir-ctl                    pcre-config                           systemd-tty-ask-password-agent   zcat
 delpart                                ir-keytable               pdb3                                  systemd-umount                   zcmp
 derb                                   ischroot                  pdb3.9                                tabs                             zdiff
 desktop-file-edit                      isotpdump                 peekfd                                tac                              zdump
 desktop-file-install                   isotpperf                 perf                                  tail                             zegrep
 desktop-file-validate                  isotprecv                 perl                                  tar                              zfgrep
 df                                     isotpsend                 perl5.32.1                            tasksel                          zforce
 dh_bash-completion                     isotpserver               perl5.32-aarch64-linux-gnu            taskset                          zgrep
 dhd                                    isotpsniffer              perlbug                               tbl                              zip
 dhd_priv                               isotptun                  perldoc                               tee                              zipcloak
 dh_gstscancodecs                       ivtv-ctl                  perlivp                               tempfile                         zipdetails
 dh_perl_openssl                        j1939acd                  perlthanks                            test                             zipgrep
 dh_xsf_substvars                       j1939cat                  pfc                                   testj1939                        zipinfo
 diff                                   j1939spy                  pgrep                                 thunar                           zipnote
 diff3                                  j1939sr                   pic                                   Thunar                           zipsplit
 dir                                    join                      piconv                                thunar-settings                  zless
 dircolors                              journalctl                pidof                                 tic                              zmore
 dirmngr                                json_pp                   pidwait                               time-admin                       znew
root@linaro-alip:/#
root@linaro-alip:/# ls usr/bin/
root@linaro-alip:/# ls usr/sbin/
accessdb               delgroup              fsck.minix          iotop-py                     ldconfig             ntpdate-debian       rmt-tar                 update-fonts-alias
acpid                  deluser               fsck.nfs            ip                           lightdm              ntp-keygen           route                   update-fonts-dir
addgnupghome           depmod                fsfreeze            ip6tables                    lightdm-gtk-greeter  ntptime              rsyslogd                update-fonts-scale
addgroup               devlink               fstab-decode        ip6tables-apply              locale-gen           ntp-wait             rtacct                  update-icon-caches
add-shell              dhclient              fstrim              ip6tables-legacy             logsave              on_ac_power          rtcwake                 update-initramfs
adduser                dhclient-script       gdisk               ip6tables-legacy-restore     losetup              openvpn              rtmon                   update-locale
agetty                 dmsetup               genccode            ip6tables-legacy-save        lsmod                pam-auth-update      runlevel                update-passwd
alsabat-test           dmstats               gencmn              ip6tables-nft                MAKEDEV              pam_getenv           runuser                 update-pciids
alsactl                dnsmasq               genl                ip6tables-nft-restore        mii-tool             pam_timestamp_check  service                 update-rcconf-guide
alsa-info              dpkg-fsys-usrunmess   gennorm2            ip6tables-nft-save           mke2fs               parted               setcap                  update-rc.d
anacron                dpkg-preconfigure     gensprep            ip6tables-restore            mkfs                 partprobe            setvesablank            usb_modeswitch
applygnupgdefaults     dpkg-reconfigure      getcap              ip6tables-restore-translate  mkfs.bfs             pivot_root           sfdisk                  usb_modeswitch_dispatcher
arp                    dumpe2fs              getpcaps            ip6tables-save               mkfs.cramfs          plipconfig           sgdisk                  useradd
arpd                   e2freefrag            getty               ip6tables-translate          mkfs.ext2            pm-hibernate         shadowconfig            userdel
arptables              e2fsck                groupadd            ipmaddr                      mkfs.ext3            pm-powersave         shutdown                usermod
arptables-nft          e2image               groupdel            ipsec                        mkfs.ext4            pm-suspend           slattach                v4l2-dbg
arptables-nft-restore  e2label               groupmems           iptables                     mkfs.minix           pm-suspend-hybrid    sshd                    validlocale
arptables-nft-save     e2mmpstatus           groupmod            iptables-apply               mkfs.ntfs            powerdebug           start-stop-daemon       vcstime
arptables-restore      e2scrub               grpck               iptables-legacy              mkhomedir_helper     poweroff             sudo_logsrvd            vigr
arptables-save         e2scrub_all           grpconv             iptables-legacy-restore      mkinitramfs          powertop             sudo_sendlog            vipw
badblocks              e2undo                grpunconv           iptables-legacy-save         mklost+found         pppd                 sulogin                 visudo
blkdeactivate          e4crypt               halt                iptables-nft                 mkntfs               pppdump              swaplabel               vpnc
blkdiscard             e4defrag              hwclock             iptables-nft-restore         mkswap               pppoe-discovery      swapoff                 vpnc-connect
blkid                  ebtables              i2cdetect           iptables-nft-save            modinfo              pppstats             swapon                  vpnc-disconnect
blkzone                ebtables-nft          i2cdump             iptables-restore             modprobe             pptp                 switch_root             wipefs
blockdev               ebtables-nft-restore  i2cget              iptables-restore-translate   mount.fuse           pptpsetup            synaptic                wpa_action
bluetoothd             ebtables-nft-save     i2cset              iptables-save                mount.lowntfs-3g     pwck                 sysctl                  wpa_cli
bridge                 ebtables-restore      i2c-stub-from-dump  iptables-translate           mount.ntfs           pwconv               system-tools-backends   wpa_supplicant
capsh                  ebtables-save         i2ctransfer         iptunnel                     mount.ntfs-3g        pwunconv             tarcat                  xfce4-pm-helper
cfdisk                 escapesrc             iconvconfig         irqbalance                   nameif               rarp                 tc                      xfpm-power-backlight-helper
cgdisk                 faillock              icupkg              isosize                      NetworkManager       raw                  telinit                 xl2tpd
chat                   fdformat              ifconfig            iw                           newusers             rcconf               th-cmd                  xl2tpd-control
chcpu                  fdisk                 ifdown              iwconfig                     nfnl_osf             readprofile          thd                     xtables-legacy-multi
chgpasswd              filefrag              ifquery             iwevent                      nologin              reboot               tipc                    xtables-monitor
chmem                  findfs                ifup                iwgetid                      ntfsclone            regdbdump            tune2fs                 xtables-nft-multi
chpasswd               fixparts              init                iwlist                       ntfscp               remove-shell         tzconfig                zic
chroot                 fsck                  insmod              iwpriv                       ntfslabel            resize2fs            umount.udisks2          zramctl
cpgr                   fsck.cramfs           insserv             iwspy                        ntfsresize           resolvconf           unix_chkpwd
cppw                   fsck.ext2             installkernel       kbdrate                      ntfsundelete         rfkill               unix_update
ctrlaltdel             fsck.ext3             invoke-rc.d         killall5                     ntpd                 rmmod                update-binfmts
debugfs                fsck.ext4             iotop               ldattach                     ntpdate              rmt                  update-ca-certificates
root@linaro-alip:/#
root@linaro-alip:/# ls
root@linaro-alip:/# ls bin
'['                                     dirmngr-client            kbdinfo                               pinentry                         timedatectl
 aarch64-linux-gnu-addr2line            dirname                   kbd_mode                              pinentry-curses                  timeout
 aarch64-linux-gnu-ar                   disk-helper               kbxutil                               ping                             tload
 aarch64-linux-gnu-as                   dmesg                     kernel-install                        ping4                            toe
 aarch64-linux-gnu-c++filt              dm-tool                   kill                                  ping6                            top
 aarch64-linux-gnu-cpp                  dnsdomainname             killall                               pinky                            touch
 aarch64-linux-gnu-cpp-10               domainname                kmod                                  pkaction                         tput
 aarch64-linux-gnu-dwp                  dpkg                      kmsgrab                               pkcheck                          tr
 aarch64-linux-gnu-elfedit              dpkg-architecture         kmstest                               pkexec                           trace-cmd
 aarch64-linux-gnu-g++                  dpkg-buildflags           koi8rxterm                            pkg-config                       tracker
 aarch64-linux-gnu-g++-10               dpkg-buildpackage         l2ping                                pkgdata                          transset
 aarch64-linux-gnu-gcc                  dpkg-checkbuilddeps       l2test                                pkill                            troff
 aarch64-linux-gnu-gcc-10               dpkg-deb                  last                                  pkttyagent                       true
 aarch64-linux-gnu-gcc-ar               dpkg-distaddfile          lastb                                 pl2pm                            truncate
 aarch64-linux-gnu-gcc-ar-10            dpkg-divert               lastlog                               play                             tset
 aarch64-linux-gnu-gcc-nm               dpkg-genbuildinfo         lcf                                   pldd                             tsort
 aarch64-linux-gnu-gcc-nm-10            dpkg-genchanges           ld                                    plog                             tty
 aarch64-linux-gnu-gcc-ranlib           dpkg-gencontrol           ld.bfd                                pmap                             tzselect
 aarch64-linux-gnu-gcc-ranlib-10        dpkg-gensymbols           ldd                                   pm-is-supported                  ucf
 aarch64-linux-gnu-gcov                 dpkg-maintscript-helper   ld.gold                               pod2html                         ucfq
 aarch64-linux-gnu-gcov-10              dpkg-mergechangelogs      less                                  pod2man                          ucfr
 aarch64-linux-gnu-gcov-dump            dpkg-name                 lessecho                              pod2text                         uconv
 aarch64-linux-gnu-gcov-dump-10         dpkg-parsechangelog       lessfile                              pod2usage                        ucs2any
 aarch64-linux-gnu-gcov-tool            dpkg-query                lesskey                               podchecker                       udevadm
 aarch64-linux-gnu-gcov-tool-10         dpkg-realpath             lesspipe                              poff                             udisksctl
 aarch64-linux-gnu-gold                 dpkg-scanpackages         lexgrog                               pon                              ul
 aarch64-linux-gnu-gprof                dpkg-scansources          libnetcfg                             POST                             ulockmgr_server
 aarch64-linux-gnu-ld                   dpkg-shlibdeps            libpng16-config                       power-key.sh                     umount
 aarch64-linux-gnu-ld.bfd               dpkg-source               libpng-config                         pr                               uname
 aarch64-linux-gnu-ld.gold              dpkg-split                lightdm-gtk-greeter-settings          preconv                          uncompress
 aarch64-linux-gnu-lto-dump-10          dpkg-statoverride         lightdm-gtk-greeter-settings-pkexec   printenv                         unexpand
 aarch64-linux-gnu-nm                   dpkg-trigger              link                                  printf                           unicode_start
 aarch64-linux-gnu-objcopy              dpkg-vendor               linux32                               prlimit                          unicode_stop
 aarch64-linux-gnu-objdump              du                        linux64                               prove                            uniq
 aarch64-linux-gnu-pkg-config           dumpkeys                  linux-check-removal                   prtstat                          unlink
 aarch64-linux-gnu-ranlib               dvb-fe-tool               linux-update-symlinks                 ps                               unlzma
 aarch64-linux-gnu-readelf              dvb-format-convert        linux-version                         psfaddtable                      unmkinitramfs
 aarch64-linux-gnu-size                 dvbv5-daemon              listres                               psfgettable                      unshare
 aarch64-linux-gnu-strings              dvbv5-scan                ln                                    psfstriptable                    unxz
 aarch64-linux-gnu-strip                dvbv5-zap                 lnstat                                psfxtable                        unzip
 aarch64-unknown-linux-gnu-pkg-config   dwp                       loadkeys                              pslog                            unzipsfx
 aconnect                               echo                      loadunimap                            pstree                           update
 acpi_listen                            editor                    locale                                pstree.x11                       update-alternatives
 adbd                                   editres                   localectl                             ptar                             update-desktop-database
 addpart                                egrep                     localedef                             ptardiff                         update-leap
 addr2line                              elfedit                   log2asc                               ptargrep                         update-mime-database
 alsabat                                enc2xs                    log2long                              ptx                              upgrade_tool
 alsaloop                               encguess                  logcat                                pulseaudio                       upower
 alsamixer                              env                       logger                                pwd                              uptime
 alsatplg                               eqn                       log-guardian                          pwdx                             usbdevice
 alsaucm                                evtest                    login                                 py3clean                         usb-devices
 amidi                                  ex                        loginctl                              py3compile                       usbhid-dump
 amixer                                 exo-desktop-item-edit     logname                               py3versions                      usbreset
 aplay                                  exo-open                  look                                  pydoc3                           users
 aplaymidi                              expand                    lowntfs-3g                            pydoc3.9                         users-admin
 appres                                 expiry                    ls                                    pygettext3                       user-setup
 apropos                                expr                      lsattr                                pygettext3.9                     utmpdump
 apt                                    factor                    lsblk                                 python3                          uxterm
 apt-cache                              faillog                   lsb_release                           python3.9                        v4l2-compliance
 apt-cdrom                              fallocate                 lscpu                                 qemu-aarch64-static              v4l2-ctl
 apt-config                             false                     lsinitramfs                           qv4l2                            v4l2-sysfs-path
 apt-extracttemplates                   fc-cache                  lsinput                               ranlib                           vdir
 apt-ftparchive                         fc-cat                    lsipc                                 rbash                            vendor_storage
 apt-get                                fc-conflist               lslocks                               rcconf                           vi
 apt-key                                fc-list                   lslogins                              rcp                              view
 apt-mark                               fc-match                  lsmem                                 rctest                           viewres
 apt-sortpkgs                           fc-pattern                lsmod                                 rdma                             vim
 ar                                     fc-query                  lsns                                  rds-ctl                          vim.basic
 arch                                   fc-scan                   lsof                                  readelf                          vimdiff
 arecord                                fc-validate               lspci                                 readlink                         vim.tiny
 arecordmidi                            fgconsole                 lspgpot                               realpath                         vimtutor
 as                                     fgrep                     lsusb                                 rec                              vmstat
 asc2log                                file                      lto-dump-10                           rendercheck                      vpu_api_test
 aseqdump                               fincore                   luit                                  renice                           w
 aseqnet                                find                      lwp-download                          reset                            wall
 async-commit                           findmnt                   lwp-dump                              resize                           watch
 atobm                                  flock                     lwp-mirror                            resize-helper                    watchgnupg
 awk                                    fmt                       lwp-request                           resizepart                       wayland-scanner
 axfer                                  fold                      lxterm                                resolvectl                       wc
 b2sum                                  fonttosfnt                lzcat                                 restart_rknn.sh                  wdctl
 base32                                 free                      lzcmp                                 rev                              wget
 base64                                 funzip                    lzdiff                                rfcomm                           whatis
 basename                               fuser                     lzegrep                               rgrep                            whereis
 basenc                                 fusermount                lzfgrep                               rhythmbox                        which
 bash                                   g++                       lzgrep                                rhythmbox-client                 whiptail
 bashbug                                g++-10                    lzless                                rkaiq_3A_server                  who
 bccmd                                  gapplication              lzma                                  rkaiq_tool_server                whoami
 bcmserver                              gatttool                  lzmainfo                              rknn_common_test                 wifi_ap6xxx_rftest.sh
 bdftopcf                               gcc                       lzmore                                rknn_server                      wifibt-bus
 bdftruncate                            gcc-10                    make                                  rk_wifibt_init                   wifibt-chip
 bitmap                                 gcc-ar                    makeconv                              rlogin                           wifibt-id
 blueman-adapters                       gcc-ar-10                 make-first-existing-target            rm                               wifibt-info
 blueman-applet                         gcc-nm                    man                                   rmdir                            wifibt-init.sh
 blueman-assistant                      gcc-nm-10                 mandb                                 routef                           wifibt-module
 blueman-manager                        gcc-ranlib                manpath                               routel                           wifibt-util.sh
 blueman-report                         gcc-ranlib-10             man-recode                            rpcgen                           wifibt-vendor
 blueman-sendto                         gcov                      mapscrn                               rsh                              wifi-connect.sh
 blueman-services                       gcov-10                   mawk                                  rstart                           wl
 blueman-tray                           gcov-dump                 mcookie                               rstartd                          wpa_passphrase
 bluemoon                               gcov-dump-10              md5sum                                rtk_hciattach                    write
 bluetoothctl                           gcov-tool                 md5sum.textutils                      rtlbtmp                          write.ul
 bmtoa                                  gcov-tool-10              media-ctl                             rtstat                           X
 bootanim                               gdbus                     memtester                             rtwpriv                          X11
 bootctl                                gdbus-codegen             mesg                                  runcon                           x11perf
 brcm_patchram_plus1                    gdk-pixbuf-csource        migrate-pubring-from-classic-gpg      run-parts                        x11perfcomp
 btattach                               gdk-pixbuf-pixdata        mkdir                                 rview                            xargs
 btmgmt                                 gdk-pixbuf-thumbnailer    mkfifo                                rvim                             xauth
 btmon                                  genbrk                    mkfontdir                             savelog                          xbiff
 bt-tty                                 gencat                    mkfontscale                           scp                              xcalc
 bunzip2                                gencfu                    mk_modmap                             screendump                       xclipboard
 busctl                                 gencnval                  mknod                                 script                           xclock
 busybox                                gendict                   mktemp                                scriptlive                       xcmsdb
 bwrap                                  generate_logs             modetest                              scriptreplay                     xconsole
 bzcat                                  genrb                     more                                  sdiff                            xcursorgen
 bzcmp                                  geqn                      mount                                 sdptool                          xcutsel
 bzdiff                                 GET                       mount-helper                          sed                              xdg-dbus-proxy
 bzegrep                                getconf                   mountpoint                            select-editor                    xdg-desktop-icon
 bzexe                                  get-edid                  mpi_dec_mt_test                       sensible-browser                 xdg-desktop-menu
 bzfgrep                                getent                    mpi_dec_multi_test                    sensible-editor                  xdg-email
 bzgrep                                 getkeycodes               mpi_dec_nt_test                       sensible-pager                   xdg-icon-resource
 bzip2                                  getopt                    mpi_dec_test                          seq                              xdg-mime
 bzip2recover                           gio                       mpi_enc_mt_test                       sessreg                          xdg-open
 bzless                                 gio-querymodules          mpi_enc_test                          setarch                          xdg-screensaver
 bzmore                                 git                       mpi_rc2_test                          setfont                          xdg-settings
 c++                                    git-receive-pack          mpp_info_test                         setkeycodes                      xditview
 c89                                    git-shell                 mpris-proxy                           setleds                          xdpyinfo
 c89-gcc                                git-upload-archive        mt                                    setlogcons                       xdriinfo
 c99                                    git-upload-pack           mt-gnu                                setmetamode                      xedit
 c99-gcc                                glib-compile-resources    multivideoplayer                      setpci                           xev
 cal                                    glib-compile-schemas      mv                                    setpriv                          xeyes
 calc_tickadj                           glib-genmarshal           namei                                 setsid                           xfce4-about
 canbusload                             glib-gettextize           nautilus                              setterm                          xfce4-accessibility-settings
 can-calc-bit-timing                    glib-mkenums              nautilus-autorun-software             setupcon                         xfce4-appearance-settings
 candump                                glmark2                   nawk                                  setvtrgb                         xfce4-appfinder
 canfdtest                              glmark2-drm               ncal                                  setxkbmap                        xfce4-color-settings
 cangen                                 glmark2-es2               neqn                                  sftp                             xfce4-display-settings
 cangw                                  glmark2-es2-drm           netstat                               sg                               xfce4-find-cursor
 canlogserver                           glmark2-es2-wayland       networkctl                            sh                               xfce4-keyboard-settings
 canplayer                              glmark2-wayland           newgrp                                sha1sum                          xfce4-mime-helper
 cansend                                glxdemo                   nice                                  sha224sum                        xfce4-mime-settings
 cansequence                            glxgears                  nisdomainname                         sha256sum                        xfce4-mouse-settings
 cansniffer                             glxheads                  nl                                    sha384sum                        xfce4-panel
 captoinfo                              glxinfo                   nm                                    sha512sum                        xfce4-popup-applicationsmenu
 cat                                    gmake                     nm-applet                             shares-admin                     xfce4-popup-directorymenu
 catchsegv                              gnome-www-browser         nmcli                                 shasum                           xfce4-popup-windowmenu
 catman                                 gobject-query             nm-connection-editor                  showconsolefont                  xfce4-power-manager
 cc                                     gold                      nm-online                             showkey                          xfce4-power-manager-settings
 cec-compliance                         gpasswd                   nmtui                                 showrgb                          xfce4-screenshooter
 cec-ctl                                gpg                       nmtui-connect                         shred                            xfce4-session
 cec-follower                           gpg-agent                 nmtui-edit                            shuf                             xfce4-session-logout
 c++filt                                gpgcompose                nmtui-hostname                        size                             xfce4-session-settings
 chage                                  gpgconf                   nohup                                 skill                            xfce4-settings-editor
 chardet                                gpg-connect-agent         nproc                                 slabtop                          xfce4-settings-manager
 chardetect                             gpgparsemail              npu-image.sh                          slcan_attach                     xfconf-query
 chattr                                 gpgsm                     npu_powerctrl                         slcand                           xfd
 chcon                                  gpgsplit                  npu_powerctrl_combine                 slcanpty                         xfdesktop
 cheese                                 gpgtar                    npu_transfer_proxy                    sleep                            xfdesktop-settings
 chfn                                   gpgv                      npu_upgrade                           slogin                           xfhelp4
 chgrp                                  gpg-wks-server            npu_upgrade_pcie                      smproxy                          xflock4
 chmod                                  gpg-zip                   npu_upgrade_pcie_combine              snice                            xfontsel
 choom                                  gpic                      nroff                                 soelim                           xfrun4
 chown                                  gprof                     nsenter                               sort                             xfsettingsd
 chromium                               grep                      nstat                                 sox                              xfwm4
 chrt                                   gresource                 ntfs-3g                               soxi                             xfwm4-settings
 chsh                                   groff                     ntfs-3g.probe                         speaker-test                     xfwm4-tweaks-settings
 chvt                                   grog                      ntfscat                               splain                           xfwm4-workspace-settings
 ciptool                                grops                     ntfscluster                           split                            xgamma
 cisco-decrypt                          grotty                    ntfscmp                               splitfont                        xgc
 ckbcomp                                groups                    ntfsdecrypt                           ss                               xhost
 cksum                                  gsettings                 ntfsfallocate                         ssh                              xinit
 clear                                  gst-device-monitor-1.0    ntfsfix                               ssh-add                          xkbbell
 clear_console                          gst-discoverer-1.0        ntfsinfo                              ssh-agent                        xkbcomp
 cmake                                  gst-inspect-1.0           ntfsls                                ssh-argv0                        xkbevd
 cmp                                    gst-launch-1.0            ntfsmove                              ssh-copy-id                      xkbprint
 codepage                               gst-play-1.0              ntfsrecover                           ssh-import-id                    xkbvleds
 col                                    gst-stats-1.0             ntfssecaudit                          ssh-import-id-gh                 xkbwatch
 colcrt                                 gst-tester-1.0            ntfstruncate                          ssh-import-id-lp                 xkeystone
 colrm                                  gst-transcoder-1.0        ntfsusermap                           ssh-keygen                       xkill
 column                                 gst-typefind-1.0          ntfswipe                              ssh-keyscan                      xload
 comm                                   gtbl                      ntpdc                                 startpar                         xlogo
 corelist                               gtester                   ntpq                                  start-pulseaudio-x11             xlsatoms
 cp                                     gtester-report            ntpsweep                              start_rknn.sh                    xlsclients
 cpack                                  gtf                       ntptrace                              startx                           xlsfonts
 cpan                                   gtk-builder-convert       numfmt                                startxfce4                       xmag
 cpan5.32-aarch64-linux-gnu             gtk-update-icon-cache     obconf                                stat                             xman
 cpio                                   gunzip                    obexctl                               stdbuf                           xmessage
 cpp                                    gzexe                     objcopy                               strace                           xmlcatalog
 cpp-10                                 gzip                      objdump                               strace-log-merge                 xmllint
 cpufreq-aperf                          h2ph                      oclock                                streamzip                        xmodmap
 cpufreq-info                           h2xs                      od                                    stress                           xmore
 cpufreq-set                            hardinfo                  odbcinst                              stressapptest                    Xorg
 c_rehash                               hciattach                 on_ac_power                           stress-ng                        xprop
 csplit                                 hciconfig                 open                                  strings                          xrandr
 ctest                                  hcitool                   opencv_annotation                     strip                            xrdb
 ctstat                                 hd                        opencv_interactive-calibration        stty                             xrefresh
 curl                                   head                      opencv_version                        su                               x-session-manager
 cut                                    HEAD                      opencv_visualisation                  sudo                             xset
 cvt                                    helpztags                 opencv_waldboost_detector             sudoedit                         xsetmode
 cvtsudoers                             hex2hcd                   openssl                               sudoreplay                       xsetpointer
 cx18-ctl                               hexdump                   openvt                                sum                              xsetroot
 dash                                   hostid                    orc-bugreport                         synaptic-pkexec                  xsm
 date                                   hostname                  orcc                                  sync                             xstdcmap
 dbus-cleanup-sockets                   hostnamectl               pacat                                 systemctl                        xsubpp
 dbus-daemon                            iceauth                   pacmd                                 systemd                          xterm
 dbus-launch                            ico                       pactl                                 systemd-analyze                  x-terminal-emulator
 dbus-monitor                           iconv                     padsp                                 systemd-ask-password             xvidtune
 dbus-run-session                       icuinfo                   pager                                 systemd-cat                      xvinfo
 dbus-send                              id                        pa-info                               systemd-cgls                     xwd
 dbus-update-activation-environment     iecset                    pamon                                 systemd-cgtop                    x-window-manager
 dbus-uuidgen                           infocmp                   pango-list                            systemd-delta                    xwininfo
 dd                                     infotocap                 pango-view                            systemd-detect-virt              xwud
 ddcmon                                 inotifywait               paplay                                systemd-escape                   x-www-browser
 deallocvt                              input-event-daemon        parec                                 systemd-hwdb                     xxd
 debconf                                input-events              parecord                              systemd-id128                    xz
 debconf-apt-progress                   input-kbd                 parse-edid                            systemd-inhibit                  xzcat
 debconf-communicate                    install                   partx                                 systemd-machine-id-setup         xzcmp
 debconf-copydb                         instmodsh                 passwd                                systemd-mount                    xzdiff
 debconf-escape                         io                        paste                                 systemd-notify                   xzegrep
 debconf-set-selections                 ionice                    pasuspender                           systemd-path                     xzfgrep
 debconf-show                           ip                        patch                                 systemd-resolve                  xzgrep
 deb-systemd-helper                     ipcmk                     pathchk                               systemd-run                      xzless
 deb-systemd-invoke                     ipcrm                     pavucontrol                           systemd-socket-activate          xzmore
 decode-dimms                           ipcs                      pax11publish                          systemd-stdio-bridge             yes
 decode-edid                            iperf                     pcf2vpnc                              systemd-sysusers                 ypdomainname
 decode_tm6000                          iptables-xml              pcre2-config                          systemd-tmpfiles                 zathura
 decode-vaio                            ir-ctl                    pcre-config                           systemd-tty-ask-password-agent   zcat
 delpart                                ir-keytable               pdb3                                  systemd-umount                   zcmp
 derb                                   ischroot                  pdb3.9                                tabs                             zdiff
 desktop-file-edit                      isotpdump                 peekfd                                tac                              zdump
 desktop-file-install                   isotpperf                 perf                                  tail                             zegrep
 desktop-file-validate                  isotprecv                 perl                                  tar                              zfgrep
 df                                     isotpsend                 perl5.32.1                            tasksel                          zforce
 dh_bash-completion                     isotpserver               perl5.32-aarch64-linux-gnu            taskset                          zgrep
 dhd                                    isotpsniffer              perlbug                               tbl                              zip
 dhd_priv                               isotptun                  perldoc                               tee                              zipcloak
 dh_gstscancodecs                       ivtv-ctl                  perlivp                               tempfile                         zipdetails
 dh_perl_openssl                        j1939acd                  perlthanks                            test                             zipgrep
 dh_xsf_substvars                       j1939cat                  pfc                                   testj1939                        zipinfo
 diff                                   j1939spy                  pgrep                                 thunar                           zipnote
 diff3                                  j1939sr                   pic                                   Thunar                           zipsplit
 dir                                    join                      piconv                                thunar-settings                  zless
 dircolors                              journalctl                pidof                                 tic                              zmore
 dirmngr                                json_pp                   pidwait                               time-admin                       znew
root@linaro-alip:/#
root@linaro-alip:/# ls
root@linaro-alip:/# ls sbin
accessdb               delgroup              fsck.minix          iotop-py                     ldconfig             ntpdate-debian       rmt-tar                 update-fonts-alias
acpid                  deluser               fsck.nfs            ip                           lightdm              ntp-keygen           route                   update-fonts-dir
addgnupghome           depmod                fsfreeze            ip6tables                    lightdm-gtk-greeter  ntptime              rsyslogd                update-fonts-scale
addgroup               devlink               fstab-decode        ip6tables-apply              locale-gen           ntp-wait             rtacct                  update-icon-caches
add-shell              dhclient              fstrim              ip6tables-legacy             logsave              on_ac_power          rtcwake                 update-initramfs
adduser                dhclient-script       gdisk               ip6tables-legacy-restore     losetup              openvpn              rtmon                   update-locale
agetty                 dmsetup               genccode            ip6tables-legacy-save        lsmod                pam-auth-update      runlevel                update-passwd
alsabat-test           dmstats               gencmn              ip6tables-nft                MAKEDEV              pam_getenv           runuser                 update-pciids
alsactl                dnsmasq               genl                ip6tables-nft-restore        mii-tool             pam_timestamp_check  service                 update-rcconf-guide
alsa-info              dpkg-fsys-usrunmess   gennorm2            ip6tables-nft-save           mke2fs               parted               setcap                  update-rc.d
anacron                dpkg-preconfigure     gensprep            ip6tables-restore            mkfs                 partprobe            setvesablank            usb_modeswitch
applygnupgdefaults     dpkg-reconfigure      getcap              ip6tables-restore-translate  mkfs.bfs             pivot_root           sfdisk                  usb_modeswitch_dispatcher
arp                    dumpe2fs              getpcaps            ip6tables-save               mkfs.cramfs          plipconfig           sgdisk                  useradd
arpd                   e2freefrag            getty               ip6tables-translate          mkfs.ext2            pm-hibernate         shadowconfig            userdel
arptables              e2fsck                groupadd            ipmaddr                      mkfs.ext3            pm-powersave         shutdown                usermod
arptables-nft          e2image               groupdel            ipsec                        mkfs.ext4            pm-suspend           slattach                v4l2-dbg
arptables-nft-restore  e2label               groupmems           iptables                     mkfs.minix           pm-suspend-hybrid    sshd                    validlocale
arptables-nft-save     e2mmpstatus           groupmod            iptables-apply               mkfs.ntfs            powerdebug           start-stop-daemon       vcstime
arptables-restore      e2scrub               grpck               iptables-legacy              mkhomedir_helper     poweroff             sudo_logsrvd            vigr
arptables-save         e2scrub_all           grpconv             iptables-legacy-restore      mkinitramfs          powertop             sudo_sendlog            vipw
badblocks              e2undo                grpunconv           iptables-legacy-save         mklost+found         pppd                 sulogin                 visudo
blkdeactivate          e4crypt               halt                iptables-nft                 mkntfs               pppdump              swaplabel               vpnc
blkdiscard             e4defrag              hwclock             iptables-nft-restore         mkswap               pppoe-discovery      swapoff                 vpnc-connect
blkid                  ebtables              i2cdetect           iptables-nft-save            modinfo              pppstats             swapon                  vpnc-disconnect
blkzone                ebtables-nft          i2cdump             iptables-restore             modprobe             pptp                 switch_root             wipefs
blockdev               ebtables-nft-restore  i2cget              iptables-restore-translate   mount.fuse           pptpsetup            synaptic                wpa_action
bluetoothd             ebtables-nft-save     i2cset              iptables-save                mount.lowntfs-3g     pwck                 sysctl                  wpa_cli
bridge                 ebtables-restore      i2c-stub-from-dump  iptables-translate           mount.ntfs           pwconv               system-tools-backends   wpa_supplicant
capsh                  ebtables-save         i2ctransfer         iptunnel                     mount.ntfs-3g        pwunconv             tarcat                  xfce4-pm-helper
cfdisk                 escapesrc             iconvconfig         irqbalance                   nameif               rarp                 tc                      xfpm-power-backlight-helper
cgdisk                 faillock              icupkg              isosize                      NetworkManager       raw                  telinit                 xl2tpd
chat                   fdformat              ifconfig            iw                           newusers             rcconf               th-cmd                  xl2tpd-control
chcpu                  fdisk                 ifdown              iwconfig                     nfnl_osf             readprofile          thd                     xtables-legacy-multi
chgpasswd              filefrag              ifquery             iwevent                      nologin              reboot               tipc                    xtables-monitor
chmem                  findfs                ifup                iwgetid                      ntfsclone            regdbdump            tune2fs                 xtables-nft-multi
chpasswd               fixparts              init                iwlist                       ntfscp               remove-shell         tzconfig                zic
chroot                 fsck                  insmod              iwpriv                       ntfslabel            resize2fs            umount.udisks2          zramctl
cpgr                   fsck.cramfs           insserv             iwspy                        ntfsresize           resolvconf           unix_chkpwd
cppw                   fsck.ext2             installkernel       kbdrate                      ntfsundelete         rfkill               unix_update
ctrlaltdel             fsck.ext3             invoke-rc.d         killall5                     ntpd                 rmmod                update-binfmts
debugfs                fsck.ext4             iotop               ldattach                     ntpdate              rmt                  update-ca-certificates
```