# Windows RKDevTool

## Pre-requisites

### USB drivers installation

Download the Rockchip [USB DriverAssistant](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/DriverAssitant_v5.12.zip) and unpack it.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../_static/images/windows-usb-driver-assistant-run-anyway.png
:::

::::

Click on `Install` button available on the floating menu.

:::{image} ../../_static/images/windows-usb-driver-assistant-install.png
:width: 50%
:::

Click on `Yes` button to confirm the installation.

After the installation is complete, click on `OK` button to close the window.

:::{image} ../../_static/images/windows-usb-driver-assistant-install-finished.png
:width: 50%
:::

### RKDevTool installation

Download the Rockchip [RKDevTool](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/RKDevTool_Release_v2.96.zip) and unpack it.

Change Tool language to English.

- Open the `RKDevTool` folder and edit the `config.ini` file.
- Change the `Selected` value from `1`  to `2` for `Language` option.
- Save the file and close it.

:::{image} ../../_static/images/windows-rkdevtool-language.png
:width: 50%
:::

Open the RKDevTool folder and run the `RKDevTool.exe` file.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../_static/images/windows-rkdevtool-run-anyway.png
:::

::::

:::{image} ../../_static/images/windows-rkdevtool-main-window.png
:::

## RKDevTool usage

- Connect the Vaaman board to the PC using the USB cable. You will see the `Found One LOADER Device` or `Found One MASKROM Device` message in the RKDevTool window.

<!--
:::{image} ../../_static/images/windows-rkdevtool-device-found.png
:width: 50%
:::
-->

- Click on the `Upgrade Firmware` button from the top bar and select the `firmware` option.