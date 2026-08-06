.. _axon-mini-qdl-raw-image:

######################################
How to Flash Raw Image into eMMC
######################################

This document explains how to flash a raw OS image to Axon Mini storage using
the Qualcomm Device Loader (QDL).

Supported Boot / Flash Devices
==============================

- eMMC

.. TODO: Add UFS flashing guide

.. note::

   This guide currently covers **eMMC** flashing only. UFS support will be
   added later.

Download Image
==============

Download the Axon Mini Debian eMMC image package (includes ``prog_firehose_ddr.elf``,
``rawprogram*.xml``, and ``patch*.xml``) from :ref:`axon-mini-downloads`.

Example package name:

.. code-block:: console

   V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc.tar.gz

Uncompressing the Image
=======================

.. code-block:: console

   tar -xvf <download_image.tar.gz>
   cd <extracted_image_directory>

The extracted directory should contain files similar to:

- ``prog_firehose_ddr.elf``
- ``rawprogram*.xml``
- ``patch*.xml``
- partition / image binaries referenced by the XML files

Flashing RAW Image to eMMC
==========================

Put Axon Mini into **EDL mode**, then flash using QDL:

.. tab-set::

   .. tab-item:: Linux

      Follow: :doc:`linux-qdl-tool`

      .. code-block:: console

         sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s emmc --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

   .. tab-item:: Windows

      Follow: :doc:`windows-qdl-tool`

      .. code-block:: console

         & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Successful Flash
================

When flashing completes successfully, the tool reports:

.. code-block:: console

   26 patches applied
   partition 0 is now bootable

After that:

1. Disconnect power from Axon Mini.
2. Power on the board normally (do **not** hold the EDL button).
3. The board should boot from eMMC.

.. warning::

   Ensure the board remains in EDL mode and connected over USB for the entire
   flash process. Interrupting the flash can leave the board unbootable until
   it is re-flashed.

.. seealso::

   - :ref:`axon-mini-qdl-tool-guide`
   - :ref:`axon-mini-downloads`
   - :ref:`axon-mini-getting-started`
