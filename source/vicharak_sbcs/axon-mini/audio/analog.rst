#################
Analog Mic
#################

.. TODO: Add Axon Mini analog mic connector image

The Analog Mic input on the Axon Mini board provides a flexible interface for
acoustic sensing using analog microphone technologies. Axon Mini supports
**1 × Analog Mic**.

Wiring and connectors
---------------------

- Connector Type: (Wire To Board) JST
- MPN: WAFER-125L-2A
- Pin: 2 Pin
- Pitch: 1.25 mm
- Current rating (max): 1A each pin

Axon Mini supports an **Analog differential mic**.

.. note::
   If you want to use an analog single-ended microphone, connect the positive
   point to the positive pin of the mic connector and the negative point to ground.

For Single ended mic: `Reference Mic To Buy <https://robu.in/product/microphone-97mm-pack-of-3/>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Mic output → ANALOG_MIC pin (+)
* Mic ground → GND (GPIO GND) on the Axon Mini header

For Differential mic:
^^^^^^^^^^^^^^^^^^^^^

* Mic output → ANALOG_MIC pin (+)
* Mic ground → ANALOG_MIC pin (-)

How to Setup
------------

Follow these steps to connect and use an analog microphone with the Axon Mini board.

1. Connect the microphone
^^^^^^^^^^^^^^^^^^^^^^^^^

Connect your microphone to the Axon Mini board:

* If you are using a single-ended mic, connect ``MIC_OUT`` to ANALOG_MIC (+) and
  microphone ground to Axon Mini GND (GPIO GND)
* If you are using a differential mic, connect ``MIC_OUT`` to ANALOG_MIC (+) and
  ``MIC_GND`` to ANALOG_MIC (-)

Power off the board before connecting the microphone.

2. Detect the microphone
^^^^^^^^^^^^^^^^^^^^^^^^

Boot the Axon Mini board and open a terminal.

Run:

.. code-block:: bash

   arecord -l

This will list available recording devices.

Example:

.. code-block:: text

   vicharak@axon-mini:~$ arecord -l
   **** List of CAPTURE Hardware Devices ****
   ...

* Note the card and device number for the analog mic / codec capture path.
* In commands below, ``plughw:0,0`` is used as an example — replace with your values.

3. Record Audio from Microphone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites
"""""""""""""

Ensure:

* Microphone is properly connected to the SBC
* ALSA utilities are installed

Install if needed:

.. code-block:: bash

   sudo apt install alsa-utils

Step 1: Record Audio
""""""""""""""""""""

.. code-block:: bash

   arecord -D plughw:0,0 -f S16_LE -r 16000 -c 1 test.wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Select microphone device
   * - ``-f S16_LE``
     - 16-bit signed little-endian format
   * - ``-r 16000``
     - Sampling rate (16 kHz)
   * - ``-c 1``
     - Mono recording
   * - ``test.wav``
     - Output file

Step 2: Stop Recording
""""""""""""""""""""""

Press:

.. code-block:: text

   Ctrl + C

The audio will be saved as ``test.wav``.

Step 3: Playback Recorded Audio
"""""""""""""""""""""""""""""""

.. code-block:: bash

   aplay test.wav

Recommended Settings for Speech Applications
"""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   arecord -D plughw:0,0 -f S16_LE -r 16000 -c 1 speech.wav

This configuration is ideal for:

* Speech recognition
* Voice assistants
* Embedded AI applications

Notes
,,,,,

* Use ``plughw`` instead of ``hw`` to allow automatic format conversion
* 16 kHz mono is sufficient for most voice applications
* Higher sample rates (e.g., 44100 Hz) may be used for higher quality audio

Example:

.. code-block:: bash

   arecord -D plughw:0,0 -f S16_LE -r 44100 -c 2 audio.wav

Troubleshooting
---------------

Quick Diagnostic Commands
^^^^^^^^^^^^^^^^^^^^^^^^^

List supported hardware parameters:

.. code-block:: bash

   arecord -D hw:0,0 --dump-hw-params

Check microphone levels:

.. code-block:: bash

   alsamixer

Press ``F4`` → Capture devices

Increase capture volume if needed.

---

No audio detected
^^^^^^^^^^^^^^^^^

Check the following:

* Microphone is connected correctly
* Ground connection is secure
* Microphone output is connected to MIC input
* Device is visible using:

  .. code-block:: bash

     arecord -l

* Capture volume is not muted:

  .. code-block:: bash

     alsamixer

  Press ``F4`` and increase Capture volume.

---

Low audio volume
^^^^^^^^^^^^^^^^

Possible solutions:

* Increase microphone gain using ``alsamixer``
* Use a microphone module with built-in amplifier
* Move closer to the microphone

---

Excessive noise or interference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ensure proper grounding
* Keep microphone wires short
* Avoid routing microphone wires near power or digital signal lines
* Use shielded cables if necessary

---

Hum or buzzing sound
^^^^^^^^^^^^^^^^^^^^

Possible causes:

* Ground loop issues
* Poor shielding
* Electrical interference from nearby components

Solutions:

* Ensure common ground between microphone and Axon Mini
* Use shielded microphone cable
* Keep microphone away from power sources and high-frequency components

---

Verification Checklist
----------------------

Ensure the following:

* Microphone is securely connected
* Microphone appears in ``arecord -l``
* Audio recording works using ``arecord``
* Audio playback works using ``aplay``
* Capture volume is properly set using ``alsamixer``
