Installation for linux 
======================

The FPGA used on vaaman is efinix's trion T120F324.Efinity IDE is used for  generating the bit/hex stream 
of your RTL code to run in on FPGA.

You can download the the software from `here <https://www.efinixinc.com/support/efinity.php>`_.

Run the following command on your terminal to extract the downloaded folder content.


.. code-block:: shell

   tar -xvf downloaded_folder_name.tar.bz2

cd <efinix-folder>/bin/ directory and run the following command to setup your IDE

.. code-block:: shell

   source setup.sh

.. Note::

   In some version of ubuntu  after running this command terminal may throw core aborted error.
   This due  missing dev files of libxcb libraries.You can simply install them via 
  
.. code-block:: shell
        
   sudo apt install libxcb*

.. tip::
   Write the above command  at the end of your .bashrc file to avoid writing it every time you start.

For Installation of drivers , from the <efinix-folder>/bin directory run:

.. code-block:: shell

   sudo ./install_usb_driver.sh
   
   After setting up just writing efinity on your terminal will start the efinity software.

For  detailed information: see  `software guide <https://www.efinixinc.com/docs/efinity-ug-v13.1.pdf>`_.


