.. _getting-started:

#################
 Getting Started
#################

***************
 Turning it on
***************

-  PD Adapter + PD cable required with operating 12V/5A (12V Input
   only!)

      .. image:: images/Power_option.webp
         :width: 800

-  Boot from SDcard

         .. image:: images/SDcard.webp
            :width: 800

      To make an SD card bootable, follow these steps:

         #. Format the SD card using a suitable file system (such as
            FAT32).
         #. Obtain the bootable image or operating system files for your
            desired platform.
         #. Use a disk imaging tool (e.g., Etcher, Win32 Disk Imager) to
            write the bootable image onto the SD card.
         #. Safely eject the SD card from your computer.
         #. Insert the bootable SD card into the target device.
         #. Power on the device to initiate the boot process from the SD
            card.

-  Boot from eMMC (Remove SDcard if inserted)

      .. image:: images/eMMC_boot.webp
         :width: 800

-  When the power cable is connected, the red LED will be activated, and
   you can observe its illumination in the image displayed below.

      .. image:: images/Power_LED.webp
         :width: 800

Once the booting process is finished, you will notice the activation of
the blue LED, indicated by a blinking pattern, as demonstrated in the
image provided below.

   .. image:: images/User_LEDs.webp
      :width: 800

How it can be accessed
======================

   -  *Micro HDMI*: Vaaman SBC is equipped with a micro HDMI port, which
      allows for easy connection to a display. By using a micro HDMI to
      HDMI cable or adapter, users can connect Vaaman to a monitor or TV
      with an HDMI input. This enables direct visual access to the
      graphical user interface (GUI) or command-line interface (CLI) on
      the connected display.

         .. image:: images/HDMI_Option.webp
            :width: 800

   -  *Serial*: Vaaman also provides a serial interface, typically in
      the form of UART (Universal Asynchronous Receiver-Transmitter)
      pins. Users can access the system's console or terminal interface
      by connecting to these serial pins using a serial cable or
      adapter. This method is often used for debugging, troubleshooting,
      or accessing the system when other interfaces are not available.

         .. image:: images/USB_Serial.webp
            :width: 800

         When accessing Vaaman SBC through the serial interface, it is
         important to configure the serial parameters correctly. For
         RK3399-based systems, the following parameters are typically
         used:

         Baud rate: 1500000

         Data bit: 8

         Stop bit: 1

         Parity check: none

         Flow control: none

         For Windows users, you can download PuTTY,
         :https://www.putty.org/

         .. image:: images/Putty_step.webp
            :width: 800

         To use serial debugging on Ubuntu

            #. Open a terminal on your Ubuntu machine. You can do this
               by searching for "Terminal" in the applications menu or
               by using the shortcut Ctrl+Alt+T.

            #. Update the package list to ensure you have the latest
               package information. In the terminal, run the following
               command:

                  sudo apt update

            #. Install GTKTerm by running the following command:

                  sudo apt install gtkterm

            #. After the installation is complete, connect your Vaaman
               SBC to your Ubuntu machine using a serial cable. Ensure
               that the cable is properly connected to the appropriate
               serial port on both devices.

            #. Run GTKTerm by executing the following command:

                  sudo gtkterm

            #. To access the configuration settings for GTKTerm, you can
               follow either of these methods:

                  #. Click on the "Configuration" menu and select
                     "Port."

                        OR

                  #. Press Ctrl+Shift+S.

                  By using either of these methods, you will be able to
                  access the configuration settings in GTKTerm, where
                  you can make adjustments to the port settings for your
                  serial connection, as shown in the image below:

         .. image:: images/GTKTerm.webp
            :width: 800

   -  SSH: Vaaman supports SSH (Secure Shell), which allows for secure
      remote access to the system. By establishing an SSH connection,
      users can remotely connect to Vaaman from another device, such as
      a computer or smartphone, over a network. This method provides a
      secure command-line interface to administer, configure, and
      execute commands on the Vaaman SBC.

         #. Install OpenSSH server by executing the following command:

               sudo apt install openssh-server

         #. Once OpenSSH is installed, it should start automatically.
            You can verify its status by running:

               sudo systemctl status ssh

               If it is active and running, you should see a "active
               (running)" message.

         #. Next, install Avahi-daemon to enable local name resolution.
            Run the following command:

               sudo apt install avahi-daemon

         #. After the installation, Avahi-daemon should start
            automatically. Verify its status by running:

               sudo systemctl status avahi-daemon

               Ensure that it is active and running.

         To access Vaaman SBC through SSH, you can use either of the
         following commands:

         5. SSH using the IP address:

               ssh username@ip_address

               Replace "username" with the appropriate username for
               Vaaman and "ip_address" with the actual IP address
               assigned to Vaaman on the network.

         #. SSH using the PC name (hostname):

               ssh username@pc-name.local

               Replace "username" with the appropriate username for
               Vaaman and "pc-name" with the actual PC name assigned to
               Vaaman on the network.

***********************
 Where to go from here
***********************

   -  :ref:`Vaaman Application <vaaman-applications>`
   -  :ref:`Downloads <Downloads>`
