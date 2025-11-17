#################
PERIPLEX ONE-WIRE
#################

.. variable 
.. _DS18B20 docs: https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf
.. _DS2430A docs: https://www.analog.com/media/en/technical-documentation/data-sheets/DS2430A.pdf

This section explains how to interact with the ``ONE-WIRE`` peripherals generated on Vaaman via Periplex.

How to Generate ONE-WIREs on Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``2 ONE-WIRE`` peripherals, you need to create a JSON file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2cmaster": [],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [],
            "onewire": [
               {
                  "id": 0,
                  "ONEWIRE": "GPIOT_RXP28"
               },
               {
                  "id": 1,
                  "ONEWIRE": "GPIOL_73"
               },
            ],
            "can": [],
            "i2s": [],
            "i2cslave": [],
            "jtag": [],
            "swi": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``2 ONE-WIRE`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

      sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting the system, the two ONE-WIRE peripherals will be automatically initialized on Vaaman.

     .. raw:: html

         <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 70%; height: 67px; overflow: auto; white-space: pre-wrap;">
            vicharak@vicharak:/sys/bus/w1/devices$ ls
            <span style="color:red;">14-000009904f27</span>  <span style="color:red;">28-0ee9d4443c4a</span>  w1_bus_master1  w1_bus_master2
         </pre>

   - For example, if two ONE-WIRE peripherals are connected — a temperature sensor ``(DS18B20)`` on ``GPIOT_RXP28`` and an EEPROM ``(DS2430A)`` on ``GPIOL_73`` — you can access them through the following device files:

   - **Temperature Sensor (DS18B20)** : ``/sys/bus/w1/devices/28-0ee9d4443c4a``
   - **EEPROM (DS2430A)** : ``/sys/bus/w1/devices/14-000009904f27``

   .. Note::
      
      - The device file names may vary depending on the specific devices connected and their unique IDs.

      - Ensure that the required ONE-WIRE kernel modules are properly loaded to enable device detection. For example, the ``w1-gpio`` and ``w1_therm`` modules are typically required for temperature sensors, while the ``w1_ds2430`` module is needed for the DS2430A EEPROM.

      - If the ``/sys/bus/w1/devices/`` directory appears empty, verify the hardware connections and ensure that the ONE-WIRE devices are correctly connected to the specified GPIO pins.

      - You can read data from these device files using standard Linux commands such as ``cat``, or by writing custom scripts to interact with the devices programmatically.
         
How to interact with generated ONE-WIREs ?
==========================================

The Periplex platform dynamically generates ``ONE-WIRE`` devices, which are accessible through device nodes such as:
   .. code-block::

      /sys/bus/w1/devices/XX-XXXXXXXXXXXX

   - Where ``XX-XXXXXXXXXXXX`` represents the unique identifier for each ``ONE-WIRE`` device connected to the bus.
   
   - For example, a ``DS18B20 temperature sensor`` might appear as ``28-0ee9d4443c4a``, while a ``DS2430A EEPROM device`` could show up as ``14-000009904f27``.

   - These device nodes can be used to read data from or write data to the connected ``ONE-WIRE`` devices, depending on their functionality.

Using cat command / shell scripts
---------------------------------

1. **Using the cat command:**

   - To read temperature data from a ``DS18B20 temperature sensor``, you can use the following command:
   
   .. code-block::
      
      cat /sys/bus/w1/devices/28-0ee9d4443c4a/temperature

2. **Using shell scripts:** 

   - Using shell scripts interact with the devices programmatically is also possible.Here is a simple example of a shell script that firstly writes data to a ``DS2430A EEPROM device`` and then reads it back to verify the operation:
      
   .. code-block::
      
      #!/bin/bash

      # Navigate to your device
      cd /sys/bus/w1/devices/14-000009904f27

      # Test with simple data
      TEST_DATA="12345678"

      echo "=== EEPROM Write and Verify Test ==="
      echo "Device: $(pwd)"
      echo "Test data: '$TEST_DATA'"
      echo

      # Check if eeprom file exists
      if [ ! -f "eeprom" ]; then
         echo "ERROR: eeprom file not found in $(pwd)"
         exit 1
      fi

      # Write data to EEPROM
      echo "Writing data to EEPROM..."
      sudo bash -c "echo -n '$TEST_DATA' > eeprom"

      if [ $? -eq 0 ]; then
         echo "✓ Written: '$TEST_DATA'"
      else
         echo "✗ Failed to write data to EEPROM"
         exit 1
      fi

      # Small delay to ensure write is complete
      sleep 1

      # Read data back from EEPROM
      echo "Reading data from EEPROM..."
      READ_DATA=$(sudo cat eeprom | tr -d '\0' | head -c ${#TEST_DATA})

      echo "✓ Read: '$READ_DATA'"
      echo

      # Compare written and read data
      if [ "$TEST_DATA" = "$READ_DATA" ]; then
         echo "✓ SUCCESS: Data verification passed!"
         echo "  Written: '$TEST_DATA'"
         echo "  Read:    '$READ_DATA'"
      else
         echo "✗ FAILURE: Data verification failed!"
         echo "  Expected: '$TEST_DATA'"
         echo "  Got:      '$READ_DATA'"
         echo "  Length expected: ${#TEST_DATA}"
         echo "  Length got:      ${#READ_DATA}"

         # Show hex dump for debugging
         echo
         echo "Hex dump of first 16 bytes from EEPROM:"
         sudo xxd -l 16 eeprom
      fi

      echo
      echo "Test completed."

.. tip::
      
      - You can refer this link fot the temperature sensor `DS18B20 docs`_.
      - You can refer this link for the EEPROM `DS2430A docs`_.