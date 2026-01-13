[x86 GRUB](../../../x86.md#%E5%BC%95%E5%AF%BCgrub)  
[GRUB Boot Menu](../iso-qemu.png)  

```c
# Create GRUB configuration matching Ubuntu style
create_grub_config() {
    log_info "Creating GRUB configuration (Ubuntu style)..."
    cd "$WORK_DIR/iso"
    
    # Create main grub.cfg with Ubuntu-style entries
    cat > boot/grub/grub.cfg << 'EOF'
set timeout=10
set default=0

if [ ${grub_platform} == efi ]; then
    insmod efi_gop
    insmod efi_uga
else
    insmod vbe
fi

insmod gzio
insmod part_gpt
insmod ext2

set menu_color_normal=white/black
set menu_color_highlight=black/light-gray

menuentry "Try or Install Custom Ubuntu" {
    linux /casper/vmlinuz boot=casper quiet splash ---
    initrd /casper/initrd.gz
}

menuentry "Try or Install Custom Ubuntu (safe graphics)" {
    linux /casper/vmlinuz boot=casper quiet splash nomodeset ---
    initrd /casper/initrd
}

menuentry "OEM install (for manufacturers)" {
    linux /casper/vmlinuz boot=casper only-ubiquity oem-config/enable=true ---
    initrd /casper/initrd
}

menuentry "Check disc for defects" {
    linux /casper/vmlinuz boot=casper integrity-check quiet splash ---
    initrd /casper/initrd
}
EOF

    # Create loopback.cfg for GRUB loopback boot
    cat > boot/grub/loopback.cfg << 'LOOPBACK_EOF'
set timeout=10
menuentry "Try or Install Custom Ubuntu" {
    linux /casper/vmlinuz boot=casper file=/cdrom/preseed/ubuntu.seed quiet splash ---
    initrd /casper/initrd
}
LOOPBACK_EOF

    # Create isolinux configuration (for legacy BIOS)
    cat > isolinux/isolinux.cfg << 'ISOLINUX_EOF'
DEFAULT live
TIMEOUT 300
PROMPT 1

LABEL live
  MENU LABEL Try or Install Custom Ubuntu
  KERNEL /casper/vmlinuz
  APPEND initrd=/casper/initrd boot=casper quiet splash ---

LABEL live-nomodeset
  MENU LABEL Try or Install Custom Ubuntu (safe graphics)
  KERNEL /casper/vmlinuz
  APPEND initrd=/casper/initrd boot=casper quiet splash nomodeset ---

LABEL oem
  MENU LABEL OEM install (for manufacturers)
  KERNEL /casper/vmlinuz
  APPEND initrd=/casper/initrd boot=casper only-ubiquity oem-config/enable=true ---

LABEL check
  MENU LABEL Check disc for defects
  KERNEL /casper/vmlinuz
  APPEND initrd=/casper/initrd boot=casper integrity-check quiet splash ---

LABEL memtest
  MENU LABEL Memory test
  KERNEL /install/mt86plus
  APPEND -

LABEL hd
  MENU LABEL Boot from first hard disk
  LOCALBOOT 0x80
  APPEND -
ISOLINUX_EOF

    # Create txt.cfg for alternative boot methods
    cat > isolinux/txt.cfg << 'TXT_EOF'
default live
label live
  menu label ^Try or Install Custom Ubuntu
  kernel /casper/vmlinuz
  append initrd=/casper/initrd boot=casper quiet splash ---
label live-nomodeset
  menu label ^Try or Install Custom Ubuntu (safe graphics)
  kernel /casper/vmlinuz
  append initrd=/casper/initrd boot=casper quiet splash nomodeset ---
TXT_EOF

    log_info "GRUB configuration created (Ubuntu style)"
    cd "$WORK_DIR"
}
```
```c
# FIXED: Enhanced 32-bit EFI support check and creation
check_efi_32bit_support() {
    if [ -d "/usr/lib/grub/i386-efi" ] && [ -f "/usr/lib/grub/i386-efi/modinfo.sh" ]; then
        # Check if we can actually create 32-bit EFI images
        if grub-mkstandalone --help 2>&1 | grep -q "i386-efi"; then
            return 0
        fi
    fi
    return 1
}

# FIXED: Create GRUB boot structure with better error handling
create_grub_boot_structure() {
    log_info "Creating GRUB boot structure..."
    cd "$WORK_DIR/iso"

    # === BIOS boot (i386-pc) ===
    mkdir -p boot/grub/i386-pc
    local grub_pc_dir="/usr/lib/grub/i386-pc"
    if [ ! -d "$grub_pc_dir" ]; then
        log_error "Cannot find GRUB i386-pc directory"
        exit 1
    fi
    
    log_info "Creating BIOS bootloader..."
    cp "$grub_pc_dir"/*.mod "$grub_pc_dir"/*.lst "$grub_pc_dir"/boot.img boot/grub/i386-pc/ 2>/dev/null || true
    if grub-mkimage -p /boot/grub -O i386-pc -o boot/grub/core.img \
        biosdisk part_msdos iso9660 ext2 normal configfile boot linux search 2>/dev/null; then
        cat "$grub_pc_dir/boot.img" boot/grub/core.img > boot/grub/grub.img
        log_info "BIOS bootloader created successfully"
    else
        log_error "Failed to create BIOS bootloader"
        exit 1
    fi

    # === UEFI boot (x86_64-efi) ===
    mkdir -p EFI/BOOT

    log_info "Creating 64-bit UEFI bootloader..."
    cat > /tmp/grub-efi-cfg << 'GRUB_EFI_EOF'
set timeout=10
set default=0

menuentry "Try or Install Custom Ubuntu" {
    linux /casper/vmlinuz boot=casper quiet splash ---
    initrd /casper/initrd
}
GRUB_EFI_EOF

    # Create 64-bit EFI bootloader (most common)
    if grub-mkstandalone -O x86_64-efi \
        -o EFI/BOOT/bootx64.efi \
        --compress=xz \
        "/boot/grub/grub.cfg=/tmp/grub-efi-cfg" 2>/dev/null; then
        log_info "64-bit UEFI bootloader created successfully"
    else
        log_warn "Failed to create 64-bit UEFI bootloader, trying without compression..."
        if grub-mkstandalone -O x86_64-efi \
            -o EFI/BOOT/bootx64.efi \
            "/boot/grub/grub.cfg=/tmp/grub-efi-cfg" 2>/dev/null; then
            log_info "64-bit UEFI bootloader created successfully (no compression)"
        else
            log_warn "Failed to create 64-bit UEFI bootloader, continuing without it"
        fi
    fi

    # Create 32-bit EFI bootloader (optional - don't fail if not available)
    if check_efi_32bit_support; then
        log_info "Creating 32-bit UEFI bootloader..."
        if grub-mkstandalone -O i386-efi \
            -o EFI/BOOT/bootia32.efi \
            --compress=xz \
            "/boot/grub/grub.cfg=/tmp/grub-efi-cfg" 2>/dev/null; then
            log_info "32-bit UEFI bootloader created successfully"
        else
            log_info "32-bit UEFI bootloader creation failed (normal on most modern systems)"
        fi
    else
        log_info "32-bit EFI support not available, skipping 32-bit UEFI bootloader (this is normal)"
    fi

    rm -f /tmp/grub-efi-cfg

    # === ISOLINUX (legacy BIOS) ===
    mkdir -p isolinux
    log_info "Creating legacy BIOS bootloader..."
    if [ -f "/usr/lib/syslinux/modules/bios/isolinux.bin" ]; then
        cp /usr/lib/syslinux/modules/bios/isolinux.bin isolinux/
    elif [ -f "/usr/lib/ISOLINUX/isolinux.bin" ]; then
        cp /usr/lib/ISOLINUX/isolinux.bin isolinux/
    else
        log_error "Cannot find isolinux.bin"
        exit 1
    fi

    # Copy necessary modules
    for mod in ldlinux.c32 libutil.c32 libcom32.c32 vesamenu.c32 menu.c32 chain.c32 hdt.c32 libgpl.c32 reboot.c32 poweroff.c32; do
        if [ -f "/usr/lib/syslinux/modules/bios/$mod" ]; then
            cp "/usr/lib/syslinux/modules/bios/$mod" isolinux/
        fi
    done

    # Check what bootloaders were actually created
    log_info "Bootloader creation summary:"
    if [ -f "boot/grub/grub.img" ]; then
        log_info "BIOS bootloader created"
    else
        log_error "BIOS bootloader failed"
        exit 1
    fi
    
    if [ -f "EFI/BOOT/bootx64.efi" ]; then
        log_info "64-bit UEFI bootloader created"
    else
        log_warn "64-bit UEFI bootloader missing - UEFI boot may not work"
    fi
    
    if [ -f "EFI/BOOT/bootia32.efi" ]; then
        log_info "32-bit UEFI bootloader created"
    else
        log_info "32-bit UEFI bootloader not created (normal on most modern systems)"
    fi
    
    if [ -f "isolinux/isolinux.bin" ]; then
        log_info "Legacy BIOS bootloader created"
    else
        log_error "Legacy BIOS bootloader failed"
        exit 1
    fi

    cd "$WORK_DIR"
    return 0
}

```
[x86 GRUB](../../../x86.md#%E5%BC%95%E5%AF%BCgrub)  