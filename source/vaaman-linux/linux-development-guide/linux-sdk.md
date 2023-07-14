# Build Linux SDK from source

Vicharak Linux SDK is based on Rockchip Linux SDK.
It is a collection of tools and scripts to build Linux rootfs image for Vicharak boards.

Vicharak provides two different sources for Linux rootfs images.

1. Debian bullseye (11)
2. Ubuntu Jammy (20.04)

These sources are available at [Vicharak GitHub](https://github.com/vicharak-in)

## Build Vaaman Linux SDK

### Installing the package dependencies for environment setup

```{admonition} Prerequisites
:class: warning

You host system needs to be either Debian bullseye (11) or Ubuntu Jammy (20.04) to build the rootfs image.
```

**The following packages are required to build the rootfs image.**

```bash
sudo apt-get update

sudo apt-get install repo git-core gitk git-gui gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
gcc-aarch64-linux-gnu mtools parted libudev-dev libusb-1.0-0-dev python-linaro-image-tools \
linaro-image-tools gcc-arm-linux-gnueabihf libssl-dev liblz4-tool genext2fs lib32stdc++6 \
gcc-aarch64-linux-gnu g+conf autotools-dev libsigsegv2 m4 intltool libdrm-dev curl sed make \
binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio python unzip rsync file bc wget \
libncurses5 libqt4-dev libglib2.0-dev libgtk2.0-dev libglade2-dev cvs git mercurial rsync openssh-client \
subversion asciidoc w3m dblatex graphviz python-matplotlib libssl-dev texinfo fakeroot \
libparse-yapp-perl default-jre patchutils swig chrpath diffstat gawk
```

### Getting the sources

TODO: Manifest setup here!

### Syncing the source

```bash
repo sync --no-tags --no-clone-bundle -j$(nproc)
```

### Compile Linux SDK

::::{tab-set}

:::{tab-item} Vaaman Ubuntu Jammy (20.04)
:selected:

The configuration file for Vaaman Ubuntu Jammy (20.04) is located at `device/rockchip/rk3399/vaaman-rk3399-ubuntu.mk`

#### Source the Ubuntu configuration file

```bash
./build.sh device/rockchip/rk3399/vaaman-rk3399-ubuntu.mk
```

To ensure successful configuration, `the device/rockchip/.BoardConfig.mk` will be linked to the effective configuration file.
It is recommended to verify the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-ubuntu.mk` is the configuration file obtained after compiling the Ubuntu firmware.
Users can also create new configuration files based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for make update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-ubuntu-package-file
```

#### The root file system image path

```bash
# rootfs image path
export RK_ROOTFS_IMG=xxxx/xxxx.img
```

```

````

#### Building the Ubuntu firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```

The compiled firmware will be located in the `rockdev` directory.

:::

:::{tab-item} Vaaman Debian bullseye (11)

The configuration file for Vaaman Debian bullseye (11) is located at `device/rockchip/rk3399/vaaman-rk3399-debian.mk`

#### Source the Debian configuration file

```bash
./build.sh device/rockchip/rk3399/vaaman-rk3399-debian.mk
```

To ensure successful configuration, `the device/rockchip/.BoardConfig.mk` will be linked to the effective configuration file.
It is recommended to verify the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-debian.mk` is the configuration file obtained after compiling the Debian firmware.

Users can also create new configuration files based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for make update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-debian-package-file
```

#### The root file system image path

```bash
# rootfs image path
export RK_ROOTFS_IMG=xxxx/xxxx.img
```

```

````

#### Building the Debian firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```

The compiled firmware will be located in the `rockdev` directory.
:::

::::

### Partial compilation feature

If you only need to compile a certain part of the firmware.
Use the following command to compile the corresponding part of the firmware.

#### Kernel

```bash
./build.sh kernel
```

#### U-boot

```bash
./build.sh uboot
```

#### Recovery

```bash
./build.sh recovery
```

#### Rootfs

```bash
./build.sh rootfs
```

## Packing the firmware

````{admonition} Important
:class: tip

Before packing the firmware, you need to make sure that the firmware has been compiled successfully.

```
ls -l

├── boot.img -> ~/vicharak/linux_sdk/kernel/boot.img
├── idbloader.img -> ~/vicharak/linux_sdk/u-boot/idbloader.img
├── MiniLoaderAll.bin -> ~/vicharak/linux_sdk/u-boot/rk3399_loader_v1.20.130.bin
├── misc.img -> ~/vicharak/linux_sdk/device/rockchip/rockimg/wipe_all-misc.img
├── parameter.txt -> ~/vicharak/linux_sdk/device/rockchip/RK3399/parameter-ubuntu.txt
├── recovery.img -> ~/vicharak/linux_sdk/buildroot/output/rockchip_rk3399_recovery/images/recovery.img
├── rootfs.img -> ~/vicharak/linux_sdk/ubuntu/ubuntu-focal.img
├── trust.img -> ~/vicharak/linux_sdk/u-boot/trust.img
├── uboot.img -> ~/vicharak/linux_sdk/u-boot:/uboot.img
└── userdata.img
```
````

After the firmware is compiled, you can use the following command to pack the firmware.

```bash
./mkfirmware.sh
```

### Pack the firmware into a single image

````{admonition} Important
:class: note

Please make sure that the `tools/linux/Linux_Pack_Firmware/rockdev/package-file` is the correct package file.

The partition information in the package file is very important.
If the partition information is incorrect, the firmware will not be able to boot normally.

The packed firmware image will be located in the `rockdev/pack/` directory.

##### Rockhip Pack Firmware Image

Rockchip provides a tool called `Linux_Pack_Firmware` to pack the firmware into a single image.
It uses Rockchip's own image format,
and can be used to flash the firmware to the eMMC of the development board or any SD Card using the tools provided by Rockchip.

```bash
./build.sh updateimg
```


```{seealso} Learn more about the Rockchip paramater.txt file\
[Rockchip paramater.txt](./rockchip-parameter-file.md)
```

````

---

### Vicharak RAW Image

Vicharak provides another method to pack the firmware into a single image.
This script uses the RAW image format,
and can be used to flash the firmware to the eMMC of the development board or any SD Card using
the `dd` command or using `Balena Etcher` tool.

```{seealso}
[How to use Balena Etcher](#how-to-use-balena-etcher)
```

```bash
./build.sh rawimg
```

```{admonition} References

For more information about the `Linux_Pack_Firmware` tool, please refer to the following link.\
[Linux_Pack_Firmware](../linux-usage-guide/rockchip-develop-guide.md)

Also check out the following link for\
[How to flash the firmware]()

```
