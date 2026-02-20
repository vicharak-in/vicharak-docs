######################
MIPI Camera Interface 
######################

.. image::  /_static/images/rk3588-axon/axon-multiCam.webp
    :width: 65%

Hardware Required
------------------

- Camera ( OV5647  or any other RPI supported camera)
- Vicharak Flex Cable 30 Pin 0.4mm Pitch Cable (Golden Color)
- Vicharak Camera PCB 
- FPC50 15 Pin 1mm Pitch Cable

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

2. Install ffmpeg and v4l2 tools

.. code-block::

    sudo apt install ffmpeg
    sudo apt install v4l-utils

2. Ensure your axon is powred off before connecting the camera

How to Attach Camera to Axon
----------------------------

1. First, Connect Vicharak Flex Cable To Vicharak CAM PCB Connector.
 
.. image::  /_static/images/rk3588-axon/axon-camera-start.gif
    :width: 40%

.. danger::
        Make sure to connect the Vicharak flex cable's AXON PCB side connector to the AXON board, and the display/camera side connector to the Vicharak CAM PCB.

.. image::  /_static/images/rk3588-axon/axon-camera-2.gif
    :width: 40%

2. Attach Camera Module To FPC50 15 Pin 1mm Pitch Cable.

.. image::  /_static/images/rk3588-axon/axon-camera-3.gif
    :width: 40%

3. Connect Camera To Vicharak CAM PCB Connector. 

.. image::  /_static/images/rk3588-axon/axon-camera-4.gif
    :width: 40%

4. Connect Axon Side Vicharak Flex Cable to Axon.

.. note::

   Note down the pin names where yor are connecting the camera. Accordingly overlay needs to be selected.

.. image::  /_static/images/rk3588-axon/axon-camera-mipi-p.webp
    :width: 50%

.. image::  /_static/images/rk3588-axon/axon-camera-5.gif
    :width: 40%


5. After Using Camera, User can remove camera using twizer.

.. image::  /_static/images/rk3588-axon/axon-camera-6.gif
    :width: 40%

Camera Interface PCBs
---------------------

2 Lane Alpha PCB ( Rpi compatible )
====================================

.. image::  /_static/images/rk3588-axon/axon-camera-alpha.webp
    :width: 30%

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

5. If you got the device name and number then it confirms that axon has detected the Camera. If it is not visible, check the connection and pins again.


Enable Overlays In Axon 
------------------------

**Here, you can find which overlay should be turned on for each MIPI Connector.**

.. list-table::
   :header-rows: 1
   :widths: 15 15 15 15

   * - **Interface on Vicharak board**
     - **Lane option**
     - **Vicharak camera PCB**
     - **Turn on Overlay in Linux**

   * - MIPI CSI0
     - 2 Lane
     - α
     - Alpha

   * - MIPI CSI1
     - 2 Lane
     - α
     - Alpha

   * - MIPI DPHY RX0
     - 2 Lane
     - α
     - Alpha

   * - MIPI DPHY RX1
     - 2 Lane
     - α
     - Alpha

   * - MIPI CSI0

       MIPI CSI1

       MIPI DPHY RX0

       MIPI DPHY RX1
     - 4 Lane
     - α
     - Alpha

.. note::
    **Alpha 4 lane PCB will be available soon**

**Steps to follow for Configuration**
    
1. Open a terminal window(``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``Overlays`` options in it by pressing ``enter`` key.
           
.. image:: /_static/images/rk3399-vaaman/Overlays_1.webp
                   :width: 50%

4. You will see Warning Page, click on ``yes`` and select ``Manage Overlays`` options.

.. image:: /_static/images/rk3399-vaaman/Overlays_2.webp
                   :width: 50%
    
5. Select overlays as per your camera sensor ``( OV5647 )`` and port to which it is connected ``( CSI0 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. note::

    If you want to connect multiple cameras, check which Sensor your camera is using from your camera docs like OV5647 or IMX519 and the ports to which it is connected like CSI0/CSI1 or dphy RX0/RX1 on axon. Then select the overlay according to it. 
    
.. image:: /_static/images/rk3588-axon/axon-overlay-list.webp
                   :width: 50%
    
6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.

.. danger::
   Make sure that whenever you are going to connect Camera, Device should be power off.


To use the camera(s):
-----------------------------------------------------------------------

.. Tip::

    Connect a monitor to axon to see the captured feed.

Run Camera Using qV4l2 (GUI tool)
==================================

**Step 1: Install the GUI tool (qv4l2) on RX Axon**

.. code-block:: bash

   sudo apt install qv4l2

**Step 2: Open qv4l2**

.. code-block:: bash

   qv4l2

**Step 3: Select your camera device**

1. Click on Open Devices on top-left corner

.. image:: /_static/images/rk3588-axon/axon-mipi-camera03.webp
           :width: 65%

2. Select the device name from here like video22 or video31 from the menu (You can get device name by running ``v4l2-ctl --list-devices``)

.. image:: /_static/images/rk3588-axon/axon-mipi-camera01.webp
            :width: 65%

**Step 4: Start the camera**

Click on start capturing

.. image:: /_static/images/rk3588-axon/axon-mipi-camera02.webp
           :width: 65%

.. tip::
    If you have connected multiple camera devices to axon, open multiple qV4l2 windows in the same way and select different camera device name. Using this you can use all the MIPI ports.


Run camera live feed using ffmpeg
=================================

1. Install ffmpeg using ``sudo apt install ffmpeg``
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
    
for Debian-based systems (like Ubuntu): 

.. code-block::

           sudo apt update
           sudo apt install python3-pip


2. Install the OpenCV library using pip
            
for Debian-based systems (like Ubuntu):

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

