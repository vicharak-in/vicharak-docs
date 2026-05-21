#!/usr/bin/env python3
import spidev
import sys

class SimpleSPI:
    def __init__(self, bus=1, device=0):
        """Initialize SPI connection"""
        self.spi = spidev.SpiDev()
        self.bus = bus
        self.device = device

    def open_connection(self):
        """Open SPI connection and configure settings"""
        try:
            self.spi.open(self.bus, self.device)

            # Basic SPI configuration
            self.spi.max_speed_hz = 25000000  # 25MHz
            self.spi.mode = 0  # SPI Mode 0
            self.spi.bits_per_word = 8

            print(f"SPI connection opened: /dev/spidev{self.bus}.{self.device}")
            print(f"Speed: {self.spi.max_speed_hz} Hz, Mode: {self.spi.mode}")
            return True

        except Exception as e:
            print(f"Error opening SPI: {e}")
            return False

    def close_connection(self):
        """Close SPI connection"""
        if self.spi:
            self.spi.close()
            print("SPI connection closed")

    def write_data(self, data):
        """Write data to SPI device"""
        try:
            if isinstance(data, int):
                data = [data]

            print(f"Writing: {[hex(x) for x in data]}")
            self.spi.writebytes(data)
            return True

        except Exception as e:
            print(f"Write error: {e}")
            return False

    def read_data(self, length):
        """Read data from SPI device"""
        try:
            data = self.spi.readbytes(length)
            print(f"Read: {[hex(x) for x in data]}")
            return data

        except Exception as e:
            print(f"Read error: {e}")
            return None

    def transfer_data(self, tx_data):
        """Transfer data (simultaneous read/write)"""
        try:
            if isinstance(tx_data, int):
                tx_data = [tx_data]

            # Store original data before xfer2 call
            tx_original = tx_data.copy()

            rx_data = self.spi.xfer2(tx_data)
            print(f"TX: {[hex(x) for x in tx_original]} → RX: {[hex(x) for x in rx_data]}")
            return rx_data

        except Exception as e:
            print(f"Transfer error: {e}")
            return None

def main():
    """Main function demonstrating basic SPI operations"""
    print("Simple SPI Communication")
    print("=" * 30)

    # Create SPI instance
    spi = SimpleSPI(bus=1, device=0)  # /dev/spidev1.0

    # Open connection
    if not spi.open_connection():
        sys.exit(1)

    try:
        # Basic operations
        print("\n--- Write Operation ---")
        spi.write_data([0x01, 0x02, 0x03])

        print("\n--- Read Operation ---")
        spi.read_data(3)

        print("\n--- Transfer Operation ---")
        spi.transfer_data([0xAA, 0xBB, 0xCC])

    except Exception as e:
        print(f"Error: {e}")

    finally:
        spi.close_connection()

if __name__ == "__main__":
    main()