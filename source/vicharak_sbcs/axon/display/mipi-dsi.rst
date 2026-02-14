##################
MIPI DSI
##################

.. image:: /_static/images/rk3588-axon/axon-dsi.webp
   :width: 80%

Axon provides a MIPI-DSI host controller and multiple DSI lanes; a display panel is driven by a DSI bridge/panel driver with appropriate timing, format, and polarity settings. In standard configurations, TX0 on RK3588 is used for direct or bridged DSI connections to Waveshare or compatible panels.

Getting Started
----------------

Prerequisites
``````````````

- MIPI DSI Display
- Configure Kernel and make overlays according to MIPI-DSI Display
- Vicharak PCB For DSI Display
- Vicharak Flex Cable 30 Pin 0.4mm Pitch Cable (Golden Color)
- Make sure, You have installed latest kernel, If not. Please run command below.

.. code-block::

   sudo apt update
   sudo apt reinstall linux-image-6.1.75-axon

Configure display timings and panel driver
```````````````````````````````````````````

For Open Source Contribution:

**Vicharak Kernel**

.. code-block:: bash

  https://github.com/vicharak-in/vicharak-linux-kernel.git


- Give support of Display driver and overlays, and compile kernel and add overlays in ``/boot/overlays-<uname -r>-axon`` folder.
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


5. Select overlays as per your connection of MIPI Display of connector **Tx0 / Tx1** by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. code-block:: console

    ┌──────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
    │ Please select overlays:                                                                  │
    │                                                                                                         │
    │  [ ] Enable DP connector-split mode Axon V0.3                                            │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI0 Alpha Axon V0.3 [OFF]                     │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 Alpha Axon V0.3 [OFF]                     │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 Alpha Axon V0.3 [OFF]                     │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 Alpha Axon V0.3 [OFF]                     │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on dphy RX0 Alpha Axon V0.3 [OFF]                 │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on dphy RX1 Aplha Axon V0.3 [OFF]                 │
    │  [ ] Enable I2C1 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C2 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C5 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C7 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM0 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [ ] Enable UART1 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART4 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART6 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [*] Enable Waveshare 4inch DSI LCD DPHY TX0 Axon V0.3                                   │
    │  [ ] Enable Waveshare 4inch DSI LCD DPHY TX1 Axon V0.3                                   │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                     <Ok>                         <Cancel>                                │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘


6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.


Verify after reboot
````````````````````

.. image:: /_static/images/rk3588-axon/axon-dsi-waveshare.webp
   :width: 35%


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
  - TX0 / TX1 wiring and connector integrity
  - Correct overlay name and that the overlay is loaded
  - Kernel supports the specific MIPI Display
- If the display remains dark, check that a valid panel/bridge device is registered and that the framebuffer is assigned (fb0, fb1, etc.)
- Review documentation for model-specific timing and initialization sequences of Display
