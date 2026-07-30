# Windows RKDevTool

<!-- TODO: Rewrite this with better explanation (https://docs.radxa.com/en/rock5/rock5a/getting-started/rkdevtool) -->

## Pre-Requisites

(usb-driver)=
### USB drivers installation

Download the Rockchip [USB Drivers-Assistant](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/DriverAssitant_v5.12.zip)
and unpack it.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-run-anyway.webp
:::

::::

Click on `Install` button available on the floating menu.

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-install.webp
:width: 50%
:::

Click on `Yes` button to confirm the installation.

After the installation is complete, click on `OK` button to close the window.

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-install-finished.webp
:width: 50%
:::

(rkdev-install)=
### RKDevTool Installation

Download the Rockchip [RKDevTool](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/RKDevTool_Release_v3.19.zip) and unpack it.

Change Tool language to English.

- Open the `RKDevTool` folder and edit the `config.ini` file.
- Change the `Selected` value from `1` to `2` for `Language` option.
- Save the file and close it.

:::{image} ../../\../../_static/images/windows-rkdevtool-language.webp
:width: 50%
:::

Open the RKDevTool folder and run the `RKDevTool.exe` file.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../\../../_static/images/windows-rkdevtool-run-anyway.webp
:::

::::

:::{image} ../../\../../_static/images/windows-rkdevtool-main-window.webp
:::

## How to use RKDevTool on Windows

Connect the Axon Lite board to the PC using the USB cable. You will see the
`Found One LOADER Device` or `Found One MASKROM Device` message in the RKDevTool window.

:::{image} ../../\../../_static/images/windows-rkdevtool-main-window.webp
:width: 78%
:::

:::{tip}
If you don't see the `Found One LOADER Device` or `Found One MASKROM Device`
message, then you need to put the Axon Lite board in the `Loader Mode` or `Maskrom Mode`.

Refer to the [How to enter Maskrom Mode](https://www.youtube.com/watch?v=rW-R1MJhBGA&ab_channel=Vicharak) for more details.
:::

## Flash RAW Image in eMMC to Axon Lite Board

:::{tip}
Raw image can be flashed in any type of Multi-Media devices like, SD Card, USB including eMMC as well.
Flashing guide in SD Card(#
:::


**1. Once the Axon Lite board is booted into **Maskrom mode**, you can flash the **RAW image** in eMMC to the board.**

**2. [Downloade Loader](https://downloads.vicharak.in/vicharak-axon-lite/rk3576_spl_loader_v1.09.108.bin)**

**3. [Download Video Guide and do follow same instruction](https://vicharak-files.vicharak.in/axon-lite/Flash-All-Image.mp4.7z)**
