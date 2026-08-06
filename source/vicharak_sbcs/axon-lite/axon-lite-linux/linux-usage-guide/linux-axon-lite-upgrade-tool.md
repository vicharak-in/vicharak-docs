# Linux Upgrade Tool (upgrade_tool)

## What is Linux Upgrade Tool

Rockchip's **Linux Upgrade tool** is a proprietary solution developed by
Rockchip for flashing images onto various storage devices such as `SPI`,
`eMMC`, `SD-card`, and more. Unlike open-source
[rkdeveloptool](https://github.com/rockchip-linux/rkdeveloptool) software,
this tool does not provide access to its source code.

Instead, it is distributed solely in **binary executable** form,
allowing users to utilize the provided executable files for the purpose of
flashing images onto their desired storage devices.

## How to use Linux Upgrade Tool

(install-upgrade-tool)=
### Installing required system dependencies

Linux Upgrade Tool requires the following dependencies to be installed on your Debian or Debian system.

```bash
sudo apt-get install libudev-dev libusb-1.0-0-dev
```

---

For other Linux distributions, please refer to the following table for the equivalent package names.

|  Debian/Debian   |    Fedora    | Arch Linux |
| :--------------: | :----------: | :--------: |
|   libudev-dev    |              |            |
| libusb-1.0-0-dev | libusb-devel |   libusb   |


### Download Linux Upgrade Tool

**Download from [Vicharak GitHub](https://github.com/vicharak-in/Linux_Upgrade_Tool)**

```bash
git clone https://github.com/vicharak-in/Linux_Upgrade_Tool
```

(boot-into-maskrom-mode)=

---


### Flash RAW image in Axon Lite

Raw Images are versatile and complete filesystem blocks that can be flsahed onto a pendrive, 
an SD-Card,a flash drive, as well as nvme SSD or any other medium to boot onto.
As long as the firmware(U-Boot) supports the medium, entire OS can be kept on it.

1. Check whether device is in MaskRom Mode or not.

```bash
sudo ./upgrade_tool ld
```
Below, output will be shown.

```bash
List of rockusb connected(1)
DevNo=1	Vid=0x2207,Pid=0x350e,LocationID=13	Mode=Maskrom	SerialNo=
```

2. [Download RK3576 SPL Loader](https://downloads.vicharak.in/vicharak-axon-lite/rk3576_spl_loader_v1.09.108.bin)

3. Flash SPL Loader using **db**.

```bash
sudo ./upgrade_tool db rk3576_spl_loader_v1.09.108.bin
```

4. Flash image using **wl** command.

```bash
sudo ./upgrade_tool wl 0 <Version_vicharak-axon-lite-Kernel_Version_Date-debian_version-raw.img>
```

You will see this type of process:

```bash
[sudo] password for vicharak:
Loading firmware...
Support Type:330C FW Ver:8.1.00 FW Time:2023-07-07 14:11:41
Loader ver:1.1e Loader Time:2023-07-07 14:11:08
Start to upgrade firmware...
Download Boot Start
Download Boot Success
Wait For Maskrom Start
Wait For Maskrom Success
Test Device Start
Test Device Success
Check Chip Start
Check Chip Success
Get FlashInfo Start
Get FlashInfo Success
Prepare IDB Start
Prepare IDB Success
Download IDB Start
Download IDB Success
Download Firmware Start
Download Image... (12%)
```

5. Reset Device using reset buttton on board or you can run below command.

```bash
sudo ./upgrade_tool rd
```

:::{note}
Upon completion of the flashing process, the board will automatically reboot twice to install essential packages and apply necessary changes.
Please allow a few minutes for the process to finalize.
:::

### To Erase the flash

```bash
sudo ./upgrade_tool ef <Firmware_Image>
```

Example:

```bash
sudo ./upgrade_tool ef V1.0_vicharak_axon-lite-6.1-04032025-debian-noble-emmc.img
```

:::{warning}
Firmware Image should be the same image which you have flashed in Axon Lite eMMC. 
:::

### Data Recovery

To recover data from your eMMC, you can use the `upgrade_tool rl <offset> <size> output.img` command. This command allows you to read a specific range of sectors from the eMMC and save it as an image file.

1. **Calculate Offset and Size**:
   Determine the offset and size of the partition you want to recover. The offset is where the partition starts, and the size is the number of sectors in the partition. This is the standard for Axon Lite:

   ```bash
    Device           Start      End  Sectors  Size Type
    /dev/mmcblk0p1  32768    557055    524288  256M Linux extended boot
    /dev/mmcblk0p2 557056 122142656 121585601   58G Linux root (ARM-64)
   ```

   The partition starts at sector `557056` and has a size of `121585601`.

3. **Run the Data Recovery Command**:
   Use the `upgrade_tool rl <offset> <size> rootfs.img` command to read the partition data and save it as an image file. Replace `<offset>` and `<size>` with the actual values from your `fdisk` output.

   ```bash
    sudo ./upgrade_tool rl 0x88000 0x3826c9f rootfs.img
   ```

   This command will read the first partition (starting at sector `0x218000`) with a size of `0x3826c9f` and save it as `rootfs.img`.

4. **Extract Data from the Image File (Optional)**:
   You should now be able to mount this file and read the data.

   ```bash
   mkdir /mnt/recovery
   sudo mount -o loop rootfs.img /mnt/recovery
   ls /mnt/recovery
   ```

By following these steps, you should be able to recover data from your eMMC using `upgrade_tool`.

::::

[comment]: < :::{seealso} >
[comment]: < [axon-lite Linux starting guide](linux-start-guide.md) >
[comment]: < [Frequently Asked Questions](../../faq.rst) >
[comment]: < ::: >
