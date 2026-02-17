
##############
HDMI RX
##############

.. image:: /_static/images/rk3588-axon/axon-hdmi1.webp
   :width: 74%

The HDMI RX (Receiver) port on Axon allows you to capture video input from HDMI sources. This documentation covers how to set up and receive video data using two Axon boards and the V4L2 (Video4Linux2) tool.

.. note::

   Instead of using another Axon board as a video source, you can use any other source. This page shows how to connect two Axon boards.


Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

- 2x Axon boards (one as TX/transmitter and one as RX/receiver)
- 2x HDMI cables 
- Mini-HDMI to HDMI converter

Hardware Setup
~~~~~~~~~~~~~~

**Connect the Boards**

1. Connect the HDMI TX output from the first Axon board (TX board) to **Mini-HDMI to HDMI converter** then connect HDMI RX input of the second Axon board (RX board) to it.
2. Power on both boards
3. Ensure both boards are running and have network connectivity

**Receiving the data**

**Verify HDMI RX Detection**

1. SSH into the RX Axon board:

.. code-block:: bash

   ssh root@<RX-BOARD-IP>

2. Install v4l2 tools

.. code-block:: bash

   sudo apt install v4l-utils

3. Check if the HDMI RX port is detected:

.. code-block:: bash

   v4l2-ctl --list-devices

4. You should see output listing the HDMI RX device (typically ``/dev/video0`` or similar):

.. code-block:: text

   rk_hdmirx (fde0000.hdmirx-controller):
      /dev/video0

5. You can get more info about connected device by :

.. code-block:: bash

   v4l2-ctl -d /dev/video0 --all

Receiving Video Data with V4L2
-------------------------------

.. note::

   You can either use qv4l2 (the official V4L2 GUI tool) to detect devices and view the video or use the terminal. Both methods are explained below.

Using qv4l2(GUI Tool)
~~~~~~~~~~~~~~~~~~~~~

**Step 1: Install the GUI tool (qv4l2) on RX Axon**

.. code-block:: bash

   sudo apt install qv4l2

**Step 2: Open qv4l2**

.. code-block:: bash

   qv4l2

**Step 3: Click the 'Start Capturing' button as shown below**

.. image:: /_static/images/rk3588-axon/axon-q4l2.webp
   :width: 70%

Using Terminal
~~~~~~~~~~~~~~

**Step 1: Verify Supported Formats**

Check the available video formats and resolutions supported by the HDMI RX:

.. code-block:: bash

   v4l2-ctl --device=/dev/video0 --list-formats-ext

Example output:

.. code-block:: text

   ioctl: VIDIOC_ENUM_FMT

   Type: Video Capture Multiplanar

   [0]: 'BGR3' (24-bit BGR 8-8-8)
   [1]: 'NV24' (Y/CbCr 4:4:4)
   [2]: 'NV16' (Y/CbCr 4:2:2)
   [3]: 'NV12' (Y/CbCr 4:2:0)

**Step 2: Detect Input Signal**

Check if a video signal is being received:

.. code-block:: bash

   v4l2-ctl --device=/dev/video0 --get-fmt-video

You should see information about the detected input resolution and format:

.. code-block:: text

   Format Video Capture:
     Width/Height      : 1920/1080
     Pixel Format      : 'UYVY'
     Field             : None
     Bytes per Line    : 3840
     Size Image        : 8294400
     Colorspace        : Default
     Transfer Function : Default
     YCbCr/HSV Encoding: Default
     Quantization      : Default

**Step 3: Capture Video Stream**

Use V4L2 to capture and save the video stream:

.. code-block:: bash

   v4l2-ctl --device=/dev/video0 --stream-mmap --stream-count=100 --stream-to=capture.yuv

This command:

- ``--device=/dev/video0``: Specifies the HDMI RX device
- ``--stream-mmap``: Uses memory-mapped I/O for efficient streaming
- ``--stream-count=100``: Captures 100 frames
- ``--stream-to=capture.yuv``: Saves the captured video to a file

**Step 4: View Captured Video**

Convert and view the captured YUV data using ffmpeg (if installed):

.. code-block:: bash

   ffplay -f rawvideo -pixel_format uyvy422 -video_size 1920x1080 -framerate 60 capture.yuv

Or save as a video file:

.. code-block:: bash

   ffmpeg -f rawvideo -pixel_format uyvy422 -video_size 1920x1080 -framerate 60 -i capture.yuv output.mp4

Common V4L2 Commands
--------------------

.. list-table::
   :header-rows: 1
   :widths: 40 50

   * - Command
     - Description
   * - ``v4l2-ctl --list-devices``
     - List all V4L2 devices
   * - ``v4l2-ctl -d /dev/video0 --list-formats-ext``
     - List supported video formats and resolutions
   * - ``v4l2-ctl -d /dev/video0 --get-fmt-video``
     - Get current video format and resolution
   * - ``v4l2-ctl -d /dev/video0 --set-fmt-video=width=1920,height=1080``
     - Set specific video resolution
   * - ``v4l2-ctl -d /dev/video0 --stream-mmap --stream-count=N``
     - Capture N frames from the HDMI RX input

Troubleshooting
---------------

**No HDMI RX device detected**

- Verify the HDMI cable is properly connected to both boards
- Ensure the TX board is actively transmitting a video signal
- Check if the HDMI RX driver is loaded: ``lsmod | grep hdmirx``
- Reboot the RX board if the device is not detected

**No signal detected in v4l2-ctl**

- Confirm the TX board is sending video data
- Check HDMI cable connectivity
- Try resetting both boards and reconnecting
- Verify the HDMI source resolution is supported by Axon

**Cannot capture video or corrupted data**

- Ensure both boards have adequate power supply
- Try capturing fewer frames first (``--stream-count=10``)
- Check if the pixel format is correct
- Verify network connectivity if using remote access

.. note::

   The HDMI RX input resolution is detected automatically from the incoming signal. The supported resolutions depend on the HDMI TX source and board capabilities up to 4K resolution.
