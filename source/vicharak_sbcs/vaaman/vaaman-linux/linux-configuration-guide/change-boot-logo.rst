How to change Boot Logo
=======================

This guide explains how to replace the default boot logo on Vaaman using
the Yocto kernel build system and otherwise if not on Yocto.

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

Manual kernel build method
---------------------------

If you are not using Yocto, you can still replace the boot logo by
directly modifying the kernel source and rebuilding the kernel.

Clone the kernel repository:

.. code:: bash

   git clone https://github.com/vicharak-in/rockchip-linux-kernel.git

Navigate to the repository:

.. code:: bash

   cd rockchip-linux-kernel

Replace the following files with your custom logo:

- ``logo.bmp``
- ``logo_kernel.bmp``

For detailed kernel build instructions, see :doc:`Linux Kernel Build <../linux-development-guide/linux-kernel>`.

Rebuild the kernel and install or flash the newly built kernel image and DTBs to the board
using your preferred flashing or deployment method. To resize the image, you may need to edit the DTS
(see :ref:`fullscreen-logo-scaling`).

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

Add the patch to the appropriate BitBake recipe (``meta-rockchip/recipes-bsp/u-boot/u-boot-rockchip.bb`` in our case):

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