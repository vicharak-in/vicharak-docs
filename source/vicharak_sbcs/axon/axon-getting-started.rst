.. _axon-getting-started:

Getting Started
###############

For Axon, Vicharak has provided all the necessary accessories and
information to get started with the board. This section will guide you through
the initial setup process and provide you with the necessary information to get
started with Axon.

.. TODO: Modify this for Axon
What's in the box?
==================

**1. Axon**

**2. 12V/5A Power Adapter with PD cable**

**3. Pre-installed eMMC**

What else do you need?
======================

**1. Micro HDMI to HDMI cable or adapter**
 
**2. USB Keyboard and Mouse**
 
**3. Monitor with HDMI input**

**4. USB-C to USB-A Male cable (optional)**

**5. SD-card (optional)**

**6. Internet Connection (optional)**

**7. USB to TTL Serial Cable (optional)**

.. note::
    | The items listed above are not included in the box.
    | You can purchase them from the :ref:`axon-accessories` page.


Getting Started with eMMC
=========================

Turning board on
----------------

Axon comes pre-loaded with **Ubuntu** (``Jammy``) operating system on
its ``eMMC`` (embedded MultiMediaCard) storage, and it offers support for
``SD-card`` boot mode.

If users wish to explore different operating systems, they must utilize the
appropriate firmware to program the board accordingly.

In the boot priority, ``SD-card`` takes the highest precedence, followed by
``eMMC``. In practical terms, if there's a SD-card attached to Axon,
it will initiate the boot process from it. In the absence of an SD-card,
the default boot destination becomes the eMMC storage.

For the purpose of this guide, we will focus on the ``eMMC`` storage and the
pre-installed ``Ubuntu (Jammy)``, omitting detailed instructions for
``SD-card`` boot configurations.

Connect the PD cable to the Axon board and the PD adapter to the power socket.
Once the power is connected, the board will automatically turn on.

.. danger::
    |
    | **12V Power Input only! Do not use 5V power input.**
    |
    | Using a 12V power input is crucial for the proper functioning of the Axon.
    | The board is designed to operate with a 12V power supply, and using a 5V power
    | input may lead to instability and potential damage.
    | Ensure that you use the provided 12V/5A Power Adapter with PD cable to
    | power the Axon SBC.

.. image:: ../../_static/images/rk3588-axon/axon-power-option.webp
   :width: 50%

Axon is pre-installed with Ubuntu (``Jammy``) on its eMMC storage.
So, when you power on the board, it will boot from the eMMC storage by default.

.. warning::
   Remove SD-card if inserted

Verify the power LED
--------------------

Upon connecting the power cable, the activation of the **Red LED** serves as an
immediate visual indicator of the board's power status. This LED signifies that
the Axon is receiving power, and its illumination provides users with a
tangible confirmation of the successful power connection.

.. image:: ../../_static/images/rk3588-axon/axon-power-led.webp
    :width: 50%

Verify the status LED
---------------------

The activation of the **white LED**, marked by a blinking pattern, signifies
the completion of the booting process. This visual cue assures users that the
Axon has successfully booted from its storage medium and is ready for further
configuration.

.. image:: ../../_static/images/rk3588-axon/axon-leds.webp
    :width: 50%

.. warning::
   |
   | Please ensure you wait for the system to complete its reboot.
   | This is necessary because the system requires configuration adjustments
   | before you proceed to the next step. Taking the time to allow the system to
   | finish restarting ensures that it is fully set up for the subsequent tasks.

Available Boot Modes
====================


.. TODO: Add Axon SD card boot doc
Booting from SD card
--------------------
To boot from SD card, please follow below document.

    :doc:`axon-sdcard-boot`

.. TODO: Add suppoprt for Axon 
How to access your Axon board ?
=================================
There are multiple ways to access your Axon. You can connect the Axon
SBC to a monitor using the **micro HDMI port**, or you can connect it to your
computer headless using **SSH** or **serial console**.

For the initial setup process, we recommend connecting the Axon to a
monitor using the **micro HDMI port**. Once the initial setup is complete, you can
connect the Axon to your computer using the USB-C port.

