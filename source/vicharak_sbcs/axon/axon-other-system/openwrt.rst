#################
OpenWRT for Axon
#################

`OpenWRT <https://openwrt.org/>`_ is a Linux-based, open-source operating system
designed for embedded devices such as routers and single-board computers.
It provides a fully writable filesystem with package management, allowing users
to customize the system according to their requirements.

.. image:: /_static/images/openwrt-0.webp
   :width: 95%

Steps to Follow
==================

-------------------
Image Information
-------------------

.. warning::

   - **Kernel Version:** ``5.10.238-axon``
   - **OpenWrt Version:** ``24.10.1``

-------------------
Download Image
-------------------

The latest OpenWRT image for Axon can be downloaded from the following link:

`OpenWRT Image <https://downloads.vicharak.in/vicharak-axon/openwrt/>`_

-------------------
Flashing the Image
-------------------

.. warning::

   The image can be flashed into **eMMC** or other external storage devices such as an **SD Card** or **USB Drive**.
   After flashing, make sure to power-cycle the device before booting.

------------------------------
Flash Image into eMMC
------------------------------

Follow this guide for flashing the image into eMMC:

`Flashing Guide Using Linux_Upgrade_Tool (Linux) </vicharak_sbcs/axon/axon-linux/linux-usage-guide/linux-axon-upgrade-tool/#flash-raw-image-in-axon>`_

--------------------------------
Flash Image into SD Card / USB
--------------------------------

Follow this guide to flash the image into an SD Card or USB drive:

`Flashing Guide Using Balena Etcher </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-raw-image/#flashing-with-balena-etcher>`_

Accessing Axon via Wi-Fi
=========================

After booting Axon, the **OpenWRT** Wi-Fi hotspot is automatically enabled.

.. danger::

   Make sure an antenna is connected to the Wi-Fi U.FL connector.

- **SSH:** ``ssh root@10.0.0.1``
- **HTTP:** ``10.0.0.1``

.. note::

   - **Username:** root  
   - **Password:** root

Steps:

1. Connect your host device to the **OpenWRT** Wi-Fi network.  
2. Open ``10.0.0.1`` in a web browser and enter the password ``root``.  
3. The LuCI web interface will be displayed.

.. image:: /_static/images/openwrt-1.webp
   :width: 95%

Configuring Wi-Fi Access Point
===============================

By default, the Wi-Fi Access Point is already configured.  
However, users can modify the configuration using the LuCI interface.

Navigate to **Network → Wireless** to manage Wi-Fi settings.

Configuring Axon as a Router
=============================

1. Go to **Network → Firewall**.  
2. Click on **NAT Rules**.

.. image:: /_static/images/openwrt-3.webp
   :width: 95%

3. To configure a NAT rule, click the **Edit** button.

.. image:: /_static/images/openwrt-4.webp
   :width: 95%

4. Select **Rewrite IP Address** to the interface **end1**, which connects the Axon to the internet via Ethernet.

PCI-to-Ethernet Setup
======================

---------------
Block Diagram
---------------

.. image:: /_static/images/openwrt-5.webp
   :width: 95%

----------------
LuCI Interface
----------------

.. image:: /_static/images/openwrt-6.webp
   :width: 95%

--------------------
Physical Connection
--------------------

.. image:: /_static/images/openwrt-7.webp
   :width: 95%

Objective
==========

- Use a PCI Ethernet port (**end1**) as the uplink to the internet.  
- Create a bridge (**br-lan**) that includes multiple interfaces:
  - **Wired:** ``enP2p33s0``, ``enP3p49s0``  
  - **Wireless:** ``phy0-ap0``  
- All LAN and Wi-Fi devices receive IP addresses from the DHCP server automatically.

Notes / Troubleshooting
========================

1. **Accessing OpenWRT GUI (LuCI):**

   If ``http://10.0.0.1/`` does not open or the **OpenWRT** Wi-Fi is not visible, simply reboot the Axon by pressing the **Reset** button.

2. **Testing Connectivity:**

.. code-block:: bash

   ping -c 4 8.8.8.8

.. note::

   If you face any difficulties using ``OpenWRT``, please post your query on the `Vicharak Forum <https://discuss.vicharak.in/>`_ for community and developer support.
