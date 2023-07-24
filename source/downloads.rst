.. _downloads:

Vaaman Downloads
================

OS Images
^^^^^^^^^
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - **Operating System**
      - **Variant**

    * - Android
      - `Android 12.1 <http://24.199.117.173/linux-system-images/vaaman/android/>`_

    * - Debian
      - `Bullseye <http://24.199.117.173/linux-system-images/vaaman/debian>`_

    * - Ubuntu
      - `Focal 20.04 <http://24.199.117.173/linux-system-images/vaaman/ubuntu>`_

    * - Community Images
      - **Coming Soon**

.. note::
    The images are compressed using XZ. You can use `7zip <https://www.7-zip.org/>`_ or `WinRAR <https://www.win-rar.com/>`_ to extract the file.

    For **Linux**, you can use the following command to extract the image:

    .. code-block:: console

       xz -d <image_name>.xz

|

.. seealso::
   How to flash the image to the board: :doc:`Flashing the image <vaaman-linux/linux-usage-guide/rockchip-develop-guide>`

   :doc:`Vaaman Debian and Ubuntu Guide <vaaman-linux/linux-usage-guide/debian-ubuntu-guide>`

OS Utilities
^^^^^^^^^^^^

.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - **Utility**
      - **Download Link**

    * - Rockchip Linux Upgrade Tool
      - `V2.1 <https://github.com/vicharak-in/Linux_Upgrade_Tool>`_

    * - Rockchip RkDevTool
      - `V2.96 <https://github.com/vicharak-in/rockchip-tools/blob/master/windows/RKDevTool_Release_v2.96.zip>`_

    * - Rockchip Windows Drivers
      - `V5.12 <https://github.com/vicharak-in/rockchip-tools/blob/master/windows/DriverAssitant_v5.12.zip>`_

    * - Balena Etcher
      - `V1.18.11 <https://github.com/balena-io/etcher/releases/tag/v1.18.11>`_

FPGA Sample files
^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - **FPGA flash file type**
      - **Download Link**

    * - Hex file
      - `Simple LED Blink Hex Demo <_static/files/sample_led_blink_t120_demo_hex.zip>`_

    * - Bitstream file
      - `Simple LED Blink Bit Demo <_static/files/sample_led_blink_t120_demo_bit.zip>`_

Data-sheets
^^^^^^^^^^^
`Rockchip RK3399 Datasheet <https://www.rockchip.fr/RK3399%20datasheet%20V1.8.pdf>`_

`Efinix Trion T120 Datasheet <https://www.efinixinc.com/docs/trion120-ds-v3.4.pdf>`_

`Rockchip RK3399 TRM V1.3 Part1 <https://rockchip.fr/Rockchip%20RK3399%20TRM%20V1.3%20Part1.pdf>`_

`Rockchip RK3399 TRM V1.3 Part2 <https://rockchip.fr/Rockchip%20RK3399%20TRM%20V1.3%20Part2.pdf>`_

`Rockchip RK3399 TRM V1.4 Part1 <https://opensource.rock-chips.com/images/e/ee/Rockchip_RK3399TRM_V1.4_Part1-20170408.pdf>`_


Vaaman Pin-outs Guide
^^^^^^^^^^^^^^^^^^^^^
`Download Pinouts <_static/files/Vaaman0.3_Pinout_Guide_Rev0.2.pdf>`_

:ref:`rk3399-gpio-numbers-count`

Mechanical Information
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - **Property**
      - **Value**

    * - Dimensions
      - 85mm x 85mm

    * - Weight
      - X grams

    * - Mounting holes
      - 4x M2.5 holes for easy installation

Step File
^^^^^^^^^
`Download Vaaman 3D File <_static/files/Vaaman_3D_file_V0.3.step.7z>`_

.. note::
   The step file is compressed using 7zip. You can use `7zip <https://www.7-zip.org/>`_ or `WinRAR <https://www.win-rar.com/>`_ to extract the file.

|

.. seealso::
   How to :ref:`Contribute to Vaaman <contributing>`

   :ref:`Frequently asked questions <faq>`

   :ref:`Vaaman FPGA Programming <vaaman-fpga>`
