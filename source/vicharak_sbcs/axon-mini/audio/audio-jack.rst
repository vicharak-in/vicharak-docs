3.5 mm Audio Jack
==================

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-audio-jack.webp
   :width: 80%

The 3.5 mm audio jack on Axon Mini (QCS6490) provides analog stereo output and,
where supported by the hardware, a microphone input.

Key Features
------------

- Analog stereo output via a 3.5 mm TRS jack
- Headset/jack-detect support where implemented by the board
- Full integration with ALSA, and compatibility with PulseAudio or PipeWire

Getting Started
---------------

Prerequisites

- Linux kernel with QCS6490 audio drivers enabled
- Root access
- ALSA utilities installed (``alsa-utils``)

Headphone jack (3.5 mm)
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   aplay -l
   arecord -l
   aplay -D plughw:0,0 /usr/share/sounds/alsa/Front_Center.wav
   speaker-test -D plughw:0,0 -c 2 -t wav

Headset mic (jack)
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   arecord -D hw:0,0 -f cd -d 5 /tmp/test.wav
   aplay -D plughw:0,0 /tmp/test.wav

Volume
^^^^^^

.. code-block:: bash

   alsamixer

- Press ``F6`` to select the sound card, then unmute **Headphone** / **Output** / **Master**.

6. To play an **.mp3** file, use a program that can decode MP3s.

Install and use a command-line player such as ``mpg123``, ``mpv``, or ``ffplay``.

For example, using ``mpg123``:

.. code-block:: bash

   sudo apt install mpg123
   mpg123 <Audio>.mp3

7. Optional: using PulseAudio or PipeWire

- If you rely on PulseAudio or PipeWire, ensure the ALSA sink is mapped to the
  3.5 mm output.
- Use a mixer application (``pavucontrol`` or ``pw-cli``) to select the correct
  output device (Headphones or Speaker) and input (Microphone) as needed.

Notes
-----

- Board-specific device-tree or kernel configuration may be required to enable
  the 3.5 mm jack or mic bias.
- Sound servers (PulseAudio/PipeWire) may override ALSA settings; ensure the
  correct sink/source is selected for your application.

See Also
--------

- ALSA Project: Advanced Linux Sound Architecture
- PulseAudio and PipeWire sound servers
- alsa-utils: ``arecord``, ``aplay``, ``amixer``
