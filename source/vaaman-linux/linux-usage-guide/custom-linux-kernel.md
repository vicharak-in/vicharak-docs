# How to use custom linux kernel

:::{important}
[Read the linux development guide first](#build-linux-kernel)
:::

(flash-custom-kernel)=

## How to flash compiled linux kernel

::::{tab-set}
:::{tab-item} Simple Copy Image method

<br/>

### Copy the compiled kernel image to the device

```bash
scp out/arch/arm64/boot/Image <user>@<device-ip>:~/
scp out/arch/arm64/boot/dts/rockchip/rk3399-vaaman-linux.dtb <user>@<device-ip>:~/

scp out/modules_rk3399_vaaman.tar.gz <user>@<device-ip>:~/
```

### Flash the kernel image

1. **ssh** login into the device or open the terminal on the device running linux
   system and run the following commands

```bash
sudo cp Image /boot/Image
sudo cp rk3399-vaaman-linux.dtb /boot/rk3399-vaaman-linux.dtb
```

2. Copy modules to the device

```bash
sudo tar -xvf modules_rk3399_vaaman.tar.gz -C /
```

### Reboot the device

```bash
sudo reboot
```

:::

:::{tab-item} Installing as a debian package

#### You can install the linux kernel as a debian package

Vicharak has created a custom package configuration for building a fully functional
debian package for the linux kernel.

```bash
sudo apt install linux-image-rk3399-vaaman-XXXXXX.deb
```

After successful installation you can safely reboot your board.

### Reboot the device

```bash
sudo reboot
```

:::

:::{tab-item} Flashing using **dd** tool

#### You can also flash the boot image using the following commands

<br />

```bash
sudo dd if=boot.img of=/dev/mmcblkXp4 status=progress; sync
```

```{note}
Here `mmcblkXp4` is the boot partition of the device. Replace `X` with the device number

0. SD-card
1. eMMC
```

:::
::::

:::{seealso}
For flashing the boot image using Rockchip upgrade tool refer to
[Rockchip Linux Upgrade Tool](./rockchip-upgrade-tool-misc.rst)
:::

(vicharak-kernel-script)=

## Introduction to Vicharak kernel building script

:::{admonition} Vicharak kernel build script usage
:class: info

```bash
--------------------------------------------------------------------------------
    Build script for Vicharak kernel
    Usage: ./build.sh [OPTIONS]
    Options:
      lunch                	Lunch device to setup environment
      info                 	Show current kernel setup information
      clean                	Cleanup the kernel build files
      kernel               	Build linux kernel image
      update               	Update defconfig with latest changes
      help                 	Show this help

    Example: ./build.sh <lunch|info|clean|kernel|update|help>
--------------------------------------------------------------------------------
```

:::

Vicharak kernel build script is a script written in bash that makes it easy for users to compile the kernel
based on their specific needs. It offers a set of customization options that can be adjusted as desired.

For example, users can choose whether to use clang or GCC as the compiler for the kernel compilation.
They can also decide whether to include the building of kernel modules or not.
This script gives users the flexibility to customize the kernel compilation process according to their preferences and requirements.

:::{admonition} Fact
:class: info
This script automates the process of getting the compatible toolchain to compile the kernel.
:::

**lunch**
: Allows to select the specific vicharak device configuration.
For example:
:::{card} ./build.sh lunch

```bash
    processing option: lunch
----------------------------------------------------------------
1) rk3399_vaaman.mk
2) rk3588_axon.mk
Select device: 1
----------------------------------------------------------------
```

:::

**info**
: Displays the current kernel setup information.

:::{card} ./build.sh info

```bash
    processing option: info
----------------------------------------------------------------
    Device Building Information
----------------------------------------------------------------
    Device makefile: rk3399_vaaman.mk
    Device name: rk3399_vaaman
    Device defconfig: rockchip_linux_defconfig
    Device config fragment: rk3399_vaaman.config
    Device DTB: rk3399-vaaman-linux
    Device compiler: Clang
    Build kernel modules: Yes
    Build debian package: No
--------------------------------------------------------------------------------
    Build script for Vicharak kernel
    Usage: ./build.sh [OPTIONS]
    Options:
      lunch                	Lunch device to setup environment
      info                 	Show current kernel setup information
      clean                	Cleanup the kernel build files
      kernel               	Build linux kernel image
      dtbs                 	Build linux dtbs
      kerneldeb            	Build linux kernel debian package
      update_defconfig     	Update defconfig with latest changes
      help                 	Show this help

    Example: ./build.sh <lunch|info|clean|kernel|update_defconfig|help>
--------------------------------------------------------------------------------
```

:::

**clean**
: Cleans up the kernel build files.

:::{card} ./build.sh clean
:::

**kernel**
: Builds the linux kernel image.

:::{card} ./build.sh kernel

```bash
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang: 17
----------------------------------------------------------------
..
..
..
----------------------------------------------------------------
    Kernel build completed
----------------------------------------------------------------
```

:::

**dtbs**
: Builds the linux dtbs.

:::{card} ./build.sh dtbs

```bash
    processing option: dtbs
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang: 17
----------------------------------------------------------------
make[1]: Entering directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
  DTC     arch/arm64/boot/dts/rockchip/rk3399-vaaman-android.dtb
  DTC     arch/arm64/boot/dts/rockchip/rk3399-vaaman-linux.dtb
make[1]: Leaving directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out/arch/arm64/boot/dts
----------------------------------------------------------------
    DTBS build completed
----------------------------------------------------------------
```

:::

**kerneldeb**
: Builds the linux kernel debian package.

:::{card} ./build.sh kerneldeb

```bash
    processing option: kerneldeb
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang: 17
----------------------------------------------------------------
..
..
..
----------------------------------------------------------------
    Deb package build completed
----------------------------------------------------------------
```

:::

**update_defconfig**
: Updates defconfig with latest changes.

:::{card} ./build.sh update_defconfig

```bash
    processing option: update_defconfig
----------------------------------------------------------------
    Using standalone clang: 17
----------------------------------------------------------------
...
----------------------------------------------------------------
    Updated rockchip_linux_defconfig with savedefconfig
----------------------------------------------------------------
```

:::

**help**
: Displays the help menu.

:::{card} ./build.sh help

```bash
└─[󰄛] ./build.sh help
--------------------------------------------------------------------------------
    Build script for Vicharak kernel
    Usage: ./build.sh [OPTIONS]
    Options:
      lunch                	Lunch device to setup environment
      info                 	Show current kernel setup information
      clean                	Cleanup the kernel build files
      kernel               	Build linux kernel image
      dtbs                 	Build linux dtbs
      kerneldeb            	Build linux kernel debian package
      update_defconfig     	Update defconfig with latest changes
      help                 	Show this help

    Example: ./build.sh <lunch|info|clean|kernel|update_defconfig|help>
--------------------------------------------------------------------------------
```

:::

:::{seealso}
[Flash kernel image with Linux_Upgrade_Tool](#rockchip-upgrade-tool-misc)

[Flash individual images with Linux_Upgrade_Tool](#rockchip-upgrade-tool-misc)

[Frequently Asked Questions](#faq)
:::
