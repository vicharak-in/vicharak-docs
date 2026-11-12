#################
Speakers
#################

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-speaker.webp
   :width: 80%

Axon Mini provides **2 × speaker** outputs. Users can connect a broad range of
speakers to the board for stereo analog playback through the onboard audio path.

Hardware Interface
==================

Speaker Specifications
----------------------

- Quantity: 2 × speaker channels (Left / Right)
- Connector Type: (Wire To Board) JST
- MPN: WAFER-125L-2A
- Pin: 2 Pin
- Pitch: 1.25 mm
- Current rating (max): 1A each pin
- Load Impedance: 4 ohm
- Rated Power: 3W

Reference Speaker
=================

User can buy `TR-WS-2014B Ultra-Thin Cavity Speaker <https://techiesms.com/product/tr-ws-2014b-ultra-thin-cavity-speaker/>`_

How to Setup
============

Follow these steps to connect and use speakers with the Axon Mini board.

1. Connect the Speaker
----------------------

Connect your speakers to the Axon Mini board:

* Speaker positive → Speaker output pin on Axon Mini (``SPK_L`` / ``SPK_R``)
* Speaker negative → Axon Mini GND

Ensure connections are secure and properly seated. Power off the board before
wiring speakers.

2. Play Audio through Speaker
-----------------------------

This section describes how to play audio through the speaker connected to the
SBC using ALSA utilities.

Prerequisites
^^^^^^^^^^^^^

Ensure:

* Speakers are properly connected to the SBC
* ALSA utilities are installed

Install if needed:

.. code-block:: bash

   sudo apt install alsa-utils

.. code-block:: bash

   aplay -l
   speaker-test -D plughw:0,0 -c 2 -t wav
   aplay -D plughw:0,0 /usr/share/sounds/alsa/Front_Left.wav
   aplay -D plughw:0,0 /usr/share/sounds/alsa/Front_Right.wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Select playback device
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

----

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
* Load impedance must match speaker specifications (4 ohm for Axon Mini)
* Rated power is 3W per channel
