
#################
Speakers
#################


.. image:: /_static/images/rk3588-axon/axon-analog-speaker.webp
   :width: 60%

The axon users can connect broad range of speakers to the board. The axon board uses a ES8388 chip, which integrates a DAC (Digital-to-Analog Converter) and an ADC (Analog-to-Digital Converter) which provides a codec interfaces with the system via the I2S bus and is commonly used in designs requiring high-quality analog audio capture and playback.

Hardware Interface
==================

.. image:: /_static/images/rk3588-axon/axon-audio.webp
   :width: 60%

- **Speaker Specifications:**
  - Load Impedance: 4 ohm
  - Rated Power: 3W

How to Setup
============

Follow these steps to connect and use speakers with the Axon board.

1. Connect the Speaker
----------------------

Connect your speaker to the Axon board:

* Speaker positive → Speaker output pin on Axon (shown in image)
* Speaker negative → Axon GND

Ensure connections are secure and properly seated.

2. Play Audio through Speaker
------------------------------

This section describes how to play audio through the speaker connected to the SBC using ALSA utilities.

Prerequisites
^^^^^^^^^^^^^

Ensure:

* Speaker or headphones are properly connected to the SBC
* ALSA utilities are installed

Install if needed:

.. code-block:: bash

   sudo apt install alsa-utils

Step 1: Identify the Speaker Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List available playback devices:

.. code-block:: bash

   aplay -l

Example output:

.. code-block:: text

   **** List of PLAYBACK Hardware Devices ****
   card 0: Analog [Analog Device], device 0: DAC Playback

Note the:

* card number
* device number

In this example: ``card 0, device 0 → plughw:0,0``

Step 2: Play Audio File
^^^^^^^^^^^^^^^^^^^^^^^

Play an audio file using:

.. code-block:: bash

   aplay -D plughw:0,0 test.wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Select playback device
   * - ``test.wav``
     - Audio file to play

Step 3: Verify Playback
^^^^^^^^^^^^^^^^^^^^^^^

You should hear audio from the connected speaker or headphones.

Step 4: Test Speaker with Built-in Sound
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a test tone or system sound:

.. code-block:: bash

   speaker-test -D plughw:0,0 -c 2 -t wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Playback device
   * - ``-c 2``
     - Stereo channels
   * - ``-t wav``
     - WAV test sound

Stop test with:

.. code-block:: text

   Ctrl + C

Supported Audio Formats
^^^^^^^^^^^^^^^^^^^^^^^

ALSA supports:

* WAV (recommended)
* 16-bit PCM
* Mono or Stereo
* Various sample rates (16 kHz, 44.1 kHz, 48 kHz)

Example:

.. code-block:: bash

   aplay -D plughw:0,0 -f S16_LE -r 16000 -c 1 test.wav

Volume Control
^^^^^^^^^^^^^^

Open ALSA mixer:

.. code-block:: bash

   alsamixer

Use:

* Arrow keys → adjust volume
* ``F6`` → select sound card
* ``M`` → mute/unmute

Ensure output is not muted.

Minimal Quick Start (Recommended for users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   aplay test.wav

This uses the default configured audio output device.

Recommended Playback Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   aplay test.wav

---

Troubleshooting
===============

No sound output
---------------

Check device list:

.. code-block:: bash

   aplay -l

Check volume:

.. code-block:: bash

   alsamixer

Ensure:

* Output channel is enabled
* Volume is not muted
* Test speaker hardware directly:

  .. code-block:: bash

     speaker-test -c 2

---

Notes
=====

* Use ``plughw`` for automatic format conversion
* WAV format is recommended for compatibility
* Ensure speaker is properly powered (if external)
* Load impedance must match speaker specifications (4 ohm for Axon)
* Rated power is 3W per channel

