Usage guide for Periplex
========================

.. variable 
.. _GPIO pins: https://docs.vicharak.in/_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf
.. _DTS demo: https://www.youtube.com/watch?v=fVuv8Rr6arM

1. **Run `periplex-sync` Command:**

   - The ``periplex-sync`` command requires a ``<filename>.json`` configuration file.

   - ``<file_name>.json`` is your ``.json`` file defining the peripherals and pin configurations. 
   - For example, if you need to configure  ``3 UART`` and  ``2 I2C`` devices, you can define the ``TX`` and ``RX`` pins for ``UART`` and the ``SCL`` and ``SDA`` pins for ``I2C`` like this:
   .. code-block:: json
        
        {
            "uart": [
                {
                    "id": 0,
                    "TX": "GPIOT_RXP28",
                    "RX": "GPIOT_RXN28"
                },
                {
                    "id": 1,
                    "TX": "GPIOL_73",
                    "RX": "GPIOL_75"
                },
                {
                    "id": 2,
                    "TX": "GPIOR_173",
                    "RX": "GPIOL_72"
                }
            ],
            "i2c": [
                {
                    "id": 3,
                    "SCL": "GPIOT_RXP27",
                    "SDA": "GPIOT_RXP24"
                },
                {
                    "id": 4,
                    "SCL": "GPIOL_63",
                    "SDA": "GPIOT_RXN24"
                }
            ],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [],
            "onewire": [],
            "can": [],
            "i2s": []
        }

   - Another example: if you need to configure ``1 UART``, ``1 I2C``, ``1 GPIO``, ``1 PWM``, and ``1 SPI`` device, define each peripheral with its specific pins. For ``SPI``, the ``SLAVE`` parameter specifies the number of slave devices. If you set ``SLAVE`` to 2, you must define both ``SLAVE-0`` and ``SLAVE-1`` pins. If only one slave device is used, set ``SLAVE`` to 1 and define only the ``SLAVE-0`` pin.
   .. code-block:: json
        
        {
            "uart": [
                {
                    "id": 0,
                    "TX": "GPIOT_RXP28",
                    "RX": "GPIOT_RXN28"
                }
            ],
            "i2c": [
                {
                    "id": 1,
                    "SCL": "GPIOL_73",
                    "SDA": "GPIOL_75"
                }
            ],
            "gpio": [
                {
                    "id": 2,
                    "GPIO-0": "GPIOR_168",
                    "GPIO-1": "GPIOL_17",
                    "GPIO-2": "GPIOL_20",
                    "GPIO-3": "GPIOL_18",
                    "GPIO-4": "GPIOR_187",
                    "GPIO-5": "GPIOL_24",
                    "GPIO-6": "GPIOL_66",
                    "GPIO-7": "GPIOL_62"
                }
            ],
            "pwm": [
                {
                    "id": 3,
                    "PWM": "GPIOT_RXN24"
                }
            ],
            "ws": [],
            "spi": [
                {
                    "id": 4,
                    "SLAVE": 2,
                    "CLK-OUT": "GPIOR_173",
                    "MISO-IN": "GPIOR_174",
                    "MOSI-OUT": "GPIOT_RXN27",
                    "SLAVE-0": "GPIOT_RXP27",
                    "SLAVE-1": "GPIOL_63"
                }
            ],
            "onewire": [],
            "can": [],
            "i2s": []
        }

    
    
   .. note::
    
    1. you can refer this documentation for gpio name `GPIO pins`_.
    2. Increase the ``id`` parameter by 1 sequentially. Gaps in the ``id`` sequence are not allowed.
    3. Duplicate pins are not allowed, for example, each pin (e.g., ``GPIOT_RXP28``) can only be assigned once.
    4. Ensure the ``JSON`` file has the following sequence of peripheral's:

        .. code-block:: json
            
                {
                    "uart": [],
                    "i2c": [],
                    "gpio": [],
                    "pwm": [],
                    "ws": [],
                    "spi": [],
                    "onewire": [],
                    "can": [],
                    "i2s": []
                }

    5. Do not skip any peripherals. If a peripheral is not required, leave the brackets empty for that peripheral.   

   - Run the ``periplex-sync`` command:
   .. code-block::

        sudo periplex-sync -p <filename>.json

   - When running ``periplex-sync``, you may be prompted to edit the Device Tree Source Overlay (DTS) file.
   - For DTS reference documentation, see the video: `DTS demo`_.
   - The DTSO file includes specific configuration details that need to be customized for your device.
   - If any issues occur during the process, the script will display an error message. 
   
2. **Reboot the board:**

   - After making changes in the DTSO, a system reboot is required to apply these configurations.

3. **After reboot:**

   - After rebooting, all configurations have been successfully applied.
