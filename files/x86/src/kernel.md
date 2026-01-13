[x86](../../../x86.md#%E5%86%85%E6%A0%B8kernel)  


```c
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

```

```c
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
```

[x86](../../../x86.md#%E5%86%85%E6%A0%B8kernel)  