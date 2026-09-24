######################
MIPI Camera Interface 
######################

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-mipi-p.webp
    :width: 80%

The Axon Lite SBC includes 5 CSI Interfaces onboard, namely 
**CSI0,** **CSI1/2** and **CSI3/4**.
CSI1 and CSI2 share the physical connector, similarly, CSI3 and CSI4 share their
physical connectors.


MIPI CSI0
==========

.. image::  /_static/images/rk3576-axon-lite/axon-lite-csi0.webp
    :width: 65%

Hardware Required
------------------

- Camera ( OV5647  or any other RPI supported camera)
- Raspberry Pi 22 Pin 0.5mm pitch Camera Cable / Raspberry Pi 5 FPC Camera Cable 22-pin 0.5mm to 15-pin 1mm

Steps to follow 
----------------
1. Connect the hardware
2. Configure the overlays
3. Run Camera

Pre-Requisites
--------------
1. You must update the kernel using the command below.

.. code-block::

   sudo apt update
   sudo apt upgrade

.. important::
    The ``ffmpeg-rockchip`` package replaces the standard ``ffmpeg`` package from the Debian servers. It is specifically optimized for Rockchip hardware to leverage hardware-accelerated video processing on Axon Lite.

2. Install ffmpeg and v4l2 tools

.. code-block::

    sudo apt install ffmpeg-rockchip
    sudo apt install v4l-utils

3. Ensure your axon-lite is powered off before connecting the camera

How to Attach Camera to Axon Lite (CSI 0)
-----------------------------------------

1. First, connect the Raspberry Pi 22 Pin 0.5mm Camera Cable to your camera module.
 
.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-start.gif
    :width: 40%

.. danger::
        Make sure the contacts of the cable are facing the correct direction relative to the connector on the camera.

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-2.gif
    :width: 40%

2. Secure the connection on the camera module side.

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-3.gif
    :width: 40%

3. Next, prepare the MIPI CSI0 port on the Axon Lite board. 

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-4.gif
    :width: 40%

4. Connect the other end of the 22 Pin Camera Cable directly to the MIPI CSI0 port on the Axon Lite.

.. note::
   Note down the pin names where you are connecting the camera. Accordingly overlay needs to be selected.

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-5.gif
    :width: 40%

5. After Using Camera, User can remove camera using twizer.


MIPI CSI-1/2 and CSI-3/4
========================

.. image::  /_static/images/rk3576-axon-lite/axon-lite-csi1234.webp
    :width: 65%

Hardware Required
------------------

- Camera ( OV5647  or any other RPI supported camera)
- Vicharak Flex Cable 40-Pin 0.4mm Pitch Cable (Golden Color)
- FPC50 15 Pin 1mm Pitch Cable
- Vicharak Camera PCB 

Steps to follow 
----------------
1. Connect the hardware
2. Configure the overlays
3. Run Camera

Pre-Requisites
--------------
Please ensure you have completed the prerequisites (updating the kernel and installing ``ffmpeg-rockchip``/``v4l-utils``) as described in the previous section. Ensure your board is powered off.

How to Attach Camera to Axon Lite (CSI-1/2 and CSI-3/4)
-------------------------------------------------------

1. Connect the Vicharak Flex Cable (40-Pin 0.4mm Pitch) to the MIPI port on the Axon Lite board.
2. Connect the other end of the Vicharak Flex Cable to the Vicharak Camera PCB.
3. Attach your camera module to the Vicharak Camera PCB.

.. danger::
        Make Pure to connect the Vicharak flex cable's AXON LITE PCB side connector to the AXON LITE board, and the display/camera side connector to the Vicharak CAM PCB.

.. note::
   Note down the pin names where you are connecting the camera. Accordingly overlay needs to be selected.

Camera Interface PCBs
=====================

Alpha PCB ( Raspberry Pi compatible )
-------------------------------------

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-alpha.webp
    :width: 30%

Enable Overlays In Axon Lite 
----------------------------

**Here, you can find which overlay should be turned on for each MIPI Connector.**

.. list-table::
   :header-rows: 1
   :widths: 15 15 15 15

   * - **Interface on Vicharak board**
     - **Lane option**
     - **Connector type**
     - **Turn on Overlay in Linux**

   * - MIPI CSI0 RX
     - 4 Lane
     - 22 Pin 0.5mm RasPi
     - RPi

   * - MIPI CSI1 & CSI2
     - 2/4 Lane
     - Vicharak α Cam PCB
     - Alpha

   * - MIPI CSI3 & CSI4
     - 2/4 Lane
     - Vicharak α Cam PCB
     - Alpha

.. note::
    **Alpha 4 lane PCB will be available soon**

.. important::
   **CSI-1/CSI-3 are 4 Lane, CSI-2/CSI-4 are 2 Lane. CSI-1/2 cannot work simultaneously, similarly CSI-3/4 cannot work at the same time**

**Steps to follow for Configuration**
    
