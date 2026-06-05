Change Boot Logo
===================

The ``boot`` partition of the file system, includes ``logo.bmp`` and ``logo_kernel.bmp``,  which appear on screen while booting Axon. Here are the instructions to change them:

.. contents:: Contents
  :local:
  :depth: 2

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

.. important::

   - ``logo.bmp`` is used by U-Boot (the bootloader) to display the early
     boot logo.
   - ``logo_kernel.bmp`` is used by the Linux kernel when it initializes the
     framebuffer later in the boot process.

Copying to the boot partition
-------------------------------

If you want the same image for both stages, copy the logo file over:

.. code:: bash

   sudo cp /boot/logo.bmp /boot/logo_kernel.bmp

Run ``lsblk`` command to show boot partition.

.. code-block:: bash

     mmcblk0      179:0    0  29.1G  0 disk
    ├─mmcblk0p1  179:1    0     4M  0 part
    ├─mmcblk0p2  179:2    0     4M  0 part
    ├─mmcblk0p3  179:3    0   512M  0 part /boot
    ├─mmcblk0p4  179:4    0   288M  0 part
    ├─mmcblk0p5  179:5    0   256M  0 part /userdata
    └─mmcblk0p6  179:6    0  28.1G  0 part /

You can change the logo and replace ``logo.bmp``, ``logo_kernel.bmp`` files with your own files.

.. warning::

   Make sure, you have to convert any logo file into ``.bmp`` format in order to apply.


Copy the files to the boot partition:

.. code:: bash

    sudo cp logo.bmp /boot/
    sudo cp logo_kernel.bmp /boot/

If you need to change the image size or scaling you will have to rebuild
the kernel after making the required DTS changes. See the :doc:`Linux Kernel Build <../../../vaaman/vaaman-linux/linux-development-guide/linux-kernel>`
guide and the Vaaman :ref:`Fullscreen logo scaling <fullscreen-logo-scaling>` section for details.
