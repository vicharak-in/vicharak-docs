.. _downloads:

Vaaman Downloads
================

OS Images
^^^^^^^^^
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - **Operating System**
      - **Download Link**

    * - Android 12.1
      - http://24.199.117.173/linux-system-images/vaaman/android/

    * - Debian 11
      - http://24.199.117.173/linux-system-images/vaaman/debian

    * - Ubuntu 20.04
      - http://24.199.117.173/linux-system-images/vaaman/ubuntu

    * - Community Images
      - Coming Soon

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

    * - Rockchip Android Tool
      - `V1.0 <https://github.com/vicharak-in/Android_Tool>`_

    * - Balena Etcher
      - `V1.18.11 <https://github.com/balena-io/etcher/releases/tag/v1.18.11>`_

FPGA Sample Bitstream and HEX files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Simple LED Blink Demo HEX file <_static/files/sample_led_blink_t120_demo_hex.zip>`_

`Simple LED Blink Demo BIT file <_static/files/sample_led_blink_t120_demo_bit.zip>`_

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
