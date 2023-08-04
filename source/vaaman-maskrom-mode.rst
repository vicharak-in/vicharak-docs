:orphan:

.. _vaaman-maskrom-mode:

#####################
 Vaaman Maskrom Mode
#####################

Maskrom Mode is a special mode that allows the device to be programmed
via USB. This mode can be entered through multiple ways on Vaaman board.

1. Shorting the pads with pogo pin
2. Interrupting the boot process by pressing ``rbrom`` shortcut key.
3. Enter maskrom mode from u-boot by running ``rbrom`` command.

.. note::
    The ``rbrom`` command is only available in u-boot version 2017.09 or
    later. If you are using an older version of u-boot, you can use the
    ``rbrom`` command from the u-boot binary provided in the ``tools``

.. tab-set::

    .. tab-item:: Pogo pins

        .. image:: _static/images/vaaman-maskrom-mode.webp
            :width: 50%

        1. Connect the pogo pin to the pads and continue to hold it.

        2. Connect the USB cable to the board and power it on using the
            power delivery.

        3. Release the pogo pin after the device enumerates on the host.

        4. The device should now be in maskrom mode.

    .. tab-item:: Interrupting boot process

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Quickly press ``CTRL + B`` to interrupt the boot process and force
           the device to enter ``rbrom`` mode.

        3. The device should now be in maskrom mode.

    .. tab-item:: U-Boot

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Interrupt the boot process by pressing ``CTRL + C`` to enter u-boot
           command line.

        3. Run the ``rbrom`` command to enter maskrom mode.

        4. The device should now be in maskrom mode.
