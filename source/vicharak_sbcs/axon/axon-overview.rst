Overview
========

Block Diagram
-------------

.. image:: ../../_static/images/rk3588-axon/axon-v2-blockdiagram.webp
   :width: 100%

Features
--------

The Axon Single Board Computer (SBC) offers a range of hardware features, including:

.. list-table::
   :widths: 10 50
   :header-rows: 1
   :class: feature-table

   * - **Type**
     - **Feature**
   * - Display
     - | 2 X HDMI 2.1 TX (maximum support up to `8K@60fps`)
       | 2 X DP 1.4a (maximum support up to `8K@30fps`) multiplexed over Type-C DisplayPort Alt Mode
       | 2 X MIPI-DSI D-PHY TX (maximum support up to `4K@60fps`)
       | 1 X HDMI 2.0 RX / HDMI-IN (maximum support up to `4K@60fps`), supports HDCP 2.2 / 1.4
   * - Audio
     - | 2 X Analog speaker output
       | 1 X Headphone stereo output
       | 2 X HDMI audio output
       | 2 X DP audio output
       | 1 X Headphone input
       | 1 X Analog MIC input
   * - Wireless
     - Fn-Link 6252B-SR (RTL8852BS) Wi-Fi 6 (2.4GHz/5GHz dual-band) and Bluetooth 5.2
   * - Ethernet
     - 1 X RJ45, 10/100/1000Mbps (Realtek RTL8211F)
   * - Camera
     - | 4 X MIPI CSI D-PHY [2 lanes] / 2 X MIPI CSI D-PHY [4 lanes] (2.5 Gbps per lane)
       | 2 X MIPI D/C-PHY RX [4-lane D-PHY / 3-trio C-PHY] (4.5 Gbps per lane)
   * - PCIe
     - | 1 X PCIe 3.0 [4-lane] with NVMe M.2 M-Key (8 GT/s)
       | 2 X PCIe 2.1 [1-lane] via FPC connector (5 GT/s)
   * - SATA
     - | 1 X SATA 3.0 [1-lane] with 22-pin standard connector (6 Gbps)
       | 1 X SATA 3.0 multiplexed with PCIe 2.1 FPC connector (6 Gbps)
   * - USB
     - | 2 X USB 2.0 Host
       | 2 X USB 3.1 Gen 1 Type-C (with DisplayPort 1.4a Alt Mode)
   * - Real time clock
     - RTC support via built-in battery interface
   * - Video Decoder
     - | H.265 / HEVC, VP9, AVS2 up to `8K@60fps`
       | H.264 / AVC, H.264 MVC up to `8K@30fps`
       | AV1 up to `4K@60fps`
   * - Video Encoder
     - | H.264 / AVC, H.265 / HEVC up to `8K@30fps`
   * - JPEG / MJPEG
     - | JPEG Decoder up to 65536x65536 (1080p@280fps)
       | JPEG Encoder up to 8192x8192 (MJPEG supported)

Physical Information
--------------------

.. list-table::
   :header-rows: 1

   * - **Property**
     - **Details**
   * - Weight
     - 69 g
   * - Length
     - 101.5 mm
   * - Width
     - 75 mm
   * - Height
     - 21.125 mm

.. image:: ../../_static/images/rk3588-axon/axon-dimension.webp
   :width: 75%

Axon is designed to cater to a diverse audience, including but not limited to:

**Software Developers:**
    - **Leverage**: Octa-core CPU ( 4x, Arm Cortex A76 ( 2.4 Ghz ) & 4x, Arm Cortex A55 ), multi-OS support
    - **Ideal For**: Application development, performance optimization, AI-driven software
    - **Cache**: 64KB L1 data & instruction cache ( seperate ), 512KB L2 Cache for Cortex A76 also 32KB L1 data & instruction cache ( seperate ) , 128KB L2 cache for A55

**Researchers:**
    - **Leverage**: RK3588 SoC, robust NPU, extensive connectivity
    - **Ideal For**: Custom algorithms, experiments, AI and machine learning prototyping

**Hardware Designers:**
    - **Leverage**: 30-pin GPIO header, multiple interfaces
    - **Ideal For**: Developing, testing, and rapid prototyping of hardware designs

**Hobbyist Users:**
    - **Leverage**: Versatile interfaces, compact design
    - **Ideal For**: Robotics, home automation, multimedia centers, DIY electronics

**AI and Machine Learning Enthusiasts:**
    - **Leverage**: 6 TOPS NPU, major deep learning frameworks support
    - **Ideal For**: Machine learning applications, computer vision tasks

**Multimedia Professionals:**
    - **Leverage**: High-definition video, dual HDMI, USB-C for 8K output
    - **Ideal For**: Video editing, streaming, digital signage

**Educators and Students:**
    - **Leverage**: Hands-on learning tool
    - **Ideal For**: Teaching computing technologies, programming, hardware-software integration

**IoT Implementers:**
    - **Leverage**: WiFi 6, Bluetooth 5.2, peripheral interfaces
    - **Ideal For**: IoT projects, sensor integration, smart home solutions

**Gaming and Entertainment:**
    - **Leverage**: ARM Mali-G610 MC4 GPU
    - **Ideal For**: Superior gaming experience, multimedia playback
    - **Drivers**: OpenGL ES 1.1, 2.0 and 3.2, OpenCL 2.2, Vulkan1.2 etc.

.. tip::

    For more information on the Axon GPIOs, see :ref:`axon-gpio-description`

|

.. seealso::

    :ref:`Getting Started  with Vicharak Axon <axon-getting-started>`

    :ref:`Downloads section <axon-downloads>`

