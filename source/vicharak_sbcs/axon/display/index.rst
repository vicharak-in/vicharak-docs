####################################
Display Interfaces
####################################

Axon supports up to 4 independent displays simultaneously using the RK3588 display subsystem.

The RK3588 contains four internal display controllers called Video Ports (VP0, VP1, VP2, VP3). Each Video Port can drive one display output independently. Therefore, a maximum of four independent displays can be active at the same time.

Physical display connectors on the board are mapped internally to these Video Ports through various display interfaces such as HDMI, DisplayPort, and MIPI-DSI.

.. image:: /_static/images/rk3588-axon/axon-videoPorts.webp
   :width: 70%

Video Ports Specifications
==========================

+----------+--------------------------------+
| Video    | Max Output Resolution          |
| Port     |                                |
+==========+================================+
| VP0      | 7680×4320 @ 60Hz              |
+----------+--------------------------------+
| VP1      | 4096×4320 @ 60Hz              |
+----------+--------------------------------+
| VP2      | 4096×4320 @ 60Hz              |
+----------+--------------------------------+
| VP3      | 2048×1080 @ 60Hz              |
+----------+--------------------------------+

Available Display Interface Ports on Axon
=========================================

Axon exposes multiple physical display interface ports. These connectors are internally mapped to the four Video Ports.

.. note::

   Although six physical display connectors are available, only four independent displays can be active simultaneously due to the hardware limitation of four Video Ports.

   Any combination of up to four display interface ports can be used simultaneously.

Available display interface ports:

1. HDMI TX0
2. HDMI TX1
3. MIPI-DPHY TX0
4. MIPI-DPHY TX1
5. Type-C1/DP (USB-C)
6. Type-C0/DP (USB-C)

Detailed documentation for each interface is provided below:

.. toctree::
   :maxdepth: 3

   HDMI TX 2.1  <display-interfaces>
   MIPI DSI 2.0 <mipi-dsi>
   Type-C DisplayPort 1.4a <type-c-dp>
