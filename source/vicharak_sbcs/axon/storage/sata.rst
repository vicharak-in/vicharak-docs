#############
SATA
#############

.. note::

   The vicharak-axon board includes a native SATA interface designed to connect one or more SATA drives. This page documents how to use the SATA interface on the board.

Overview
--------

- The SATA interface on the vicharak-axon board is AHCI-compliant and exposed to the host operating system as standard storage devices (e.g., /dev/sdX).
- Supported drives include 2.5" and 3.5" SATA HDDs and SSDs, powered by the board or an attached supply.
- Additional power slots are also given besides the SATA slot of 5v and 12v for power supply.
- The interface is designed for straightforward data transfer, drive management, and typical OS-level tooling (partitioning, formatting, mounting, SMART monitoring).

.. image:: /_static/images/rk3588-axon/axon-SATA.webp
   :width: 70%

SATA connectors and power
--------------------------

- Data connector: standard 7-pin SATA data connector.
- Power connector: power slots are provided for 5v and 12v besides SATA slot
- Cables: use proper SATA data and power cables.

Getting started
---------------

.. image:: /_static/images/rk3588-axon/axon-sataConnection.webp
   :width: 70%

- Prerequisites:
  - A powered vicharak-axon board with an operating system installed that supports SATA/AHCI (Linux is demonstrated here).
  - One SATA data cable and a suitable power source for connected drives.
- Steps:

  1) Connect a SATA drive to the board using a SATA data cable.
  2) Connect the drive’s power via the SATA power connector from the board or the power supply.
  3) Power on the board and boot into the operating system.
  4) Confirm the OS detects the drive:
     - Linux: run lsblk or dmesg | grep -i sata to verify /dev/sdX appears.
  5) Partition and format the drive as needed:

     - Create a partition table and partitions.
     - Create filesystems (e.g., ext4, xfs).
  6) Mount the filesystem:
     - Create a mount point and mount the new partition, e.g., sudo mount /dev/sdX1 /mnt/data.

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
