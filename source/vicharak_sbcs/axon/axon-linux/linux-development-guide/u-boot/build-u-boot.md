(build-axon-u-boot)=

# U-Boot (Universal Boot Loader)

## What actually is u-boot?

U-Boot `Das U-Boot` is an open-source bootloader that can be used on various
platforms such as ARM, X86, MIPS, RISC-V and many more.
It is the Universal Boot Loader project and is actually used to boot the
Linux kernel in your Vicharak board.

:::{note}
More information on u-boot can be found on [U-Boot Wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot).
:::

(axon-mainline-u-boot-important)=

:::{important}

Vicharak provides vendor-specific U-Boot for the Axon board (RK3588), based on
Rockchip U-Boot with additional features and Axon board support.

It is generally recommended to use **vendor-specific U-Boot** with Vicharak
Linux images, because those images follow [Rockchip's boot flow](#axon-rockchip-boot-flow).
:::

## Build Vicharak Axon u-boot from source

:::{warning}
It is recommended to use **Ubuntu 20.04** and Higher or **Debian 11**
and Higher environment for building.
:::

### Installing the system dependencies

```bash
sudo apt update -y

sudo apt-get install -y build-essential python3 python-is-python3 libssl-dev \
    git-core gcc-arm-linux-gnueabi gcc-arm-linux-gnueabihf u-boot-tools \
    device-tree-compiler gcc-aarch64-linux-gnu mtools parted pv bc bison flex \
    debhelper
```

:::{note}
Debian package builds require ``debhelper-compat (= 12)``.
:::

### Getting the source

The source code for the u-boot has been published to our
[GitHub organisation](https://github.com/vicharak-in/rockchip-linux-u-boot).

You can either clone the repository or download the source code from GitHub.

:::{tip}
We recommend that you use `git clone` method to clone the repository as it is
easier to maintain.
:::

::::{tab-set}

:::{tab-item} Using git clone

```bash
git clone https://github.com/vicharak-in/rockchip-linux-u-boot -b master
```

```{tip}
Use `git clone --depth=1` to shallow clone the repository
```

:::

:::{tab-item} Using Web Browser

![vicharak-uboot-github](/_static/images/vicharak-uboot-github.webp)

**Follow the steps in above image.**

1. Open the [GitHub repository](https://github.com/vicharak-in/rockchip-linux-u-boot)
   and click on the ``< > Code`` button.

2. Click on the "Download ZIP" option.

3. After successful download, unpack the archive using any archiver tool
   (7zip, unzip, etc).

:::

:::{tab-item} Using Terminal

Use the following command to download the source code

```bash
wget https://github.com/vicharak-in/rockchip-linux-u-boot/archive/refs/heads/master.zip

unzip master.zip
mv rockchip-linux-u-boot-master rockchip-linux-u-boot
```

:::
::::

### Compiling Axon u-boot

There are two methods to compile Axon u-boot.

1. Rockchip u-boot build script
2. Vicharak u-boot build script

#### Enter the u-boot directory

```bash
cd <u-boot-directory>
```

::::{tab-set}

:::{tab-item} Compile using Rockchip u-boot script

```bash
./make.sh rk3588-axon
```

:::

:::{tab-item} Compile using Vicharak u-boot script

```bash
git submodule update --init
```

Select the Axon device profile:

```bash
./vicharak/build.sh -l
```

````{card} Example output

```text
    Processing option: -l
----------------------------------------------------------------
1) rk3399-vaaman.mk
2) rk3588-axon.mk
Select device: 2
```

When prompted, enter ``2`` to select ``rk3588-axon.mk``.
````

Then build U-Boot and the debian package:

```bash
./vicharak/build.sh -b
./vicharak/build.sh -B
```

````{tip}
Vicharak u-boot script is recommended for ease of use

The script is located in `vicharak/build.sh` and basic operations are as follows:

```text
    ─────────────────────────────────────────────────────────────────────
              Vicharak U-Boot Build Script - Usage Guide
    ─────────────────────────────────────────────────────────────────────
     Usage: ./vicharak/build.sh [OPTIONS]

     Available Options:
      lunch            | -l    : Prepare the environment for the chosen device
      info             | -i    : Display current u-boot setup details
      clean            | -c    : Remove u-boot build artifacts
      build            | -b    : Compile the u-boot for the chosen device
      ubootdeb         | -B    : Generate a debian package for the u-boot
      update_defconfig | -u    : Update the u-boot configuration with the latest changes
      help             | -h    : Display this usage guide
    ─────────────────────────────────────────────────────────────────────
```
````

:::

::::

Output files will be inside the current folder.
Make sure the following images are present:

:::{card} Confirm these files in the current directory

idbloader.img

rk3588_spl_loader_v1.xx.xxx.bin (or `rk3588_spl_*`)

uboot.img
:::

:::{tip}
To create **u-boot.itb** for flashing with `upgrade_tool`, run:

```bash
./make.sh itb
```

This generates `u-boot.itb` in the current directory.
:::

:::{note}

What exactly are `rk3588_spl_*`, `idbloader.img` and `u-boot.itb`?

- `rk3588_spl_*` — Rockchip SPL loader used by `upgrade_tool` in MaskROM mode
- `idbloader.img` — Secondary Program Loader (TPL/SPL), written at sector 64
- `u-boot.itb` — FIT image containing U-Boot proper and ATF, written at sector 16384

Read [Rockchip's boot option](http://opensource.rock-chips.com/wiki_Boot_option)
for more information.
:::

(flash-axon-u-boot)=

## How to flash or upgrade u-boot

(axon-rockchip-boot-flow)=

:::{admonition} Rockchip's boot flow
:class: note

```text
+--------+----------------+----------+-------------+---------+
| Boot   | Terminology #1 | Actual   | Rockchip    | Image   |
| stage  |                | program  |  Image      | Location|
| number |                | name     |   Name      | (sector)|
+--------+----------------+----------+-------------+---------+
| 1      |  Primary       | ROM code | BootRom     |         |
|        |  Program       |          |             |         |
|        |  Loader        |          |             |         |
|        |                |          |             |         |
| 2      |  Secondary     | U-Boot   |idbloader.img| 0x40    | pre-loader
|        |  Program       | TPL/SPL  |             |   (64)  |
|        |  Loader (SPL)  |          |             |         |
|        |                |          |             |         |
| 3      |  -             | U-Boot   | u-boot.itb  | 0x4000  | including u-boot and atf
|        |                | + ATF    |             | (16384) |
|        |                |          |             |         |
| 4      |  -             | kernel   | boot.img    | 0x8000  |
|        |                |          |             |         |
| 5      |  -             | rootfs   | rootfs.img  | 0x40000 |
+--------+----------------+----------+-------------+---------+
```

Read more information on [Rockchip's boot option](http://opensource.rock-chips.com/wiki_Boot_option)
:::

Once you have successfully compiled the u-boot, you are ready to flash it on
your Axon board.

::::{tab-set}

:::{tab-item} Flashing with upgrade_tool (recommended)

### Prerequisites

1. Install and set up
   [Linux Upgrade Tool](../../linux-usage-guide/linux-axon-upgrade-tool.md#install-upgrade-tool).

2. Put the board into **MaskROM mode** before updating U-Boot.
   See [Boot into MaskROM mode](../../linux-usage-guide/linux-axon-upgrade-tool.md#boot-into-maskrom-mode).

```{warning}
Always confirm the board is in MaskROM mode before writing U-Boot images.
Flashing while the board is not in MaskROM can fail or brick the bootloader.
```

### 1. Confirm MaskROM mode

```bash
sudo ./upgrade_tool ld
```

Expected output should show `Mode=Maskrom`:

```text
List of rockusb connected(1)
DevNo=1	Vid=0x2207,Pid=0x350b,LocationID=12	Mode=Maskrom	SerialNo=
```

### 2. Load the Rockchip SPL loader

```bash
sudo ./upgrade_tool db rk3588_spl_*
```

Example:

```bash
sudo ./upgrade_tool db rk3588_spl_loader_v1.14.113.bin
```

```{tip}
You can use the SPL loader produced by the U-Boot build, or download one from
[Vicharak Axon downloads](https://downloads.vicharak.in/vicharak-axon/rk3588_spl_loader_v1.14.113.bin).
```

### 3. Flash idbloader.img

```bash
sudo ./upgrade_tool wl 64 idbloader.img
```

### 4. Create and flash u-boot.itb

If `u-boot.itb` is not already present in the U-Boot directory, create it:

```bash
./make.sh itb
```

Then flash it:

```bash
sudo ./upgrade_tool wl 16384 u-boot.itb
```

### 5. Reset the board

```bash
sudo ./upgrade_tool rd
```

:::

:::{tab-item} Flashing on eMMC with dd

If you are not using `UMS mode`, make sure you can boot your board using any
other storage media (SD-card, NVMe, or even the same eMMC).

Assuming the eMMC is at `/dev/mmcblk1`:

**Secondary Program Loader (idbloader)**

```bash
sudo dd if=idbloader.img of=/dev/mmcblk1 seek=64; sync
```

**U-Boot FIT image (u-boot.itb)**

```bash
sudo dd if=u-boot.itb of=/dev/mmcblk1 seek=16384; sync
```

```{warning}
The block device `/dev/mmcblk1` may be different as per the board's storage
configuration.

Confirm the block device using `parted /dev/mmcblk<X>` or `lsblk`.
```

:::

:::{tab-item} Flashing on SD-Cards

1. Plug the SD-Card into the SD-Card reader and insert it into your PC.

2. Use the linux `dd` utility to write the images. (Assuming the SD card is at
   `/dev/sdb`)

**Secondary Program Loader (idbloader)**

```bash
sudo dd if=idbloader.img of=/dev/sdb seek=64; sync
```

**U-Boot FIT image (u-boot.itb)**

```bash
sudo dd if=u-boot.itb of=/dev/sdb seek=16384; sync
```

```{warning}
The block device `/dev/sdb` may be different as per the number of storage
devices connected to your PC.

To check the block device of the SD-Card, run `dmesg -Hw` in a terminal and
plug the SD-Card into your PC. Confirm with `parted /dev/sd<X>` or `lsblk`.
```

:::

:::{tab-item} Flashing on NVMe

1. Plug the NVMe into the NVMe reader and insert it into your PC.

2. Use the linux `dd` utility to write the images. (Assuming the NVMe is at
   `/dev/nvme0n1`)

**Secondary Program Loader (idbloader)**

```bash
sudo dd if=idbloader.img of=/dev/nvme0n1 seek=64; sync
```

**U-Boot FIT image (u-boot.itb)**

```bash
sudo dd if=u-boot.itb of=/dev/nvme0n1 seek=16384; sync
```

```{warning}
The block device `/dev/nvme0n1` may be different as per the number of storage
devices connected to your PC.

Confirm the block device using `parted /dev/nvme<X>n1` or `lsblk`.
```

:::

::::

Finally reboot the board (if you used `dd` instead of `upgrade_tool rd`):

```bash
sudo reboot
```

## Verify the u-boot version

To ensure that U-Boot has been successfully updated, verify the version.

### Enter the u-boot shell

:::{warning}
Make sure that you have followed the serial console setup in the
[Axon serial console guide](../../linux-usage-guide/axon-linux-start-guide.md#axon-linux-uart-serial-console).
:::

1. Open your preferred serial console application.

2. Reset or power on the board.

:::{admonition} Developer Note
:class: note

Axon U-Boot allows a short delay to enter the U-Boot shell before booting the
kernel. You can also use **Ctrl + C** on the HDMI console when the Vicharak
logo appears.
:::

3. Quickly press ``CTRL+c`` when you see some logs starting to appear on the
   console.

If you have followed the above steps successfully, you should be able to access
a u-boot shell or terminal.

you can verify the u-boot version by using `version` command.

```bash
version
```

or you can just directly boot the board and see the serial console output during
the initial boot process.

There will be a version string printed on the console during boot up.

```text
U-Boot 2017.09-gXXXXXXXX-XXXXXX #vicharak (Mon DD YYYY - HH:MM:SS +0530)
```

## Getting U-Boot from APT Source

You can also install a prebuilt U-Boot package instead of building from source.

```{seealso}
Refer to [Updating U-Boot Version Using APT](axon-u-boot.md)
```

```bash
sudo apt update
sudo apt install u-boot-rk3588-axon
```

:::{seealso}
[How to build linux kernel](#build-axon-linux-kernel)

[Linux Upgrade Tool](../../linux-usage-guide/linux-axon-upgrade-tool.md)
:::
