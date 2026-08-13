##############
RTC
##############

The Axon Mini SBC includes a hardware Real-Time Clock (RTC).
This RTC allows the system to keep accurate time even when the main power is turned off and preserves system time across reboots and power cycles.


Specification
--------------

- Connector Type: JST
- Pins: 2
- Pitch: 1mm

Reference/Buy RTC
------------------

User can buy `Raspberry Pi compatible RTC Battery CR2032 <https://thinkrobotics.com/products/rtc-battery-rpi5?variant=49314316943677>`_
with Rated Voltage 3V (Max Voltage 3.3V )


Linux Support
-------------

.. TODO: Add Axon Mini RTC detection / dmesg verification steps


Usage
-----

.. TODO: Add Axon Mini RTC usage commands


Notes
-----

- RTC requires a backup battery to retain time when powered off
- Without a battery, time will reset after power loss

Warnings
--------

- Ensure correct battery polarity before connecting
- Use a compatible RTC battery with the JST connector
- Do not exceed the recommended voltage rating
