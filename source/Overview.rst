.. _Overview:

Overview
========

Testing build_and_deploy

1. What is Vaaman

	.. |text_vaaman| replace:: The Vaaman Single Board Computer (SBC) combines the RK3399 processor and Efinix Trion T120 FPGA. It offers a powerful yet energy-efficient computing solution for various applications. The RK3399 processor provides high performance and low power consumption, while the Trion T120 FPGA allows for customizable hardware acceleration. With its compact size, the Vaaman SBC is suitable for space-constrained environments and offers a range of connectivity options. Overall, it empowers developers to create innovative solutions that require both processing power and hardware customization. 

	.. |image_vaaman| image:: images/Vaaman-top.png
		:width: 100%

	.. table:: 
		:widths: 50 50

		+----------------+---------------+
		| |image_vaaman| + |text_vaaman| +
		+----------------+---------------+

2. Features

	The Vaaman Single Board Computer (SBC) offers a range of hardware features, including:

	DISPLAY
		1 x HDMI 2.0 (Micro), Support maximum 4K@60Hz display.

		1 x MIPI, Support 2560x1600@60fps output with dual channel.

	AUDIO
		3.5mm jack with mic
	ETHERNET
		10/100/1000Mbps Ethernet (Realtek RTL8211E)
	CAMERA
		MIPI CSI 2 lanes via FPC connector, support up to 800MP camera
	WIRELESS
   		Integrated WiFi Combo Module (6222B-SRC)

   		WiFi 2.4G+5G WiFi 2T2R

   		BT5.0
	PCIe
   		PCIe Interface via FPC connector
	USB
   		2x USB2.0 HOST, 1x USB3.0, 1x USB3.0 Type-C
	RTC
   		Support RTC, on-board backup battery interface
	IO
		1 x UART

		2 x SPI bus

		2 x I2C bus

		1 x PCM/I2S

		1 x SPDIF

		1 x PWM

		1 x ADC

		6 x GPIO

		2 x 5V DC

		2 x 3.3V power pin
	FPGA Features
		Efinix® T120F324 device in a 324-ball FineLine BGA package.
		
		DRAM Chip DDR3 SDRAM 4Gbit 256Mx16 1.35V/1.5V.
		
		128 Mbit SPI NOR flash memory.
		
		MIPI-CSI RX connector with 4 data lanes and 1 clock lane.
		
		MIPI-CSI TX connector with 4 data lanes and 1 clock lane.
		
		LVDS Transmitter interface connector that supports 20 Lanes.
		
		LVDS Receiver interface connector that supports 20 Lanes.
		
		JTAG headers for configuration.
		
		User selectable voltages from 1.8 V, 2.5 V, and 3.3 V for bank 1B, 1C, and 2F.
		
		40-pin GPIO header supported with 12-pin 1 PMOD and 2 LVDS lane or 25 GPIOs.
		
		10, 20, 25, 30, 50, and 74.25 MHz oscillators for T120F324 PLL input.
		
		4 User LEDs on T120F324 bank 2F.

3. Link to :ref:`getting started <getting-started>`
4. Link to :ref:`vaaman applications <vaaman-applications>`
5. Link to :ref:`Downloads <Downloads>`

