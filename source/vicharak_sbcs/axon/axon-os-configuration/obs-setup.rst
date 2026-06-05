######################
OBS Setup
######################

Requirements
============

- Ubuntu 24.04.3
- Kernel image ``6.1.75-axon``

Mesa3D Configuration
====================

Check your OpenGL version to verify Mesa3D installation:

.. code-block:: bash

   glxinfo | grep "version"
   glxinfo | grep "renderer"

For the RK3588, Mesa (Panfrost) only supports **OpenGL 3.1**. OBS requires **OpenGL 3.3 or higher**. To bypass this check (temporarily), you can override the Mesa version:

.. warning::

   Mesa version override is not recommended for general use, but it works fine for running OBS.

.. code-block:: bash

   export DRI_DRIVER=panfrost
   export MESA_GL_VERSION_OVERRIDE=3.3
   export MESA_GLSL_VERSION_OVERRIDE=330

Dependencies
============

Install required development libraries:

.. code-block:: bash

   sudo apt install libobs-dev libasound2-dev

OBS Installation
================

Install OBS Studio using the official PPA:

.. code-block:: bash

   sudo add-apt-repository ppa:obsproject/obs-studio
   sudo apt update
   sudo apt install obs-studio

Axon OBS Video Capture Plugin
===============

Install the ``v4l2-obs-plugin-axon`` for camera capturing:

.. code-block:: bash

   git clone https://github.com/vicharak-in/v4l2-obs-plugin-axon.git
   cd v4l2-obs-plugin-axon
   mkdir build && cd build
   cmake ..
   make
   sudo make install

The plugin installs to ``/home/vicharak/.config/obs-studio/plugins``.

.. code-block:: text

   /usr/local/lib/obs-plugins/obs-plugin-axon.so

Run OBS
============

Launch OBS with verbose logs:

.. code-block:: bash

   obs --verbose

Select the plugin named ``V4L2 axon camera`` for capturing capturing.
