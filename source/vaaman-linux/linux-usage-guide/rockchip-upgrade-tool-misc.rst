:orphan:

#################################################
 Flash different images using Linux_Upgrade_Tool
#################################################

.. attention::

   **Pre-requisites**

   #. You need to have the **Linux_Upgrade_Tool** on your host machine.
         Download `Linux_Upgrade_Tool
         <https://github.com/vicharak-in/Linux_Upgrade_Tool>`_.

   #. You need to load the **rk3399_loader_v1.xx.xxx.bin** file to the
      board.

   .. code::

      ./upgrade_tool db rk3399_loader_v1.xx.xxx.bin

***************************************
 Flashing idbloader.img or idblock.bin
***************************************

.. code::

   ./upgrade_tool wl 0x40 idbloader.img

or

.. code::

   ./upgrade_tool wl 64 idbloader.img

*********************
 Flashing u-boot.img
*********************

.. code::

   ./upgrade_tool wl 0x4000 u-boot.img

or

.. code::

   ./upgrade_tool wl 16384 u-boot.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -u u-boot.img

********************
 Flashing trust.img
********************

.. code::

   ./upgrade_tool wl 0x6000 trust.img

or

.. code::

   ./upgrade_tool wl 24576 trust.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -t trust.img

*******************
 Flashing misc.img
*******************

.. code::

   ./upgrade_tool wl 0x8000 misc.img

or

.. code::

   ./upgrade_tool wl 32768 misc.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -m misc.img

*******************
 Flashing boot.img
*******************

.. code::

   ./upgrade_tool wl 0xa000 boot.img

or

.. code::

   ./upgrade_tool wl 40960 boot.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -b boot.img

***********************
 Flashing recovery.img
***********************

.. code::

   ./upgrade_tool wl 0x2a000 recovery.img

or

.. code::

   ./upgrade_tool wl 174080 recovery.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -r recovery.img

Flashing backup.img

.. code::

   ./upgrade_tool wl 0x3a000 backup.img

or

.. code::

   ./upgrade_tool wl 241664 backup.img

or if you used **Rockchip updateimg firmware** method to flash system
image, you can use

.. code::

   ./upgrade_tool di -k backup.img

***********************
 Flashing userdata.img
***********************

.. code::

   ./upgrade_tool wl 0x4a000 userdata.img

or

.. code::

   ./upgrade_tool wl 307200 userdata.img

*********************
 Flashing rootfs.img
*********************

.. code::

   ./upgrade_tool wl 0xca000 rootfs.img

or

.. code::

   ./upgrade_tool wl 81920 rootfs.img
