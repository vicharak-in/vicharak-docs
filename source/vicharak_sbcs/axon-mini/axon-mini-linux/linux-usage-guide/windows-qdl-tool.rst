.. _axon-mini-windows-qdl-tool:

###################
Windows QDL Tool
###################

This guide explains how to install the Qualcomm Device Loader (QDL) on Windows
and flash a raw eMMC image to Axon Mini.

Download QDL Tool
=================

Download the Windows QDL package:

`Qualcomm Device Loader (Windows) <https://softwarecenter.qualcomm.com/catalog/item/Qualcomm_Device_Loader?osArch=X86&osType=Windows&version=2.7.1>`_

Extract the archive, then open the extracted ``QDL_Win_x64`` directory.

Install WinUSB Driver
=====================

1. Open the QDL folder.
2. Run ``install_driver.bat``.

Flash Raw Image to eMMC
=======================

1. Download the Debian eMMC image package (with XML flashing files) from
   :ref:`axon-mini-downloads`.

2. Extract the image package and enter the directory:

.. code-block:: console

   tar -xvf V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc.tar.gz
   cd V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc

3. Put Axon Mini into **EDL mode** (see :ref:`axon-mini-qdl-tool-guide`).

4. Run QDL from PowerShell (or Command Prompt):

.. code-block:: console

   & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Example:

.. code-block:: console

   PS C:\Users\Vicharak\Downloads\QCM6490_bootbinaries\QCM6490_bootbinaries> & "C:\Users\Suraj Sonawane\Downloads\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Expected output (abbreviated):

.. code-block:: console

   Flashing device (PID 0x9008, serial: 2E5ABDDD)
   device is already in Firehose mode, skipping Sahara
   waiting for Firehose programmer...
   flashed "xbl_a" successfully
   flashed "xbl_b" successfully
   ...
   flashed "system" successfully
   flashed "PrimaryGPT" successfully
   flashed "BackupGPT" successfully
   26 patches applied
   partition 0 is now bootable

.. note::

   ``-s emmc`` selects eMMC as the target storage device.

   UFS flashing will be documented separately.

.. note::

   If wildcards are not expanded in your shell, list each ``rawprogram`` /
   ``patch`` XML file explicitly in the command.

5. After a successful flash, disconnect power, then power on the board normally
   (without holding the EDL button).

.. warning::

   Do not interrupt flashing once it has started. Wait until you see
   ``partition 0 is now bootable``.
