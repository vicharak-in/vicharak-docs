Overview
========

Axon Lite is designed to cater to a diverse audience, including but not limited to:

**Software Developers:**
    - **Leverage**: Octa-core CPU ( 4x, Arm Cortex A76 ( 2.4 Ghz ) & 4x, Arm Cortex A55 ), multi-OS support
    - **Ideal For**: Application development, performance optimization, AI-driven software
    - **Cache**: 64KB L1 data & instruction cache ( seperate ), 512KB L2 Cache for Cortex A76 also 32KB L1 data & instruction cache ( seperate ) , 128KB L2 cache for A55

**Researchers:**
    - **Leverage**: RK3576 SoC, robust NPU, extensive connectivity
    - **Ideal For**: Custom algorithms, experiments, AI and machine learning prototyping

**Hardware Designers:**
    - **Leverage**: 40-Pin GPIO header, multiple interfaces
    - **Ideal For**: Developing, testing, and rapid prototyping of hardware designs

**Hobbyist Users:**
    - **Leverage**: Versatile interfaces, compact design
    - **Ideal For**: Robotics, home automation, multimedia centers, DIY electronics

**AI and Machine Learning Enthusiasts:**
    - **Leverage**: 6 TOPS NPU, major deep learning frameworks support
    - **Ideal For**: Machine learning applications, computer vision tasks

**Multimedia Professionals:**
    - **Leverage**: High-definition video, HDMI for 4K output, MIPI DSI for up to 2K output, USB-C DP for 1080p
    - **Ideal For**: Video editing, streaming, digital signage

**Educators and Students:**
    - **Leverage**: Hands-on learning tool
    - **Ideal For**: Teaching computing technologies, programming, hardware-software integration

**IoT Implementers:**
    - **Leverage**: WiFi 6, Bluetooth 5.2, peripheral interfaces
    - **Ideal For**: IoT projects, sensor integration, smart home solutions

**Gaming and Entertainment:**
    - **Leverage**: ARM Mali-G52 MC3 GPU
    - **Ideal For**: Superior gaming experience, multimedia playback
    - **Drivers**: OpenGL ES 1.1, 2.0 and 3.2, OpenCL 2.2, Vulkan1.2 etc.

Block Diagram
-------------

.. image:: ../../_static/images/rk3576-axon-lite/Axon-lite_Block_diagram.webp
   :width: 100%

Features
--------

The Axon Lite Single Board Computer (SBC) offers a range of hardware features, including:

.. list-table::
   :widths: 10 50
   :header-rows: 1
   :class: feature-table

   * - **Type**
     - **Feature**
   * - Display
     - | 1 X micro HDMI 2.1 TX
       | 1 X TYPE-C Alt DisplayPort (4 lane)
       | 1 X MIPI DSI (4 lane)
   * - Audio
     - | Audio Codec ES8316
       | 1 X Audio Jack
       | HDMI and DP audio output
   * - Wireless 
     - FG6252BSRB-03 WiFi 6 and Bluetooth 5.3 module
   * - Ethernet
     - 1 X Gigabit Ethernet (PHY 1000M) with PoE support
   * - Camera 
     - | 1 X MIPI CSI [4 lanes]
       | 4 X MIPI CSI [2 lanes]
   * - PCIE     
     - | PHY0: 1 X PCIE 2.0 (5GT/s) via B2B Connector
       | PHY1: 1 X PCIE 2.1 (x1 lane) via B2B Connector for Daughter Board
   * - SATA
     - 1 X SATA 3.1 (6GT/s) via B2B Connector (multiplexed with PCIe 2.0)
   * - USB 
     - | 1 X USB Host 2.0 (via CH334F HUB)
       | 1 X TYPE-C Alt DisplayPort
       | USB 3.0 via Daughter Board
   * - Real time clock 
     - RTC support via built-in battery interface

Physical Information
--------------------

.. list-table::
   :header-rows: 1

   * - **Property**
     - **Details**
   * - Weight
     - 69 g
   * - Length
     - 93 mm
   * - Width
     - 75 mm
   * - Height
     - 21.125 mm

.. image:: ../../_static/images/rk3576-axon-lite/axon-lite-dimension.webp
   :width: 75%

.. tip::

    For more information on the Axon Lite GPIOs, see :ref:`axon-lite-gpio-description`

|

.. seealso::

    :ref:`Getting Started  with Vicharak Axon Lite <axon-lite-getting-started>`

    :ref:`Downloads section <axon-lite-downloads>`

