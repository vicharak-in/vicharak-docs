Usage guide for Periplex
========================

.. variable 
.. _GPIO docs: https://docs.vicharak.in/_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf
.. _DTS demo: https://www.youtube.com/watch?v=fVuv8Rr6arM
.. _JSON video: https://www.youtube.com/watch?v=iiADhChRriM

.. raw:: html

   <h4>What is <code><span style="font-size: 20px;">periplex-sync</span></code>?</h4>

- ``periplex-sync`` is a command-line tool that can be run on the linux terminal.  
  You can run the following command to get help:

  .. code-block:: console

      vicharak@vicharak:~$ sudo periplex-sync -h
      Usage: periplex-sync <command> [arguments]
      Commands:
          -h/help                                For help                
          -p/path           [Json_file]          Give json file          
          -s/status                              Status of periplex      
          -v/verbose                             Verbose information     
          -a/app            [App name]           Attach applications     

.. raw:: html

   <h4>How to use <code><span style="font-size: 20px;">periplex-sync</span></code>?</h4>

1. **Create the json file:**

   - The ``periplex-sync`` command requires a ``<filename>.json`` configuration file.
   - ``<file_name>.json`` is your ``.json`` file defining the peripherals and pin configurations. 
   
   .. tip::
       - You can refer this video to know what is json file `JSON video`_.
       - You can refer this documentation for gpio pins name `GPIO docs`_.

   - For example, if you need to configure  ``3-UARTs`` and  ``2-I2Cs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs`` and the ``SCL`` and ``SDA`` pins for ``I2Cs`` like this, For :download:`download JSON file </_static/files/periplex1.json>`
   
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
    
   .. note::
    
    1. Increase the ``id`` parameter by 1 sequentially. Gaps in the ``id`` sequence are not allowed.
    2. Duplicate pins are not allowed, for example, each pin (e.g., ``GPIOT_RXP28``) can only be assigned once.
    3. Ensure the ``JSON`` file has the following sequence of peripheral's:

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

    4. Do not skip any peripherals. If a peripheral is not required, leave the brackets empty for that peripheral.   

   - Run the ``periplex-sync`` command:
   .. code-block::

        sudo periplex-sync -p <filename>.json

   - When running ``periplex-sync``, you may be prompted to edit the Device Tree Source Overlay (DTS) file.

   .. tip::
       For non-linux background, DTS reference documentation, see the video: `DTS demo`_.
   
   - The DTSO file includes specific configuration details that need to be customized for your device.
   - If any issues occur during the process, the error message will display on the screen. 

2. **Reboot the board:**

   - After making changes in the DTSO, a system reboot is required to apply these configurations.

3. **After reboot:**

   - After rebooting, all configurations have been successfully applied.
   - You got the ``3-UARTs`` and ``2-I2Cs`` devices like this: 

   .. raw:: html

        <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
        vicharak@vicharak:~$ ls /dev
        autofs           drm_dp_aux0  hugepages    initctl  loop-control  mmcblk0p5    pts        stdin    tty16  tty27  tty38  tty49  tty6      ttyS0     usbmon6      vcs7   vcsu3           video-dec0
        block            fb0          hwrng        input    mali0         mmcblk0p6    ram0       stdout   tty17  tty28  tty39  tty5   tty60     ubi_ctrl  v4l          vcsa   vcsu4           video-enc0
        btrfs-control    fd           i2c-0        kmsg     mapper        mmcblk0p7    random     sw_sync  tty18  tty29  tty4   tty50  tty61     uhid      v4l-subdev0  vcsa1  vcsu5           watchdog
        bus              full         i2c-1        log      media0        mmcblk0p8    rfkill     tty      tty19  tty3   tty40  tty51  tty62     uinput    v4l-subdev1  vcsa2  vcsu6           watchdog0
        cec0             fuse         i2c-10       loop0    mem           mmcblk0rpmb  rga        tty0     tty2   tty30  tty41  tty52  tty63     urandom   v4l-subdev2  vcsa3  vcsu7           zero
        char             gpiochip0    <span style="color:red;">i2c-11</span>       loop1    mmcblk0       mpp_service  rk_cec     tty1     tty20  tty31  tty42  tty53  tty7      usb-ffs   vcs          vcsa4  vendor_storage  zram0
        console          gpiochip1    <span style="color:red;">i2c-12</span>       loop2    mmcblk0boot0  mqueue       rtc        tty10    tty21  tty32  tty43  tty54  tty8      usbmon0   vcs1         vcsa5  vhci
        cpu_dma_latency  gpiochip2    i2c-4        loop3    mmcblk0boot1  net          rtc0       tty11    tty22  tty33  tty44  tty55  tty9      usbmon1   vcs2         vcsa6  video0
        crypto           gpiochip3    i2c-7        loop4    mmcblk0p1     null         shm        tty12    tty23  tty34  tty45  tty56  ttyFIQ0   usbmon2   vcs3         vcsa7  video1
        disk             gpiochip4    i2c-9        loop5    mmcblk0p2     periplex     snd        tty13    tty24  tty35  tty46  tty57  <span style="color:red;">ttyPERI0</span>  usbmon3   vcs4         vcsu   video2
        dma_heap         gpiochip5    iep          loop6    mmcblk0p3     port         spidev0.0  tty14    tty25  tty36  tty47  tty58  <span style="color:red;">ttyPERI1</span>  usbmon4   vcs5         vcsu1  video3
        dri              hdmi_hdcp1x  iio:device0  loop7    mmcblk0p4     ptmx         stderr     tty15    tty26  tty37  tty48  tty59  <span style="color:red;">ttyPERI2</span>  usbmon5   vcs6         vcsu2  video4
        </pre>

   .. tip::
        
        For example, you can try diffrent ``json`` configurations: 

        I. **1-UART**, **1-I2C**, **1-GPIO**, **1-PWM**, and **1-SPI**:
        
        - If you need to configure ``1-UART``, ``1-I2C``, ``1-GPIO``, ``1-PWM`` and ``1-SPI`` device, define each peripheral with its specific pins. For ``SPI``, the ``SLAVE`` parameter specifies the number of slave devices. If you set ``SLAVE`` to 2, you must define both ``SLAVE-0`` and ``SLAVE-1`` pins. If only one slave device is used, set ``SLAVE`` to 1 and define only the ``SLAVE-0`` pin. 
        - For :download:`download JSON file </_static/files/periplex2.json>`
        
        II. **26-UARTs**, **10-I2Cs**, and **12-PWMs**:
        
        - If you need to configure  ``26-UARTs``, ``10-I2Cs`` and ``12-PWMs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs`` and the ``SCL`` and ``SDA`` pins for ``I2Cs`` and the ``PWM`` pins for ``PWMs``.
        - For :download:`download JSON file </_static/files/periplex3.json>`
        
        
        III. **40-UARTs**:
        
        - If you need to configure ``40-UARTs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs``.
        - For :download:`download JSON file </_static/files/periplex4.json>`
            
