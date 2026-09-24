import re

with open('source/vicharak_sbcs/axon-lite/axon-lite-video/video-input/mipi.rst', 'r') as f:
    content = f.read()

replacement = """######################
MIPI Camera Interface 
######################

MIPI CSI 0
==========

Hardware Required
------------------

- Camera ( OV5647  or any other RPI supported camera)
- Raspberry Pi 22 Pin 0.5mm Camera Cable

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

3. Next, prepare the MIPI CSI 0 port on the Axon Lite board. 

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-4.gif
    :width: 40%

4. Connect the other end of the 22 Pin Camera Cable directly to the MIPI CSI 0 port on the Axon Lite.

.. note::
   Note down the pin names where you are connecting the camera. Accordingly overlay needs to be selected.

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-mipi-p.webp
    :width: 50%

.. image::  /_static/images/rk3576-axon-lite/axon-lite-camera-5.gif
    :width: 40%

5. After Using Camera, User can remove camera using twizer.


MIPI CSI 1/2 and CSI 3/4
========================

.. image::  /_static/images/rk3576-axon-lite/axon-lite-multiCam.webp
    :width: 65%

Hardware Required
------------------

- Camera ( OV5647  or any other RPI supported camera)
- Vicharak Flex Cable 40-Pin 0.4mm Pitch Cable (Golden Color)
- Vicharak Camera PCB 

Steps to follow 
----------------
1. Connect the hardware
2. Configure the overlays
3. Run Camera

Pre-Requisites
--------------
Please ensure you have completed the prerequisites (updating the kernel and installing ``ffmpeg-rockchip``/``v4l-utils``) as described in the previous section. Ensure your board is powered off.

How to Attach Camera to Axon Lite (CSI 1/2 and CSI 3/4)
-------------------------------------------------------

1. Connect the Vicharak Flex Cable (40-Pin 0.4mm Pitch) to the MIPI port on the Axon Lite board.
2. Connect the other end of the Vicharak Flex Cable to the Vicharak Camera PCB.
3. Attach your camera module to the Vicharak Camera PCB.

.. danger::
        Make sure to connect the Vicharak flex cable's AXON LITE PCB side connector to the AXON LITE board, and the display/camera side connector to the Vicharak CAM PCB.

.. note::
   Note down the pin names where you are connecting the camera. Accordingly overlay needs to be selected.

Camera Interface PCBs"""

start_idx = content.find("######################\nMIPI Camera Interface")
end_idx = content.find("Camera Interface PCBs\n---------------------")

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + replacement + content[end_idx + len("Camera Interface PCBs"):]
    with open('source/vicharak_sbcs/axon-lite/axon-lite-video/video-input/mipi.rst', 'w') as f:
        f.write(new_content)
    print("Updated successfully")
else:
    print("Could not find start or end index")

