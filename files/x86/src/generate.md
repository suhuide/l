[x86 Generate](../../../x86.md#%E7%94%9F%E6%88%90generate)  

```c
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
```
[x86 Generate](../../../x86.md#%E7%94%9F%E6%88%90generate)    