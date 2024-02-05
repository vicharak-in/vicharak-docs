========================
Installation  in Windows
========================

Double-click the efinity_version.msi installer package and follow the on-screen instructions or,

for installing the shortcut in your desktop directory then run this script :

.. code-block:: shell

   <installation directory>/bin/install_desktop.sh

*********************************
Efinity Quick Start
*********************************

For launching the Efinity Graphical User interface (GUI), Double click on the desktop icon.

or 

Use the Efinity tool using command line and for lunch use this steps :

1. For Setup the environment and path:

.. code-block:: shell

   bin\setup.bat

2. Launch Efinity GUI : 

.. code-block:: shell 
   
   bin\setup.bat --run

3. Run the Efinity  : 
- For changing the Project directory : 

.. code-block:: shell

   cd %EFINITY_HOME%\project\<project name>

- Run Efinity :

.. code-block:: shell

   efx_run.bat <project name>.xml

4. For help : 

.. code-block:: shell

   efx_run.bat --help


*********************************
Installing USB Drivers 
*********************************

Download the Zadig software(version 2.7 or later) from `zadig.akeo.ie <https://zadig.akeo.ie/>`_.

Note : Do not need to install in only run this downloaded file.

********************************
Steps for install the drivers 
********************************

1. Connect the board to your computer and power it on.
2. Run Zadig software.
   - Note: Run Zadig as an administrator for persistent USB driver settings.
3. Choose Options > List All Devices.
4. For each interface (ending with "Interface N"):
   - Select libusb-win32 from the Driver drop-down list.
   - Click Replace Driver.
5. Close Zadig software.


