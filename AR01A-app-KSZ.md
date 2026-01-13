[AR01A](AR01A.md) 
```c
# cd /
# ls
bin      lib      media    proc     run      tmp
dev      lib32    mnt      ptp      sbin     usr
etc      linuxrc  opt      root     sys      var
# ls bin
ash            dumpkmap       ln             ping           stty
busybox        echo           login          ping6          su
cat            egrep          ls             pipe_progress  swcfg
catv           false          mkdir          printenv       sync
chgrp          fdflush        mknod          ps             tar
chmod          fgrep          mktemp         pwd            touch
chown          getopt         more           rm             true
cp             grep           mount          rmdir          umount
cpio           gunzip         mountpoint     run-parts      uname
date           gzip           mt             sed            usleep
dd             hostname       mv             setarch        vi
df             kill           netstat        setserial      watch
dmesg          linux32        nice           sh             zcat
dnsdomainname  linux64        pidof          sleep
# ls sbin/
arp                hdparm             ldconfig           runlevel
blkid              hwclock            loadkmap           setconsole
devmem             ifconfig           losetup            start-stop-daemon
dosfsck            ifdown             lsmod              sulogin
fdisk              ifup               makedevs           swapoff
freeramdisk        init               mdev               swapon
fsck.fat           insmod             mkswap             switch_root
fsck.msdos         ip                 modprobe           sysctl
fsck.vfat          ipaddr             nameif             syslogd
fstrim             iplink             pivot_root         udhcpc
fw_printenv        iproute            poweroff           uevent
fw_setenv          iprule             reboot             vconfig
getty              iptunnel           rmmod              watchdog
halt               klogd              route
# ls usr/bin
[             find          logname       python2.7     tr
[[            flock         lsof          readlink      traceroute
ar            fold          lspci         realpath      truncate
awk           free          lsusb         renice        tty
basename      ftpget        lzcat         reset         uniq
bunzip2       ftpput        lzma          resize        unix2dos
bzcat         fuser         makeweb       seq           unlink
chrt          getconf       md5sum        setkeycodes   unlzma
chvt          head          mesg          setsid        unxz
cksum         hexdump       microcom      sha1sum       unzip
clear         hostid        mkfifo        sha256sum     uptime
cmp           htpasswd      mkpasswd      sha3sum       uudecode
crontab       iconv         nohup         sha512sum     uuencode
cut           id            nslookup      sort          vlock
dc            install       nuttcp        strings       wc
deallocvt     ipcrm         od            syslogtocern  wget
diff          ipcs          openvt        tail          which
dirname       iperf3        passwd        tee           who
dos2unix      killall       patch         telnet        whoami
du            last          printf        test          xargs
eject         ldd           ptp           tftp          xz
env           less          python        time          xzcat
expr          logger        python2       top           yes
# ls usr/sbin
addgroup        e2undo          i2cget          pmc
adduser         e4crypt         i2cset          ptp4l
arping          ether-wake      inetd           ptp_cli
authen          ethtool         killall5        rdate
brctl           fbset           kszsw           readprofile
chroot          fdformat        l               regs_bin
crond           fsck            loadfont        setlogcons
delgroup        fsck.ext2       mdio-tool       t
deluser         fsck.ext3       mrpd            tcpdump
dlr_daemon      fsck.ext4       mrpl            telnetd
dnsd            fsck.ext4dev    mrpq            thttpd
dumpe2fs        hwstamp_ctl     nettest         thttpd_wrapper
e2fsck          i2cdetect       phc2sys         ubirename
e2label         i2cdump         phc_ctl
# ls ptp/
Makefile  e2e       phc.sh    power.sh
avb       p2p       power     rstp
# ls ptp/e2e/
default.cfg  linuxptp.sh  tc

# ls /dev
bus                 null                tty37
console             pps0                tty38
cpu_dma_latency     ptmx                tty39
full                ptp0                tty4
i2c-0               ptp_dev             tty40
i2c-1               ptp_event           tty41
i2c-2               pts                 tty42
iio:device0         ptyp0               tty43
input               ptyp1               tty44
kmem                ptyp2               tty45
kmsg                ptyp3               tty46
log                 ram0                tty47
loop-control        ram1                tty48
loop0               ram2                tty49
loop1               ram3                tty5
loop2               random              tty50
loop3               rtc0                tty51
loop4               shm                 tty52
loop5               snd                 tty53
loop6               sw_dev              tty54
loop7               tty                 tty55
mem                 tty0                tty56
memory_bandwidth    tty1                tty57
mtd0                tty10               tty58
mtd0ro              tty11               tty59
mtd1                tty12               tty6
mtd1ro              tty13               tty60
mtd2                tty14               tty61
mtd2ro              tty15               tty62
mtd3                tty16               tty63
mtd3ro              tty17               tty7
mtd4                tty18               tty8
mtd4ro              tty19               tty9
mtd5                tty2                ttyGS0
mtd5ro              tty20               ttyS0
mtd6                tty21               ttyS1
mtd6ro              tty22               ttyS2
mtd7                tty23               ttyS5
mtd7ro              tty24               ttyp0
mtd8                tty25               ttyp1
mtd8ro              tty26               ttyp2
mtdblock0           tty27               ttyp3
mtdblock1           tty28               ubi0
mtdblock2           tty29               ubi0_0
mtdblock3           tty3                ubi_ctrl
mtdblock4           tty30               urandom
mtdblock5           tty31               vcs
mtdblock6           tty32               vcs1
mtdblock7           tty33               vcsa
mtdblock8           tty34               vcsa1
network_latency     tty35               zero
network_throughput  tty36

```
```c
# cd /sys/class/net/
# ls
can0      eth0.100  eth0.102  eth0.104  lo
eth0      eth0.101  eth0.103  eth0.105  sit0
# cd eth0
# ls
addr_assign_type  duplex            phys_port_id      sw1
addr_len          flags             power             sw2
address           ifalias           ptpfs             sw3
broadcast         ifindex           queues            sw4
carrier           iflink            registers         sw5
carrier_changes   link_mode         speed             sw6
dev_id            mtu               statistics        tx_queue_len
dev_port          name_assign_type  subsystem         type
device            netdev_group      sw                uevent
dormant           operstate         sw0
# cd ../eth0.100
# ls
addr_assign_type  dev_port          link_mode         queues
addr_len          dormant           mtu               speed
address           duplex            name_assign_type  statistics
broadcast         flags             netdev_group      subsystem
carrier           ifalias           operstate         tx_queue_len
carrier_changes   ifindex           phys_port_id      type
dev_id            iflink            power             uevent
# cd ../eth0.101
# ls
addr_assign_type  dev_port          link_mode         queues
addr_len          dormant           mtu               speed
address           duplex            name_assign_type  statistics
broadcast         flags             netdev_group      subsystem
carrier           ifalias           operstate         tx_queue_len
carrier_changes   ifindex           phys_port_id      type
dev_id            iflink            power             uevent
```
```c
# cd ../eth0/sw
# ls
aggr_backoff       fair_flow_ctrl     mcast_storm        stp_version
aging              fast_aging         mib                sw_flow_ctrl
alu_addr           features           mirror_mode        sw_half_duplex
alu_dst            fid2mstid          mrp_src_addr       two_dev
alu_fid            flow_ctrl          msrpEnabled        tx_queue_based
alu_index          force              msrp_info          unk_mcast_fwd
alu_info           host_port          msrp_sr_a          unk_mcast_ports
alu_mstp           hsr                mtu                unk_ucast_fwd
alu_override       hsr_addr           no_color           unk_ucast_ports
alu_ports          hsr_age_cnt        no_exc_drop        unk_vid_fwd
alu_prio           hsr_index          null_vid           unk_vid_ports
alu_src            hsr_info           overrides          version
alu_type           hsr_net_id         p_802_1p_map       vid
alu_use_fid        hsr_path_id        pass_pause         vid2fid
alu_valid          hsr_redbox_id      pme                vlan
authen             hsr_state          pme_polarity       vlan_bound
avb                hsr_table          ports              vlan_fid
back_pressure      hsr_valid          reg                vlan_index
bcast_per          igmp_snoop         speed              vlan_info
color_green        info               static_table       vlan_mstp
color_red          ipv6_mld_option    stp                vlan_option
color_yellow       ipv6_mld_snoop     stp_br_fwd_delay   vlan_ports
dev_start          isp                stp_br_hello_time  vlan_prio
diffserv_map       jumbo_packet       stp_br_info        vlan_start
double_tag         legal_packet       stp_br_max_age     vlan_table
drop_inv_vid       length_check       stp_br_on          vlan_untag
duplex             link_aging         stp_br_prio        vlan_valid
dynamic_table      macaddr            stp_br_tx_hold
# cat info
duplex:         0 for auto; set to 1 for half-duplex; 2, full-duplex
speed:          0 for auto; set to 10 or 100
force:          set to 1 to force link to specific speed setting
flow_ctrl:      set to 0 to disable flow control
mib:            display the MIB table

dynamic_table:  display the switch's dynamic MAC table
static_table:   display the switch's static MAC table
vlan_table:     display the switch's VLAN table

aging:          disable/enable aging
fast_aging:     disable/enable fast aging
link_aging:     disable/enable link change auto aging

bcast_per:      set broadcast storm percentage
mcast_storm:    disable multicast storm protection
diffserv_map:   set DiffServ value.  Use "decimal=hexadecimal" format
p_802_1p_map:   set 802.1p value.  Use "decimal=hexadecimal" format

vlan:           disable/enable 802.1Q VLAN
null_vid:       set to 1 to replace null vid
macaddr:        set switch MAC address
mirror_mode:    set to 1 to use mirror rx AND tx mode

igmp_snoop:     disable/enable IGMP snooping
ipv6_mld_snoop: disable/enable IPv6 MLD snooping
ipv6_mld_option:disable/enable IPv6 MLD option snooping

aggr_backoff:   disable/enable aggressive backoff in half-duplex mode
no_exc_drop:    disable/enable no excessive collision drop
buf_reserve:    disable/enable buffer reserve

huge_packet:    disable/enable huge packet support
legal_packet:   disable/enable legal packet
length_check:   disable/enable legal packet length check

back_pressure:  set back pressure mode
sw_flow_ctrl:   disable/enable switch host port flow control
sw_half_duplex: disable/enable switch host port half-duplex mode
rx_flow_ctrl:   disable/enable receive flow control
tx_flow_ctrl:   disable/enable transmit flow control
fair_flow_ctrl: disable/enable fair flow control mode
vlan_bound:     disable/enable unicast VLAN boundary
pass_pause:     set to 1 to pass PAUSE frames for debugging

switch port settings:
duplex:         display the port's duplex setting
speed:          display the port's link speed
linkmd:         write to start LinkMD test.  read for result
mib:            display the port's MIB table
vid:            set default VID value
member:         set VLAN membership
bcast_storm:    disable/enable broadcast storm protection
diffserv:       disable/enable DiffServ priority
p_802_1p:       disable/enable 802.1p priority
port_based:     disable/enable port-based priority
prio_queue:     disable/enable priority queue
tx_p0_ctrl:     set priority queue 0 control
tx_p1_ctrl:     set priority queue 1 control
tx_p2_ctrl:     set priority queue 2 control
tx_p3_ctrl:     set priority queue 3 control
tx_p0_ratio:    set priority queue 0 ratio
tx_p1_ratio:    set priority queue 1 ratio
tx_p2_ratio:    set priority queue 2 ratio
tx_p3_ratio:    set priority queue 3 ratio
prio_rate:      disable/enable priority queue rate limiting
rx_limit:       set rx rate limiting mode
cnt_ifg:        set to 1 to count IPG
cnt_pre:        set to 1 to count preamble
rx_p0_rate:     set rx priority queue 0 rate in 64Kbps unit
rx_p1_rate:     set rx priority queue 1 rate in 64Kbps unit
rx_p2_rate:     set rx priority queue 2 rate in 64Kbps unit
rx_p3_rate:     set rx priority queue 3 rate in 64Kbps unit
tx_p0_rate:     set tx priority queue 0 rate in 64Kbps unit
tx_p1_rate:     set tx priority queue 1 rate in 64Kbps unit
tx_p2_rate:     set tx priority queue 2 rate in 64Kbps unit
tx_p3_rate:     set tx priority queue 3 rate in 64Kbps unit

pass_all:       set to 1 to pass all frames for debugging
tail_tag:       disable/enable tail tagging
rx:             disable/enable rx
tx:             disable/enable tx
learn:          disable/enable learning
mirror_port:    disable/enable mirror port
mirror_rx:      disable/enable mirror receive
mirror_tx:      disable/enable mirror transmit

non_vid:        set to 1 to discard non-VID packets
ingress:        disable/enable ingress VLAN filtering
drop_tagged:    disable/enable drop tagged packet feature
replace_prio:   disable/enable replace 802.1p priority feature
back_pressure:  disable/enable back pressure in half-duplex mode
force_flow_ctrl:set to 1 to force flow control

macaddr:        set port MAC address

static MAC table:
addr:           set MAC address
ports:          set destination ports
override:       set override bit
use_fid:        set use FID bit
fid:            set FID
valid:          set valid bit and write to table

VLAN table:
vid:            set VID
fid:            set FID
member:         set membership
valid:          set valid bit and write to table
#
# cd ../sw0
# ls
0_acl                    0_mib                    0_rx
0_acl_act                0_mirror_port            0_rx_flow_ctrl
0_acl_act_index          0_mirror_rx              0_rx_p0_rate
0_acl_addr               0_mirror_tx              0_rx_p1_rate
0_acl_cnt                0_mmd_id                 0_rx_p2_rate
0_acl_enable             0_mmd_reg                0_rx_p3_rate
0_acl_equal              0_mmd_val                0_rx_p4_rate
0_acl_first_rule         0_mmrpEnabled            0_rx_p5_rate
0_acl_index              0_mmrp_mac               0_rx_p6_rate
0_acl_info               0_mmrp_reg               0_rx_p7_rate
0_acl_intr_mode          0_mmrp_svc               0_rx_prio_rate
0_acl_ip_addr            0_msrpEnabled            0_speed
0_acl_ip_mask            0_mstp                   0_sqi
0_acl_map_mode           0_mvrpEnabled            0_sr_0_boundary
0_acl_max_port           0_mvrp_reg               0_sr_0_rx_prio
0_acl_min_port           0_mvrp_vid               0_sr_0_tx_prio
0_acl_mode               0_non_dscp_color         0_sr_1_boundary
0_acl_msec               0_non_vid                0_sr_1_rx_prio
0_acl_port_mode          0_p_802_1p               0_sr_1_tx_prio
0_acl_ports              0_p_index                0_sr_1_type
0_acl_prio               0_pass_all               0_sr_1_vid
0_acl_prio_mode          0_phy_loopback           0_sr_2_type
0_acl_protocol           0_pme_ctrl               0_sr_2_vid
0_acl_rule_index         0_pme_status             0_src_addr_filter
0_acl_ruleset            0_police                 0_srp
0_acl_seqnum             0_police_drop_all        0_stp_admin_edge
0_acl_src                0_police_port_based      0_stp_admin_p2p
0_acl_table              0_police_type            0_stp_admin_path_cost
0_acl_tcp_flag           0_port_prio              0_stp_auto_edge
0_acl_tcp_flag_enable    0_power                  0_stp_info
0_acl_tcp_flag_mask      0_prio_acl               0_stp_mcheck
0_acl_type               0_prio_highest           0_stp_on
0_acl_vlan_prio          0_prio_mac               0_stp_path_cost
0_acl_vlan_prio_replace  0_prio_or                0_stp_prio
0_asCapable              0_prio_queue             0_tail_tag
0_authen_mode            0_prio_vlan              0_tc_map
0_back_pressure          0_q_admin_slope          0_tx
0_bcast_storm            0_q_alg                  0_tx_flow_ctrl
0_color_aware            0_q_cbs                  0_tx_prio_rate
0_color_map              0_q_cir                  0_tx_q0_rate
0_color_mark             0_q_credit_hi            0_tx_q1_rate
0_color_remap            0_q_credit_incr          0_tx_q2_rate
0_cust_vid               0_q_credit_lo            0_tx_q3_rate
0_diffserv               0_q_delta                0_vid
0_drop_non_vlan          0_q_index                0_vlan_lookup_0
0_drop_srp               0_q_oper_slope           0_vlan_restricted
0_drop_tagged            0_q_pbs                  0_vlan_untagged
0_duplex                 0_q_pir                  0_wred_avg_size
0_force_flow_ctrl        0_q_scheduling           0_wred_drop_all
0_ingress                0_q_shaping              0_wred_drop_gyr
0_learn                  0_q_tx_ratio             0_wred_drop_r
0_limit                  0_qm_burst               0_wred_drop_yr
0_limit_cnt_ifg          0_qm_drop                0_wred_max
0_limit_cnt_pre          0_qm_hi                  0_wred_min
0_limit_flow_ctrl        0_qm_lo                  0_wred_multiplier
0_limit_packet_based     0_qm_resv_space          0_wred_q_avg_size
0_limit_port_based       0_qm_tx_avail            0_wred_q_max
0_linkmd                 0_qm_tx_calc             0_wred_q_min
0_mac_802_1x             0_qm_tx_used             0_wred_q_multiplier
0_mac_loopback           0_remote_loopback        0_wred_q_pmon
0_mac_oper               0_replace_prio           0_wred_random_drop
0_member                 0_replace_vid
#

```
```c
# cd /sys/class/net/
# ls -al
total 0
drwxr-xr-x    2 root     root             0 Feb 13 07:03 .
drwxr-xr-x   36 root     root             0 Feb 13 07:03 ..
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 can0 -> ../../devices/ahb/ahb:apb/f000c000.can/net/can0
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0 -> ../../devices/ahb/ahb:apb/f0028000.ethernet/net/eth0
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.100 -> ../../devices/virtual/net/eth0.100
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.101 -> ../../devices/virtual/net/eth0.101
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.102 -> ../../devices/virtual/net/eth0.102
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.103 -> ../../devices/virtual/net/eth0.103
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.104 -> ../../devices/virtual/net/eth0.104
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 eth0.105 -> ../../devices/virtual/net/eth0.105
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 lo -> ../../devices/virtual/net/lo
lrwxrwxrwx    1 root     root             0 Feb 13 07:03 sit0 -> ../../devices/virtual/net/sit0

```