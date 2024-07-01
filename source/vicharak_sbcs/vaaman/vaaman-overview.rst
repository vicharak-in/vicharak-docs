Overview
========

Who is Vaaman For?
------------------

Vaaman is useful to a wide range of users, these include but are not limited to:

**Software Developers**:
    A significant portion of the user base consists of software developers who utilize the SBC's FPGA capabilities to optimize software performance, accelerate computations, and explore hardware acceleration.

**Researchers**:
    Vaaman with its FPGA attracts researchers who leverage its potential for implementing custom algorithms, conducting experiments, and prototyping novel solutions. The FPGA serves as a valuable tool for their research endeavors.

**Hardware Designers**:
    The SBC appeals to hardware designers as it provides a platform for developing and testing hardware designs. They can use the FPGA to prototype and verify their designs efficiently, enabling rapid iterations.

**Hobbyist Users**:
    The SBC also attracts ordinary users with an interest in tinkering and learning about cutting-edge technologies. They can utilize the SBC's versatility for various projects such as robotics, home automation, and DIY electronics.

Block Diagram
-------------

.. image:: ../../_static/images/rk3399-vaaman/block_diagram.webp
   :width: 100%

Features
--------

The Vaaman Single Board Computer (SBC) offers a range of hardware features, including:

.. list-table::
   :widths: 10 50
   :header-rows: 1
   :class: feature-table

   * - **Type**
     - **Feature**
   * - Display
     - | 1 x HDMI 2.0 (Micro), Support maximum 4K\@60Hz display
       | 1 x MIPI, Support 2560x1600\@60fps output with dual channel
       | 1 x USB-C DP, Support maximum 4K\@60Hz display
   * - Audio
     - 3.5mm jack with mic
   * - Ethernet
     - 10/100/1000Mbps Ethernet (Realtek RTL8211E)
   * - Camera
     - MIPI CSI 2 lanes via FPC connector, support up to 800MB/s bandwidth
   * - Wireless
     - Integrated RTL8822CS Wi-Fi and BT Combo Module (6222B-SRC) WiFi 2.4G+5G WiFi 2T2R BT5.0
   * - PCIe
     - PCIe Interface via FPC connector
   * - USB
     - | 2x USB2.0 HOST
       | 1x USB3.0 HOST/OTG
       | 1x USB Type-C (USB3.0 / DP Alt mode)
   * - RTC
     - Support RTC, on-board backup battery interface
   * - I/O
     - | 1 x UART
       | 2 x SPI bus
       | 2 x I2C bus
       | 1 x PCM/I2S
       | 1 x SPDIF
       | 1 x PWM
       | 1 x ADC
       | 6 x GPIO
       | 2 x 5V DC
       | 2 x 3.3V power pin
   * - FPGA
     - | Efinix® T120F324 device in a 324-ball FineLine BGA package.
       | DRAM Chip DDR3 SDRAM 4Gbit 256Mx16 1.35V/1.5V.
       | 128 Mbit SPI NOR flash memory.
       | MIPI-CSI RX connector with 4 data lanes and 1 clock lane.
       | MIPI-CSI TX connector with 4 data lanes and 1 clock lane.
       | LVDS Transmitter interface connector that supports 20 Lanes.
       | LVDS Receiver interface connector that supports 20 Lanes.
       | JTAG headers for configuration.
       | User selectable voltages from 1.8 V, 2.5 V, and 3.3 V for bank 1B, 1C, and 2F.
       | 40-pin GPIO header supported with 12-pin 1 PMOD and 2 LVDS lane or 25 GPIOs.
       | 10, 20, 25, 30, 50, and 74.25 MHz oscillators for T120F324 PLL input.
       | 4 User LEDs on T120F324 bank 2F.

.. tip::

    For more information on the Vaaman GPIOs, see :ref:`vaaman-gpio-description`

|

.. seealso::

    :ref:`Getting Started  with Vicharak Vaaman <getting-started>`

    :ref:`Vaaman Application Documentation <vaaman-applications>`

    :ref:`Downloads section <downloads>`

    :doc:`Vaaman Linux Documentation <vaaman-linux/index>`
