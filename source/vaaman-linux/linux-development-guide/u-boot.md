# Build Vicharak Vaaman U-Boot from source

:::{note}
Vicharak provides two different source for u-boot:

1. Vendor specific u-boot source.
2. Mainline u-boot source.

There are separate methods to compile and flash u-boot for these above sources.
:::

## Build Vendor specific u-boot

### Installing the system dependencies

```bash
sudo apt-get install build-essential python libssl-dev git-core \
gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler gcc-aarch64-linux-gnu mtools parted pv
```

### Getting the source

The source code for u-boot has been published to our [GitHub organisation](https://github.com/vicharak-in).

#### Clone the repository using git

```bash
git clone https://github.com/vicharak/u-boot-vicharak
```

:::{tip}
Use `git clone --depth=1` to shallow clone the repository
:::

#### Download the source code from github

![vicharak-uboot-github](../../_static/images/vicharak-uboot-github.webp)

**Follow the steps in above image or else try downloading from terminal.**

```bash
wget https://github.com/vicharak-in/u-boot-vicharak/archive/refs/heads/master.zip

unzip u-boot-vicharak-master.zip
```

### Compiling u-boot

#### Enter the u-boot directory

```bash
cd <u-boot-directory>
```

#### Compile using Rockchip u-boot script

```bash
./make.sh rk3399-vaaman
```

#### Compile using Vicharak u-boot script

```bash
./build-uboot.sh vaaman
```

Output files will be inside `vaaman/` folder. Make sure `idbloader`, `u-boot` and `trust` images are there.

#### Compile manually using commands

```bash
make ARCH=arm rk3399-vaaman_defconfig
make ARCH=arm CROSS_COMPILE=aarch64-linux-gnu- -j$(nproc --all)
```

:::{card} Confirm these files in the current directory

idblock.bin

idbloader.img

uboot.img

trust.img

rk3399_loader_v1.xx.xxx.bin
:::

## How to flash or upgrade u-boot

Once you have successfully compiled the u-boot. You are now ready to flash it on your vaaman board.

For Vicharak EMMC builds you can follow the `Linux Upgrade Tool` guide
:::{admonition} Refer to
[Flash u-boot to eMMC using upgrade_tool](../linux-usage-guide/rockchip-upgrade-tool-misc.rst)
:::

or

You can manually flash the images using unix `dd` utility.

**Primary loader <idbloader>**

```bash
sudo dd if=idblock.bin of=/dev/mmcblk1 seek=64; sync
```

:::{warning}
The block device `/dev/mmcblk1` may be different as per the board's storage configuration.

Confirm the block device using `parted /dev/mmcblk<X>`.
:::

**Secondary loader <u-boot>**

```bash
sudo dd if=uboot.img of=/dev/mmcblk1p1; sync
```

**Trust image <trust>**

```bash
sudo dd if=trust.img of=/dev/mmcblk1p2; sync
```

Finally reboot the board.

```bash
sudo reboot
```

## Verify the u-boot version

After rebooting the board, you can verify the u-boot version using `version` command.

```bash
version
```

or

There will be a version string printed on the console during boot up.

```bash
U-Boot 2017.09-ge629234bf25-230427 #vicharak (Jul 11 2023 - 16:43:11 +0530)
```

### Enter the u-boot shell or command prompt

Vaaman's u-boot is configured for development purpose.
It will allow you 3 seconds to enter the u-boot shell before booting the kernel.

Press **CTRL+C** to enter the u-boot shell.

```{tip}
Set `CONFIG_BOOTDELAY` to `0` in `configs/rk3399-vaaman_defconfig` to disable the delay.

And recompile the u-boot.
```

:::{seealso}
[How to build linux kernel](./build-linux-kernel.md)

[How to use rockchip upgrade tool](../linux-usage-guiderrockchip-develop-guide.md)
:::
