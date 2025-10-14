===============================
Home Assistant Operating System
===============================

`Home Assistant Operating System (HAOS) <https://www.home-assistant.io/>`_ is an open-source platform for home automation, offering seamless integration with numerous smart devices and services. It runs on various devices, allowing you to automate tasks, monitor your home, and control devices from a single interface. This guide provides steps to flash the image, access Home Assistant via the web interface, and enable SSH access.

.. image:: /_static/images/haos-0.webp
   :width: 95%

Steps to Follow
================

----------------------------
Download Home Assistant OS
----------------------------

`Home Assistant OS Axon image <https://downloads.vicharak.in/vicharak-axon/home-assistant-os/>`_ 

-----------------------
Flash Image in eMMC
-----------------------

Follow this guide for flashing the image into eMMC:

`Flashing Guide Using Linux_Upgrade_Tool (Linux) </vicharak_sbcs/axon/axon-linux/linux-usage-guide/linux-axon-upgrade-tool/#flash-raw-image-in-axon>`_

-----------------------------------------------------------
Flash Image in External Device Like, SD Card / USB
-----------------------------------------------------------

Option 1: Using Balena Etcher
-------------------------------

1. Download Balena Etcher: https://etcher.io
2. Insert the SD card or USB drive into your computer.
3. Select the downloaded Home Assistant OS image.
4. Select your target drive.
5. Click **Flash** and wait for completion.

Option 2: Using dd (Linux)
-------------------------------

.. code-block:: bash

   sudo dd if=<home-assistant>.img of=/dev/sdX bs=4M status=progress conv=fsync

Replace ``/dev/sdX`` with your target device (check with ``lsblk``).

.. warning::
   Make sure that image is flashed properly.
   By running below command :

   .. code-block::

      sudo parted -l /dev/sdX

----------------------------
Boot Home Assistant OS
----------------------------

.. danger::

   Kindly, Attach **Ethernet** to device. It is mandatory to configure Home Assistant OS to boot properly.

1. Insert the flashed media into Axon.
2. Power on the device.
3. Wait for the system to initialize. ( It might take 4-5 Minutes to configure ) 
4. Access Home Assistant

Once the device has booted and is connected to your local network:

- Open a web browser on your computer.

  .. code-block:: text

     http://homeassistant.local:8123

  or use the device's IP address:

  .. code-block:: text

     http://<DEVICE_IP>:8123


You will be greeted with the **Home Assistant onboarding screen**.
Follow the setup wizard to create your account and configure Home Assistant. It might take 20-25 minutes to configure.


.. image:: /_static/images/haos-3.webp
   :width: 100%

After Configuring Device setup, you will be redirected to **Dashboard** of the Home Assistand Operating System,

.. image:: /_static/images/haos-1.webp
   :width: 100%

----------------------------
Enable SSH Access
----------------------------

To enable SSH access, install the **SSH & Web Terminal Add-on** from the Home Assistant add-on store.

**Steps:**

1. Open Home Assistant web interface at ``http://homeassistant.local:8123``.
2. Navigate to **Setting** that can be found in leftend side bar:

   .. code-block:: text

      Settings > Add-ons > Add-on Store

3. Search for **SSH & Web Terminal** and install it.

.. image:: /_static/images/haos-2.webp
   :width: 100%

4. Configure the add-on:

   - Set username and password.
   - Optionally enable authorized SSH keys for secure access.

   Example configuration (in YAML):

   .. code-block:: yaml

      username: "homeassistant"
      password: "your_password"
      authorized_keys:
        - ssh-rsa AAAAB3Nz...

5. Start the add-on.

**Access via SSH:**

.. code-block:: bash

   ssh homeassistant@<DEVICE_IP> -p 22

.. code-block:: bash
  
            ▄██▄           _   _
          ▄██████▄        | | | | ___  _ __ ___   ___
        ▄████▀▀████▄      | |_| |/ _ \| '_ ` _ \ / _ \
      ▄█████    █████▄    |  _  | (_) | | | | | |  __/
     ▄██████▄  ▄██████▄   |_| |_|\___/|_| |_| |_|\___|          _
     ████████  ██▀  ▀██      / \   ___ ___(_)___| |_ __ _ _ __ | |_
     ███▀▀███  ██   ▄██     / _ \ / __/ __| / __| __/ _` | '_ \| __|
     ██    ██  ▀ ▄█████    / ___ \\__ \__ \ \__ \ || (_| | | | | |_
     ███▄▄ ▀█  ▄███████   /_/   \_\___/___/_|___/\__\__,_|_| |_|\__|
     ▀█████▄   ███████▀
     
     Welcome to the Home Assistant command line interface.
     
     Home Assistant Supervisor is running!
     System information:
       IPv4 addresses for wlan0: XXX.XX.X.XXX/24
       IPv4 addresses for end1:  XXX.XX.X.XXX/24
     
       OS Version:               Home Assistant OS 16.3.dev0
       Home Assistant Core:      2025.10.0
     
       Home Assistant URL:       http://homeassistant.local:8123
       Observer URL:             http://homeassistant.local:4357
     
     System is ready! Use browser or app to configure.


From here, you can explore integrations, automations, and extend Home Assistant with add-ons.
