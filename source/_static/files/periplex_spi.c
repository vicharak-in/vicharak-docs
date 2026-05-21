#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <mtd/mtd-user.h>
#include <string.h>
#include <errno.h>

int main()
{
    mtd_info_t mtd_info;
    erase_info_t ei;
    int fd;
    unsigned char data[10000];      // 10000 bytes to write
    unsigned char read_buf[10000];  // 10000 bytes to read back
    int i, errors = 0;
    
    printf("=== MTD 10000 Bytes Operation (W25Q128JV SPI Flash) ===\n\n");
    
    // Step 1: Open the MTD device
    printf("Opening /dev/mtd0...\n");
    fd = open("/dev/mtd0", O_RDWR);
    if (fd < 0) {
        printf("ERROR: Cannot open /dev/mtd0: %s\n", strerror(errno));
        return 1;
    }
    printf(" Device opened successfully\n\n");
    
    // Step 2: Get device information
    if (ioctl(fd, MEMGETINFO, &mtd_info) < 0) {
        printf("ERROR: Cannot get MTD info: %s\n", strerror(errno));
        close(fd);
        return 1;
    }
    
    printf("W25Q128JV Flash Info:\n");
    printf("  Total Size: %u bytes (16MB)\n", mtd_info.size);
    printf("  Erase Block Size: %u bytes (4KB sectors)\n", mtd_info.erasesize);
    printf("  Write Size: %u bytes\n", mtd_info.writesize);
    printf("  Page Size: 256 bytes for W25Q128JV\n\n");
    
    // Step 3: Prepare 10000 bytes of test data
    printf("Preparing 10000 bytes of data...\n");
    for (i = 0; i < 10000; i++) {
        data[i] = i % 256;  // Pattern: 0, 1, 2, ..., 255, 0, 1, 2, ...
    }
    printf(" Test data prepared (pattern: 0-255 repeating)\n\n");
    
    // Step 4: Erase BOTH blocks (since 10000 bytes spans two 4KB sectors)
    printf("Erasing first 4KB sector (0-4095)...\n");
    ei.start = 0;
    ei.length = mtd_info.erasesize;
    
    // Try to unlock (ignore if not supported)
    ioctl(fd, MEMUNLOCK, &ei);
    
    if (ioctl(fd, MEMERASE, &ei) < 0) {
        printf("ERROR: Cannot erase first block: %s\n", strerror(errno));
        close(fd);
        return 1;
    }
    printf(" First 4KB sector erased successfully\n");
    
    printf("Erasing second 4KB sector (4096-8191)...\n");
    ei.start = 4096;
    ei.length = mtd_info.erasesize;
    
    // Try to unlock (ignore if not supported)
    ioctl(fd, MEMUNLOCK, &ei);
    
    if (ioctl(fd, MEMERASE, &ei) < 0) {
        printf("ERROR: Cannot erase second block: %s\n", strerror(errno));
        close(fd);
        return 1;
    }
    printf(" Second 4KB sector erased successfully\n\n");
    
    // Step 5: Write data in smaller chunks (W25Q128JV has 256-byte pages)
    printf("Writing 10000 bytes to flash in page-sized chunks...\n");
    lseek(fd, 0, SEEK_SET);
    
    int total_written = 0;
    int page_size = 256;  // FIXED: Correct W25Q128JV page size
    int offset = 0;
    
    while (total_written < 10000) {
        int bytes_to_write = (10000 - total_written > page_size) ? page_size : (10000 - total_written);
        
        printf("  Writing chunk %d: %d bytes at offset %d...\n", 
               (total_written / page_size) + 1, bytes_to_write, offset);
        
        lseek(fd, offset, SEEK_SET);
        int bytes_written = write(fd, data + offset, bytes_to_write);
        
        if (bytes_written < 0) {
            printf("ERROR: Write failed at offset %d: %s\n", offset, strerror(errno));
            close(fd);
            return 1;
        } else if (bytes_written != bytes_to_write) {
            printf("WARNING: Partial write at offset %d: expected %d, wrote %d bytes\n", 
                   offset, bytes_to_write, bytes_written);
        }
        
        total_written += bytes_written;
        offset += bytes_written;
        
        // Small delay to allow flash to complete operation
        usleep(1000); // 1ms delay
    }
    
    printf(" Successfully wrote %d bytes total\n\n", total_written);
    
    // Step 6: Read back 10000 bytes
    printf("Reading 10000 bytes from flash...\n");
    lseek(fd, 0, SEEK_SET);
    
    // Try reading in smaller chunks first
    int total_read = 0;
    offset = 0;
    memset(read_buf, 0, sizeof(read_buf)); // Clear buffer first
    
    while (total_read < 10000) {
        int bytes_to_read = (10000 - total_read > page_size) ? page_size : (10000 - total_read);
        
        lseek(fd, offset, SEEK_SET);
        int bytes_read = read(fd, read_buf + offset, bytes_to_read);
        
        if (bytes_read < 0) {
            printf("ERROR: Read failed at offset %d: %s\n", offset, strerror(errno));
            close(fd);
            return 1;
        } else if (bytes_read != bytes_to_read) {
            printf("WARNING: Partial read at offset %d: expected %d, read %d bytes\n",
                   offset, bytes_to_read, bytes_read);
        }
        
        total_read += bytes_read;
        offset += bytes_read;
    }
    
    printf(" Successfully read %d bytes total\n\n", total_read);
    
    // Step 7: Verify data integrity
    printf("Verifying data integrity...\n");
    for (i = 0; i < 10000; i++) {
        if (data[i] != read_buf[i]) {
            errors++;
            if (errors <= 10) {  // Show first 10 errors only
                printf("  Mismatch at byte %d: wrote 0x%02x, read 0x%02x\n",
                       i, (unsigned int)data[i], (unsigned int)read_buf[i]);
            }
        }
    }
    
    if (errors == 0) {
        printf(" Perfect! All 10000 bytes verified successfully\n");
    } else {
        printf("✗ Found %d data mismatches\n", errors);
        if (errors > 10) {
            printf("  (showing only first 10 errors)\n");
        }
    }
    
    // Step 8: Show sample data
    printf("\nSample Data Verification:\n");
    printf("Position | Written | Read    | Status\n");
    printf("---------|---------|---------|--------\n");
    for (i = 0; i < 10; i++) {
        printf("%8d | 0x%02x    | 0x%02x    | %s\n", 
               i, 
               (unsigned int)data[i], 
               (unsigned int)read_buf[i],
               (data[i] == read_buf[i]) ? "✓" : "✗");
    }
    
    printf("   ...   |   ...   |   ...   |   ...\n");
    
    for (i = 4090; i < 10000; i++) {
        printf("%8d | 0x%02x    | 0x%02x    | %s\n", 
               i, 
               (unsigned int)data[i], 
               (unsigned int)read_buf[i],
               (data[i] == read_buf[i]) ? "✓" : "✗");
    }
    
    close(fd);
    
    // Final result
    printf("\n=== OPERATION COMPLETE ===\n");
    if (errors == 0) {
        printf("✓ SUCCESS: W25Q128JV 10000-byte operation completed perfectly!\n");
        printf("   - Two 4KB sectors erased (0-4095 and 4096-8191)\n");
        printf("   - 10000 bytes written in 256-byte page chunks\n");
        printf("   - 10000 bytes read back successfully\n");
        printf("   - Data integrity verified\n");
        return 0;
    } else {
        printf("✗ FAILED: Operation completed but with %d data errors\n", errors);
        printf("   This may indicate:\n");
        printf("   - SPI communication issues\n");
        printf("   - Flash wear/damage\n");
        printf("   - Timing problems\n");
        return 1;
    }
}