####################################
Display Interfaces
####################################

Axon Lite supports up to 3 independent displays simultaneously using the RK3576 display subsystem.

The RK3576 contains three internal display controllers called Video Ports (VP0, VP1, VP2). Each Video Port can drive one display output independently.

Physical display connectors on the board are mapped internally to these Video Ports through various display interfaces such as HDMI, DisplayPort, and MIPI-DSI.

.. image:: /_static/images/rk3576-axon-lite/axon-lite-videoPorts.webp
   :width: 70%

Video Ports Specifications
==========================

+----------+--------------------------------+
| Video    | Max Output Resolution          |
| Port     |                                |
+==========+================================+
| VP0      | 3840x2160 @ 120Hz (4K)         |
+----------+--------------------------------+
| VP1      | 2560x1600 @ 60Hz (2K)          |
+----------+--------------------------------+
| VP2      | 1920x1080 @ 60Hz (1080p)       |
+----------+--------------------------------+

Available Display Interface Ports on Axon Lite
==============================================

Axon Lite exposes three physical display interface ports:

1. micro HDMI TX
2. Type-C DP (USB-C)
3. MIPI DSI

.. note::

   In the current configuration, we are giving **VP2** to **DP0** (Type-C DisplayPort), thus limiting its maximum output resolution to **1920x1080 @ 60Hz**.

Detailed documentation for each interface is provided below:

.. toctree::
   :maxdepth: 3

   HDMI TX 2.1  <display-interfaces>
   MIPI DSI 2.0 <mipi-dsi>
   Type-C DisplayPort 1.4a <type-c-dp>
