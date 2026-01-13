[x86 Initramfs](../../../x86.md#%E5%88%9D%E5%A7%8B%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9Finitramfs)  
[Initramfs](../iso-init.png)  

```c
# Enhanced initramfs creation with proper casper integration and switch_root fix
create_initramfs() {
    log_info "Creating enhanced initramfs with proper casper integration and switch_root fix..."
    cd "$WORK_DIR"
    
    # Get actual kernel version
    if [ -d "rootfs/lib/modules" ] && [ -n "$(ls -A rootfs/lib/modules)" ]; then
        COMPILED_KERNEL_VERSION=$(ls rootfs/lib/modules/ | head -1)
        log_info "Detected kernel version: $COMPILED_KERNEL_VERSION"
    else
        log_error "No kernel modules found, cannot create initramfs"
        exit 1
    fi
    
    # Create enhanced initramfs build script with proper casper hooks and switch_root fix
    cat > /tmp/build_enhanced_initramfs.sh << 'ENHANCED_INITRAMFS_EOF'
#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

KERNEL_VERSION="$1"

echo "Building enhanced initramfs for kernel: $KERNEL_VERSION with switch_root fix"

# Ensure casper and live-boot are properly installed and configured
apt update >/dev/null 2>&1
apt install -y --reinstall casper live-boot live-boot-initramfs-tools busybox-static >/dev/null 2>&1

# CRITICAL: Ensure switch_root is available in initramfs
if [ ! -f "/usr/lib/klibc/bin/switch_root" ] && [ ! -f "/sbin/switch_root" ]; then
    echo "WARNING: switch_root not found in standard locations, ensuring busybox provides it"
    # Make sure busybox provides switch_root
    if [ -f "/bin/busybox" ]; then
        mkdir -p /usr/lib/klibc/bin
        ln -sf /bin/busybox /usr/lib/klibc/bin/switch_root 2>/dev/null || true
    fi
fi

# CRITICAL FIX: Ensure casper hooks are properly set up
mkdir -p /etc/initramfs-tools/hooks
mkdir -p /etc/initramfs-tools/scripts

# Create a custom hook to ensure casper scripts are included and switch_root is available
cat > /etc/initramfs-tools/hooks/casper-live << 'CASPER_HOOK_EOF'
#!/bin/sh
PREREQ=""
prereqs()
{
    echo "$PREREQ"
}

case $1 in
prereqs)
    prereqs
    exit 0
    ;;
esac

. /usr/share/initramfs-tools/hook-functions

# Copy casper scripts
if [ -d /usr/share/initramfs-tools/scripts/casper ]; then
    cp -r /usr/share/initramfs-tools/scripts/casper $DESTDIR/scripts/
    chmod +x $DESTDIR/scripts/casper/*
fi

# CRITICAL: Ensure switch_root is included
if [ -f "/usr/lib/klibc/bin/switch_root" ]; then
    copy_exec /usr/lib/klibc/bin/switch_root
elif [ -f "/sbin/switch_root" ]; then
    copy_exec /sbin/switch_root
else
    # Fallback: use busybox switch_root
    if [ -f "/bin/busybox" ]; then
        copy_exec /bin/busybox
        # Create symlink in initramfs
        mkdir -p $DESTDIR/usr/lib/klibc/bin
        ln -sf /bin/busybox $DESTDIR/usr/lib/klibc/bin/switch_root
    fi
fi

# Copy necessary casper binaries and libraries
copy_exec /usr/share/casper/casper-netcheck
copy_exec /sbin/cryptsetup
copy_exec /sbin/dmsetup

echo "Casper live boot hook with switch_root fix completed"
CASPER_HOOK_EOF

chmod +x /etc/initramfs-tools/hooks/casper-live

# Enhanced initramfs configuration
cat > /etc/initramfs-tools/initramfs.conf << 'INITRAMFS_CONF_EOF'
MODULES=most
BUSYBOX=y
COMPRESS=gzip
KEYMAP=n
DEVICE_SCAN=yes
BOOT=local
NFSROOT=auto
RUNSIZE=10%
COMPCACHE_SIZE=10%

# Enhanced for Live CD
MODULES_LIST="sr_mod cdrom ata_generic ata_piix usb-storage uhci-hcd ehci-hcd ohci-hcd sd_mod sg nvme"
INITRAMFS_CONF_EOF

# Enhanced modules list
cat > /etc/initramfs-tools/modules << 'MODULES_EOF'
# Block devices
loop
squashfs
overlay
fuse

# CDROM and storage
sr_mod
cdrom
ata_generic
ata_piix
ahci
sd_mod
sg

# USB support
usb-storage
uhci-hcd
ehci-hcd
ohci-hcd
xhci-hcd

# Filesystems
iso9660
udf
joliet
fat
vfat
ntfs
ext4
ext3
ext2

# NVMe
nvme
nvme_core

# SCSI
scsi_mod
scsi_transport_spi
MODULES_EOF

# Run depmod
echo "Running depmod..."
depmod -a "$KERNEL_VERSION"

# Create initramfs with verbose output
echo "Creating enhanced initramfs with switch_root fix..."
if update-initramfs -c -k "$KERNEL_VERSION" -v 2>&1; then
    echo "update-initramfs completed successfully"
else
    echo "update-initramfs failed, trying mkinitramfs..."
    mkinitramfs -o "/boot/initrd.img-$KERNEL_VERSION" "$KERNEL_VERSION" -v
fi

# Verify and copy
if [ -f "/boot/initrd.img-$KERNEL_VERSION" ]; then
    echo "Initramfs created successfully: /boot/initrd.img-$KERNEL_VERSION"
    ls -lh "/boot/initrd.img-$KERNEL_VERSION"
    cp "/boot/initrd.img-$KERNEL_VERSION" "/boot/initrd.img-custom"
    echo "Copied to /boot/initrd.img-custom"
    
    # Verify casper scripts are included
    if lsinitramfs "/boot/initrd.img-custom" | grep -q "scripts/casper"; then
        echo "Casper scripts are included in initramfs"
    else
        echo "WARNING: Casper scripts may not be properly included"
    fi
    
    # Verify switch_root is included
    if lsinitramfs "/boot/initrd.img-custom" | grep -q "switch_root"; then
        echo "switch_root is included in initramfs"
    else
        echo "WARNING: switch_root may not be properly included"
    fi
else
    echo "ERROR: Initramfs file not found after creation"
    exit 1
fi
ENHANCED_INITRAMFS_EOF

    chmod +x /tmp/build_enhanced_initramfs.sh
    sudo cp /tmp/build_enhanced_initramfs.sh "$WORK_DIR/rootfs/tmp/"
    
    log_info "Building enhanced initramfs with switch_root fix in chroot environment..."
    if sudo chroot "$WORK_DIR/rootfs" /tmp/build_enhanced_initramfs.sh "$COMPILED_KERNEL_VERSION"; then
        log_info "Enhanced initramfs with switch_root fix built successfully in chroot"
    else
        log_error "Failed to build initramfs in chroot, using advanced fallback with switch_root fix"
        create_advanced_casper_initramfs_with_fix
        return
    fi
    
    # Clean up
    sudo rm -f /tmp/build_enhanced_initramfs.sh
    sudo rm -f "$WORK_DIR/rootfs/tmp/build_enhanced_initramfs.sh"
    
    # Copy the created initramfs
    if [ -f "rootfs/boot/initrd.img-custom" ]; then
        cp "rootfs/boot/initrd.img-custom" "$WORK_DIR/initrd-custom"
        log_info "Enhanced initramfs with switch_root fix copied successfully: $WORK_DIR/initrd-custom"
        log_info "File size: $(du -h $WORK_DIR/initrd-custom | cut -f1)"
        
        # Verify the initramfs contains casper scripts and switch_root
        log_info "Checking initramfs contents..."
        if command -v lsinitramfs >/dev/null 2>&1; then
            if lsinitramfs "$WORK_DIR/initrd-custom" 2>/dev/null | grep -q "scripts/casper"; then
                log_info "Casper scripts are included in initramfs"
            else
                log_warn "Casper scripts may not be properly included, using fallback"
                create_advanced_casper_initramfs_with_fix
                return
            fi
            
            if lsinitramfs "$WORK_DIR/initrd-custom" 2>/dev/null | grep -q "switch_root"; then
                log_info "switch_root is included in initramfs"
            else
                log_warn "switch_root may not be properly included, using fallback"
                create_advanced_casper_initramfs_with_fix
                return
            fi
        else
            log_warn "lsinitramfs not available, cannot verify contents"
            # Continue anyway as the initramfs might still work
        fi
    else
        log_error "Enhanced initramfs file not found after build"
        create_advanced_casper_initramfs_with_fix
    fi
}

```
[x86 Initramfs](../../../x86.md#%E5%88%9D%E5%A7%8B%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9Finitramfs)    