1. Open a terminal window(``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``Overlays`` options in it by pressing ``enter`` key.
           
.. image:: /_static/images/rk3576-axon-lite/Overlays_1.webp
                   :width: 50%

4. You will see Warning Page, click on ``yes`` and select ``Manage Overlays`` options.

.. image:: /_static/images/rk3576-axon-lite/Overlays_2.webp
                   :width: 50%
    
5. Select overlays as per your camera sensor ``( OV5647 )`` and port to which it is connected ``( CSI0 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. note::

    If you want to connect multiple cameras, check which Sensor your camera is using from your camera docs like OV5647 or IMX519 and the ports to which it is connected like CSI0/CSI1/CSI3 on axon-lite. Then select the overlay according to it.
    
.. image:: /_static/images/rk3576-axon-lite/axon-lite-overlay-list.webp
                   :width: 50%
    
6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.

.. danger::
   Make sure that whenever you are going to connect Camera, Device should be power off.

Verify Camera Connection and Detection:
---------------------------------------

1. Open a terminal by clicking ctrl+alt+t 

2. Install v4l2 tools

.. code-block:: bash

   sudo apt install v4l-utils

3. Check if the camera device is detected:

.. code-block:: bash

   v4l2-ctl --list-devices

4. You should see output listing all the camera devices and sensors (look for rkisp_mainpath):

.. code-block:: text

   rkisp_mainpath (platform:rkisp0-vir0):
       /dev/video22
       /dev/video23
       /dev/video24
       /dev/video25
       /dev/video26
       /dev/video27
       /dev/video28
       /dev/media2

   rkisp_mainpath (platform:rkisp1-vir0):
       /dev/video31
       /dev/video32
       /dev/video33
       /dev/video34
       /dev/video35
       /dev/video36
       /dev/video37
       /dev/media3

.. note::

    Here, the first device below rkisp_mainpath that is /dev/video22 and /dev/video31 are your camera devices. Similarly, your cameras will be listed here, note down the device name like video22 and video31.

5. If you got the device name and number then it confirms that axon-lite has detected the Camera. If it is not visible, check the connection and pins again.

To use the camera(s):
-----------------------------------------------------------------------

.. Tip::

    Connect a monitor to axon-lite to see the captured feed.

Run Camera Using qV4l2 (GUI tool)
==================================

**Step 1: Install the GUI tool (qv4l2) on RX Axon Lite**

.. code-block:: bash

   sudo apt install qv4l2

**Step 2: Open qv4l2**

.. code-block:: bash

   qv4l2

**Step 3: Select your camera device**

1. Click on Open Devices on top-left corner

.. image:: /_static/images/rk3576-axon-lite/axon-lite-mipi-camera03.webp
           :width: 65%

2. Select the device name from here like video22 or video31 from the menu (You can get device name by running ``v4l2-ctl --list-devices``)

.. image:: /_static/images/rk3576-axon-lite/axon-lite-mipi-camera01.webp
            :width: 65%

**Step 4: Start the camera**

Click on start capturing

.. image:: /_static/images/rk3576-axon-lite/axon-lite-mipi-camera02.webp
           :width: 65%

.. tip::
    If you have connected multiple camera devices to axon-lite, open multiple qV4l2 windows in the same way and select different camera device name. Using this you can use all the MIPI ports.


Run camera live feed using ffmpeg
=================================

1. Install ffmpeg using ``sudo apt install ffmpeg-rockchip``
2. Find the camera device number and substitute in the below command
3. Run ``ffplay -f v4l2 -pixel_format nv12 -video_size 1920x1080 /dev/video<camera_device_number>``
4. In case of multiple camera open a new terminal and run the same command with different device number

Run Camera Using V4l2 Utility 
===============================

1. Use v4l2-ctl to capture camera frame data

.. note::
    
    At place of ``<camera_device_number>`` add your camera device name like 22 or 31

.. code-block::

            v4l2-ctl --verbose -d /dev/video<camera_device_number> \
            --set-fmt-video=width=1920,height=1080,pixelformat=NV12 \
            --stream-mmap=4 \
            --stream-count=60 \
            --set-selection=target=crop,flags=0,top=0,left=0,width=1920,height=1080 \
            --stream-to=sample.yuv

.. note::
        For Single Camera, Default Camera Number would be 11.
        As you can verfiy by below process.

        You can get <camera_device> Number by running below command :

        ls -l /dev/video*

        or

        v4l2-ctl --list-devices

        => /dev/video-camera0 -> video<camera_device>
        e.g. - 11, 31 etc.
 
2. Playing Captured File

.. code-block::

        ffplay -f rawvideo -pixel_format nv12 -video_size 1920x1080 -framerate 30 sample.yuv

.. tip::

    For multiple cameras, first verify and find out the device number of the camera then open a new terminal & run the same command with new device number.


Run Camera Using Python Script
==============================

.. note::

    The py script given below is for 1 camera, 
 
1. Install Python if not already installed. You can download Python from the official website: `Python Downloads <https://www.python.org/downloads/>`__.
    
for Debian-based systems (like Debian): 

.. code-block::

           sudo apt update
           sudo apt install python3-pip


2. Install the OpenCV library using pip
            
for Debian-based systems (like Debian):

.. code-block::

           pip install opencv-python
            
Setup
------

1. Open a terminal window(``Ctrl+Alt+T``).

2. To create a (``.py``) file in vim editor, Run command ``vim <file_name>.py`` in terminal. 

3. Copy this below content into the file and paste it by pressing ``Ctrl + Shift + v``, then press ``Esc`` and to save this file, type ``:wq``.


.. code-block::
   :emphasize-lines: 3

                # !/bin/env python3
                import cv2
                cap = cv2.VideoCapture(<camera_device_number>)
                while True:
                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                # After the loop release the cap object
                cap.release()
                # Destroy all the windows
                cv2.destroyAllWindows()
               
   
.. note::
        For Single Camera, Default Camera Number would be 11.
        As you can verfiy by below process.

        You can get <camera_device> Number by running below command :

        ls -l /dev/video*

        => /dev/video-camera0 -> video<camera_device>
        e.g. - 11, 31 etc.
    
.. Tip::

    For multiple cameras you just have to add more VideoCapture objects. Given below is a example of python script for 2 cameras.

.. code-block::
   :emphasize-lines: 3,4

            #!/bin/env python3
            import cv2
            cap0 = cv2.VideoCapture(<camera_device_number>)
            cap1 = cv2.VideoCapture(<camera_device_number>)
            while True:
                ret0, frame0 = cap0.read()
                ret1, frame1 = cap1.read()
                if ret0:
                    cv2.imshow("Camera 0", frame0)

                if ret1:
                    cv2.imshow("Camera 1", frame1)

                # Press q to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release cameras
            cap0.release()
            cap1.release()
            cv2.destroyAllWindows()
               

4. Open a terminal window(``Ctrl+Alt+T``).

5. Navigate to the directory where your Python program is located using the ``cd`` command.

6. Run Python program using the following command:

.. code-block::

             python3 <file_name>.py


If you have multiple versions of Python installed, ensure you use ``python3`` to run the program for Python 3.x.
 

**Troubleshooting**

- If you encounter any errors related to missing modules or libraries, ensure that Python and OpenCV are properly installed on your system.
- If the camera frame does not open or the program does not behave as expected, check for any
  errors in the terminal output and review your program for potential issues.
- Check Camera I2C address is detected or not.

.. note::
    sudo i2cdetect -y <i2c_bus_number>
 
 I2C Bus number is mentioned in Camera DTS node in device tree file

.. _axon-lite-run-camera-live-stream-over-rtsp:

Run Camera Live Stream over RTSP
================================

This section demonstrates how to stream a camera feed over the network using GStreamer and MediaMTX.

Prerequisites
-------------

Install the required packages:

.. code-block:: bash

   sudo apt update

   sudo apt install \
       gstreamer1.0-tools \
       gstreamer1.0-plugins-base \
       gstreamer1.0-plugins-good \
       gstreamer1.0-plugins-bad \
       gstreamer1.0-plugins-ugly \
       gstreamer1.0-libav \
       v4l-utils \
       ffmpeg-rockchip

Verify that the required GStreamer plugins are available:

.. code-block:: bash

   gst-inspect-1.0 mpph264enc
   gst-inspect-1.0 rtspclientsink

Install MediaMTX
----------------

Download the latest `Mediamtx relase <https://github.com/bluenviron/mediamtx/releases/>`__ for Linux ARM64:

.. code-block:: bash

   wget https://github.com/bluenviron/mediamtx/releases/download/<version>/mediamtx_<version>_linux_arm64.tar.gz

   tar -xzf mediamtx_linux_arm64v8.tar.gz

Start MediaMTX:

.. code-block:: bash

   ./mediamtx &

By default, MediaMTX listens on:

- RTSP: ``8554``
- WebRTC: ``8889``

Publish Camera Stream
---------------------

Replace ``<camera_device_number>`` with your camera device number.

Examples:

- ``/dev/video11``
- ``/dev/video22``
- ``/dev/video31``

Run:

.. code-block:: bash

   gst-launch-1.0 -e \
     v4l2src device=/dev/video<camera_device_number> io-mode=mmap ! \
     videoscale ! \
     video/x-raw,width=1280,height=720 ! \
     mpph264enc bps=2000000 gop=15 ! \
     h264parse config-interval=-1 ! \
     rtspclientsink protocols=tcp location=rtsp://127.0.0.1:8554/cam

View Stream Using FFplay
------------------------

From another machine on the same network, replace ``<axon_lite_ip>`` with the IP address of the AXON LITE board:

.. code-block:: bash

   ffplay \
     -fflags nobuffer \
     -flags low_delay \
     -rtsp_transport tcp \
     rtsp://<axon_lite_ip>:8554/cam

