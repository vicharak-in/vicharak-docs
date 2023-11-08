(build-u-boot)=

# U-Boot (Universal Boot Loader)

## What actually is u-boot?

U-Boot `Das U-Boot` is an open-source bootloader that can be used on various
platforms such as ARM, X86, MIPS, RISC-V and many more.
It is the Universal Boot Loader project and is actually used to boot the
Linux kernel in your Vicharak board.

:::{note}
More information on u-boot can be found on [u-boot wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot).
:::

(mainline-u-boot-important)=

:::{important}
Vicharak provides two different sources of u-boot for the Vaaman board.

**1. Vendor specific u-boot**
   - Vendor specific u-boot is a fork of u-boot provided by Rockchip with
     additional features including Vaaman board support.

**2. Mainline u-boot**
   - Mainline u-boot is the upstreamed u-boot maintained by Open-source
     developers. It contains the bleeding edge features, SoC improvements and bug fixes.

There are separate methods to compile and flash u-boot for these above sources.
:::

:::{tip}
It is generally not recommended to use **mainline u-boot** with your Vicharak linux
images. Because those images follows [Rockchip's boot flow](#rockchip-boot-flow).
And things may break due to incompatible changes in mainline u-boot.

You can use mainline u-boot for your own custom images or community images such
as _Manjaro ARM, Armbian_, etc.
:::

## Build Vicharak Vaaman u-boot from source

## 1. Build Vendor specific u-boot

:::{warning}
It is recommended to use **Ubuntu 20.04** and Higher or **Debian 11**
and Higher environment for building.
:::

### Installing the system dependencies

```bash
sudo apt update -y

sudo apt-get install -y build-essential python libssl-dev git-core \
    gcc-arm-linux-gnueabi gcc-arm-linux-gnueabihf u-boot-tools \
    device-tree-compiler gcc-aarch64-linux-gnu mtools parted pv
```

### Getting the source

The source code for the u-boot has been published to our
[GitHub organisation](https://github.com/vicharak-in/u-boot-vicharak).

You can either clone the repository or download the source code from GitHub.

:::{tip}
We recommend that you use `git clone` method to clone the repository as it is
easier to maintain.
:::

#### Clone the repository using git

```bash
git clone https://github.com/vicharak-in/u-boot-vicharak -b master
```

:::{tip}
Use `git clone --depth=1` to shallow clone the repository
:::

#### Download the source code archive from GitHub

![vicharak-uboot-github](../../_static/images/vicharak-uboot-github.webp)

**Follow the steps in above image.**

1. Open the GitHub repository and click on the code section on the top right
   corner.

2. Click on the "Download ZIP" button.

3. After successful download, unpack the archive using any archiver tool (7zip, unzip, etc).

---

**Alternatively you can use your terminal to directly download the source code.**

Use the following command to download the source code

```bash
wget https://github.com/vicharak-in/u-boot-vicharak/archive/refs/heads/master.zip

unzip master.zip
```

### Compiling vendor specific u-boot

There are two methods to compile vendor specific u-boot.

1. Rockchip u-boot build script
2. Vicharak u-boot build script

#### Enter the u-boot directory

```bash
cd <u-boot-directory>
```

::::{tab-set}

:::{tab-item} Compile using Rockchip u-boot script

```bash
./make.sh rk3399-vaaman
```
:::

:::{tab-item} Compile using Vicharak u-boot script

```bash
git submodule update --init

./vicharak/build.sh vicharak/rk3399-vaaman.mk
./vicharak/build.sh -b
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

Output files will be inside current folder.
Make sure `idblock.bin`, `uboot.img` and `trust.img` images are there.

:::{card} Confirm these files in the current directory

idblock.bin

uboot.img

trust.img

rk3399_loader_v1.xx.xxx.bin
:::

:::{tip}
For Vendor u-boot source there is an option to build debian package as well.


If you are using Vicharak build script then, use the following command to build
a debian package of the uboot.

```bash
./vicharak/build.sh -B
```

or if you are using Rockchip build script then use the following command to build
a debian package of the uboot.

```bash
dpkg-buildpackage -b -rfakeroot -us -uc -a arm64
```

:::

(flash-u-boot)=

## How to flash or upgrade u-boot

(rockchip-boot-flow)=

:::{note} Rockchip's boot flow

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
|        |  Program       | TPL/SPL  |idblock.bin  |         |
|        |  Loader (SPL)  |          |             |         |
|        |                |          |             |         |
| 3      |  -             | U-Boot   | u-boot.itb  | 0x4000  | including u-boot and atf
|        |                |          | uboot.img   |         | only used with miniloader
|        |                |          |             |         |
|        |                | ATF/TEE  | trust.img   | 0x6000  | only used with miniloader
|        |                |          |             |         |
| 4      |  -             | kernel   | boot.img    | 0x8000  |
|        |                |          |             |         |
| 5      |  -             | rootfs   | rootfs.img  | 0x40000 |
+--------+----------------+----------+-------------+---------+

```
Read more information on [Rockchip's boot option](http://opensource.rock-chips.com/wiki_Boot_option)
:::


Once you have successfully compiled the u-boot. You are now ready to flash it on your vaaman board.

**Secondary Program Loader (SPL)**

For Vicharak eMMC builds you can follow the `Linux Upgrade Tool` guide
:::{admonition} Refer to
[Flash u-boot to eMMC using upgrade_tool](../linux-usage-guide/rockchip-upgrade-tool-misc.rst)
:::

or

```bash
sudo dd if=idblock.bin of=/dev/mmcblk1 seek=64; sync
```

:::{warning}
The block device `/dev/mmcblk1` may be different as per the board's storage configuration.

Confirm the block device using `parted /dev/mmcblk<X>`.
:::

**U-boot proper (uboot)**

```bash
sudo dd if=uboot.img of=/dev/mmcblk1p1; sync
```

**Trust image (trust)**

```bash
sudo dd if=trust.img of=/dev/mmcblk1p2; sync
```

Finally reboot the board.

```bash
sudo reboot
```

## Verify the u-boot version

### Enter the u-boot shell or command prompt

Vaaman's u-boot is configured for development purpose.
It will allow you 3 seconds to enter the u-boot shell before booting the kernel.

Press **CTRL+c** to enter the u-boot shell.

```{tip}
Set `CONFIG_BOOTDELAY` to `0` in `configs/rk3399-vaaman_defconfig` to disable the delay.

And recompile the u-boot.
```

you can verify the u-boot version by using `version` command.

```bash
version
```

or you can just see the serial console output.

There will be a version string printed on the console during boot up.

```text
U-Boot 2017.09-ge629234bf25-230427 #vicharak (Jul 11 2023 - 16:43:11 +0530)
```

## 2. Build Mainline u-boot from source

#### Installing the required system dependencies

```bash
sudo apt-get update -y

sudo apt-get install -y build-essential python libssl-dev git-core \
    libgnutls28-dev gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
    gcc-aarch64-linux-gnu mtools parted pv
```

#### Getting the Mainline u-boot source

The source code for the mainline u-boot has been published to our
[GitHub organisation](https://github.com/vicharak-in/u-boot-vicharak/tree/vicharak-mainline).

##### Clone the repository using git

```bash
git clone https://github.com/vicharak-in/u-boot-vicharak -b vicharak-mainline
```

#### Compile ARM trusted firmware

Clone the ARM trusted firmware source code from [ARM's git server](https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git) and compile it.

```bash
git clone https://git.trustedfirmware.org/TF-A/trusted-firmware-a -b master --depth=1

cd trusted-firmware-a
```

Compile the ARM trusted firmware.

```bash
make realclean -j$(nproc --all)
make CROSS_COMPILE=aarch64-linux-gnu- PLAT=rk3399 -j$(nproc --all)
```

Upon successful compilation, the `build/` directory will be created.

Now, copy the compiled `bl31.elf` file to the u-boot directory.

```bash
cp build/rk3399/release/bl31/bl31.elf <u-boot-directory>
```

#### Compile Mainline u-boot
Enter the u-boot directory and compile the u-boot.

```bash
export BL31=bl31.elf

make rk3399-vaaman_defconfig
make CROSS_COMPILE=aarch64-linux-gnu- -j$(nproc --all)
```

:::{card} Confirm these files in the current directory

idbloader.img

u-boot.itb

u-boot-rockchip.bin
:::

### Flashing Mainline u-boot

:::{important}
Please read the [Mainline u-boot note](#mainline-u-boot-important)
:::

::::{tab-set}

:::{tab-item} Flashing on SD-Cards

Vicharak's mainline u-boot supports a single boot image using binman called
`u-boot-rockchip.bin` which combines the `idbloader.img` and `u-boot.itb` images.

To write this image to a SD card, use the following commands.
(Assuming the SD card is at `/dev/sdX`.)

```bash
sudo dd if=u-boot-rockchip.bin of=/dev/sdX seek=64; sync
```
:::

:::{tab-item} Flashing on eMMC

Vicharak's mainline u-boot supports a single boot image using binman called
`u-boot-rockchip.bin` which combines the `idbloader.img` and `u-boot.itb` images.

````{note}
Follow the [u-boot USB Mass Storage (UMS) mode](../linux-usage-guide/u-boot-ums.md)
for using eMMC as a USB storage device on your Host computer and for flashing.
````

To write this image to an eMMC, use the following commands.
(Assuming the eMMC is at `/dev/sdX`.)

```bash
sudo dd if=u-boot-rockchip.bin of=/dev/sdX seek=64; sync
```

````{tip}
For Vicharak provided eMMC/SD-Card builds you need to merge partition 1 and 2
into one partition.

**Delete the trust partition**

```bash
sudo parted /dev/mmcblkX rm 2
```

**Resize the u-boot partition**

```bash
sudo parted /dev/mmcblkX resizepart 1 100%
```

**Flash the TPL/SPL combined image**

```bash
sudo dd if=u-boot-rockchip.bin of=/dev/mmcblkX seek=64; sync
```
````

:::

:::{tab-item} Flashing on NVMe

Vicharak's mainline u-boot supports a single boot image using binman called
`u-boot-rockchip.bin` which combines the `idbloader.img` and `u-boot.itb` images.

To write this image to an NVMe, use the following commands.
(Assuming the NVMe is at `/dev/nvmeX`.)

```bash
sudo dd if=u-boot-rockchip.bin of=/dev/nvmeX seek=64; sync
```

:::

::::

Finally reboot the board.

```bash
sudo reboot
```

:::{seealso}
[How to build linux kernel](#build-linux-kernel)

[How to use rockchip upgrade tool](#rockchip-develop-tool)
:::
