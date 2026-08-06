.. _axon-mini-wifi-hotspot:

##################
Set WiFi hotspot
##################

This documenatation will guide, how to set hotspot manully with configuration user provide.


Using Command
=================

Set SSID and Password
--------------------

.. code::

    sudo nmcli device wifi hotspot ifname wlan0 con-name Axon-Mini-Host ssid Axon-Mini-Host password 12345678

Sets the Wi-Fi security method to use WPA-PSK (Wi-Fi Protected Access Pre-Shared Key )
--------------------------------------------------------------------------------------

.. code::

    sudo nmcli connection modify Axon-Mini-Host 802-11-wireless-security.key-mgmt wpa-psk

Set a static IPv4 address
-------------------------

.. code::
    
    sudo nmcli connection modify Axon-Mini-Host ipv4.addresses 10.9.8.7/24

Brings up the network connection
--------------------------------

.. code::

    sudo nmcli connection up Axon-Mini-Host
