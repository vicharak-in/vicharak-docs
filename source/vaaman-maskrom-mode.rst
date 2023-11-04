:orphan:

.. _vaaman-maskrom-mode:

#####################
 Vaaman Maskrom Mode
#####################

Maskrom Mode is a special mode that allows the device to be programmed
via USB. This mode can be entered through multiple ways on Vaaman board.

1. Manually shorting the pads using the pogo pin.
2. Interrupting the boot process by pressing ``rbrom`` shortcut key from serial console using keyboard.
3. Enter maskrom mode from u-boot by running ``rbrom`` command from serial console.
4. Pressing the recovery key to enter maskrom mode.

.. note::
    The ``rbrom`` command is only available in u-boot version 2017.09 or
    later. If you are using an older version of u-boot, you can use the
    ``rbrom`` command from the u-boot binary provided in the ``tools``

.. tab-set::

    .. tab-item:: Pogo pins

        .. image:: _static/images/vaaman-maskrom-mode.webp
            :width: 50%

        1. Press the Pogo pin to the pads and continue to hold it.

        2. Connect the USB cable to the board and power it on using the
            power delivery.

        3. Release the Pogo pin after the device enumerates on the host.

        4. The device should now be in maskrom mode.

        .. dropdown:: Success Logs in dmesg

            .. code-block::

                [167792.354111] usb 7-1.4.4: new high-speed USB device number 121 using xhci_hcd
                [167792.432282] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167792.432286] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167799.094533] usb 7-1.4.4: USB disconnect, device number 121
                [167802.337917] usb 7-1.4.4: new high-speed USB device number 122 using xhci_hcd
                [167802.416160] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167802.416165] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167815.734169] usb 7-1.4.4: USB disconnect, device number 122
                [167816.418675] usb 7-1.4.4: new high-speed USB device number 123 using xhci_hcd
                [167816.496530] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167816.496535] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167826.230184] usb 7-1.4.4: USB disconnect, device number 123
                [167826.402492] usb 7-1.4.4: new high-speed USB device number 124 using xhci_hcd
                [167826.482774] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167826.482778] usb 7-1.4.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
                [167826.482779] usb 7-1.4.4: Product: USB-MSC
                [167826.482780] usb 7-1.4.4: Manufacturer: RockChip
                [167826.482781] usb 7-1.4.4: SerialNumber: rockchip
                [167992.118283] usb 7-1.4.4: USB disconnect, device number 124

        .. error::
            Remove the SD-Card or NVMe drive from the board.

        .. note::
            If you are not able to enter Maskrom mode on the first try then,
            Reattach the Pogo pin and press the reset key.

            Try this multiple times until you are able to enter Maskrom mode.

    .. tab-item:: Interrupting boot process

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Connect the TTL serial converter to the board and your host computer.

        .. image:: _static/images/vaaman-serial-uart-pins.webp
           :width: 50%

        3. Quickly press ``CTRL + b`` to interrupt the boot process and force
           the device to enter Maskrom mode.

        4. The device should now be in maskrom mode.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=


    .. tab-item:: U-Boot

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Connect the TTL serial converter to the board and your host computer.

        .. image:: _static/images/vaaman-serial-uart-pins.webp
           :width: 50%

        3. Interrupt the boot process by pressing ``CTRL + c`` on the serial
            console on your host computer.

        4. Run the ``rbrom`` command to enter maskrom mode.

        5. The device should now be in maskrom mode.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=

    .. tab-item:: Recovery key

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Quickly press recovery key to interrupt the boot process and force
           the device to enter Maskrom mode.

        3. The device should now be in maskrom mode.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=

