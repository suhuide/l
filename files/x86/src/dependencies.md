[x86 Dependencies](../../../x86.md#%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83dependencies)  

```c
# Check dependencies
check_dependencies() {
    log_info "Checking system dependencies..."
    local deps=("git" "debootstrap" "squashfs-tools" "xorriso" "grub2-common" "grub-pc-bin" "grub-efi-amd64-bin" 
    "mtools" "syslinux" "syslinux-common" "dosfstools" "isolinux" "syslinux" "syslinux-common" "qemu-system-x86")
    
    for dep in "${deps[@]}"; do
        if ! dpkg -l | grep -q "^ii  $dep" 2>/dev/null; then
            log_error "Missing dependency: $dep"
            log_info "Run: sudo apt update && sudo apt install -y ${deps[*]}"
            exit 1
        fi
    done
    log_info "All dependencies satisfied"
}
```
[x86 Dependencies](../../../x86.md#%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83dependencies)  