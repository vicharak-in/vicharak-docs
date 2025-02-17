Installation guide for Periplex
===============================

1. **Update package List:**
   
   - Run the following command to refresh the package list:
    
   .. code-block::

      sudo apt update && sudo apt upgrade


2. **Install periplex Package:**
   
   - Install the periplex package,run the following command:
     
   .. code-block::

      sudo apt install periplex
   
3. **Enable the overlay of Vaaman FPGA Communication:**
   
   - After successfully installing the Periplex package, you need enable ``Vaaman FPGA Communication`` overlay .
   - Run the following command to open the overlay settings.
    
   .. code-block::

      sudo vicharak-config

   - Select the ``Overlays`` option.
   - After selecting Overlays, choose ``Manage overlays``.
   - you can see the ``Enable Vaaman FPGA Communication`` overlay,  enable it, and save the settings.

   .. note::
     Skip the step 3, if overlay is already enabled.

4. **Reboot the Board:**

   - After installing the periplex package and enable the ``Vaaman FPGA Communication`` overlay , you need to reboot the Board.