.. note::
    If you want to access the **serial console**,
    Skip to the :ref:`Serial Console <axon-serial-console>` section.

    If you want to access the **Axon using SSH**,
    Skip to the :ref:`SSH <ssh>` section.


.. TODO: Add axon start guide
1. Using Micro HDMI port
-------------------------

Axon is equipped with two **micro HDMI ports**, which allows for easy
connection to a display. By using a micro HDMI to HDMI cable or adapter, users
can connect Axon to a monitor or TV with an HDMI input.

This enables direct visual access to the graphical user interface (GUI) or
command-line interface (CLI) on the connected display.

.. image:: ../../_static/images/rk3588-axon/axon-hdmi.webp
    :width: 50%

Connect the Micro HDMI to HDMI cable to the Axon and the monitor.
Once the cable is connected, the Axon will automatically detect the
monitor and display the output.

.. admonition:: Check out Linux Start Guide
   :class: tip

   Once the Axon is connected to the monitor, you can follow the
   :ref:`Linux Start Guide <axon-linux-start-guide>` to complete the initial setup.

.. _axon-serial-console:

2. Using Serial Console
------------------------

Axon also provides a serial interface, typically in the form of UART
(Universal Asynchronous Receiver-Transmitter) pins.

Users can access the system's console or terminal interface by connecting to
these serial pins using a serial cable or adapter. This method is often used
for debugging, troubleshooting, or accessing the system when other interfaces
are not available.

Preparation
```````````

To access Axon through the serial interface, you will need the following:

- A computer with a serial terminal application installed
  (such as PuTTY or minicom).
- A USB to TTL serial cable or adapter (such as FTDI or PL2303).
- Micro USB or USB-C cable.

Hardware Setup
``````````````

1. Connect the USB to TTL serial cable or adapter to your computer.

2. Connect the serial cable or adapter to Axon.

.. list-table::
   :widths: 20 40 130
   :header-rows: 1
   :class: feature-table

   * - **Serial FTDI Pin**
     - **Header GPIO Pin**
     - **Schematic Name**
   * - GND
     - Pin 6
     - GND
   * - TX
     - Pin 4 (GPIO0_B6)
     - UART2_TX_M0_DEBUG
   * - RX
     - Pin 2 (GPIO0_B5)
     - UART2_RX_M0_DEBUG

.. image:: ../../_static/images/rk3588-axon/axon-serial-uart-pins.webp
   :width: 50%

.. note::
    When accessing Axon through the serial interface, it is important to
    configure the serial parameters correctly. For RK3588-based systems,
    the following parameters are typically used:

    | Baud rate: `1500000`
    | Data bit: `8`
    | Stop bit: `1`
    | Parity check: `none`
    | Flow control: `none`

.. warning::
   |
   | Durning the first boot you will see a warning on your serial console.
   | So, please ensure that you wait for the system to complete its reboot.
   | This is necessary because the system requires configuration adjustments
   | before you proceed to the next step. Taking the time to allow the system to
   | finish restarting ensures that it is fully set up for the subsequent tasks.

Running the Serial Console Program
``````````````````````````````````

.. tab-set::

    .. tab-item:: PuTTY (GUI)

        1. Download and install the `PuTTY <https://www.putty.org/>`_ program.

        2. Open the PuTTY program and configure the serial parameters as shown
		   in the image below.

        .. image:: ../../_static/images/Putty_step.webp
           :width: 50%

        3. Click on the **Open** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: TeraTerm (GUI)

        1. Download and install the
            `TeraTerm <https://osdn.net/projects/ttssh2/releases/>`_ program.

        2. Open the TeraTerm program and configure the serial parameters.

        - On the **Setup** menu, click on **Serial port**.
        - Select the serial port number and configure the serial parameters
          as shown in the image below.

        .. image:: ../../_static/images/teraterm-configuration.webp
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Linux GTK-Term (GUI)

        1. Install the GTK-Term program using the following command:

        .. code-block:: bash

            sudo apt-get install gtkterm

        2. Open the GTK-Term program and configure the serial parameters.

        - On the **File** menu, click on **Port**.
        - Select the serial port number and configure the serial parameters as
          shown in the image below.

        .. image:: ../../_static/images/gtkterm-configuration.webp
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Minicom (CLI)

        .. note::
            Read minicom configuration from
            :ref:`Linux Minicom guide <minicom-guide>`.

