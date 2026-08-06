.. _axon-mini-qdl-tool-guide:

#######################
QDL Flash Tool Guide
#######################

Qualcomm provides the **Qualcomm Device Loader (QDL)** tool for flashing firmware
on Qualcomm SoCs. On Axon Mini, QDL is the primary tool used to flash **Linux**
images to onboard storage while the board is in **EDL (Emergency Download)**
mode.

.. tip::

   Axon Mini supports **EDL mode** (also known as Qualcomm **9008** / QDL mode),
   which allows the board to be flashed with new firmware.

   Use the **Linux QDL Tool** on Linux hosts and the **Windows QDL Tool** on
   Windows hosts.

This tool supports the following operations:

- Downloading / flashing firmware
- Writing partitions from ``rawprogram*.xml`` / ``patch*.xml``
- Fusing / programming via Firehose (``prog_firehose_ddr.elf``)
- Recovering a board that fails to boot normally

.. toctree::
   :caption: Contents
   :maxdepth: 2

   Linux QDL Tool <linux-qdl-tool>
   Windows QDL Tool <windows-qdl-tool>

Entering EDL Mode
=================

Before flashing, put Axon Mini into EDL mode:

1. Power off the board (or disconnect power).
2. Hold the **EDL** button.
3. Connect / apply power while holding EDL.
4. Release the EDL button.

The board should enumerate as a Qualcomm download device (**PID ``0x9008``**).

Verify enumeration
------------------

**Linux**

Run ``lsusb``:

.. code-block:: console

   lsusb

Example output:

.. code-block:: console

   Bus 001 Device 068: ID 05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)

**Windows**

In Device Manager, the board should appear as a Qualcomm download / QDL device
(PID ``9008``):

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-windows-edl.png
   :width: 50%
   :alt: Axon Mini in EDL mode on Windows Device Manager

See also :ref:`axon-mini-getting-started` for the button guide.
