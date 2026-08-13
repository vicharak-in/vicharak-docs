#############
Ethernet
#############

.. important::

   Axon Mini provides Gigabit Ethernet ports via our
   :doc:`Dual Gigabit Ethernet HAT <../axon-mini-accessories/axon-mini-dual-ethernet>`
   and
   :doc:`Ethernet and Dual USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-ethernet-usb3>`
   modules!

These modules connect to the swappable PCIe HAT port (**PCIe 1**) and give
Axon Mini wired Gigabit Ethernet connectivity.

Supported Ethernet Expansion HATs
---------------------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1
   :class: feature-table

   * - **HAT**
     - **Ethernet Ports**
   * - :doc:`Dual Gigabit Ethernet HAT <../axon-mini-accessories/axon-mini-dual-ethernet>`
     - 2 × Gigabit Ethernet (RJ45)
   * - :doc:`Ethernet and Dual USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-ethernet-usb3>`
     - 1 × Gigabit Ethernet (RJ45) + 2 × USB 3.0

See :doc:`../axon-mini-accessories` for the full list of PCIe expansion modules,
and :doc:`../peripherals/pcie` for PCIe port details.

Connecting the Ethernet HAT
---------------------------

.. note::

   Connect the expansion HAT only while Axon Mini is powered off to avoid damage.

1. Power off Axon Mini and disconnect power.
2. Seat the Ethernet HAT firmly on the swappable **PCIe 1** modular port.
3. Reconnect power and boot the board.
4. Insert one end of an Ethernet cable into an RJ45 port on the HAT and connect
   the other end to a network switch, router, or Ethernet wall outlet.

The Ethernet interface supports auto-negotiation and will automatically
establish a link at the highest speed supported by both the HAT and the
connected network equipment.

Once connected, the link/activity LEDs on the RJ45 connector should illuminate
or blink to indicate a successful network connection.

Verify PCIe Enumeration
-----------------------

After installing the HAT, confirm that the PCIe endpoint is visible:

.. code-block:: console

   vicharak@axon-mini:~$ lspci

For USB/Ethernet HATs that expose a VIA USB controller, you should see an
endpoint similar to:

.. code-block:: console

   0000:01:00.0 USB controller: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller (rev 01)

See :doc:`../peripherals/pcie` for more PCIe verification steps.

Linux Support
-------------

Ethernet on these HATs is supported by the Linux kernel. No additional
out-of-tree drivers are required on the official Vicharak image.

Network interfaces usually appear as ``eth0``, ``eth1``, or similar names
depending on the HAT and Linux distribution. Dual Ethernet HATs expose two
interfaces.

Basic Linux Commands
--------------------

Check Ethernet Interface
^^^^^^^^^^^^^^^^^^^^^^^^^

List all network interfaces:

.. code-block:: bash

   ip link show

Check the IP address assigned to an Ethernet interface (replace ``eth0`` with
your interface name):

.. code-block:: bash

   ip addr show eth0

Bring Interface Up or Down
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bring the Ethernet interface up:

.. code-block:: bash

   sudo ip link set eth0 up

Bring the Ethernet interface down:

.. code-block:: bash

   sudo ip link set eth0 down

Check Link Status and Speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install ``ethtool`` if not already available:

.. code-block:: bash

   sudo apt install ethtool

Check link status and negotiated speed:

.. code-block:: bash

   ethtool eth0

Expected output includes link state and speed, for example::

   Speed: 1000Mb/s
   Duplex: Full
   Link detected: yes

Test Network Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^

Check connectivity using ping:

.. code-block:: bash

   ping -c 4 8.8.8.8

Check default gateway and routing table:

.. code-block:: bash

   ip route

Notes
-----

- Use a **CAT5e or higher** Ethernet cable to achieve Gigabit (1000 Mbps) speed.
- Always install or remove the PCIe Ethernet HAT with the board powered off.
- Link LEDs on the HAT RJ45 connector indicate activity and connection status.
- For USB ports on the Ethernet and Dual USB 3.0 Hub HAT, see
  :doc:`../peripherals/usb3`.
