##################
MIPI DSI
##################

.. image:: /_static/images/rk3576-axon-lite/axon-lite-dsi.webp
   :width: 80%

Axon Lite provides a MIPI-DSI host controller and multiple DSI lanes; a display panel is driven by a DSI bridge/panel driver with appropriate timing, format, and polarity settings. In standard configurations, TX0 on RK3576 is used for direct or bridged DSI connections to Waveshare or compatible panels.

Getting Started
----------------

Prerequisites
``````````````

- MIPI DSI Display
- Configure Kernel and make overlays according to MIPI-DSI Display
- Vicharak PCB For DSI Display
- Vicharak Flex Cable 22-Pin 0.5mm Pitch Cable (Golden Color)
- Make sure, You have installed latest kernel, If not. Please run command below.

.. code-block::

   sudo apt update
   sudo apt reinstall linux-image-6.1.75-axon-lite

Configure display timings and panel driver
```````````````````````````````````````````

For Open Source Contribution:

**Vicharak Kernel**

.. code-block:: bash

  https://github.com/vicharak-in/vicharak-linux-kernel.git


- Give support of Display driver and overlays, and compile kernel and add overlays in ``/boot/overlays-<uname -r>-axon-lite`` folder.
  You can look ``arch/arm64/boot/dts/rockchip/overlays`` folder.

- Ensure the kernel panel/bridge driver is configured with the correct mode (e.g., resolution, refresh rate, and color depth) via the device tree overlay or panel driver.

- If a custom timing is required, provide a panel node in the overlay with:
  - display-mode or timing parameters
  - pixel clock, hsync/vsync, and back porch values
  - bus format (e.g., RGB888)

Waveshare 4inch MIPI Display Support
-------------------------------------

`Waveshare 4inch DSI Displays <https://www.waveshare.com/4inch-dsi-lcd.htm>`_

Steps to follow for Configuration
````````````````````````````````````````

1. Open a terminal window (``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``Overlays`` options in it by pressing ``enter`` key.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────-───────────┐
    │ Please select an option below:                                                           │
    │                                                                                          │
    │                                   System Maintanince                                     │
    │                                       Hardware                                           │
    │                                       Overlays                                           │
    │                                     Connectivity                                         │
    │                                   Advanced Options                                       │
    │                                     User Settings                                        │
    │                                     Localization                                         │
    │                                         About                                            │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘


4. You will see Warning Page, click on ``yes`` and select ``Manage Overlays`` options.


.. code-block:: console


    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Configure Device Tree Overlay                                                            │
    │                                                                                          │
    │                                Manage overlays                                           │
    │                                View overlay info                                         │
    │                                Install 3rd party overlay                                 │
    │                                Reset overlays                                            │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘


5. Select overlays as per your connection of MIPI Display of connector **Tx0** by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. code-block:: console


    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │  [ ] Enable IMX219 camera on R-Pi connector / DCPHY RX0 (Axon Lite V0.2)                 │
    │  [ ] Enable IMX415 camera on CSI connector (Axon Lite V0.2)                              │
    │  [ ] Enable IMX415 camera on R-Pi connector / DCPHY RX0 (Axon Lite V0.2)                 │
    │  [*] Enable MIPI DSI Waveshare 4 Inch Panel on Axon Lite V0.2                            │
    │  [ ] Enable PWM2_CH2_M3 on 30 Pin GPIO Header Axon Lite V0.2                             │
    │  [ ] Enable PWM2_CH4_M2 on 30 Pin GPIO Header Axon Lite V0.2                             │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 connector (Axon Lite V0.2)                │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI2 connector (Axon Lite V0.2)                │
    │  [ ] Enable Sata0 support on Combo PHY 0 on Axon Lite V0.2                               │
    │  [ ] Enable Sata1 support on Combo PHY 1 on Axon Lite V0.2                               │
    │  [ ] Enable U-FL antenna (Axon Lite V0.2)                                                │
    │  [ ] Enable UART3m0 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    │  [ ] Enable UART3m1 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    │  [ ] Enable UART5m0 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    │  [ ] Enable USB3.0 support on Combo PHY 1 on Axon Lite V0.2                              │
    │  [ ] Enable can3m3 on 30 Pin GPIO Header Axon Lite V0.2                                  │
    │  [ ] Enable sai0 on 30 Pin GPIO Header Axon Lite V0.2                                    │
    │  [ ] Enable sai1m1 on 30 Pin GPIO Header Axon Lite V0.2                                  │
    │  [ ] Enable sai3m2 on 30 Pin GPIO Header Axon Lite V0.2                                  │
    │  [ ] Enable spi1 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable spi3 on 30 Pin GPIO Header axon-lite V0.2                                    │
    │  [ ] Enable uart7 on 30 Pin GPIO Header Axon Lite V0.2                                   │
    │  [ ] Enable uart8m0 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    │  [ ] Enable uart8m1 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    │  [ ] Enable uart8m2 on 30 Pin GPIO Header Axon Lite V0.2                                 │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.


Verify after reboot
````````````````````

.. .. image:: /_static/images/rk3576-axon-lite/axon-lite-dsi-waveshare.webp
.. :width: 35%


- **xrandr** will be shown all supported resolution by DSI Display.

.. code-block:: none

   xrandr


- Check kernel **logs** for DSI panel/properties:

.. code-block:: none

     dmesg | grep -i dsi

- Confirm a display is **active** (if supported by the kernel):

.. code-block:: none

     ls /sys/class/graphics/fb*

.. code-block:: none

     cat /sys/class/graphics/fb0/name

Troubleshooting
````````````````
- If **dmesg** reports inability to initialize DSI, verify:
  - TX0 wiring and connector integrity
  - Correct overlay name and that the overlay is loaded
  - Kernel supports the specific MIPI Display
- If the display remains dark, check that a valid panel/bridge device is registered and that the framebuffer is assigned (fb0, fb1, etc.)
- Review documentation for model-specific timing and initialization sequences of Display
