(build-u-boot)=

# U-Boot (Universal Boot Loader)

## What actually is u-boot?

U-Boot `Das U-Boot` is an open-source bootloader that can be used on various
platforms such as ARM, X86, MIPS, RISC-V and many more.
It is the Universal Boot Loader project and is actually used to boot the
Linux kernel in your Vicharak board.

:::{note}
More information on u-boot can be found on [U-Boot Wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot).
:::

## Getting U-Boot from APT Source

This section explains how to obtain U-Boot from APT sources and the additional features supported exclusively in these package builds.

### Features Exclusive to APT U-Boot Packages
- **HDMI Console & Bootmenu Support**: Users can access U-Boot logs, the console, and the bootmenu on a display connected with HDMI TX0.
- **Keyboard Shortcuts**:
  - To enter the U-Boot console, start pressing Ctrl + C continuously as soon as the vicharak logo appears on the screen. This will allow you to configure the boot process.
- **UART Console**: Users can also access U-Boot logs via the UART interface. Refer to [this guide](https://docs.vicharak.in/vicharak_sbcs/axon/axon-getting-started/#using-serial-console) for instructions on setting up UART.

### Installation
If you need to obtain U-Boot using the APT package manager, you can do so by running:

```sh
sudo apt update
sudo apt install u-boot-rk3588-axon
```

### Potential Issues & Troubleshooting
1. **Keyboard Disconnected During U-Boot**
   - Hot-plugging is not supported in U-boot. If the keyboard is removed while inside U-Boot it will not reconnect automatically. A system reboot is required to detect the keyboard again.
   - If the keyboard does not respond properly, it might be due to an unsupported keyboard. This issue is known and will be addressed in a future update.

2. **Boot console not appearing**
   - Ensure the correct key combination (**Ctrl + C**) is used during boot.
   - If the system boots too quickly, try pressing the key earlier.
