#########################
Linux Development Guide
#########################

This guide focuses on the creation of the Vaaman Linux Operating System.
It includes instructions on developing components like the bootloader,
kernel, and rootfs.

U-Boot (Universal Bootloader)
------------------------------
U-Boot, or the Universal Bootloader, plays a crucial role in booting the
Linux kernel on your target hardware. It provides essential features for
initializing hardware and loading the kernel.

Linux Kernel
------------
The Linux kernel serves as the core of the operating system. This section
provides information on building and customizing the Linux kernel for
your Vicharak computer board.

Linux SDK (Software Development Kit)
------------------------------------
The Linux SDK is a crucial component for developing applications and tools
that run on your target hardware. Here, we discuss setting up the Linux SDK
and cross-compiling software for your embedded system. We will demonstrate
how to build your own Debian, Ubuntu, Yocto or Android system.

.. toctree::
   :maxdepth: 2
   :caption: Development Guide

   U-Boot <u-boot>
   Linux Kernel <linux-kernel>
   Linux SDK <linux-sdk>
