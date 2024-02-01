Efinix Install in Windows
============================

Double-click the efinity_version.msi installer package and follow the on-screen instructions or,

for installing the shortcut in your desktop directory then run this script :

> <installation directory>/bin/install_desktop.sh

*********************************
Efinity Quik Start
*********************************

For lunching the Efinity Graphical User interface (GUI), Double click on the desktop icon.

or 

Use the Efinity tool using command line and for lunch use this steps :

1. For Setup the environment and path:

   `bin\setup.bat`

 2. Lunch Efinity GUI : 
 
      `bin\setup.bat --run`

 3. Run the Efinity  : 

   - For changing the Project directory : 
   
       `cd %EFINITY_HOME%\project\<project name>`

   - Run Efinity :
   
       `efx_run.bat <project name>.xml`

 4. For help : 

    `efx_run.bat --help`
                        
*********************************
Installing USB Drivers 
*********************************

Download the Zadig software(version 2.7 or later) from [zadig.akeo.ie](https://zadig.akeo.ie/)

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

*********************************
Installing Simulation Tool
*********************************

Install iVerilog, a free Verilog simulation tool, for compiling and simulating Verilog HDL source code.

- Download the simulator from [bleyer.org/icarus](bleyer.org/icarus).
  or
- To access the source code, visit [github.com/steveicarus/iverilog](github.com/steveicarus/iverilog).






Use of Debugger 
====================

The Efinity software features a hardware Debugger, facilitating signal probing in FPGA designs through the JTAG interface.
The Debugger encompasses two debug cores:

- Configure Virtual I/O (vio) cores using a manual flow and the Profile Editor.
- Configure Logic Analyzer (la) cores either through a manual flow or the automated flow of the Debug Wizard.

The subsequent sections provide detailed guidance on both the automated and manual flows.

***********************************************
**Automated debugger** 
***********************************************
Create a Debug Profile:

1. Open the project.
2. Synthesize the design.
3. Launch the Debug Wizard by clicking its icon in the main icon bar.
4. Choose "Elaborated Netlist" or "Post-Map" in the Signals from list.
5. Select led and counter buses from the left list and move them to the right using the >> button.
6. Keep the Probe Type as default, DATA AND TRIGGER.
7. Proceed to the next step. The wizard generates a debug profile.
8. Ensure "Auto Instantiation" is enabled to integrate the debug profile into your project. Click Finish.
9. The software prompts for recompilation. Click OK.
10. Perform a full compile.

.. image:: 
   :width:

Program Trion T20 FPGA on Development Board:

1. Launch the Debugger by choosing Tools > Open Debugger. 
2. Ensure the Trion T20 Development Board is recognized as the USB Target. If not, connect the board and click Refresh USB Targets.
3. Click the Select Image File button.
4. Navigate to the outflow directory and choose bitstream file.
5. Click Start Programming. The console will display programming messages.

.. image:: 
   :width:

Observing Probed Signals in Debugger:

1. Initiate Debugger connection.
2. In Trigger Setup tab, add desired nets.
3. Specify trigger conditions (e.g., value).
4. Start Debugger to capture data upon trigger.
5. Upon completion, GTKWave opens automatically to display waveform.
6. Disconnect Debugger to halt operation.


*******************************************
**Manual Debugger**
*******************************************

*****************************
Create Debugger Profile: 
*****************************

To configure Virtual I/O and Logic Analyzer debug cores in a profile:

1. Open the project.
2. Launch the Debugger via Tools > Open Debugger. Since no debug profile exists, the Profile Editor perspective opens.
3. Add a Virtual I/O core (VIO) using Add Debug Core > Virtual I/O. Configure Probes(input) and source(output) signals as specified (i.e name and width).
4. Add a Logic Analyzer core (LA) via Add Debug Core > Logic Analyzer. Configure probes to capture signals matching VIO settings. the vio0 tab to view captured data in the Value fields.
5. Generate Debug RTL to create necessary debug files.
6. Open debug_top.v and rename "edb_top" as "edb_top_manual."
7. Close the debugger.

.. image:: 
   :width:

**********************************
Add Debug core in your project:  
**********************************

To integrate debug code into your project and compile it:

1. Open the Efinity main window and go to the Project tab.
2. In the Interface Designer, add the JTAG User Tap block, configure it, and generate SDC constraints.
3. Close the Interface Designer.
4. Modify design file by uncommenting specific lines to enable debug code and instantiate debug_top module.
5. Save your changes.
6. Compile the design.

.. image:: 
   :width:

**********************************
Programm the FPGA:  
**********************************

To program the Trion® T20 FPGA on the development board:

1. Open Debugger by choosing Tools > Open Debugger.
2. Confirm the Trion T20 Development Board is recognized as the USB Target; refresh if necessary.
3. Select the FPGA configuration file (bitstream) from the outflow directory using the Select Image File button.
4. Initiate programming by clicking Start Programming, and monitor programming messages in the console.

.. image:: 
   :width:

**********************************
Run the Debugger:  
**********************************

Observing Probed Signals in Debugger:

1. Connect Debugger and navigate to the la0 tab for trigger setup.
2. Add the desire trigger condition.
3. If want the change the vio0 values and Run the debugger.
4. Then its wait for thrigger, after applying trigger open the GTKWave for checking the debug signal.
5. Disconnect Debugger to stop capturing data.