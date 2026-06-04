#########################################
Peer-to-peer networking via WiFi Direct
#########################################

Sometimes you may encounter situations where you need to connect a cluster of Axons/other devices to share data over a short distance. While this is relatively trivial using wired methods, wirelessly doing so requires some extra setup steps. This page gives step-by-step instructions for setting up WiFi Direct on the Axon board, as well as similar devices.

Workflow
=========

A typical Wi-Fi network consists of multiple devices communicating through a central Access Point (AP). The AP is responsible for receiving and forwarding traffic, as well as handling routing, filtering, and other network functions. WiFi Direct removes the need for such an external device, and devices can negotiate amongst themselves. 
In this guide, we will be setting up a connection between two Axons. The process will look roughly like so:

.. image:: /_static/images/rk3588-axon/p2p_diagram.png
    :width: 70%
    :alt: P2P WiFi Direct Connection Workflow

#. Discovery - Devices locate one another using probe requests.

#. GO Negotiation - Devices negotiate which device will become the Group Owner (GO).

#. Group Formation - Once the GO has been selected, it creates a P2P group and advertises its SSID.

#. WPS Authentication - This guide uses ``wps_pbc`` for authentication, although other methods are available. During this stage, devices authenticate and join the group.

#. Data Transfer - Once connected, devices can communicate using standard networking tools and protocols.

WiFi P2P Setup
==============

This guide establishes a direct WiFi P2P connection between two Axon boards.

.. note::

   **Axon 1** acts as the Group Owner (GO).

   **Axon 2** acts as the Station (Client).

Configure P2P
=============

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        .. code-block:: bash

            sudo vim /etc/wpa_supplicant/p2p.conf

        .. code-block:: ini

            ctrl_interface=/var/run/wpa_supplicant
            update_config=1
            country=IN

            device_name=AXON_1

            p2p_go_intent=15
            p2p_go_ht40=1

    .. grid-item-card:: Axon 2

        .. code-block:: bash

            sudo vim /etc/wpa_supplicant/p2p.conf

        .. code-block:: ini

            ctrl_interface=/var/run/wpa_supplicant
            update_config=1
            country=IN

            device_name=AXON_2

            p2p_go_intent=1
            p2p_go_ht40=1


Kill Existing Instances
=======================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        .. code-block:: bash

            sudo pkill wpa_supplicant

        Verify:

        .. code-block:: bash

            ps -ef | grep wpa_supplicant

    .. grid-item-card:: Axon 2

        .. code-block:: bash

            sudo pkill wpa_supplicant

        Verify:

        .. code-block:: bash

            ps -ef | grep wpa_supplicant

Only the grep process should remain.


Start wpa_supplicant
====================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        .. code-block:: bash

            sudo wpa_supplicant \
                -Dnl80211 \
                -i wlan0 \
                -c /etc/wpa_supplicant/p2p.conf \
                -B

    .. grid-item-card:: Axon 2

        .. code-block:: bash

            sudo wpa_supplicant \
                -Dnl80211 \
                -i wlan0 \
                -c /etc/wpa_supplicant/p2p.conf \
                -B


Open Control Interface
======================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        .. code-block:: bash

            sudo wpa_cli

    .. grid-item-card:: Axon 2

        .. code-block:: bash

            sudo wpa_cli

Keep both terminals open.


Create the P2P Group
====================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        Inside ``wpa_cli``:

        .. code-block:: text

            p2p_group_add

        Expected:

        .. code-block:: text

            P2P-GROUP-STARTED wlan0 GO

    .. grid-item-card:: Axon 2

        No action required.


Enable WPS Push Button
======================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        Inside ``wpa_cli``:

        .. code-block:: text

            wps_pbc

        Expected:

        .. code-block:: text

            WPS-PBC-ACTIVE

    .. grid-item-card:: Axon 2

        No action required.


Discover the Group Owner
========================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        No action required.

    .. grid-item-card:: Axon 2

        Inside ``wpa_cli``:

        .. code-block:: text

            p2p_find

        Expected:

        .. code-block:: text

            P2P-DEVICE-FOUND <GO_MAC>

        Make a note of the Group Owner's MAC address.


Connect
=======

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        No action required.

    .. grid-item-card:: Axon 2

        .. code-block:: text

            p2p_connect <GO_MAC> pbc join

        Replace ``<GO_MAC>`` with the MAC address of the Group Owner.


Verify Success
==============

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        Inside ``wpa_cli``:

        .. code-block:: text

            status

        Expected:

        .. code-block:: text

            mode=P2P_GO
            wpa_state=COMPLETED

    .. grid-item-card:: Axon 2

        Inside ``wpa_cli``:

        .. code-block:: text

            status

        Expected:

        .. code-block:: text

            mode=station
            wpa_state=COMPLETED
            ssid=DIRECT-*


Assign IP Addresses
===================

P2P creates the wireless link but does not automatically assign IPv4 addresses.

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        Exit ``wpa_cli`` and run:

        .. code-block:: bash

            sudo ip addr add 192.168.50.1/24 dev wlan0

    .. grid-item-card:: Axon 2

        Exit ``wpa_cli`` and run:

        .. code-block:: bash

            sudo ip addr add 192.168.50.2/24 dev wlan0


Test Connectivity
=================

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Axon 1

        .. code-block:: bash

            ping 192.168.50.2

    .. grid-item-card:: Axon 2

        .. code-block:: bash

            ping 192.168.50.1

Expected output:

.. code-block:: text

    64 bytes from 192.168.50.X: icmp_seq=1 ttl=64 time=<latency>


Project Ideas
=============


Once peer-to-peer connectivity has been established, the connection can be
used for low-latency camera streaming between two Axon boards.

See :ref:`run-camera-live-stream-over-rtsp`.