.. _ssh:

3. Using SSH
-------------

Axon supports **SSH (Secure Shell)**, which allows for secure remote access
to the system. By establishing an SSH connection, users can remotely connect to
Axon from another device, such as a computer or smartphone, over a network.
This method provides a secure command-line interface to administer, configure,
and execute commands on the Axon.

Install OpenSSH server
``````````````````````

You can install both OpenSSH components on Windows devices using the
**Windows Settings**.

To install the OpenSSH components, follow these steps:

1. Open the Settings menu and click on Apps, then select **Optional Features**.
2. Look through the list to check if OpenSSH is already installed.
   If it's not, at the top of the page, click on **Add a feature** and then:

   - Find OpenSSH Client and click on Install.
   - Find OpenSSH Server and click on Install.
3. After the installation process is complete, go back to
   **Apps and Optional Features** to verify that **OpenSSH** is listed.
4. Open the Services desktop app. (``Click on Start, type services.msc in the
   search box, and then click on the Service app or press ENTER.``)
5. In the details pane, double-click on **OpenSSH SSH Server**.
6. On the General tab, choose **Automatic** from the Startup type drop-down
   menu.
7. To start the service, click on **Start**.


Verify OpenSSH server
`````````````````````

Once installed, you can connect to **OpenSSH Server** from a Windows device
with the **OpenSSH client** installed.

From a PowerShell prompt, run the following command.

.. code-block:: powershell

    ssh username@ip_address

Example:

.. code-block:: powershell

    ssh vicharak@192.168.29.69

.. tip::

	To find your IP address on Windows, use the following command:
	``ipconfig``

	For Linux users, use the following command:
	``ip a``

Accessing Axon through SSH
````````````````````````````

To access Axon through SSH, you can use either of the following commands:

|

1. SSH using the IP address

.. code-block::

    ssh username@ip_address

.. tip::
    Replace **"username"** with the appropriate username for Axon and
    **"ip_address"** with the actual IP address assigned to Axon on the
    network.

2. SSH using the PC name (hostname)

.. code-block::

    ssh username@pc-name.local

.. tip::
    Replace **"username"** with the appropriate username for Axon and
    **"pc-name"** with the actual PC name assigned to Axon on the network.

    For Linux users, you can find your username using ``whoami`` command and,
    hostname using ``cat /etc/hostname``

4. Set up automatic Wi-Fi connection on boot
--------------------------------------------

In the following example, we will set up automatic Wi-Fi connection on boot
for the **wlan0** interface. This will be useful if you are using a
headless system. That means you will not need to connect a monitor, keyboard,
or mouse to your system to connect to WiFi.

**1. Edit the ** ``/usr/lib/vicharak-config/conf.d/before.txt`` ** file and add
the following lines:**

::

    connect-wi-fi <network name> <password>

Example:

::

    connect-wi-fi vicharak_5g vcaa_g123

**2. Reboot the system.**

Axon Boot modes
=================
.. TODO: Add axon-maskrom-mode document
.. list-table::
   :widths: 20 40
   :header-rows: 1

   * - **Boot Mode**
     - **Description**
   * - Normal Mode
     - Normal boot mode is the default boot mode. In this mode, the board boots
       from the `eMMC` or `SD-card`. Each partition loads in order and enters
       the system normally.
   * - Loader Mode
     - Loader mode is used to upgrade the `bootloader`. In this mode, the
       bootloader will wait for the host command for `firmware upgrade`.
       On success, the board boots from the `eMMC` or `SD-card`,
       and the board enters the system normally.
   * - Maskrom Mode
     - | Maskrom mode is used to `repair` the board. In a situation where the
         bootloader is damaged, the board can enter the maskrom mode.
         In general, there is no need to enter `Maskrom` mode.
         In this mode, the bootrom code waits for the host to transmit the
         bootloader code through the USB-C port, load and run it.
       | :ref:`Learn more about maskrom mode <axon-maskrom-mode>`.

.. seealso::

    :ref:`axon-downloads`
