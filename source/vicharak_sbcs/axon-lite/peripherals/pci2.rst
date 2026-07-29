
##############
PCIe 2.1
##############

.. warning::

    We recommend using Vicharak 6.1 kernel and latest `Debian 13 trixie
    <https://downloads.vicharak.in/vicharak-axon-lite/debian/13_trixie/>`_ in order to support the overlays below. Flash Image using this `Documentation </vicharak_sbcs/axon-lite/axon-lite-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon-lite linux-headers-6.1.75-axon-lite

Introduction
------------

The Rockchip RK3576 processor featured on the Axon Lite includes two independent PCIe 2.1 controllers. Both controllers operate exclusively in **Root Complex (RC) mode** and provide high-speed data rates of up to 5 GT/s per lane. They are used for point-to-point communication with peripherals like NVMe SSDs, network cards, and expansion HATs.

PCIe 2.1 utilizes the following signal lines for data transmission and control:

- **Transmit Differential Pair (TX±)**: Carries high-speed data from the device to the host.
- **Receive Differential Pair (RX±)**: Carries high-speed data from the host to the device.
- **Reference Clock Pair (REFCLK±)**: Supplies a differential reference clock for data synchronization and serialization.
- **PCIe Reset (PERST#)**: Active-low signal to reset the PCIe interface logic on the device.
- **Wake Request (WAKE#, optional)**: Allows the device to signal the host to transition from a low-power state to an active state.
- **Clock Request (CLKREQ#, optional)**: Used by the device to request a clock from the host when transitioning from low-power to active state.

.. _pcie2_0_implementation:

PCIe 2.1 Implementation on Axon Lite
------------------------------------

Axon Lite provides support for 2 PCIe 2.1 (x1) Controllers. These controllers are operated by devices known as Combo PHYs, which share pins with other high-speed interfaces like SATA or USB 3.0. 

The following table explains the relationship between the Combo PHYs and the supported protocols on Axon Lite:

.. list-table::
   :widths: 20 30 30 20
   :header-rows: 1
   :class: feature-table

   * - **PHY**
     - **Supported Protocols**
     - **Hardware Interface**
     - **Constraints**
   * - Combo PHY 0

       ``combphy0_ps``
     -
       PCIe 2.1: ``pcie0``

       SATA: ``sata0``
     - Modular NVMe/SATA Connector
     - PCIe and SATA are mutually exclusive
   * - Combo PHY 1

       ``combphy1_psu``
     -
       PCIe 2.1: ``pcie1``

       SATA: ``sata1``

       USB3.0: ``usbhost_dwc3_0``
     - Swappable PCIe HAT Port
     - All supported protocols can be used, but only one at a time


Modular NVMe/SATA Connector (PCIe 0)
====================================

The Axon Lite features a dedicated modular connector mapped to **PCIe 0** (Combo PHY 0). This is designed for high-speed storage devices.

.. image:: /_static/images/rk3576-axon-lite/axon-lite-pcie-nvme.png
    :width: 80%

Swappable PCIe Modular Port (PCIe 1)
====================================

For expansion, **PCIe 1** (Combo PHY 1) is routed to a modular port that supports swappable HAT modules. 

.. image:: /_static/images/rk3576-axon-lite/axon-lite-pcie-hat.png
    :width: 80%

Various HATs can be mounted on this connector to expand the board's capabilities, including:
- Dual Ethernet HAT
- Ethernet + Dual USB 3.0 Hub HAT
- Quadruple USB 3.0 Hub HAT

.. warning::
    A Combo PHY supports only one protocol at a time.

    For instance, if Combo PHY 1 is configured to operate as USB 3.0, it cannot simultaneously function as a PCIe interface.
    However, if USB 3.0 is not in use, the same PHY can be reconfigured to support PCIe communication instead.

.. _device-tree-overlays:

Verifying Absence of Conflicting Device Tree Overlays
-----------------------------------------------------

To use PCIe, you must ensure that no other overlays (such as SATA or USB 3.0) are conflicting with the Combo PHY you intend to use. 

**Steps to follow for Configuration**

1. Open a terminal window (``Ctrl+Alt+T``).
2. Run command ``sudo vicharak-config`` in it.
3. Select ``Overlays`` options in it by pressing ``enter`` key.
4. You will see a Warning Page, click on ``yes`` and select ``Manage Overlays`` option.
5. Identify which Combo PHY your device is connected to. 
   - For **Combo PHY 0** (NVMe/SATA port), ensure SATA overlays for PHY 0 are disabled if you intend to use PCIe (NVMe).
   - For **Combo PHY 1** (HAT port), ensure USB 3.0 and SATA overlays for PHY 1 are disabled if you intend to use a PCIe HAT.

6. To return back to terminal, keep pressing the ``Esc`` key until you exit from it.
7. In order to enable your configuration, Restart your board or Run command ``sudo reboot`` in terminal.

Checking success of PCIe Communication
======================================

.. warning::

    Many embedded platforms and PCIe devices do not support hot plugging. Ensure the device is connected before powering on or initializing the board.

    Always load device-specific drivers and firmware. While the PCIe link may establish without drivers or firmware, most devices will not enumerate or function correctly unless the appropriate driver and firmware are installed.

The ``lspci`` command can be used to check whether the PCIe device has completed training and a link has been established. 

.. code-block:: console

    vicharak@vicharak:~$ lspci
    0000:00:00.0 PCI bridge: Rockchip Electronics Co., Ltd RK3576 (rev 01)
    0000:01:00.0 Non-Volatile memory controller: Silicon Motion, Inc. Device 2261
    0001:10:00.0 PCI bridge: Rockchip Electronics Co., Ltd RK3576 (rev 01)
    0001:11:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)


The ``dmesg | grep pcie`` command can be used to debug whether the PCIe link has been correctly initialized. The output shown below denotes successful initialization of PCIe Links for both controllers.

.. code-block:: console

   vicharak@vicharak:~$ dmesg | grep pcie
   [    9.559855] rk-pcie 2a200000.pcie: max MSI vector is 32
   [    9.559914] rk-pcie 2a200000.pcie: host bridge /pcie@2a200000 ranges:
   [    9.559965] rk-pcie 2a200000.pcie:      err 0x0020000000..0x00200fffff -> 0x0020000000
   [    9.560015] rk-pcie 2a210000.pcie: max MSI vector is 32
   [    9.560014] rk-pcie 2a200000.pcie:       IO 0x0020100000..0x00201fffff -> 0x0020100000
   [    9.560035] rk-pcie 2a200000.pcie:      MEM 0x0020200000..0x0020ffffff -> 0x0020200000
   [    9.560060] rk-pcie 2a200000.pcie:      MEM 0x0900000000..0x097fffffff -> 0x0900000000
   [    9.560065] rk-pcie 2a210000.pcie: host bridge /pcie@2a210000 ranges:
   [    9.560084] rk-pcie 2a210000.pcie:      err 0x0021000000..0x00210fffff -> 0x0021000000
   [    9.560104] rk-pcie 2a210000.pcie:       IO 0x0021100000..0x00211fffff -> 0x0021100000
   [    9.560120] rk-pcie 2a210000.pcie:      MEM 0x0021200000..0x0021ffffff -> 0x0021200000
   [    9.560148] rk-pcie 2a210000.pcie:      MEM 0x0980000000..0x09ffffffff -> 0x0980000000
   [    9.560220] rk-pcie 2a200000.pcie: iATU unroll: enabled
   [    9.560242] rk-pcie 2a200000.pcie: iATU regions: 8 ob, 8 ib, align 64K, limit 8G
   [    9.560272] rk-pcie 2a210000.pcie: iATU unroll: enabled
   [    9.560289] rk-pcie 2a210000.pcie: iATU regions: 8 ob, 8 ib, align 64K, limit 8G

.. note::

   ``2a200000.pcie`` corresponds to PCIe 0 (Modular NVMe/SATA Port).

   ``2a210000.pcie`` corresponds to PCIe 1 (Swappable PCIe HAT Port).

Testing NVMe Storage (PCIe 0)
-----------------------------

Follow these steps to interface a NVMe device with Axon Lite:

1. Verify proper overlay settings using the :ref:`guide <device-tree-overlays>` to ensure SATA is not overriding Combo PHY 0.
2. Insert the NVMe into the Modular NVMe/SATA connector and ``reboot`` Axon Lite.

.. code-block:: console

   vicharak@vicharak:~$ sudo reboot

3. Use ``lspci`` to check PCIe Link Training Success.
4. Use ``lsblk`` to check if NVMe is listed under block devices.

.. code-block:: console

   vicharak@vicharak:~$ lsblk | grep nvme
   nvme0n1      259:0    0 119.2G  0 disk
   ├─nvme0n1p1  259:1    0     4M  0 part
   ├─nvme0n1p2  259:2    0     4M  0 part
   ├─nvme0n1p3  259:3    0   512M  0 part
   ├─nvme0n1p4  259:4    0   288M  0 part
   ├─nvme0n1p5  259:5    0   256M  0 part
   └─nvme0n1p6  259:6    0 118.2G  0 part

5. If you have ``nvme-cli`` installed, you can use ``smart-log`` to test NVMe health:

.. code-block:: console

   sudo nvme smart-log /dev/nvme0n1

.. warning::

   The SSD works without manual driver or firmware installation as support is built into the kernel and the SSD has inbuilt firmware.

