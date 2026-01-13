[x86](../../../x86.md)  

```c
# Enhanced root filesystem creation with proper casper support
create_rootfs_smart() {
    local skip_create=false
    
    # Check if we can use cached rootfs
    if check_rootfs_cache && restore_rootfs_from_cache; then
        log_info "Successfully using cached rootfs"
        skip_create=true
    else
        log_info "No rootfs cache available, need to create"
        skip_create=false
    fi
    
    # If creation is needed
    if [ "$skip_create" = false ]; then
        log_info "Creating Ubuntu Base root filesystem..."
        cd "$WORK_DIR"
        
        # Use cache to speed up debootstrap
        local debootstrap_cache="/var/cache/debootstrap"
        if [ -d "$debootstrap_cache" ]; then
            log_info "Using debootstrap cache to speed up..."
            sudo debootstrap --cache-dir="$debootstrap_cache" "$UBUNTU_VERSION" ./rootfs http://archive.ubuntu.com/ubuntu/
        else
            sudo debootstrap "$UBUNTU_VERSION" ./rootfs http://archive.ubuntu.com/ubuntu/
        fi

        log_info "Configuring base system with enhanced casper support..."
        cat > chroot_setup.sh << 'EOF'
#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

# Set hostname
echo "custom-ubuntu" > /etc/hostname

# Set basic hosts file
cat > /etc/hosts << HOSTS_EOF
127.0.0.1 localhost
127.0.1.1 custom-ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
HOSTS_EOF

# Update package lists
apt update

# Install essential system packages
apt install -y systemd-sysv initramfs-tools sudo bash-completion nano less
apt install -y grub2-common grub-pc-bin
apt install -y casper lupin-casper discover
apt install -y net-tools iputils-ping curl wget
apt install -y udev dbus kmod dmsetup lvm2
apt install -y busybox-static  # CRITICAL: Ensure busybox with switch_root is installed
apt install -y fuse overlayfs-tools
apt install -y dosfstools mtools
apt install -y locales

# Install additional utilities and casper dependencies
apt install -y pciutils usbutils lsb-release
apt install -y python3
apt install -y rsync
apt install -y user-setup
apt install -y archdetect-deb
apt install -y live-boot
apt install -y live-boot-initramfs-tools
apt install -y live-tools

# Install network support
apt install -y network-manager
apt install -y wireless-tools
apt install -y wpasupplicant

# CRITICAL: Verify busybox provides switch_root
if ! busybox --list | grep -q switch_root; then
    echo "WARNING: busybox does not include switch_root, installing klibc-utils"
    apt install -y klibc-utils
fi

# CRITICAL FIX: Ensure casper scripts are properly installed and configured
apt install -y --reinstall casper

# Set root password
echo "root:ubuntu" | chpasswd

# Create normal user
useradd -m -s /bin/bash -G sudo user
echo "user:user" | chpasswd

# Configure network
systemctl enable systemd-networkd

# Configure initramfs for live CD with casper hooks
cat > /etc/initramfs-tools/initramfs.conf << INITRAMFS_EOF
MODULES=most
BUSYBOX=y
COMPRESS=gzip
DEVICE=
NFSROOT=auto
BOOT=local
KEYMAP=n
COMPCACHE_SIZE=10%
INITRAMFS_EOF

# Create casper configuration
mkdir -p /etc/casper
echo "custom-ubuntu" > /etc/casper.conf
echo "boot=casper" >> /etc/casper.conf

# Clean up
apt clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Generate locales
locale-gen en_US.UTF-8

echo "Base system configuration completed successfully"
EOF
        
        sudo cp chroot_setup.sh rootfs/
        sudo chmod +x rootfs/chroot_setup.sh
        sudo chroot rootfs /chroot_setup.sh
        sudo rm rootfs/chroot_setup.sh
        
        # Save to cache
        save_rootfs_cache
        
        log_info "Root filesystem creation completed"
    else
        log_info "Using existing rootfs cache"
    fi
}

# Advanced casper initramfs with switch_root fix as fallback
create_advanced_casper_initramfs_with_fix() {
    log_info "Creating advanced casper initramfs with built-in switch_root fix..."
    cd "$WORK_DIR"
    
    local temp_dir=$(mktemp -d)
    
    # Create complete directory structure
    mkdir -p "$temp_dir"/{bin,dev,etc/init.d,lib,lib64,mnt/root,proc,root,sbin,sys,cdrom,rootfs,run,scripts,usr/lib/klibc/bin}
    
    # Copy busybox from rootfs if available
    if [ -f "rootfs/bin/busybox" ]; then
        cp "rootfs/bin/busybox" "$temp_dir/bin/"
        chmod +x "$temp_dir/bin/busybox"
        # Create symlinks
        cd "$temp_dir/bin"
        for cmd in sh mount umount ls mkdir rmdir cp mv rm cat echo sleep losetup blkid find grep sed awk switch_root; do
            ln -s busybox $cmd 2>/dev/null || true
        done
        cd "$WORK_DIR"
        
        # Also create switch_root in klibc location for compatibility
        mkdir -p "$temp_dir/usr/lib/klibc/bin"
        ln -sf /bin/busybox "$temp_dir/usr/lib/klibc/bin/switch_root"
    else
        log_warn "busybox not found in rootfs, trying to use system busybox"
        if command -v busybox >/dev/null 2>&1; then
            cp $(command -v busybox) "$temp_dir/bin/busybox"
            chmod +x "$temp_dir/bin/busybox"
            cd "$temp_dir/bin"
            for cmd in sh mount umount ls mkdir rmdir cp mv rm cat echo sleep losetup blkid find grep sed awk switch_root; do
                ln -s busybox $cmd 2>/dev/null || true
            done
            cd "$WORK_DIR"
            mkdir -p "$temp_dir/usr/lib/klibc/bin"
            ln -sf /bin/busybox "$temp_dir/usr/lib/klibc/bin/switch_root"
        else
            log_error "busybox not available, cannot create initramfs"
            rm -rf "$temp_dir"
            exit 1
        fi
    fi
    
    # Create device nodes
    sudo mknod "$temp_dir/dev/console" c 5 1 2>/dev/null || true
    sudo mknod "$temp_dir/dev/null" c 1 3 2>/dev/null || true
    sudo mknod "$temp_dir/dev/sr0" b 11 0 2>/dev/null || true
    sudo mknod "$temp_dir/dev/sr1" b 11 1 2>/dev/null || true
    sudo mknod "$temp_dir/dev/loop0" b 7 0 2>/dev/null || true
    sudo mknod "$temp_dir/dev/loop1" b 7 1 2>/dev/null || true
    
    # Create the main init script that handles casper boot with switch_root fix
    cat > "$temp_dir/init" << 'ADVANCED_CASPER_INIT_FIX_EOF'
#!/bin/sh
export PATH=/bin:/sbin:/usr/bin:/usr/sbin

# Mount essential filesystems
mount -t proc proc /proc
mount -t sysfs sysfs /sys
mount -t devtmpfs devtmpfs /dev
mkdir -p /dev/pts
mount -t devpts devpts /dev/pts

echo "=== Custom Ubuntu Live Environment ==="
echo "Advanced Casper initramfs with switch_root fix booting..."

# Load necessary modules if available
[ -d /lib/modules ] && for module in loop squashfs overlay; do
    insmod /lib/modules/*/kernel/drivers/block/loop.ko 2>/dev/null
    insmod /lib/modules/*/kernel/fs/squashfs/squashfs.ko 2>/dev/null
    insmod /lib/modules/*/kernel/fs/overlayfs/overlay.ko 2>/dev/null
done

# Wait for devices to settle
echo "Waiting for devices to settle..."
sleep 3

# Try to probe CDROM devices
echo "Probing for CDROM devices..."
for i in 0 1 2 3; do
    mknod /dev/sr$i b 11 $i 2>/dev/null || true
done

# Try to mount CDROM with multiple attempts
echo "Attempting to mount CDROM..."
CD_DEVICE=""
for device in /dev/sr0 /dev/sr1 /dev/sr2 /dev/sr3 /dev/cdrom; do
    if [ -b "$device" ]; then
        echo "Found block device: $device"
        if mount -t iso9660 -o ro "$device" /cdrom 2>/dev/null; then
            echo "Successfully mounted CDROM from $device"
            CD_DEVICE="$device"
            break
        else
            echo "Failed to mount $device, trying udf..."
            if mount -t udf -o ro "$device" /cdrom 2>/dev/null; then
                echo "Successfully mounted UDF from $device"
                CD_DEVICE="$device"
                break
            fi
        fi
    fi
done

if [ -z "$CD_DEVICE" ]; then
    echo "ERROR: Could not mount any CDROM device"
    echo "Available block devices:"
    ls -la /dev/sd* /dev/sr* /dev/loop* 2>/dev/null || echo "Cannot list devices"
    echo "Starting recovery shell..."
    exec /bin/sh
fi

# Check for casper files
echo "Looking for casper filesystem..."
if [ ! -f "/cdrom/casper/filesystem.squashfs" ]; then
    echo "ERROR: Could not find filesystem.squashfs"
    echo "CDROM contents:"
    ls -la /cdrom/ 2>/dev/null || echo "Cannot list CDROM"
    echo "Starting recovery shell..."
    exec /bin/sh
fi

# Mount the root filesystem
echo "Mounting root filesystem..."
mkdir -p /rootfs
if mount -t squashfs -o loop /cdrom/casper/filesystem.squashfs /rootfs 2>/dev/null; then
    echo "Successfully mounted root filesystem"
else
    echo "ERROR: Failed to mount squashfs"
    exec /bin/sh
fi

# Check if switch_root is available
echo "Checking for switch_root..."
if command -v switch_root >/dev/null 2>&1; then
    echo "switch_root found at: $(command -v switch_root)"
    SWITCH_ROOT_CMD="switch_root"
elif [ -f "/usr/lib/klibc/bin/switch_root" ]; then
    echo "switch_root found at: /usr/lib/klibc/bin/switch_root"
    SWITCH_ROOT_CMD="/usr/lib/klibc/bin/switch_root"
else
    echo "switch_root not found, checking busybox..."
    if busybox --list | grep -q switch_root; then
        echo "switch_root available via busybox"
        SWITCH_ROOT_CMD="busybox switch_root"
    else
        echo "switch_root not available, using fallback to chroot"
        SWITCH_ROOT_CMD="chroot_fallback"
    fi
fi

# Clean up and switch to new root
echo "Switching to root filesystem..."

if [ "$SWITCH_ROOT_CMD" = "chroot_fallback" ]; then
    echo "Using chroot fallback method..."
    # Mount necessary filesystems for chroot
    mount --move /proc /rootfs/proc
    mount --move /sys /rootfs/sys
    mount --move /dev /rootfs/dev
    
    # Try to execute init in the new root
    echo "Executing init via chroot..."
    exec chroot /rootfs /sbin/init
else
    echo "Using switch_root method with: $SWITCH_ROOT_CMD"
    # Clean up mounts
    umount /cdrom 2>/dev/null || true
    umount /proc 2>/dev/null || true
    umount /sys 2>/dev/null || true
    umount /dev/pts 2>/dev/null || true
    umount /dev 2>/dev/null || true
    
    # Use switch_root to switch to the new root
    exec $SWITCH_ROOT_CMD /rootfs /sbin/init
fi
ADVANCED_CASPER_INIT_FIX_EOF

    chmod +x "$temp_dir/init"
    
    # Copy kernel modules if available
    if [ -d "rootfs/lib/modules" ]; then
        mkdir -p "$temp_dir/lib/modules"
        cp -r "rootfs/lib/modules/$COMPILED_KERNEL_VERSION" "$temp_dir/lib/modules/" 2>/dev/null || true
    fi
    
    # Create the initramfs archive
    log_info "Creating initramfs archive with switch_root fix..."
    (cd "$temp_dir" && find . | cpio -H newc -o | gzip -9 > "$WORK_DIR/initrd-custom")
    
    # Clean up
    rm -rf "$temp_dir"
    
    log_info "Advanced casper initramfs with switch_root fix created: $WORK_DIR/initrd-custom"
    log_info "File size: $(du -h $WORK_DIR/initrd-custom | cut -f1)"
    
    # Update the fallback function reference
    create_advanced_casper_initramfs() {
        create_advanced_casper_initramfs_with_fix "$@"
    }
}

```
[x86](../../../x86.md)  