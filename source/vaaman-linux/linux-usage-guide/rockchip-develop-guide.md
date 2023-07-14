{#rockchip-develop-tool}

# Rockchip Development Tool Guide

Rockchip offers the [**RKDevTool**](#windows-rkdevtool) as a fundamental development tool for Windows operating systems,
while the **Linux Upgrade Tool** serves as a straightforward development solution for Linux and Mac platforms.

:::::{tab-set}
::::{tab-item} Windows RKDevTool

{#windows-rkdevtool}
TODO

::::

::::{tab-item} Linux Upgrade Tool
:selected:

## Linux Upgrade Tool

Rockchip's Linux Upgrade tool is a proprietary solution developed by the company for flashing images onto
various storage devices such as SPI eMMC, SD Card, and more. Unlike open-source software,
this tool does not provide access to its source code.

Instead, it is distributed solely in binary form, allowing users to utilize the provided executable files
for the purpose of flashing images onto their desired storage devices.

### Install system dependencies

Linux Upgrade Tool requires the following dependencies to be installed on your Debian or Ubuntu system.

```bash
sudo apt-get install libudev-dev libusb-1.0-0-dev
```

---

For other Linux distributions, please refer to the following table for the equivalent package names.

|  Debian/Ubuntu   |    Fedora    | Arch Linux |
| :--------------: | :----------: | :--------: |
|   libudev-dev    |              |            |
| libusb-1.0-0-dev | libusb-devel |   libusb   |

**Download the Linux_Upgrade_Tool from [Vicharak Github](https://github.com/vicharak-in/Linux_Upgrade_Tool)**

```bash
git clone https://github.com/vicharak-in/Linux_Upgrade_Tool
```

---

:::{admonition} **Linux Upgrade Tool Usage**
:class: dropdown

```bash
---------------------Tool Usage ---------------------
Help:             H
Version:          V
Log:              LG
------------------Upgrade Command ------------------
ChooseDevice:		CD
ListDevice:		LD
SwitchDevice:		SD
UpgradeFirmware:	UF <Firmware> [-noreset]
UpgradeLoader:		UL <Loader> [-noreset] [FLASH|EMMC|SPINOR|SPINAND]
DownloadImage:		DI <-p|-b|-k|-s|-r|-m|-u|-t|-re image>
DownloadBoot:		DB <Loader>
EraseFlash:		EF <Loader|firmware>
PartitionList:		PL
WriteSN:		SN <serial number>
ReadSN:			RSN
ReadComLog:		RCL <File>
CreateGPT:		GPT <Input Parameter> <Output Gpt>
SwitchStorage:		SSD
----------------Professional Command -----------------
TestDevice:		TD
ResetDevice:		RD [subcode]
ResetPipe:		RP [pipe]
ReadCapability:		RCB
ReadFlashID:		RID
ReadFlashInfo:		RFI
ReadChipInfo:		RCI
ReadSecureMode:		RSM
WriteSector:		WS  <BeginSec> <PageSizeK> <PageSpareB> <File>
ReadLBA:		RL  <BeginSec> <SectorLen> [File]
WriteLBA:		WL  <BeginSec> [SizeSec] <File>
EraseLBA:		EL  <BeginSec> <EraseCount>
EraseBlock:		EB <CS> <BeginBlock> <BlokcLen> [--Force]
RunSystem:		RUN <uboot_addr> <trust_addr> <boot_addr> <uboot> <trust> <boot>
-------------------------------------------------------
```

:::{tip}
You can use the above command by using `sudo ./upgrade_tool` prefix before any of the command.

**For example to erase flash:**

```bash
sudo ./upgrade_tool db <loader path>
sudo ./upgrade_tool ef
```

:::

:::

## Flashing RAW image using Linux_Upgrade_Tool

### Check for connected devices

:::{card} sudo ./upgrade_tool ld

```bash
List of rockusb connected(1)

DevNo=1 Vid=0x2207,Pid=0x330c,LocationID=7143 Mode=Maskrom SerialNo=
```

:::

### Reboot the device

:::{card} sudo ./upgrade_tool rd

```bash
[sudo] password for vicharak:

Reset Device Success!
```

:::

:::{tip}
If you encounter **Reset Device Fail!** then try to manually reboot using the power button on the board.
:::

### Flash the loader binary

:::{card} sudo ./upgrade_tool db rk3399_loader_xxx.bin

```bash
Download boot ok.
```

:::

### Flash the RAW GPT image to storage device

:::{danger}
Make sure to flash the loader first to the storage device.
:::

:::{card} sudo ./upgrade_tool wl 0 <some_gpt_image>.img

```bash
Write LBA OK.
```

:::

---

:::{tip}
**Alternatively you can directly flash update image to EMMC using `update firmware` method.**
:::

{#flash-update-img}

## Flash update.img using (update firmware) method

:::{card} sudo ./upgrade_tool uf update.img

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

:::

:::{seealso} [Flash different images with Linux_Upgrade_Tool](#rockchip-upgrade-tool-misc)
::::

:::::
