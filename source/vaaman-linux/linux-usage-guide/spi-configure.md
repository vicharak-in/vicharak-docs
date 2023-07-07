# How to configure SPI Flash from Linux userspace

**Vicharak Vaaman** contains a shared SPI flash between **Processor** and **FPGA**.
The SPI Flash needs to be configured to use FPGA.

Make sure you are using Vicharak's kernel and system image. Otherwise this guide will
not follow for you.

## Flashing to SPI

For flashing to SPI flash, Vicharak has modified a utility called `flashcp`.
`flashcp -v hexfile.hex`
