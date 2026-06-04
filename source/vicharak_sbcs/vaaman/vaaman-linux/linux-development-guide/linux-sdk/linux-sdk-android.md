# Android

### Installing the package dependencies for environment setup

#### Install source control tools

Building Vicharak linux systems requires both **Git** (For source code management)
and **Repo** (Google-built repository management tool).

Please refer to Android's source control tools setup (https://source.android.com/docs/setup/download) as we follow the same for building Vicharak's Linux systems.

#### Install package dependencies

:::{important}
Make sure you have properly installed `repo` tool before proceeding.
:::

**The following packages are required to build the rootfs image.**

```bash
sudo apt-get update -y

sudo apt install -y asciidoc autotools-dev bash bc binutils bison \
build-essential bzip2 chrpath cpio curl cvs dblatex default-jre \
device-tree-compiler diffstat expect-dev fakeroot file flex g++ gawk gcc \
gcc-aarch64-linux-gnu gcc-arm-linux-gnueabihf g+conf genext2fs git git-core \
git-gui gitk graphviz gzip intltool lib32stdc++6 libdrm-dev libglade2-dev \
libglib2.0-dev libgtk2.0-dev liblz4-tool libncurses5 libparse-yapp-perl \
libsigsegv2 libssl-dev libudev-dev libusb-1.0-0-dev m4 make mercurial mtools \
openssh-client parted patch patchutils perl python3 python-is-python3 \
qemu-user-static rsync sed subversion swig tar texinfo u-boot-tools unzip w3m \
wget
```

<!-- TODO: Fix when the issues section is available -->

:::{note}
The above packages might not be available to install on your system. Please
try to find the alternatives or a solution from the internet.
:::

### Getting the sources

We have structured our Linux development source code in the same way as the
official Android sources. i.e. we have various manifests with different
branches for different releases of our supported Linux distributions and products.
**repo** tool will take care of the source code syncing and updating.

Take a look at the following table to get the latest sources.

| Manifest         | Tag                 | URL                                                                                |
| ---------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Android 12       | android-12          | https://github.com/vicharak-in/rockchip-android-manifest                  |

#### Cloning the source

To clone the latest Android sources, use the following command.

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-android-manifest -b master -m rockchip-s-vicharak.xml
```

:::{tip}
You can also shallow clone entire SDK using `--depth=1` option.
Use the following command to sync the source with shallow history:

```bash
repo init --depth=1 --no-tags --no-clone-bundle -u <url> -b <branch> -m <manifest>
```

:::

#### Syncing the source

To download the code sources from the repositories to your local machine, use the following command.

```bash
repo sync -j$(nproc)
```

### Building Android 12

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the SDK source directory, and confirm that you have a `build.sh` file in the current directory.

#### 1. Source the Android 12 environment setup

```bash
source build/envsetup.sh
```

#### 2. Copy Android Specific configs into Kernel Repository

```bash
cp -vr mkcombinedroot/configs/android-1* kernel-5.10/arch/arm64/configs
```

The device specific configuration file for Android 12 is located at `device/rockchip/rk3399/vaaman.mk`

#### 3. Launch the device configuration

```bash
lunch vaaman-userdebug
```

#### 4. Building the Android 12 firmware

```bash
./build.sh -UACKup
```

```{note}
`build.sh` is the firmware build script that can be used to interactively build the firmware.
It can accept command line arguments to customize the build process.

- -U -> Build U-Boot
- -A -> Build Android
- -C -> Build kernel using clang compiler
- -K -> Build kernel
- -u -> Build rockchip update image
- -p -> Pack the firmware
```

#### 5. After the firmware is compiled, you can find an `update.img` file inside `rockdev/pack`


(firmware-file-formats)=

:::{important}

## Understanding Firmware Formats

There are two primary types of firmware formats you'll encounter:

1. **Raw Firmware:**
   - **Description:** Raw Firmware is essentially a direct copy of your storage device, capturing every bit of data as is.
   - **Flashing Tools:**
     - _For SD Card:_
       - **GUI Tools:**
         - `SDCard Installer` (Linux/Windows/MacOS)
         - `Balena Etcher` (Linux/Windows/MacOS)
       - **CLI Tool:**
         - `dd` (Linux)
     - _For eMMC:_
       - **GUI Tool:**
         - `AndroidTool/RKDevTool` (Windows)
       - **CLI Tools:**
         - `upgrade_tool` (Linux/MacOS)
         - `rkdeveloptool` (Linux)

2. **RK Firmware:**
   - **Description:** RK Firmware comes in Rockchip's proprietary format. Specific tools provided by Rockchip are used to flash this firmware onto eMMC or SD Card.
   - **Flashing Tools:**
     - _For SD Card:_
       - **GUI Tool:**
         - `SD Firmware Tool` (Windows)
     - _For eMMC:_
       - **GUI Tool:**
         - `AndroidTool/RKDevTool` (Windows)
       - **CLI Tool:**
         - `upgrade_tool` (Linux)

**Partition Image:**

- **Description:** Partition Image refers to segmented images of different
  parts of the firmware, such as boot.img, kernel.img, and system.img.
  These components are assembled like pieces of a puzzle to form a complete Android system.

- **Usage:**
  - Place each specific image (e.g., kernel.img) into its corresponding
    partition on the SD card or eMMC to construct the complete Android system.

:::

---

```{seealso}
[How to use Balena Etcher](../../../vaaman-sdcard-boot.rst)
```

```{admonition} More information
For more information about the `Linux_Pack_Firmware` tool or how to flash
firmware onto your board, please refer to the [Rockchip Development Guide](../../linux-usage-guide/rockchip-develop-guide.md)
```
