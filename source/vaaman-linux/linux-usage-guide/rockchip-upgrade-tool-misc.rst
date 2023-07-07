:orphan:

Flash different images using Linux_Upgrade_Tool
===============================================

.. attention:: **Pre-requisites**

    1. You need to have the **Linux_Upgrade_Tool** on your host machine.

    2. You need to load the **rk3399_loader_v1.xx.xxx.bin** file to the board.

    ::

        ./upgrade_tool db rk3399_loader_v1.xx.xxx.bin


Flashing idbloader.img or idblock.bin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x40 idbloader.img

or

::

    ./upgrade_tool wl 64 idbloader.img


Flashing u-boot.img
^^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x4000 u-boot.img

or

::

    ./upgrade_tool wl 16384 u-boot.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -u u-boot.img

Flashing trust.img
^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x6000 trust.img

or

::

    ./upgrade_tool wl 24576 trust.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -t trust.img

Flashing misc.img
^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x8000 misc.img

or

::

    ./upgrade_tool wl 32768 misc.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -m misc.img

Flashing boot.img
^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0xa000 boot.img

or

::

    ./upgrade_tool wl 40960 boot.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -b boot.img

Flashing recovery.img
^^^^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x2a000 recovery.img

or

::

    ./upgrade_tool wl 174080 recovery.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -r recovery.img

Flashing backup.img

::

    ./upgrade_tool wl 0x3a000 backup.img

or

::

    ./upgrade_tool wl 241664 backup.img

or if you used `update firmware` method to flash system image, you can use

::

    ./upgrade_tool di -k backup.img

Flashing userdata.img
^^^^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0x4a000 userdata.img

or

::

    ./upgrade_tool wl 307200 userdata.img


Flashing rootfs.img
^^^^^^^^^^^^^^^^^^^

::

    ./upgrade_tool wl 0xca000 rootfs.img

or

::

    ./upgrade_tool wl 81920 rootfs.img
