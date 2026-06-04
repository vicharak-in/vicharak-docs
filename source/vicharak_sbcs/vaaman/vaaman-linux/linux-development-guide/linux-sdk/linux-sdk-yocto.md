# Yocto

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
| Yocto Mickledore | -                   | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |

#### Cloning the source

To clone the latest Yocto sources, use the following command.

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
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

### Building Yocto Image

#### Mickledore (4.2)

After successfully syncing the Yocto sources, you are now ready to build a Yocto-based Linux image for Vicharak boards.

#### 1. Source the Yocto build environment

From the SDK root directory, initialize the Yocto build environment:

```bash
source oe-init-build-env
```

This will create (or switch to) a build/ directory containing the Yocto configuration files.

#### 2. Configure Yocto layers

Ensure that your conf/bblayers.conf file includes the meta-rockchip layer along with other required layers.

Example conf/bblayers.conf

```bash
POKY_BBLAYERS_CONF_VERSION = "2"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  ${TOPDIR}/../meta-openembedded/meta-oe \
  ${TOPDIR}/../meta-openembedded/meta-python \
  ${TOPDIR}/../meta-openembedded/meta-networking \
  ${TOPDIR}/../meta-openembedded/meta-filesystems \
  ${TOPDIR}/../meta-openembedded/meta-multimedia \
  ${TOPDIR}/../meta-qt5 \
  ${TOPDIR}/../meta-clang \
  ${TOPDIR}/../meta-rockchip \
  ${TOPDIR}/../poky/meta \
  ${TOPDIR}/../poky/meta-poky \
  ${TOPDIR}/../poky/meta-yocto-bsp \
"
```

::::{note}
Make sure all referenced layers exist relative to your build directory.
::::

#### 3. Select the target machine

To enable a specific Vicharak board, set the MACHINE variable in conf/local.conf.

You can find the list of supported machines at:
```bash
meta-rockchip/conf/machine/
```

Example conf/local.conf
```bash
MACHINE ?= "rk3399-vaaman"
```

#### 4. Enable systemd (recommended)

Vicharak Yocto images use systemd as the default init system. Enable it by adding the following to conf/local.conf:
```bash
INIT_MANAGER = "systemd"
```

To support Vicharak Specific Application, use below **local.conf** file :

```bash
# Copyright (c) 2023 Vicharak Computers LLP

include include/common.conf
include include/demo.conf

MACHINE_FEATURES += "ext4"
PACKAGE_CLASSES = "package_deb"
EXTRA_IMAGE_FEATURES:append = " package-management "
IMAGE_INSTALL:append = " rockchip-init rockchip-mount bitman bitman-dev rah rah-dev periplex x11-vicharak u-boot-update vicharak-config vicharak-pkg" 
KERNEL_DANGLING_FEATURES_WARN_ONLY = "1"
IMAGE_BOOT_FILES += "Image rk3399-vaaman-linux-rk3399-vaaman.dtb extlinux/extlinux.conf "
MACHINE = "rk3399-vaaman"
DISTRO_FEATURES:append = "systemd pam x11"
```

::::{note}
If another init system is already configured, ensure it is removed or overridden.
::::



#### 5. Building the Yocto image

Once the environment and configuration are complete, start building the image using bitbake.

Example build command:
```bash
bitbake core-image-full-cmdline
```

#### 6. Build output

After a successful build, the generated images can be found at:
```bash
build/tmp/deploy/images/<MACHINE>/
```

If you want to customise your build further and add a boot logo, refer to the
[Yocto section of the boot logo page](change-boot-logo-yocto).

This directory will contain:

A **.wic image (SD Card)** (bootable disk image) and can directly be flashed using **dd** command or **Balena Etcher Tool**.

**Default Credential :**

```{note}
Username : root

Password : root
```

#### 7. Flashing the firmware

The generated `.wic` image is a complete disk image that can be flashed to SD card or eMMC. For flashing instructions, refer to the [Linux Usage Guide](../../linux-usage-guide/index).

### Creating patches for Yocto

When you modify source (kernel, u-boot, or other components) outside Yocto,
generate a Git patch and add it to the appropriate BitBake recipe so Yocto can
apply it during the build. This is a general workflow you can reuse for any
component.

1. Make the change in the upstream repository and commit it:

```bash
git add <modified-files>
git commit -m "Brief description of the change"
```

2. Generate one or more patch files:

```bash
# single commit
git format-patch -1
# range of commits
git format-patch <base>..HEAD
```

3. Copy the patch(es) into the Yocto layer's recipe `files/` directory:

```bash
cp 0001-*.patch <yocto-path>/meta-<layer>/recipes-*/<recipe>/files/
```

4. Update the recipe to include the patch(s) by adding to `SRC_URI` (in the
   recipe `.bb` file):

```bitbake
SRC_URI += "file://0001-My-change.patch"
```

5. Apply and build the recipe (the `-c patch` task applies patches):

```bash
bitbake <recipe> -f -c patch
bitbake <recipe>
```

Notes:
- Use the actual recipe name (for example `linux-rockchip` or `u-boot-rockchip`).
- If you produce multiple patches, list each one in `SRC_URI`.
- Keep patch commit messages short and descriptive; follow your project's
  patch naming conventions if any.



