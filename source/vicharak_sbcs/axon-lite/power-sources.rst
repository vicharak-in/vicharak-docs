.. _axon-lite-power-sources:

Power Sources
=============

Power Rating
------------

.. important::

   - **Minimum Power:** 5W (5V @ 1A or 12V @ 0.42A)
   - **Recommended Power:** 10W (5V @ 2A or 12V @ 0.83A)
   
   If you are connecting all peripherals, such as Cameras, Displays, USB, HDMI, PCIe etc. the power requirement will range between **15W-25W** (up to 5V @ 5A or 12V @ 2.1A). This is necessary when the board is running at full load.

The Axon Lite board offers multiple versatile power options to suit various use cases. Below are the 5 supported power sources:

1. 12V Power Source (Dedicated Type-C PD Port)
----------------------------------------------
You can power the board using a 12V adapter through the dedicated Type-C PD port.

- **Minimum Power:** 5W
- **Recommended Power:** 10W
- **Maximum Power:** 25W

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-power-details.webp
    :width: 60%

2. 5V Power Source (Dedicated Type-C PD Port)
---------------------------------------------
The same dedicated Type-C PD port can also accept a 5V power source.

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-5v-power.webp
    :width: 60%

3. Type-C/DP Port Power
-----------------------
The standard Type-C/DP port can also be used to power the board with a standard PD adapter.

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-typeC-power.webp
    :width: 60%

4. Power Over Ethernet (PoE)
----------------------------
Axon Lite supports Power over Ethernet (PoE), allowing you to deliver both data and power over a single Ethernet cable. This is highly useful for deployments where electrical outlets are scarce, such as remote camera installations, IoT gateways, and headless servers.

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-power-over-ethernet.webp
    :width: 60%

5. Battery Power
----------------
For portable or backup power applications, the board features a 3.7V battery connector.

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-battery-power.webp
    :width: 60%
