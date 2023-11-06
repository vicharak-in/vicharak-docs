(u-boot-ums-mode)

# U-Boot UMS

**USB Mass Storage (UMS)** mode is a feature that allows a device to function like
an external USB storage device when connected to a computer.

In UMS mode, the device's internal storage, such as eMMC (embedded MultiMediaCard),
is made accessible to the computer, similar to how you would connect a
USB drive or SD card to your computer.

This mode is useful for tasks like transferring files, flashing firmware,
or writing disk images to the device's storage.

Now, here are the steps for booting into UMS mode from either internal storage
or an SD card:

## Booting into UMS Mode from Internal Storage:

- Connect the device to a PC using a USB cable.
- Connect the FTDI to your board and to the Host computer.
- Open the serial monitor application on your Host computer.

:::{note}
More more information on Serial monitor application check out

[Serial Console Programs](#minicom-guide)
:::

- Power on the device.
- Quickly press `Ctrl + c` to enter the U-Boot console.
- From U-Boot console type `ums 1 mmc <dev number>`, where <dev number> is the device number for MMC card.

:::{dropdown} Help ums

```text
=> help ums (U-Boot cmdline)
ums - Use the UMS [USB Mass Storage]

Usage:
ums <USB_controller> [<devtype>] <dev[:part]> e.g. ums 0 mmc 0
devtype defaults to mmc
=>
```

:::

:::{note}
MMC device number is pre-configured from kernel device tree.

- `mmc0` is the device number for SD-Card.
- `mmc1` is the device number for eMMC.
  :::

- The device will automatically boot into UMS mode, allowing you to share its internal storage like a USB drive.

:::{dropdown} Success Logs from UMS

```text
=> ums 1 mmc 1
UMS: LUN 0, dev 1, hwpart 0, sector 0x0, count 0x3a3e000
```

:::

- Check kernel logs on your Host computer and you should be able to see new Storage device added.

:::{dropdown} Successful Logs from host kernel

```text
[20104.826747] usb 7-1.4.3: new high-speed USB device number 41 using xhci_hcd
[20104.909195] usb 7-1.4.3: New USB device found, idVendor=2207, idProduct=0010, bcdDevice= 2.23
[20104.909211] usb 7-1.4.3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[20104.909214] usb 7-1.4.3: Product: USB download gadget
[20104.909216] usb 7-1.4.3: Manufacturer: Rockchip
[20104.909221] usb 7-1.4.3: SerialNumber: ac4e87197c0c095
[20104.914797] usb-storage 7-1.4.3:1.0: USB Mass Storage device detected
[20104.914916] scsi host7: usb-storage 7-1.4.3:1.0
[20105.940727] scsi 7:0:0:0: Direct-Access     Linux    UMS disk 0       ffff PQ: 0 ANSI: 2
[20105.941285] sd 7:0:0:0: Attached scsi generic sg2 type 0
[20105.941594] sd 7:0:0:0: [sdc] 61071360 512-byte logical blocks: (31.3 GB/29.1 GiB)
[20105.941748] sd 7:0:0:0: [sdc] Write Protect is off
[20105.941752] sd 7:0:0:0: [sdc] Mode Sense: 0f 00 00 00
[20105.941880] sd 7:0:0:0: [sdc] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[20105.947385]  sdc: sdc1 sdc2 sdc3 sdc4 sdc5 sdc6 sdc7 sdc8
[20105.947726] sd 7:0:0:0: [sdc] Attached SCSI removable disk
```

:::

:::{note}
With UMS mode, you can easily access and manage the device's storage from your
computer, making it convenient for tasks that involve transferring or writing data to the device.
:::

:::{warning}
Do not insert SD-Card when after you previously entered UMS mode from eMMC. U-Boot will crash in such case.

Always do a reset the board before switching the storage for UMS mode.
:::
