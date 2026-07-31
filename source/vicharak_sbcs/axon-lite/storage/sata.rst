#############
SATA
#############

.. note::

   The vicharak-axon-lite board includes a native SATA interface designed to connect one or more SATA drives. This page documents how to use the SATA interface on the board.

Overview
--------

- The SATA interface on the vicharak-axon-lite board is exposed to the host operating system as standard storage devices (e.g., /dev/sda or /sdX).
- The interface is designed for straightforward data transfer, drive management, and typical OS-level tooling (partitioning, formatting, mounting, SMART monitoring).

.. .. image:: /_static/images/rk3576-axon-lite/axon-lite-SATA.webp
.. :width: 70%

SATA connectors and power
--------------------------

The SATA interface can be used with a SATA overlay by disabling pcie0 and enabling sata0.

Getting started
---------------

.. .. figure:: /_static/images/rk3576-axon-lite/axon-lite-sata-hat.webp
.. :width: 70%

.. Vicharak axon-lite board connected with SATA expansion board/HAT

.. note::

    In the following commands, the SATA storage device is represented as /dev/sdX. Use the lsblk command to determine the correct device name assigned by the Linux system, and replace /dev/sdX accordingly before executing the commands.


- Steps:

  1) Connect a SATA drive like a SATA HDD or SSD to the board using a Vicharak SATA expansion board or HAT with SATA data cable as shown in image above.
  2) Power on the board and boot into the operating system.
  3) Confirm the OS detects the drive:

     .. code-block:: bash

        lsblk
        sudo dmesg | grep -i sata

     to verify /dev/sdX (e.g., /dev/sda or /dev/sdb) appears.
  4) Partition and format the drive as needed:

     - Create a partition table and partitions.
     - Create filesystems (e.g., ext4, xfs).
  5) Mount the filesystem:
     - Create a mount point and mount the new partition:

     .. code-block:: bash

        sudo mkdir -p /mnt/data
        sudo mount /dev/sdX1 /mnt/data

Using Linux with the SATA interface
------------------------------------

- Detecting drives:


  .. code-block:: bash

    lsblk -f
    sudo fdisk -l
- Creating partitions and filesystems:

  .. code-block:: bash

    sudo parted /dev/sdX mklabel gpt
    sudo parted -a optimal /dev/sdX mkpart primary ext4 0% 100%
    sudo mkfs.ext4 /dev/sdX1
- Mounting and fstab:

  .. code-block:: bash

    sudo mkdir -p /mnt/data
    sudo mount /dev/sdX1 /mnt/data
- Basic health and monitoring:

  .. code-block:: bash

    sudo smartctl -a /dev/sdX
    sudo lsblk -f
    sudo blkid

Troubleshooting
---------------

- Drive not detected:

  - Verify power is connected to the drive.
  - Re-seat the SATA data and power cables.
  - Try a different SATA port on the board.

- Drive detected but inaccessible:

  - Verify partition table and filesystem:

    .. code-block:: bash

      sudo fdisk -l /dev/sdX
      sudo file -s /dev/sdX1

  - Check dmesg for errors related to the SATA controller or drive:

    .. code-block:: bash

      dmesg | grep -i sata
- Data access issues:

  - Check filesystem integrity:

    .. code-block:: bash

      sudo fsck /dev/sdX1

  - Ensure proper mounting options and permissions.
