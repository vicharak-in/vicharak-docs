.. _faq:

Frequently Asked Questions
==========================

How to take logs
----------------

.. tab-set::

    .. tab-item:: Windows

        - Connect the device to the PC and use the :ref:`Serial Console Tool <using-serial-console>` to open the serial port of the device.

        - Once the serial port is opened, Take the kernel and user space logs by running the following commands in the serial port tool.

        .. code-block:: bash

            sudo dmesg > dmesg.txt
            sudo tar -cvzf system-logs.tar.gz /var/log

        - Once the logs are taken, close the serial port tool and disconnect the device from the PC.

        - Attach the logs to the issue.

        .. note::
            If the device is not booting up, then take the logs from the serial port tool and attach it to the issue.

    .. tab-item:: Linux

        - Connect the device to the PC and use the :ref:`linux-uart-serial-console` to open the serial port of the device.

        - Once the serial port is opened, Take the kernel and user space logs by running the following commands in the serial port tool.

        .. code-block:: bash

            sudo dmesg > dmesg.txt
            sudo tar -cvzf system-logs.tar.gz /var/log

        - Once the logs are taken, close the serial port tool and disconnect the device from the PC.

        - Attach the logs to the issue.

        .. note::
            If the device is not booting up, then take the logs from the serial port tool and attach it to the issue.


How to report a bug
-------------------

For reporting a bug, please follow the following template:

**Issues and Questions Template**

1. Describe the problem
2. Peripherals Connected
3. Take Logs (`<How to take logs_>`_)

.. TODO: Add the template for reporting a bug
   Improve how to report a bug section
