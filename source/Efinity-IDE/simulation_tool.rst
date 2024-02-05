*********************************
Installing Simulation Tool
*********************************

Install iVerilog, a free Verilog simulation tool, for compiling and simulating Verilog HDL source code.

- Download the simulator from `bleyer.org/icarus <bleyer.org/icarus>`_.
  or
- To access the source code, visit `github.com/steveicarus/iverilog <github.com/steveicarus/iverilog>`_.


Installing GTKWave
*******************

GTKWave is an open-source tool used for analyzing post-simulation dumpfiles, providing a graphical interface with a waveform viewer and RTL source code navigator. 
It's compatible with the iVerilog simulator, making it useful for debugging simulation models and viewing VCD waveform data.

To download and run the latest Windows version of GTKWave:

1. Visit `gtkwave - Browse Files at Sourceforge.net <https://sourceforge.net/projects/gtkwave/files/>`_. to locate the Windows files for GTKWave.
2. Download and unzip the file.
3. Optionally, add the path to GTKWave's bin folder to your System Variables path if necessary for correct launch.
4. Execute gtkwave.exe found in the bin directory of the installation folder to run the program.

GTKWave Installation in Linux
*****************************
For Linux users, use the following commands:

.. code-block:: shell

   sudo apt-get update
   
   sudo apt-get install gtkwave 



