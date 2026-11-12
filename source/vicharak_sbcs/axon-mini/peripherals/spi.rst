##############
SPI
##############

.. warning::

    We recommend to use Linux Kernel 7.1.0-rc4-mini+ and the latest Debian 13
    (Trixie) image from :ref:`axon-mini-downloads`, in order to support below
    overlays. Flash the image using this
    :doc:`QDL Flash Tool Guide <../axon-mini-linux/linux-usage-guide/qdl-tool-guide>`

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-7.1.0-rc4-mini+ linux-headers-7.1.0-rc4-mini+

Introduction
------------

SPI (Serial Peripheral Interface) is a widely used protocol for communication between microcontrollers and peripheral
devices like sensors, displays, and memory devices. Typically, SPI involves dedicated pins such as MOSI (Master Out
Slave In), MISO (Master In Slave Out), SCLK (Serial Clock), and SS (Slave Select).
In Axon Mini, general-purpose I/O (GPIO) pins can be repurposed to function as SPI pins.

Axon Mini provides a total of **4** SPI interfaces on the **40-pin GPIO Header**.

- **40-pin GPIO Header:** ``SPI8``, ``SPI9``, ``SPI12``, ``SPI14``

.. tip::
    For pinouts, see the :ref:`40-pin GPIO Header <40-pin-gpio-header>`.


Make Simple spidev1.0 device
----------------------------

How to use GPIO Pins as SPI Protocol ?
======================================

**Steps to follow for Configuration**

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



5. Select overlays ``( SPI1 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.

Check generated Device
======================

1. Open terminal. ( ``Ctrl + Alt + t`` )
2. Run below command :

.. code::

        ls -l /dev/spidev*

You will find ``/dev/spidev1.0`` device is created in ``/dev`` directory.
