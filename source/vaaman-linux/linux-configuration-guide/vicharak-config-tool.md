# Vicharak Linux Configuration Tool

Vicharak linux systems includes **vicharak-config** tool which is purely written
using shell scripts that allows users to configure and setup their linux system configuration.

It provides a **TUI** interface to configure different linux specific configurations.
Use `sudo vicharak-config` to get started.

It is supported on all Debian based systems such as Debian buster/bullseye,
Ubuntu focal/jammy and other third party systems such as Armbian.

:::{admonition} **Fact**
:class: tip
vicharak-config also has a systemd service that is use configure system
prior to system boot and after the system boots.
:::

::::{admonition} **Vicharak Config TUI**
:class: dropdown

```bash
┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
│ Please select an option below:                                                           │
│                                                                                          │
│                                   System Maintenance                                      │
│                                   Hardware                                               │
│                                   Overlays                                               │
│                                   Connectivity                                           │
│                                   Advanced Options                                       │
│                                   User Settings                                          │
│                                   Localization                                           │
│                                   About                                                  │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                                                                                          │
│                         <Ok>                             <Cancel>                        │
│                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

:::{note}
The above menu might be shown differently depending on the terminal style.
:::
::::

## How to navigate around vicharak-config

- Use **UP** or **DOWN** key to move the selection across available options.
- Use **RIGHT** or **LEFT** key to move `in` or `out` of the options menu and also,
  allows you to select **<Ok>** or **<Cancel>** option.
- Alternatively, you can also use **TAB** key to switch between them.
- **Enter** key is used to confirm the corresponding option.
- **ESC** key is used to do back to previous menu.

(#available-features)=

## Available Features

- [System maintenance](#system-maintenance)
  Update packages and bootloader.
- [Hardware configuration](#hardware)
  Capture camera frame, Enable LEDs, Change thermal governor, DSI mirroring
- [Overlays](#overlays)
  Enable DTBO overlays, Build third-party DTBO
- [Connectivity](#connectivity)
  Configure network using **nmtui**
- [Advanced Options](#advanced-options)
  Install GPU library and enable OpenGL support
- [User Settings](#user-settings)
  Change system password and hostname
- [Localization](#localization)
  Change Timezone/Locale/Keyboard and WiFi Country

(#system-maintenance)=

### System Maintenance

This feature allows you to update the packages and bootloader.

- Update packages: This option allows you to update the packages that are installed
  on the system. It uses `apt-get` to update the packages.
- Update bootloader: This option allows you to update the bootloader. It uses
  `setup.sh` installed from `vicharak-firmware` package to update the bootloader.

(#hardware)=

### Hardware

This feature allows you to configure different hardware options.

- Capture camera frame: This option allows you to capture the camera frame using
  `v4l2-ctl`. It uses `v4l2-ctl` to capture the camera frame.
- Enable LEDs: This option allows you to enable/disable the LEDs. It changes the
  leds trigger by echoing the specific trigger to the LED sysfs.
- Change thermal governor: This option allows you to change the thermal governor.
  It changes thermal governor by echoing to the specific sysfs.
- DSI mirroring: This option allows you to enable/disable DSI mirroring.
  It uses `vicharak-config` to enable/disable DSI mirroring.

(#overlays)=

### Overlays

This feature allows you to configure different overlays options.

- Enable DTBO overlays: This option allows you to enable/disable the DTBO overlays.
  It uses `update-uboot` script installed inside rootfs to enable or disable the specific
  dtbo overlay from extlinux configuration.
- Build third-party DTBO: This option allows you to build the third-party DTBO.
  It builds and installs the dtbo using the `device-tree-compiler` utility.

(#connectivity)=

### Connectivity

This feature allows you to configure different connectivity options.

- Configure network: This option allows you to configure network using `nmtui`.

(#advanced-options)=

### Advanced Options

This feature allows you to configure different advanced options.

- Install GPU library:
  This option allows you to install Mali GPU library and enable OpenGL support.

  It uses `apt install` to install the mali library from `userdata` partition
  and enables the `gl4es` library support for converting OpenGL-ES context to OpenGL.

  :::{tip}
  Use `gl4es` prefix with your desired application to run that application with OpenGL.

  Example: `gl4es supertuxkart`
  :::

(#user-settings)=

### User Settings

This feature allows you to configure different user settings.

- Change system password: This option allows you to change the system password.
  It uses `passwd` to change the system password.
- Change hostname: This option allows you to change the system hostname.
  It uses `hostnamectl` to change the system hostname.

(#localization)=

### Localization

This feature allows you to configure different localization options.

- Change Timezone: This option allows you to change the system timezone.
  It uses `timedatectl` to change the system timezone.
- Change Locale: It will generate the new locale as per the selection.
