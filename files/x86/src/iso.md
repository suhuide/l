[x86 ISO](../../../x86.md#%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E8%84%9A%E6%9C%AC)  

```c
#!/bin/bash

set -e

# Configuration variables
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ISO_NAME="custom-ubuntu"
KERNEL_VERSION="5.15"
UBUNTU_VERSION="focal"
WORK_DIR="$CURRENT_DIR/custom-ubuntu-build"
CACHE_DIR="$WORK_DIR/cache"
ISO_LABEL="CUSTOM_UBUNTU"
ISO_FILE="$WORK_DIR/${ISO_NAME}.iso"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check dependencies
check_dependencies() {
    log_info "Checking system dependencies..."
    local deps=("git" "debootstrap" "squashfs-tools" "xorriso" "grub2-common" "grub-pc-bin" "grub-efi-amd64-bin" "mtools" "syslinux" "syslinux-common" "dosfstools" "isolinux" "syslinux" "syslinux-common" "qemu-system-x86")
    
    for dep in "${deps[@]}"; do
        if ! dpkg -l | grep -q "^ii  $dep" 2>/dev/null; then
            log_error "Missing dependency: $dep"
            log_info "Run: sudo apt update && sudo apt install -y ${deps[*]}"
            exit 1
        fi
    done
    log_info "All dependencies satisfied"
}

# Initialize cache directories
init_cache() {
    mkdir -p "$CACHE_DIR/kernel" "$CACHE_DIR/rootfs" "$CACHE_DIR/initramfs" "$CACHE_DIR/firmware" "$CACHE_DIR/linux-src"
    log_info "Cache directories initialized: $CACHE_DIR"
}

# Check kernel source cache
check_kernel_source_cache() {
    local src_cache="$CACHE_DIR/linux-src"
    
    if [[ -d "$src_cache" && -f "$src_cache/Makefile" && -d "$src_cache/.git" ]]; then
        log_info "Found kernel source cache"
        return 0
    else
        log_info "No kernel source cache found"
        return 1
    fi
}

# Check kernel binary cache
check_kernel_binary_cache() {
    local kernel_cache="$CACHE_DIR/kernel"
    local kernel_file="$kernel_cache/bzImage"
    local modules_dir="$kernel_cache/modules"
    
    if [[ -f "$kernel_file" && -d "$modules_dir" && -n "$(ls -A $modules_dir)" ]]; then
        log_info "Found compiled kernel cache"
        return 0
    else
        log_info "No kernel binary cache found"
        return 1
    fi
}

# Check rootfs cache
check_rootfs_cache() {
    local rootfs_cache="$CACHE_DIR/rootfs"
    
    if [[ -d "$rootfs_cache" && -f "$rootfs_cache/etc/os-release" && -d "$rootfs_cache/usr" ]]; then
        log_info "Found configured rootfs cache"
        return 0
    else
        log_info "No rootfs cache found"
        return 1
    fi
}

# Save kernel source to cache
save_kernel_source_cache() {
    log_info "Saving kernel source to cache..."
    if [ -d "$WORK_DIR/linux" ]; then
        rsync -a "$WORK_DIR/linux/" "$CACHE_DIR/linux-src/" --delete
        log_info "Kernel source cache saved"
    else
        log_warn "No kernel source to save"
    fi
}

# Save kernel binary to cache
save_kernel_binary_cache() {
    log_info "Saving kernel binary to cache..."
    if [ -f "$WORK_DIR/kernel-bzImage" ]; then
        cp "$WORK_DIR/kernel-bzImage" "$CACHE_DIR/kernel/bzImage"
        log_info "Kernel image saved to cache"
    fi
    
    if [ -d "$WORK_DIR/rootfs/lib/modules" ] && [ -n "$(ls -A $WORK_DIR/rootfs/lib/modules)" ]; then
        log_info "Saving kernel modules to cache..."
        sudo rm -rf "$CACHE_DIR/kernel/modules"
        sudo cp -r "$WORK_DIR/rootfs/lib/modules" "$CACHE_DIR/kernel/"
        log_info "Kernel modules saved to cache, size: $(sudo du -sh $CACHE_DIR/kernel/modules | cut -f1)"
    else
        log_warn "No kernel modules to save"
    fi
    log_info "Kernel binary cache saved"
}

# Save rootfs to cache
save_rootfs_cache() {
    log_info "Saving rootfs to cache..."
    if [ -d "$WORK_DIR/rootfs" ]; then
        sudo rsync -a "$WORK_DIR/rootfs/" "$CACHE_DIR/rootfs/" --delete
        log_info "Rootfs cache saved, size: $(sudo du -sh $CACHE_DIR/rootfs | cut -f1)"
    else
        log_warn "No rootfs to save"
    fi
}

# Restore kernel source from cache
restore_kernel_source_from_cache() {
    log_info "Restoring kernel source from cache..."
    if [ -d "$CACHE_DIR/linux-src" ]; then
        rsync -a "$CACHE_DIR/linux-src/" "$WORK_DIR/linux/" --delete
        log_info "Kernel source restored"
        return 0
    else
        log_warn "No kernel source in cache"
        return 1
    fi
}

# Restore kernel binary from cache
restore_kernel_binary_from_cache() {
    log_info "Restoring kernel binary from cache..."
    if [ -f "$CACHE_DIR/kernel/bzImage" ]; then
        cp "$CACHE_DIR/kernel/bzImage" "$WORK_DIR/kernel-bzImage"
        log_info "Kernel image restored"
    else
        log_warn "No kernel image in cache"
        return 1
    fi
    
    if [ -d "$CACHE_DIR/kernel/modules" ] && [ -n "$(ls -A $CACHE_DIR/kernel/modules)" ]; then
        log_info "Restoring kernel modules..."
        sudo rm -rf "$WORK_DIR/rootfs/lib/modules"
        sudo mkdir -p "$WORK_DIR/rootfs/lib"
        sudo cp -r "$CACHE_DIR/kernel/modules" "$WORK_DIR/rootfs/lib/"
        log_info "Kernel modules restored, size: $(sudo du -sh $WORK_DIR/rootfs/lib/modules | cut -f1)"
        return 0
    else
        log_warn "No kernel modules in cache"
        return 1
    fi
}

# Restore rootfs from cache
restore_rootfs_from_cache() {
    log_info "Restoring rootfs from cache..."
    if [ -d "$CACHE_DIR/rootfs" ]; then
        sudo rsync -a "$CACHE_DIR/rootfs/" "$WORK_DIR/rootfs/" --delete
        log_info "Rootfs restored, size: $(sudo du -sh $WORK_DIR/rootfs | cut -f1)"
        return 0
    else
        log_warn "No rootfs in cache"
        return 1
    fi
}

# Clean work directory but keep cache
cleanup_workdir() {
    log_info "Cleaning work directory..."
    sudo rm -rf "$WORK_DIR/rootfs" "$WORK_DIR/iso" "$WORK_DIR/linux" 2>/dev/null || true
    mkdir -p "$WORK_DIR/rootfs" "$WORK_DIR/iso"
}

# Setup environment
setup_environment() {
    log_info "Setting up build environment..."
    mkdir -p "$WORK_DIR"
    cd "$WORK_DIR"
    mkdir -p rootfs/{boot,lib,etc/initramfs-tools,tmp,var}
    mkdir -p iso/{boot/grub,casper,isolinux,.disk,EFI/BOOT}
    init_cache
}

# Enhanced kernel configuration for live CD boot with verification
configure_kernel_enhanced() {
    log_info "Configuring kernel with enhanced live CD support..."
    
    # Start with default configuration
    make defconfig
    
    # Essential for booting - FIXING THE REPORTED ERRORS
    ./scripts/config --set-val CONFIG_BLK_DEV_INITRD y
    ./scripts/config --set-val CONFIG_DEVTMPFS y
    ./scripts/config --set-val CONFIG_DEVTMPFS_MOUNT y
    
    # Critical filesystem support for live CD - FIXING THE REPORTED ERRORS
    ./scripts/config --set-val CONFIG_SQUASHFS y
    ./scripts/config --set-val CONFIG_SQUASHFS_XZ y
    ./scripts/config --set-val CONFIG_SQUASHFS_FILE_CACHE y
    ./scripts/config --set-val CONFIG_SQUASHFS_ZLIB y
    ./scripts/config --set-val CONFIG_SQUASHFS_LZO y
    ./scripts/config --set-val CONFIG_SQUASHFS_LZ4 y
    
    ./scripts/config --set-val CONFIG_ISO9660_FS y
    ./scripts/config --set-val CONFIG_JOLIET y
    ./scripts/config --set-val CONFIG_ZISOFS y
    ./scripts/config --set-val CONFIG_UDF_FS y
    
    ./scripts/config --set-val CONFIG_EXT4_FS y
    ./scripts/config --set-val CONFIG_EXT4_FS_POSIX_ACL y
    ./scripts/config --set-val CONFIG_EXT4_FS_SECURITY y
    
    ./scripts/config --set-val CONFIG_OVERLAY_FS y
    ./scripts/config --set-val CONFIG_OVERLAY_FS_REDIRECT_DIR y
    ./scripts/config --set-val CONFIG_OVERLAY_FS_REDIRECT_ALWAYS_FOLLOW y
    ./scripts/config --set-val CONFIG_OVERLAY_FS_INDEX y
    ./scripts/config --set-val CONFIG_OVERLAY_FS_XINO_AUTO y
    ./scripts/config --set-val CONFIG_OVERLAY_FS_METACOPY y
    
    # Block device and storage drivers - FIXING THE REPORTED ERRORS
    ./scripts/config --set-val CONFIG_BLK_DEV_SR y          # SCSI CD-ROM support
    ./scripts/config --set-val CONFIG_CDROM y               # CD-ROM drivers
    ./scripts/config --set-val CONFIG_BLK_DEV_LOOP y        # Loop device support
    ./scripts/config --set-val CONFIG_BLK_DEV_LOOP_MIN_COUNT 16
    
    # Enhanced SCSI support
    ./scripts/config --set-val CONFIG_SCSI y
    ./scripts/config --set-val CONFIG_BLK_DEV_SD y          # SCSI disk support
    ./scripts/config --set-val CONFIG_CHR_DEV_SG y          # SCSI generic
    
    # ATA/IDE support
    ./scripts/config --set-val CONFIG_ATA y
    ./scripts/config --set-val CONFIG_ATA_SFF y             # ATA SFF support
    ./scripts/config --set-val CONFIG_ATA_PIIX y            # Intel PIIX PATA
    ./scripts/config --set-val CONFIG_SATA_AHCI y           # SATA controllers
    ./scripts/config --set-val CONFIG_SATA_AHCI_PLATFORM y
    ./scripts/config --set-val CONFIG_PATA_ATIIXP y
    ./scripts/config --set-val CONFIG_PATA_AMD y
    ./scripts/config --set-val CONFIG_PATA_OLDPIIX y
    ./scripts/config --set-val CONFIG_PATA_SCH y
    
    # NVMe support
    ./scripts/config --set-val CONFIG_NVME_CORE y
    ./scripts/config --set-val CONFIG_BLK_DEV_NVME y
    ./scripts/config --set-val CONFIG_NVME_FC y
    ./scripts/config --set-val CONFIG_NVME_TCP y
    
    # USB support
    ./scripts/config --set-val CONFIG_USB y
    ./scripts/config --set-val CONFIG_USB_SUPPORT y
    ./scripts/config --set-val CONFIG_USB_XHCI_HCD y        # USB 3.0
    ./scripts/config --set-val CONFIG_USB_EHCI_HCD y        # USB 2.0
    ./scripts/config --set-val CONFIG_USB_OHCI_HCD y        # USB 1.1
    ./scripts/config --set-val CONFIG_USB_STORAGE y         # USB storage
    ./scripts/config --set-val CONFIG_USB_UAS y             # USB Attached SCSI
    ./scripts/config --set-val CONFIG_USB_HID y             # USB HID devices
    
    # Input device support
    ./scripts/config --set-val CONFIG_INPUT y
    ./scripts/config --set-val CONFIG_INPUT_EVDEV y
    ./scripts/config --set-val CONFIG_INPUT_KEYBOARD y
    ./scripts/config --set-val CONFIG_INPUT_MOUSE y
    ./scripts/config --set-val CONFIG_INPUT_JOYSTICK y
    ./scripts/config --set-val CONFIG_INPUT_TABLET y
    ./scripts/config --set-val CONFIG_INPUT_TOUCHSCREEN y
    
    # HID support
    ./scripts/config --set-val CONFIG_HID y
    ./scripts/config --set-val CONFIG_HID_GENERIC y
    ./scripts/config --set-val CONFIG_HID_BATTERY_STRENGTH y
    ./scripts/config --set-val CONFIG_USB_HID y
    
    # Console and display support
    ./scripts/config --set-val CONFIG_VT y
    ./scripts/config --set-val CONFIG_VT_CONSOLE y
    ./scripts/config --set-val CONFIG_TTY y
    ./scripts/config --set-val CONFIG_SERIAL_8250 y
    ./scripts/config --set-val CONFIG_SERIAL_8250_CONSOLE y
    ./scripts/config --set-val CONFIG_FB y
    ./scripts/config --set-val CONFIG_FRAMEBUFFER_CONSOLE y
    ./scripts/config --set-val CONFIG_FB_VESA y
    ./scripts/config --set-val CONFIG_LOGO y
    
    # Framebuffer drivers
    ./scripts/config --set-val CONFIG_FB_EFI y
    ./scripts/config --set-val CONFIG_FB_SIMPLE y
    ./scripts/config --set-val CONFIG_FB_VIRTUAL y
    
    # DRM drivers (basic set)
    ./scripts/config --set-val CONFIG_DRM y
    ./scripts/config --set-val CONFIG_DRM_FBDEV_EMULATION y
    ./scripts/config --set-val CONFIG_DRM_VIRTIO_GPU y
    ./scripts/config --set-val CONFIG_DRM_BOCHS y
    ./scripts/config --set-val CONFIG_DRM_VBOXVIDEO y
    
    # Network support (basic)
    ./scripts/config --set-val CONFIG_NET y
    ./scripts/config --set-val CONFIG_INET y
    ./scripts/config --set-val CONFIG_IP_PNP y
    ./scripts/config --set-val CONFIG_IP_PNP_DHCP y
    
    # Basic network drivers
    ./scripts/config --set-val CONFIG_NET_VENDOR_REALTEK y
    ./scripts/config --set-val CONFIG_8139CP y
    ./scripts/config --set-val CONFIG_8139TOO y
    ./scripts/config --set-val CONFIG_E1000 y
    ./scripts/config --set-val CONFIG_E1000E y
    ./scripts/config --set-val CONFIG_R8169 y               # Realtek 8169
    
    # Wireless support
    ./scripts/config --set-val CONFIG_WLAN y
    ./scripts/config --set-val CONFIG_CFG80211 y
    ./scripts/config --set-val CONFIG_MAC80211 y
    
    # Kernel modules support
    ./scripts/config --set-val CONFIG_MODULES y
    ./scripts/config --set-val CONFIG_MODULE_UNLOAD y
    ./scripts/config --set-val CONFIG_MODULE_FORCE_UNLOAD y
    
    # Process and system support
    ./scripts/config --set-val CONFIG_PROC_FS y
    ./scripts/config --set-val CONFIG_SYSFS y
    ./scripts/config --set-val CONFIG_TMPFS y
    ./scripts/config --set-val CONFIG_TMPFS_POSIX_ACL y
    ./scripts/config --set-val CONFIG_TMPFS_XATTR y
    
    # Executable formats
    ./scripts/config --set-val CONFIG_BINFMT_ELF y
    ./scripts/config --set-val CONFIG_BINFMT_SCRIPT y
    
    # Kernel compression
    ./scripts/config --set-val CONFIG_KERNEL_GZIP y
    ./scripts/config --set-val CONFIG_KERNEL_XZ y
    
    # EFI and firmware support
    ./scripts/config --set-val CONFIG_EFI y
    ./scripts/config --set-val CONFIG_EFI_STUB y
    ./scripts/config --set-val CONFIG_EFI_VARS y
    
    # Disable debug to reduce size
    ./scripts/config --set-val CONFIG_DEBUG_INFO n
    ./scripts/config --set-val CONFIG_DEBUG_KERNEL n
    ./scripts/config --set-val CONFIG_DEBUG_FS n
    
    # Apply configuration
    make olddefconfig </dev/null
    log_info "Kernel configuration completed"
    
    # Enhanced verification of critical configurations
    verify_kernel_config
}

# Enhanced kernel configuration verification
verify_kernel_config() {
    log_info "Verifying critical kernel configurations..."
    
    local critical_configs=(
        "CONFIG_BLK_DEV_INITRD"
        "CONFIG_DEVTMPFS_MOUNT" 
        "CONFIG_SQUASHFS"
        "CONFIG_ISO9660_FS"
        "CONFIG_OVERLAY_FS"
        "CONFIG_BLK_DEV_SR"
        "CONFIG_CDROM"
        "CONFIG_BLK_DEV_LOOP"
    )
    
    local all_passed=true
    
    for config in "${critical_configs[@]}"; do
        local state=$(./scripts/config --state "$config")
        if [ "$state" = "y" ] || [ "$state" = "m" ]; then
            log_info "$config is enabled"
        else
            log_error "✗ $config is NOT enabled - THIS WILL CAUSE BOOT FAILURE"
            all_passed=false
        fi
    done
    
    # Additional recommended configurations
    local recommended_configs=(
        "CONFIG_DEVTMPFS"
        "CONFIG_TMPFS"
        "CONFIG_EXT4_FS"
        "CONFIG_VT"
        "CONFIG_VT_CONSOLE"
        "CONFIG_FRAMEBUFFER_CONSOLE"
        "CONFIG_USB"
        "CONFIG_USB_STORAGE"
        "CONFIG_INPUT_EVDEV"
        "CONFIG_HID_GENERIC"
    )
    
    log_info "Checking recommended configurations..."
    for config in "${recommended_configs[@]}"; do
        local state=$(./scripts/config --state "$config")
        if [ "$state" = "y" ] || [ "$state" = "m" ]; then
            log_info "$config is enabled"
        else
            log_warn "$config is NOT enabled - may affect functionality"
        fi
    done
    
    if [ "$all_passed" = false ]; then
        log_error "Critical kernel configurations are missing!"
        log_error "The kernel will not be able to boot from Live CD."
        log_error "Please check the configuration and try again."
        exit 1
    else
        log_info "All critical kernel configurations are enabled ✓"
    fi
}

# Smart kernel build - only compile when needed
build_kernel_smart() {
    local skip_compile=false
    
    # Check if we can use cached binaries
    if check_kernel_binary_cache && restore_kernel_binary_from_cache; then
        log_info "Successfully using cached kernel binaries"
        
        # Check if we need to recompile (source updates)
        if check_kernel_source_cache; then
            log_info "Checking kernel source updates..."
            restore_kernel_source_from_cache
            cd "$WORK_DIR/linux"
            
            # Check if source is up to date - only update if explicitly requested
            local current_commit=$(git rev-parse HEAD)
            local cached_commit=$(cat "$CACHE_DIR/kernel/last_commit" 2>/dev/null || echo "")
            
            if [ "$current_commit" = "$cached_commit" ]; then
                log_info "Kernel source is up to date with cache, skipping compilation"
                skip_compile=true
            else
                log_info "Kernel source has updates, but using cached binaries unless forced"
                # Only update if --no-cache is specified, otherwise use cached binaries
                if [ "$FORCE_RECOMPILE" = true ]; then
                    log_info "Forced recompile, updating source..."
                    git pull
                    skip_compile=false
                else
                    log_info "Using existing cached binaries, skipping source update"
                    skip_compile=true
                fi
            fi
        else
            log_info "No source cache, need to download source"
            skip_compile=false
        fi
    else
        log_info "No kernel binary cache available, need to compile"
        skip_compile=false
    fi
    
    # If compilation is needed
    if [ "$skip_compile" = false ]; then
        log_info "Downloading/updating Linux kernel source..."
        cd "$WORK_DIR"
        
        if [ ! -d "linux" ]; then
            # Use stable kernel repository
            log_info "Cloning kernel source for the first time..."
            git clone --depth 1 --branch "linux-${KERNEL_VERSION}.y" \
                https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git linux
        else
            log_info "Updating existing linux directory"
            cd linux
            git pull
            cd ..
        fi
        
        cd linux
        
        # Save current commit to cache
        git rev-parse HEAD > "$CACHE_DIR/kernel/last_commit" 2>/dev/null || true
        
        # Clean and configure
        log_info "Cleaning previous compilation..."
        make mrproper
        
        log_info "Configuring kernel..."
        configure_kernel_enhanced
        
        log_info "Compiling kernel (this may take a long time)..."
        make -j$(nproc) </dev/null
        
        log_info "Installing kernel modules to rootfs..."
        sudo make modules_install INSTALL_MOD_PATH="$WORK_DIR/rootfs"
        
        # Check if modules installed successfully
        if [ ! -d "$WORK_DIR/rootfs/lib/modules" ] || [ -z "$(ls -A $WORK_DIR/rootfs/lib/modules)" ]; then
            log_error "Kernel modules installation failed - no modules found"
            exit 1
        fi
        
        # Copy kernel image
        cp arch/x86/boot/bzImage "$WORK_DIR/kernel-bzImage"
        
        # Save to cache
        save_kernel_source_cache
        save_kernel_binary_cache
        
        log_info "Kernel compilation completed"
    else
        log_info "Using existing kernel binaries, skipping compilation"
    fi
}

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
    echo "✗ switch_root not found, checking busybox..."
    if busybox --list | grep -q switch_root; then
        echo "switch_root available via busybox"
        SWITCH_ROOT_CMD="busybox switch_root"
    else
        echo "✗ switch_root not available, using fallback to chroot"
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

# Improved .disk directory creation matching official Ubuntu structure
prepare_iso() {
    log_info "Preparing ISO directory structure (matching official Ubuntu)..."
    cd "$WORK_DIR"
    
    # Create complete ISO directory structure matching official Ubuntu
    mkdir -p iso/{boot/grub,casper,isolinux,.disk,EFI/BOOT,preseed,dists/stable/main/binary-amd64,install,pool/main}
    
    # Copy boot, EFI, and isolinux contents if they exist in CURRENT_DIR
    if [ -d "$CURRENT_DIR/iso" ]; then
        log_info "Copying boot/EFI/isolinux directory contents..."
        cp -r "$CURRENT_DIR/iso"/* iso/ 2>/dev/null || true
	else
	log_info "Copying boot/EFI/isolinux directory failed!"
    fi
        
    # Check kernel file
    if [ ! -f "kernel-bzImage" ]; then
        log_error "Kernel file kernel-bzImage does not exist"
        exit 1
    fi
    
    # Check initramfs file
    if [ ! -f "initrd-custom" ]; then
        log_error "initramfs file initrd-custom does not exist"
        exit 1
    fi
    
    log_info "Copying kernel and initramfs to ISO directory..."
    cp kernel-bzImage iso/casper/vmlinuz
    cp initrd-custom iso/casper/initrd
    
    log_info "Checking rootfs directory..."
    if [ ! -d "rootfs" ]; then
        log_error "rootfs directory does not exist"
        exit 1
    fi
    
    log_info "Creating squashfs filesystem..."
    sudo mksquashfs rootfs iso/casper/filesystem.squashfs -comp xz -b 1M -noappend
    
    if [ ! -f "iso/casper/filesystem.squashfs" ]; then
        log_error "squashfs file was not created successfully"
        exit 1
    fi
    
    log_info "squashfs created successfully, size: $(du -h iso/casper/filesystem.squashfs | cut -f1)"
    
    # Create filesystem manifest (like official Ubuntu)
    log_info "Creating filesystem manifest..."
    sudo chroot rootfs dpkg-query -W --showformat='${Package} ${Version}\n' > iso/casper/filesystem.manifest 2>/dev/null || {
        log_warn "Cannot generate complete filesystem manifest, creating basic one"
        echo "base-files 20.04" > iso/casper/filesystem.manifest
    }
    
    # Create filesystem manifest desktop (like official Ubuntu)
    cp iso/casper/filesystem.manifest iso/casper/filesystem.manifest-desktop
    
    # Create size file
    printf $(sudo du -s --block-size=1 rootfs | cut -f1) > iso/casper/filesystem.size
    
    # Create EXACT .disk directory structure matching official Ubuntu 20.04
    log_info "Creating .disk directory with EXACT official Ubuntu structure..."
    mkdir -p iso/.disk
    
    # Generate UUID for the ISO (CRITICAL for boot)
    # This UUID is used by casper to identify the installation media
    local iso_uuid
    if command -v uuidgen >/dev/null 2>&1; then
        iso_uuid=$(uuidgen)
    elif [ -f /proc/sys/kernel/random/uuid ]; then
        iso_uuid=$(cat /proc/sys/kernel/random/uuid)
    else
        # Fallback: generate pseudo UUID based on timestamp and random data
        iso_uuid=$(date +%s | sha256sum | head -c 32)
        iso_uuid="${iso_uuid:0:8}-${iso_uuid:8:4}-${iso_uuid:12:4}-${iso_uuid:16:4}-${iso_uuid:20:12}"
    fi
    
    log_info "Generated ISO UUID: $iso_uuid"
    echo "$iso_uuid" > iso/.disk/casper-uuid-generic
    
    # Create info file with EXACT official Ubuntu format
    cat > iso/.disk/info << 'DISK_INFO_EOF'
Ubuntu 20.04 LTS "Focal Fossa" - Release amd64 ($(date +%Y%m%d))
DISK_INFO_EOF

    # Create base_installable file (EXACT official Ubuntu format)
    touch iso/.disk/base_installable
    
    # Create cd_type file (EXACT official Ubuntu format)  
    echo "full_cd/single" > iso/.disk/cd_type
    
    # Create release_notes_url file (EXACT official Ubuntu format)
    echo "http://www.ubuntu.com/getubuntu/releasenotes?os=ubuntu&ver=20.04.6&lang=${LANG}" > iso/.disk/release_notes_url
    
    # Create the following files that exist in official Ubuntu ISO but are empty
    #touch iso/.disk/ubuntu_advantage_uri
    
    # Create install directory files (like official Ubuntu)
    mkdir -p iso/install
    #echo "casper/vmlinuz" > iso/install/vmlinuz
    #echo "casper/initrd" > iso/install/initrd.gz
    
    # Copy GRUB font file
    if [ -f "/usr/share/grub/unicode.pf2" ]; then
        cp /usr/share/grub/unicode.pf2 iso/boot/grub/font.pf2
        log_info "Copied GRUB font file"
    else
        log_warn "GRUB font file not found, boot menu may not display properly"
    fi
    
    # Copy memtest86+ if available
    #if [ -f "/usr/lib/syslinux/memdisk" ]; then
    #    cp /usr/lib/syslinux/memdisk iso/install/
    #fi
    if [ -f "/boot/memtest86+.bin" ]; then
        cp /boot/memtest86+.bin iso/install/mt86plus
    elif [ -f "/usr/share/memtest86+/memtest.bin" ]; then
        cp /usr/share/memtest86+/memtest.bin iso/install/mt86plus
    else
        log_warn "memtest86+ not available, memory test option will not work"
    fi
    
    # Create minimal pool structure (like official Ubuntu)
    mkdir -p iso/pool/main
    touch iso/pool/main/.empty_directory
    
    log_info "ISO structure preparation completed (official Ubuntu layout)"
}

# Enhanced ISO structure verification
verify_iso_structure() {
    log_info "Verifying ISO structure..."
    cd "$WORK_DIR/iso"
    
    local missing_files=()
    local warnings=()
    
    # Check critical files
    [ ! -f "casper/vmlinuz" ] && missing_files+=("casper/vmlinuz")
    [ ! -f "casper/initrd" ] && missing_files+=("casper/initrd")
    [ ! -f "casper/filesystem.squashfs" ] && missing_files+=("casper/filesystem.squashfs")
    [ ! -f "boot/grub/grub.cfg" ] && missing_files+=("boot/grub/grub.cfg")
    [ ! -f "boot/grub/loopback.cfg" ] && missing_files+=("boot/grub/loopback.cfg")  
    [ ! -f "isolinux/isolinux.bin" ] && missing_files+=("isolinux/isolinux.bin")
    [ ! -f "isolinux/ldlinux.c32" ] && missing_files+=("isolinux/ldlinux.c32")  
    
    # Check official Ubuntu structure files
    [ ! -f "boot/grub/efi.img" ] && warnings+=("boot/grub/efi.img")
    [ ! -f "EFI/BOOT/BOOTx64.EFI" ] && warnings+=("EFI/BOOT/BOOTx64.EFI")
    [ ! -f "EFI/BOOT/grubx64.efi" ] && warnings+=("EFI/BOOT/grubx64.efi")
    [ ! -f "EFI/BOOT/mmx64.efi" ] && warnings+=("EFI/BOOT/mmx64.efi")
    [ ! -f "boot/grub/font.pf2" ] && warnings+=("boot/grub/font.pf2")
    
    # Check for x86_64-efi directory and modules
    if [ ! -d "boot/grub/x86_64-efi" ]; then
        warnings+=("boot/grub/x86_64-efi directory")
    elif [ -z "$(ls -A boot/grub/x86_64-efi/*.mod 2>/dev/null)" ]; then
        warnings+=("GRUB EFI modules in boot/grub/x86_64-efi")
    fi
    if [ ${#missing_files[@]} -ne 0 ]; then
        log_error "Missing critical files: ${missing_files[*]}"
        return 1
    fi
    
    if [ ${#warnings[@]} -ne 0 ]; then
        for warning in "${warnings[@]}"; do
            log_warn "Missing optional file: $warning"
        done
    fi
    
    log_info "ISO structure verification passed"
    cd "$WORK_DIR"
    return 0
}

# Generate ISO file
generate_iso() {
    log_info "Generating ISO file..."
    cd "$WORK_DIR"
    
    
    # Verify ISO structure
    if ! verify_iso_structure; then
        log_error "ISO structure verification failed, cannot generate ISO"
        exit 1
    fi
    
    # Create md5sum (like official Ubuntu)
    cd iso
    find . -type f -print0 | xargs -0 md5sum > md5sum.txt
    cd ..
        
    # Build xorriso command based on available bootloaders
    local xorriso_cmd="xorriso -as mkisofs \
        -r -V \"$ISO_LABEL\" \
        -o \"$ISO_FILE\" \
        -J -J -joliet-long \
        -iso-level 3 \
        -partition_offset 16 \
        -isohybrid-mbr \"$isohdpfx\" \
        -b isolinux/isolinux.bin \
        -c isolinux/boot.cat \
        -boot-load-size 4 \
        -boot-info-table \
        -no-emul-boot \
        -eltorito-alt-boot \
        -e boot/grub/efi.img \
        -no-emul-boot \
        -isohybrid-gpt-basdat \
        -volset \"$ISO_LABEL\" \
        -appid \"Custom Ubuntu Live CD\" \
        -publisher \"Custom Build\" \
        -preparer \"Prepared by custom build script\" \
        \"$WORK_DIR/iso\""
    
    # Execute the command
    log_info "Running: $xorriso_cmd"
    if eval $xorriso_cmd; then
        log_info "ISO created successfully: $ISO_FILE"
        log_info "File size: $(du -h "$ISO_FILE" | cut -f1)"
        
        # Show ISO info
        log_info "ISO boot capabilities:"
        if [ -f "iso/boot/grub/efi.img" ]; then
            log_info "UEFI boot supported (efi.img)"
        else
            log_info "UEFI boot not available"
        fi
        log_info "Legacy BIOS boot supported"
        
    else
        log_error "ISO creation failed"
        exit 1
    fi
}
generate_iso_directly() {
    log_info "Generating ISO directly from existing iso directory..."
    cd "$WORK_DIR"

    # 验证ISO结构
    if ! verify_iso_structure; then
        log_error "ISO structure verification failed, cannot generate ISO"
        exit 1
    fi

    # 创建md5sum
    cd iso
    find . -type f -print0 | xargs -0 md5sum > md5sum.txt
    cd ..

    # 构建xorriso命令
    local xorriso_cmd="xorriso -as mkisofs \
        -r -V \"$ISO_LABEL\" \
        -o \"$ISO_FILE\" \
        -J -J -joliet-long \
        -iso-level 3 \
        -partition_offset 16 \
        -isohybrid-mbr \"$isohdpfx\" \
        -b isolinux/isolinux.bin \
        -c isolinux/boot.cat \
        -boot-load-size 4 \
        -boot-info-table \
        -no-emul-boot \
        -eltorito-alt-boot \
        -e boot/grub/efi.img \
        -no-emul-boot \
        -isohybrid-gpt-basdat \
        -volset \"$ISO_LABEL\" \
        -appid \"Custom Ubuntu Live CD\" \
        -publisher \"Custom Build\" \
        -preparer \"Prepared by custom build script\" \
        \"$WORK_DIR/iso\""

    # 执行命令
    log_info "Running: $xorriso_cmd"
    if eval $xorriso_cmd; then
        log_info "ISO created successfully: $ISO_FILE"
        log_info "File size: $(du -h $ISO_FILE | cut -f1)"
        log_info "isoinfo -d -i $ISO_FILE | grep -A5 -B5 \"Boot\""
        log_info "xorriso -indev $ISO_FILE -report_el_torito as_mkisofs"          
        log_info "qemu-system-x86_64 -cdrom $ISO_FILE -m 2048 -bios /usr/share/ovmf/OVMF.fd"
    else
        log_error "ISO creation failed"
        exit 1
    fi
}
# Show cache status
show_cache_status() {
    log_info "=== Cache Status ==="
    
    if check_kernel_source_cache; then
        local src_size=$(du -sh "$CACHE_DIR/linux-src" | cut -f1)
        local last_commit=$(cat "$CACHE_DIR/kernel/last_commit" 2>/dev/null | cut -c1-8 || echo "unknown")
        log_info "Kernel source cache:  Available ($src_size, commit: $last_commit)"
    else
        log_info "Kernel source cache:  Not available"
    fi

    if check_kernel_binary_cache; then
        local kernel_size=$(du -sh "$CACHE_DIR/kernel" | cut -f1)
        log_info "Kernel binary cache:  Available ($kernel_size)"
    else
        log_info "Kernel binary cache:  Not available"
    fi

    if check_rootfs_cache; then
        local rootfs_size=$(sudo du -sh "$CACHE_DIR/rootfs" | cut -f1)
        log_info "rootfs cache:  Available ($rootfs_size)"
    else
        log_info "rootfs cache:  Not available"
    fi

    log_info "=== ISO File Status ==="
    if [ -f "${ISO_FILE}" ]; then
        log_info "ISO file:  Exists"
        log_info "ISO location: ${ISO_FILE}"
        log_info "ISO size: $(du -h ${ISO_FILE} | cut -f1)"
    else
        log_info "ISO file:  Does not exist"
    fi
}

# Clean cache
clean_cache() {
    log_info "Cleaning all cache..."
    sudo rm -rf "$CACHE_DIR"
    log_info "Cache cleaned"
}

# Clean specific cache
clean_specific_cache() {
    local cache_type=$1
    
    case $cache_type in
        "kernel-src")
            log_info "Cleaning kernel source cache..."
            rm -rf "$CACHE_DIR/linux-src"
            ;;
        "kernel-bin")
            log_info "Cleaning kernel binary cache..."
            sudo rm -rf "$CACHE_DIR/kernel"
            ;;
        "rootfs")
            log_info "Cleaning rootfs cache..."
            sudo rm -rf "$CACHE_DIR/rootfs"
            ;;
        "all")
            clean_cache
            ;;
        *)
            log_error "Unknown cache type: $cache_type"
            log_info "Available types: kernel-src, kernel-bin, rootfs, all"
            exit 1
            ;;
    esac
}

# Show usage
show_usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -c, --clean             Clean all cache"
    echo "  -s, --status            Show cache and ISO status"
    echo "  --clean-cache TYPE      Clean specific cache"
    echo "                          TYPE: kernel-src, kernel-bin, rootfs, all"
    echo "  --no-cache              Ignore cache, force rebuild"
    echo "  --force-recompile       Force kernel recompilation even with cache"
    echo "  --kernel-only           Build kernel only"
    echo "  --rootfs-only           Build rootfs only"
    echo "  --iso-only              Build ISO only (use existing files)"
    echo "  --from-iso              Build ISO directly from iso existing files"
}

# Main function
main() {
    local NO_CACHE=false
    local FORCE_RECOMPILE=false
    local KERNEL_ONLY=false
    local ROOTFS_ONLY=false
    local ISO_ONLY=false
    local FROM_ISO_DIR=false

    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help) show_usage; exit 0 ;;
            -c|--clean) clean_cache; exit 0 ;;
            -s|--status) show_cache_status; exit 0 ;;
            --clean-cache) clean_specific_cache "$2"; shift 2 ;;
            --no-cache) NO_CACHE=true; shift ;;
            --force-recompile) FORCE_RECOMPILE=true; shift ;;
            --kernel-only) KERNEL_ONLY=true; shift ;;
            --rootfs-only) ROOTFS_ONLY=true; shift ;;
            --iso-only) ISO_ONLY=true; shift ;;
            --from-iso) FROM_ISO_DIR=true; shift ;;
            *) log_error "Unknown parameter: $1"; show_usage; exit 1 ;;
        esac
    done

    log_info "Starting custom ISO build..."
    log_info "Work directory: $WORK_DIR"
    log_info "Kernel version: Linux $KERNEL_VERSION"
    log_info "Ubuntu version: $UBUNTU_VERSION"
    
    if [ "$NO_CACHE" = true ]; then
        log_info "Ignore cache mode, forcing rebuild"
        clean_cache
    fi

    check_dependencies
    setup_environment
    show_cache_status
	
    if [ "$FROM_ISO_DIR" = true ]; then
        log_info "Building ISO directly from existing iso directory..."
        generate_iso_directly
        exit 0
    fi
	
    if [ "$ISO_ONLY" = true ]; then
        log_info "ISO-only mode: Building ISO using existing files"
        cleanup_workdir
        mkdir -p "$WORK_DIR/rootfs"
    else
        cleanup_workdir
    fi

    # Build process
    if [ "$ROOTFS_ONLY" = true ]; then
        log_info "Building rootfs only..."
        create_rootfs_smart
    elif [ "$KERNEL_ONLY" = true ]; then
        log_info "Building kernel only..."
        build_kernel_smart
    elif [ "$ISO_ONLY" = true ]; then
        log_info "Building ISO only..."
        # Use existing files
    else
        # Full build
        build_kernel_smart
        create_rootfs_smart
    fi

    # If not specific mode, continue building ISO
    if [ "$KERNEL_ONLY" = false ] && [ "$ROOTFS_ONLY" = false ]; then
        create_initramfs
        prepare_iso
        generate_iso

        log_info "=== Build completed! ==="
        log_info "Output file: $ISO_FILE"
        log_info "Test commands:"
        log_info "isoinfo -d -i $ISO_FILE | grep -A5 -B5 \"Boot\""
        log_info "xorriso -indev $ISO_FILE -report_el_torito as_mkisofs"   	
        log_info "qemu-system-x86_64 -cdrom $ISO_FILE -m 2048 -bios /usr/share/ovmf/OVMF.fd"
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```
[x86 ISO](../../../x86.md#%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E8%84%9A%E6%9C%AC)  