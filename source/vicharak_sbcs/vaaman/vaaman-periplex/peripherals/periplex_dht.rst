############
PERIPLEX DHT
############

This section explains how to interact with the ``DHT`` devices generated on Vaaman via Periplex.

How to Generate DHTs on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``5 DHT`` devices, Your need to create a json file and copy the following content into it.

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
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": [],
            "jtag": [],
            "dht": [
               {
                  "id": 0,
                  "DHT": "GPIOT_RXP28"
               },
               {
                  "id": 1,
                  "DHT": "GPIOL_73"
               },
               {
                  "id": 2,
                  "DHT": "GPIOR_173"
               },
               {
                  "id": 3,
                  "DHT": "GPIOR_174"
               },
               {
                  "id": 4,
                  "DHT": "GPIOT_RXN27"
               }
            ]
        }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for  ``5 DHT`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

      sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot.

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``5 DHT`` devices generated through periplex like this: 

   .. raw:: html

          <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 520px; overflow: auto; white-space: pre-wrap;">
            autofs           gpiochip2    loop5         periplex   tty13  tty35  tty57     usbmon6      vcsu3
            block            gpiochip3    loop6         port       tty14  tty36  tty58     v4l          vcsu4
            btrfs-control    gpiochip4    loop7         ptmx       tty15  tty37  tty59     v4l-subdev0  vcsu5
            bus              gpiochip5    loop-control  pts        tty16  tty38  tty6      v4l-subdev1  vcsu6
            cec0             hdmi_hdcp1x  mali0         ram0       tty17  tty39  tty60     v4l-subdev2  vcsu7
            char             hugepages    mapper        random     tty18  tty4   tty61     vcs          vendor_storage
            console          hwrng        media0        rfkill     tty19  tty40  tty62     vcs1         vhci
            cpu_dma_latency  i2c-0        mem           rga        tty2   tty41  tty63     vcs2         video0
            crypto           i2c-1        mmcblk0       rk_cec     tty20  tty42  tty7      vcs3         video1
            <span style="color: red; font-weight: bold;">dht-0</span>            i2c-10       mmcblk0boot0  rtc        tty21  tty43  tty8      vcs4         video2
            <span style="color: red; font-weight: bold;">dht-1</span>            i2c-4        mmcblk0boot1  rtc0       tty22  tty44  tty9      vcs5         video3
            <span style="color: red; font-weight: bold;">dht-2</span>            i2c-7        mmcblk0p1     shm        tty23  tty45  ttyFIQ0   vcs6         video4
            <span style="color: red; font-weight: bold;">dht-3</span>            i2c-9        mmcblk0p2     snd        tty24  tty46  ttyS0     vcs7         video-dec0
            <span style="color: red; font-weight: bold;">dht-4</span>            iep          mmcblk0p3     spidev0.0  tty25  tty47  ubi_ctrl  vcsa         video-enc0
            disk             iio:device0  mmcblk0p4     stderr     tty26  tty48  uhid      vcsa1        watchdog
            dma_heap         initctl      mmcblk0p5     stdin      tty27  tty49  uinput    vcsa2        watchdog0
            dri              input        mmcblk0p6     stdout     tty28  tty5   urandom   vcsa3        zero
            drm_dp_aux0      kmsg         mmcblk0p7     sw_sync    tty29  tty50  usb-ffs   vcsa4        zram0
            fb0              log          mmcblk0p8     tty        tty3   tty51  usbmon0   vcsa5
            fd               loop0        mmcblk0rpmb   tty0       tty30  tty52  usbmon1   vcsa6
            full             loop1        mpp_service   tty1       tty31  tty53  usbmon2   vcsa7
            fuse             loop2        mqueue        tty10      tty32  tty54  usbmon3   vcsu
            gpiochip0        loop3        net           tty11      tty33  tty55  usbmon4   vcsu1
            gpiochip1        loop4        null          tty12      tty34  tty56  usbmon5   vcsu2
          </pre>

How to interact with the generated DHTs ?
==========================================

The periplex platform dynamically generates ``DHT`` devices, which are accessible through device nodes such as:

.. code-block::

   /dev/dht-0
   /dev/dht-1
   /dev/dht-2
   ...

These ``DHT`` device nodes allow seamless access to temperature and humidity data from connected ``DHT`` sensors such as ``DHT11``, ``DHT21``, and ``DHT22``.

Example of using DHT device node
--------------------------------

- You can read data from the ``DHT`` sensor using standard file operations. For example, you can use this script to read temperature and humidity data:

.. code-block::

    #include <stdio.h>
    #include <string.h>
    #include <unistd.h>
    #include <fcntl.h>

    #include <sys/ioctl.h>

    #define SET_DHT_SENSOR_TYPE _IOWR('a', 'b', enum dht_type *)
    #define MEASURE_DHT_VALUE _IOWR('a', 'c', void *)
    #define GET_TEMP_HUMD _IOWR('a', 'd', char *)

    enum dht_type {
        DHT11 = 0,
        DHT21 = 1,
        DHT22 = 2
    };

    struct buf {
        int humidity;
        int temperature;
    };

    int main(int argc, char *argv[]) {
        if (argc <= 1) {
            printf("Usage: %s <devpath>\n", argv[0]);
            return 1;
        }

        const char *filepath = argv[1];

        int fd = open(filepath, O_RDWR);
        if (fd < 0) {
            printf("%s no such file found\n", filepath);
            return 1;
        }

        enum dht_type type = DHT11;

        int ret = ioctl(fd, SET_DHT_SENSOR_TYPE, &type);
        if (ret < 0) {
            printf("sensor type set failed\n");
            close(fd);
            return 1;
        }

        ret = ioctl(fd, MEASURE_DHT_VALUE, NULL);
        if (ret < 0) {
            printf("measure failed\n");
            close(fd);
            return 1;
        }

        struct buf b;

        ret = ioctl(fd, GET_TEMP_HUMD, &b);
        if (ret < 0) {
            printf("temp get failed\n");
            close(fd);
            return 1;
        }

        printf("Humidity: %d Temperature: %f C\n", b.humidity / 10,
                (float) b.temperature / 10);

        close(fd);
        return ret;
    }

- you can use ``gcc`` to compile the above code and run the executable with the ``DHT`` device node as an argument like this:

.. code-block::

   vicharak@vicharak:~$gcc dht_read.c -o dht_read
   vicharak@vicharak:~$sudo ./dht_read /dev/dht-0

- you will get the temperature and humidity data from the connected ``DHT`` sensor like this:

.. code-block::

   Humidity: 37 Temperature: 28.500000 C

.. note::
    - Make sure to run the executable with ``sudo`` to have the necessary permissions to access the device nodes.
    - Ensure that the ``DHT`` sensor is properly connected to the specified GPIO pin corresponding to the ``DHT`` device node being accessed.
