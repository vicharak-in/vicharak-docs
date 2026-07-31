#############
USB 3.1 Gen1
#############

Axon Lite board includes one USB Type-C port, supporting USB 3.1 Gen 1 (5 Gbps) and DisplayPort output.
This guide explains how to use and inspect the Type-C USB 3.1 Gen1 interface on a Linux system. 

.. image:: /_static/images/rk3576-axon-lite/axon-lite-usb3.webp
   :width: 80%

Basic Utilities and Commands
============================

List Connected USB Devices
--------------------------

Use ``lsusb`` to displays information about USB buses and the devices connected to them.

.. code-block:: bash

    /home/vicharak# lsusb -t
    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
    |__ Port 001: Dev 002, If 0, Class=Hub, Driver=hub/4p, 480M
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 5000M
    |__ Port 004: Dev 002, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 480M
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 5000M
    
What it shows:

- USB Bus number (Bus 007, 008)

- Device number (Device 001)

- Vendor ID and Product ID (0bda:8153)

- Manufacturer and device name

.. note::

    In the output above, **Bus 002 Device 002** (a Mass Storage device, like a pen drive) is operating at SuperSpeed (**5000M** or 5 Gbps). This device is connected to a high-speed USB interface routed through the PCIe bus via a HAT.

    Users can easily expand their system with additional high-speed USB 3.0 ports using a USB PCIe HAT. Because these hubs interface directly over the high-bandwidth PCIe bus, they offer significantly faster data transfer rates (up to 5 Gbps) compared to standard USB 2.0 hubs (480 Mbps), avoiding any bottlenecks for high-speed peripherals.

    For more information on expanding with PCIe HATs, see our :doc:`../axon-lite-accessories` guide, which includes details on our Ethernet/Dual USB 3.0 Hub HAT and Quadruple USB 3.0 Hub HAT.

To get verbose information:

.. code-block:: bash

   lsusb -v

To filter by a specific device ID:

.. code-block:: bash

   lsusb -d <vendor>:<product>

.. note::

    Also See: :ref:`usb-debug`.

Host/Device Mode detection
---------------------------

- USB DRD (Dual-Role Device)

+--------------------------------------+-------------------------------+
| **USB controller's base address**    |      **Description**          |
+======================================+===============================+
|          ``23000000.usb``            |          Type-C0              |
+--------------------------------------+-------------------------------+

Go into ``root`` user by running ``su`` command. Default root password is ``root``.

.. code-block:: bash

   cat /sys/kernel/debug/usb/23000000.usb/mode

It gives you on which mode usb port act as.

- If user has connected pendrive to Axon Lite on the Type-C Port, it acts as ``host`` mode.
- If user has connected Axon Lite to Host pc on the Type-C Port, it acts as ``device`` mode.

USB Command Reference
=====================

This section lists common Linux commands used to interact with USB devices.

+----------------+-------------------------------+
| **Command**    | **Description**               |
+================+===============================+
| ``lsusb``      | List USB devices              |
+----------------+-------------------------------+
| ``usb-devices``| Detailed USB device info      |
+----------------+-------------------------------+
| ``dmesg``      | Kernel logs and hotplug info  |
+----------------+-------------------------------+
| ``mount``      | Mount USB storage device      |
+----------------+-------------------------------+


.. note::

  Speed values:
   - `1.5` Mbps - USB 1.1 (Low Speed)
   - `12` Mbps - USB 1.1 (Full Speed)
   - `480` Mbps - USB 2.0 (High Speed)
   - `5000` Mbps - USB 3.0 / USB 3.1 Gen1 (SuperSpeed)
