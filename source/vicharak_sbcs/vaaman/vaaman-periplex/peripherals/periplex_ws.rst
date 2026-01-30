################
PERIPLEX WS2812B
################

.. variable
.. _xlights Official Website: https://xlights.org/
.. _xlights Tutorial Video: https://youtu.be/zUUl6SEPphU?si=Gte4jL_36PYGWnGn

This section describes how to interect with the ``WS2812B`` led devices generated on the Vaaman via Periplex.

How to Generate WS2812Bs on Vaaman ?
====================================

1. **Create the json file:**

   - To generate ``10 WS2812B`` devices, you need to create a JSON file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2cmaster": [],
            "gpio": [],
            "pwm": [],
            "ws": [
               {
                     "id": 0,
                     "WS": "GPIOT_RXP28"
               },
               {
                     "id": 1,
                     "WS": "GPIOT_RXN28"
               },
               {
                     "id": 2,
                     "WS": "GPIOL_73"
               },
               {
                     "id": 3,
                     "WS": "GPIOL_75"
               },
               {
                     "id": 4,
                     "WS": "GPIOR_173"
               },
               {
                     "id": 5,
                     "WS": "GPIOL_72"
               },
               {
                     "id": 6,
                     "WS": "GPIOR_174"
               },
               {
                     "id": 7,
                     "WS": "GPIOR_178"
               },
               {
                     "id": 8,
                     "WS": "GPIOT_RXN27"
               },
               {
                     "id": 9,
                     "WS": "GPIOR_183"
               }
            ],
            "spi": [],
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": [],
            "jtag": [],
            "dht": []
         }
   
