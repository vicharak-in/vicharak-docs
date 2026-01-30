############
PERIPLEX SPI
############


This section explains how to interact with the ``SPI`` devices generated on Vaaman via Periplex.

How to Generate SPIs on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``3 SPI`` devices, Your need to create a json file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2cmaster": [],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [
               {
                  "id": 0,
                  "SLAVE": 1,
                  "MISO-IN": "GPIOT_RXP28",
                  "MOSI-OUT": "GPIOL_73",
                  "SLAVE-0": "GPIOR_173",
                  "CLK-OUT": "GPIOR_174"
               },
               {
                   "id": 1,
                   "SLAVE": 1,
                   "MISO-IN": "GPIOT_RXN28",
                   "MOSI-OUT": "GPIOL_75",
                   "SLAVE-0": "GPIOL_72",
                   "CLK-OUT": "GPIOR_178"
               },
               {
                   "id": 2,
                   "SLAVE": 1,
                   "MISO-IN": "GPIOR_168",
                   "MOSI-OUT": "GPIOL_17",
                   "SLAVE-0": "GPIOL_20",
                   "CLK-OUT": "GPIOL_18"
               }
            ],
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": [],
            "jtag": [],
            "dht": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``3 SPI`` peripherals is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, It will ask for editing the ``periplex-dtso`` file, press ``1`` for ``yes`` and then press ``Enter`` to continue.
   - This will open the periplex-dtso file in your default text editor (usually ``vim`` or ``nano``).You now need to add the Device Tree content for your ``3 SPI`` peripherals. For example, if you want ``2 SPI device nodes`` and ``1 SPI Flash`` node, then add the following content inside the file:
   
   .. code-block::

         //SPDX-License-Identifier: GPL-2.0+
         //Copyright (C) 2024 Vicharak Computers LLP

         /dts-v1/;
         /plugin/;

         #include "rk3399-vaaman-periplex.dtsi"

         &periplex{

         	periplex_spi3: periplex-spi3 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <2>;
                        flash: spi-flash@0 {
                                reg = <0>;
                                #address-cells = <1>;
                                #size-cells = <0>;
                                compatible = "jedec,spi-nor";
                                spi-max-frequency = <10000000>;
                                status = "okay";
                        };
         	};
         	periplex_spi2: periplex-spi2 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <1>;         		
                        spidev@0{
                                compatible = "rockchip,spidev";
                                status = "okay";
                                reg = <0>;
                                spi-max-frequency = <25000000>;
                        };
         	};
         	periplex_spi1: periplex-spi1 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <0>;                
                        spidev@0{
                                compatible = "rockchip,spidev";
                                status = "okay";
                                reg = <0>;
                                spi-max-frequency = <25000000>;
                        };
         	};

         };

   - Then save the file and exit the editor. for example, if you use ``vim`` editor, you can do this by pressing ``Esc``, then typing ``:wq`` and pressing ``Enter``.

   - After saving the file, the ``periplex-sync`` command will continue to run and apply the changes to the device tree,it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``3 SPI`` peripherals generated through Periplex like this:

   - You can see the generated ``2 spi device`` nodes:
   .. raw:: html

      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 71%; height: 67px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:~$ ls /dev/spidev*
         /dev/spidev0.0  <span style="color:red;">/dev/spidev1.0</span>  <span style="color:red;">/dev/spidev2.0</span>  
      </pre>

   - Similarly, you will see the ``SPI Flash`` device created under the MTD subsystem:
   .. raw:: html
        
      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 71%; height: 67px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:~$ ls /dev/mtd*
          <span style="color:red;">/dev/mtd0</span> /dev/mtd0ro /dev/mtdblock0
      </pre>

How to interact with the generated SPIs ?
===========================================

The Periplex platform dynamically generates ``spidev`` devices and other ``SPI-based peripheral`` nodes at runtime., which can be accessed via paths like:

.. code-block::

   /dev/spidev1.0
   /dev/spidev2.0
   /dev/mtd0
   ...

Operations on dev/spidevX.0 (SPI chips)
-----------------------------------------

Each SPI chip manages a SPI bus. For example, you want control ``spidev1.0``.

1. **Opens SPI connection:**

   - Opens SPI connection on ``/dev/spidev1.0`` using the ``spidev`` Python library.

2. **Configures SPI settings:**

   - ``Speed``: 25 MHz

   - ``Mode``: 0

   - ``Bits per word``: 8

3. **Supports the following operations:**

   - Write data to the SPI device using ``writebytes()``.

   - Read data from the SPI device using ``readbytes()``.

   - Transfer data (send and receive simultaneously) using ``xfer2()``.

4. **Gracefully closes the SPI connection after operations:**

   - ``spi.close_connection()`` is used to safely close the SPI connection after all operations are completed.

.. tip::
    - Follow this python script to control the SPI device nodes :download:`python_script </_static/files/periplex_spi.py>`


Operations on /dev/mtd0 (SPI Flash)
-----------------------------------

SPI Flash devices such as the ``W25Q128JV``, which appear as MTD (Memory Technology Device) nodes like:

1. **Opens the MTD Flash Device:**
    
   - Opens the MTD device located at ``/dev/mtd0`` using ``open()`` ioctl call for read and write operations.
   .. code-block::

       /dev/mtd0

2. **Reads Flash Device Information:**

   - Use the ``MEMGETINFO`` ioctl to retrieve flash memory details such as total flash size, erase block size (``4 KB`` for ``W25Q128JV``), write size, and page size ``256 bytes``, These parameters determine the minimum amount of data that can be erased, written, or updated at a time.

3. **Prepares 10,000 Bytes of Test Data:**

   - Generates a repeating pattern ``(0–255)``:
   .. code-block::

        0x00, 0x01, 0x02, ... 0xFF, 0x00, 0x01 ...

4. **Erases the Required Sectors:**

   - Since ``10000`` bytes > one ``4KB`` sector, the program erases:
   - Sector 0 ``(0–4095)``
   - Sector 1 ``(4096–8191)``
   - Using the ioctl: ``MEMERASE``
   - This ensures the flash is clean before writing.

5. **Writes 10,000 Bytes to Flash (in 256-byte pages):**

   - W25Q128JV allows ``256-byte`` page writes.
   - The program writes data page-by-page:
   - Automatically calculates how many bytes to write per loop.
   - Uses ``write()`` system call.
   - Adds ``1ms`` delay between writes to allow the flash to finish programming.

6. **Reads Back 10,000 Bytes:**

   - Reads the same memory from offset ``0x00000000``.
   - Reads in ``256-byte`` chunks.
   - Stores results in a separate buffer.

7. **Verifies Data Integrity:**

   - Compares each byte written vs. byte read
   - Reports mismatches (first 10 only)
   - If all bytes match:
   .. code-block::

        ✓ Perfect! All 10000 bytes verified successfully

.. tip::
    - Follow this c program to control the SPI-flash :download:`c_program </_static/files/periplex_spi.c>`
