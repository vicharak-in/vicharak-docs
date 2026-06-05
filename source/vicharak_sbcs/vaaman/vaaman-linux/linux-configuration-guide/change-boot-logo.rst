How to change Boot Logo
=======================

This guide explains how to replace the default boot logo on Vaaman using
the Yocto kernel build system and otherwise if not on Yocto.

.. contents:: Contents
   :local:
   :depth: 3

Preparing the logo
------------------

The boot logo must follow these requirements:

- BMP v3 format
- 24-bit RGB colour depth
- Recommended resolution: ``640x272``
- Maximum safe framebuffer size: ``614400 bytes``

.. warning::

   Larger images or unsupported BMP formats may cause display failures,
   DRM crashes, or IOMMU faults during boot.

You can convert an image using ImageMagick:

.. code:: bash

   convert input.png \
   -strip \
   -resize 640x272\! \
   -type TrueColor \
   -depth 8 \
   BMP3:logo.bmp

Verify the generated image:

.. code:: bash

   file logo.bmp

Expected output:

.. code:: text

   PC bitmap, Windows 3.x format, 640 x 272 x 24

.. tip::

    - ``logo.bmp`` is used by U-Boot (the bootloader) to display the early
       boot logo.
    - ``logo_kernel.bmp`` is used by the Linux kernel when it initializes the
       framebuffer later in the boot process.

If you want the same image for both stages, copy the logo file over:

.. code:: bash

   sudo cp /boot/logo.bmp /boot/logo_kernel.bmp


On Ubuntu
---------------------------

If you are not using Yocto, simply place the two BMP files on the boot partition (mounted
at ``/boot``) and reboot.

Copy the files to the boot partition:

.. code:: bash

   sudo cp logo.bmp /boot/
   sudo cp logo_kernel.bmp /boot/

If you need to change the image size or scaling (for example to use a
fullscreen logo), you will need to rebuild the kernel after making the
required changes to the device tree (DTS). See the :ref:`fullscreen-logo-scaling`
section below for the DTS changes, and :doc:`Linux Kernel Build <../linux-development-guide/linux-kernel>`
for instructions on building and deploying a new kernel/DTB.

Example `lsblk` showing a typical eMMC layout on Vaaman with ``/boot`` mounted:

.. code:: bash

   vicharak@vicharak:~$ lsblk
   NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
   mmcblk0      179:0    0 29.1G  0 disk 
   ├─mmcblk0p1  179:1    0    4M  0 part 
   ├─mmcblk0p2  179:2    0    4M  0 part 
   ├─mmcblk0p3  179:3    0    4M  0 part 
   ├─mmcblk0p4  179:4    0  512M  0 part /boot
   ├─mmcblk0p5  179:5    0  128M  0 part 
   ├─mmcblk0p6  179:6    0   32M  0 part 
   ├─mmcblk0p7  179:7    0  256M  0 part /userdata
   └─mmcblk0p8  179:8    0 28.1G  0 part /
   mmcblk0boot0 179:32   0    4M  1 disk 
   mmcblk0boot1 179:64   0    4M  1 disk 
   zram0        254:0    0    0B  0 disk 




.. _change-boot-logo-yocto:

Yocto
-------------

Here are the prerequisites for Yocto builds:

- Yocto build environment configured for Vaaman
- ``linux-rockchip`` kernel source available
- Basic familiarity with Git and BitBake

Replacing the logo
------------------

Clone the kernel repository:

.. code:: bash

   git clone https://github.com/vicharak-in/rockchip-linux-kernel.git

Navigate to the repository:

.. code:: bash

   cd rockchip-linux-kernel

Replace both logo files:

- ``logo.bmp``
- ``logo_kernel.bmp``


.. _fullscreen-logo-scaling:

Optional: Fullscreen logo scaling
---------------------------------

To scale the logo during boot, edit:

.. code:: text

   arch/arm64/boot/dts/rockchip/rk3399-vaaman-linux.dts

Modify the HDMI route:

.. code:: dts

   &route_hdmi {
      connect = <&vopb_out_hdmi>;
      status = "okay";
      logo,mode = "fullscreen";
   };

Rebuild and deploy the updated DTB after making this change.

Applying the patch in Yocto
---------------------------

For instructions on creating and adding patches to Yocto recipes, see the
Yocto SDK guide: :doc:`Yocto SDK guide <../linux-development-guide/linux-sdk/linux-sdk-yocto>`

Add the patch to the appropriate BitBake recipe (``meta-rockchip/recipes-kernel/linux/linux-rockchip_5.10.bb`` in our case):

.. code:: bitbake

   SRC_URI += "file://0001-Replace-boot-logo.patch"

Apply and build the kernel:

.. code:: bash

   bitbake linux-rockchip -f -c patch -v
   bitbake linux-rockchip


Testing
-------

Reboot the board after flashing the updated kernel and DTB.

If successful, the new logo should appear during boot.