2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``10 WS2812B`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

      sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot.

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``10 WS2812B`` devices generated through Periplex like this:

   .. raw:: html

         <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 546x; overflow: auto; white-space: pre-wrap;">
            vicharak@vicharak:~$ ls /dev
            autofs           hugepages     mapper        random     tty18  tty4   tty61        vcs    vendor_storage
            block            hwrng         media0        rfkill     tty19  tty40  tty62        vcs1   vhci
            btrfs-control    i2c-0         mem           rga        tty2   tty41  tty63        vcs2   video0
            bus              i2c-1         mmcblk0       rk_cec     tty20  tty42  tty7         vcs3   video1
            cec0             i2c-10        mmcblk0boot0  rtc        tty21  tty43  tty8         vcs4   video2
            char             i2c-4         mmcblk0boot1  rtc0       tty22  tty44  tty9         vcs5   video3
            console          i2c-7         mmcblk0p1     shm        tty23  tty45  ttyFIQ0      vcs6   video4
            cpu_dma_latency  i2c-9         mmcblk0p2     snd        tty24  tty46  ttyS0        vcs7   video-dec0
            crypto           iep           mmcblk0p3     spidev0.0  tty25  tty47  ubi_ctrl     vcsa   video-enc0
            disk             iio:device0   mmcblk0p4     stderr     tty26  tty48  uhid         vcsa1  watchdog
            dma_heap         initctl       mmcblk0p5     stdin      tty27  tty49  uinput       vcsa2  watchdog0
            dri              input         mmcblk0p6     stdout     tty28  tty5   urandom      vcsa3  <span style="color: red; font-weight: bold;">ws2812b-0</span>
            drm_dp_aux0      kmsg          mmcblk0p7     sw_sync    tty29  tty50  usb-ffs      vcsa4  <span style="color: red; font-weight: bold;">ws2812b-1</span>
            fb0              log           mmcblk0p8     tty        tty3   tty51  usbmon0      vcsa5  <span style="color: red; font-weight: bold;">ws2812b-2</span>
            fd               loop0         mmcblk0rpmb   tty0       tty30  tty52  usbmon1      vcsa6  <span style="color: red; font-weight: bold;">ws2812b-3</span>
            full             loop1         mpp_service   tty1       tty31  tty53  usbmon2      vcsa7  <span style="color: red; font-weight: bold;">ws2812b-4</span>
            fuse             loop2         mqueue        tty10      tty32  tty54  usbmon3      vcsu   <span style="color: red; font-weight: bold;">ws2812b-5</span>
            gpiochip0        loop3         net           tty11      tty33  tty55  usbmon4      vcsu1  <span style="color: red; font-weight: bold;">ws2812b-6</span>
            gpiochip1        loop4         null          tty12      tty34  tty56  usbmon5      vcsu2  <span style="color: red; font-weight: bold;">ws2812b-7</span>
            gpiochip2        loop5         periplex      tty13      tty35  tty57  usbmon6      vcsu3  <span style="color: red; font-weight: bold;">ws2812b-8</span>
            gpiochip3        loop6         port          tty14      tty36  tty58  v4l          vcsu4  <span style="color: red; font-weight: bold;">ws2812b-9</span>
            gpiochip4        loop7         ptmx          tty15      tty37  tty59  v4l-subdev0  vcsu5  zero
            gpiochip5        loop-control  pts           tty16      tty38  tty6   v4l-subdev1  vcsu6  zram0
            hdmi_hdcp1x      mali0         ram0          tty17      tty39  tty60  v4l-subdev2  vcsu7


How to interact with generated WS2812Bs ?
=========================================

The Periplex platform dynamically generates ``WS2812B`` devices, which are accessible through device nodes such as:

.. code-block::

    /dev/ws2812b-0
    /dev/ws2812b-1
    /dev/ws2812b-2
    /dev/ws2812b-3
    ...

- These WS2812B device nodes can be used to control the corresponding WS2812B LED strips connected to the specified GPIO pins. You can write data to these device files to change the color and brightness of the LEDs.

.. tip::
  - We use xLights software to control the WS2812B LEDs. You can download the software and find more information about xLights here: `xlights Official Website`_.

Python script to control WS2812B LEDs
-------------------------------------

- This is python code run into your vaaman board and start the Artnet server to get the data from xlights.

.. code-block::
	
	import sys
	import getopt
	import socket
	import logging
	import pyrah
	import os
	import datetime
	import time
	import fcntl
	import struct
	import array
	import signal
	from threading import Thread

	# Configure logging
	logging.basicConfig(
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s'
	)

	# Constants
	PIXEL_BUNCH = 400
	PERIPLEX_ID = 0
	PUSH_DATA = (1 << 30) | (8 << 16) | (ord('a') << 8) | ord('b')

	# Global dictionary to store device file descriptors
	device_fds = {}


	class ArtNetServer:
		"""
		ArtNet server to receive ArtNet packets and process them using specified peripherals.
		"""

		def __init__(self, host='0.0.0.0', port=6454):
			"""
			Initialize the ArtNet server.

			:param host: Host IP address to bind the server
			:param port: Port to bind the server
			"""
			self.host = self.get_host_ip()
			self.port = port
			self.server_socket = None

		def get_host_ip(self):
			"""
			Get host IP address.
			"""
			try:
				with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
					s.connect(("8.8.8.8", 80))
					ip = s.getsockname()[0]
				return ip
			except Exception as e:
				logging.error(f"Error obtaining host IP: {e}")
				return '127.0.0.1'

		def start(self):
			"""
			Start the ArtNet server and listen for incoming packets.
			"""
			try:
				self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				self.server_socket.bind((self.host, self.port))
				logging.info(f"ArtNet server listening on {self.host}:{self.port}")
			except Exception as e:
				logging.error(f"Server error: {e}")
				raise

		def stop(self):
			"""
			Stop the ArtNet server.
			"""
			if self.server_socket:
				self.server_socket.close()
				logging.info("ArtNet server stopped")

		def get_artnet_data(self):
			"""
			Receive ArtNet data.
			"""
			try:
				data, addr = self.server_socket.recvfrom(1024)
				return self.handle_packet(data, addr)
			except Exception as e:
				logging.error(f"Server error: {e}")
				return None

		def handle_packet(self, data, addr):
			"""
			Handle incoming ArtNet packets.
			"""
			if data[:8] == b'Art-Net\x00':
				opcode = data[8:10]
				if opcode == b'\x00\x50':
					return data
				else:
					logging.info(f"Unsupported opcode: {opcode}")
			else:
				logging.warning(f"Received non-ArtNet packet from {addr}")

			return None


	def set_matrix(argv):
		"""
		Parse command line arguments to set matrix dimensions.
		"""
		arg_help = f"{argv[0]} -r <rows> -c <cols>"

		try:
			opts, args = getopt.getopt(
				argv[1:], "h:r:c:", ["help", "rows=", "cols="]
			)
		except getopt.GetoptError:
			print(arg_help)
			sys.exit(2)

		arg_rows = None
		arg_cols = None

		for opt, arg in opts:
			if opt in ("-h", "--help"):
				print(arg_help)
				sys.exit(0)
			elif opt in ("-c", "--cols"):
				arg_cols = arg
			elif opt in ("-r", "--rows"):
				arg_rows = arg

		try:
			print("rows:", arg_rows)
			print("cols:", arg_cols)
			return int(arg_rows), int(arg_cols)
		except Exception:
			print(arg_help)
			sys.exit(2)


	def get_dmx_data(data):
		"""
		Extract DMX data from ArtNet packet.
		"""
		sequence = data[12]
		physical = data[13]
		universe = int.from_bytes(data[14:16], byteorder='little')
		length = int.from_bytes(data[16:18], byteorder='big')
		dmx_data = data[18:18 + length]

		logging.info(
			f"ArtDMX packet: universe={universe}, length={length}, "
			f"sequence={sequence}, physical={physical}"
		)

		return dmx_data


	def open_all_devices(rows):
		"""
		Open all WS2812B device files at startup.
		"""
		global device_fds
		print("Opening all WS2812B devices...")

		for row in range(rows):
			device_name = f"/dev/ws2812b-{row}"
			try:
				fd = os.open(device_name, os.O_RDWR)
				device_fds[row] = fd
			except (FileNotFoundError, PermissionError, OSError) as e:
				print(f"Error opening {device_name}: {e}")
				close_all_devices()
				raise RuntimeError(f"Failed to open device {device_name}")

		print(f"All {rows} devices opened successfully")


	def close_all_devices():
		"""
		Close all open WS2812B device files.
		"""
		global device_fds
		print("Closing all WS2812B devices...")

		for row, fd in device_fds.items():
			try:
				os.close(fd)
			except OSError as e:
				print(f"Error closing /dev/ws2812b-{row}: {e}")

		device_fds.clear()
		print("All devices closed")


	def send_to_ws2812b_device(row, data):
		"""
		Send data to a specific WS2812B device using a pre-opened file descriptor.
		"""
		global device_fds

		if row not in device_fds:
			print(f"Error: Device ws2812b-{row} not opened")
			return False

		try:
			fd = device_fds[row]
			arr = array.array('B', data)
			packed = struct.pack('IIQ', len(data), 0, arr.buffer_info()[0])
			fcntl.ioctl(fd, PUSH_DATA, packed)
			return True
		except OSError as e:
			print(f"Error sending to /dev/ws2812b-{row}: {e}")
			return False


	def signal_handler(sig, frame, server):
		"""
		Handle interrupt signals for graceful shutdown.
		"""
		print("\nReceived interrupt signal, shutting down...")
		server.stop()
		close_all_devices()
		sys.exit(0)


	if __name__ == "__main__":
		server = ArtNetServer()

		try:
			rows, cols = set_matrix(sys.argv)

			# Open all devices at startup
			open_all_devices(rows)

			frame_buffer = []

			# Setup signal handler
			signal.signal(
				signal.SIGINT,
				lambda sig, frame: signal_handler(sig, frame, server)
			)

			try:
				server.start()
				print("ArtNet LED Matrix Controller started. Press Ctrl+C to stop.")

				while True:
					artnet_data = server.get_artnet_data()
					if artnet_data is None:
						continue

					dmx_data = get_dmx_data(artnet_data)
					frame_buffer.extend(dmx_data)

					if len(frame_buffer) >= (rows * cols * 3):
						bytes_per_row = cols * 3

						for col in range(0, cols, PIXEL_BUNCH):
							print(f"Processing column batch starting at {col}")

							pixels = min(PIXEL_BUNCH, cols - col)
							start_led_bytes = col * 3

							for row in range(rows):
								row_start = start_led_bytes + (row * bytes_per_row)
								row_data = frame_buffer[
									row_start:row_start + (pixels * 3)
								]

								print(
									f"Sending to ws2812b-{row}: "
									f"{bytes(row_data).hex(' ')}"
								)

								send_to_ws2812b_device(row, bytes(row_data))

						time.sleep(5 / 1000)
						frame_buffer.clear()

			except KeyboardInterrupt:
				print("\nReceived Ctrl+C, shutting down...")
			except Exception as e:
				print(f"Error in main loop: {e}")
				logging.error("Main loop error", exc_info=True)

		except Exception as e:
			print(f"Error during initialization: {e}")
			logging.error("Initialization error", exc_info=True)

		finally:
			print("Cleaning up...")
			server.stop()
			close_all_devices()
			print("Shutdown complete")


- Run the Python script using the command below to launch the Art-Net server on the Vaaman board. Once the server starts successfully, the following output will be displayed :

.. code-block::

      vicharak@vicharak:~$ sudo python3 artnet.py -r 10 -c 20
      rows: 10
      cols: 20
      2025-12-24 11:23:45,152 - INFO - ArtNet server listening on 192.168.1.98:6454

- Here the rows are ``10`` and cols are ``20``, you can change it as per your requirement.
- Now open the xLights software on your PC and configure the Art-Net output to send data to the Vaaman board. Set the destination IP address to ``192.168.1.98`` and the Art-Net port to ``6454`` (default Art-Net port), means you need to set the Vaaman board IP address in xLights software.
 
.. tip::
  - For how to use the xlights software you can check this video : `xlights Tutorial Video`_.

.. note::
      - Make sure that the Vaaman board and your PC are on the same network to allow proper communication between xLights and the ArtNet server running on the Vaaman board.
      - You might need to run the Python script with superuser privileges (using sudo) to access the WS2812B device files.
      - Ensure that the server is running continuously in the background so it can receive Art-Net data from xLights.

Example of using the WS2812B protocol
-------------------------------------

This section explains how to connect WS2812B LED matrices to the Vaaman board for use with xLights.

1. LED Matrix Configuration

   - In your Python script running on the Vaaman board, you define the LED matrix dimensions using rows and columns.
            
   - For example:
      - ``Rows: 10``
      - ``Columns: 20``

   - Based on this configuration, xLights must be set up to transmit data for a ``10 × 20`` WS2812B LED matrix, which equals ``200`` LEDs in total.

2. Physical LED Connections

   - You must connect ``10`` individual WS2812B LED strips to the Vaaman board.

   - Each strip should contain ``20`` WS2812B LEDs.

   - Every strip represents one row of the LED matrix.

   - Connect each LED strip’s data input (DIN) to the corresponding GPIO pin on the Vaaman board as defined in your JSON configuration file.

