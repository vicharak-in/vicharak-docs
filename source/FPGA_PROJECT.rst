##########################
FPGA PROJECT DETAILS
##########################

1. LED Blinking 
2. pass the data using UART 

==========================================
STEPS FOR TESTING AND CLONNING THE PROJECT
==========================================

1. git clone <git url> for clonning the project.

    ``git clone https://github.com/vicharak-in/LED_BLINKING_DEMO.git`` for clonning the LED Blinking whole project.

    ``git clone https://github.com/vicharak-in/UART_RX_TX_DEMO.git`` for clonning the UART demo project.

2. open the .xml file of the project and follow the steps of interface design to set the desire PLL clock.

Note: There is no need to set the GPIO pins in both the projects as there already exist .peri.xml file in the repository which contain the input and output pins of the project.

3. make the proper wire connection on the Vaaman, For that follow `Download Pinouts <_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf>`_

    in the led blinking , GPIOR_188 for clock, 4 user led used for checking output that is GPIOT_RXN27, GPIOT_RXP27, GPIOT_RXP24, GPIOT_RXN24.

    .. image:: _static/images/LED_BLINK.webp 
    
    in UART test , GPIOR_188 to set the clock 100MHz, connect the UART RX to Tx on the Vaaman board that is GPIOL_62 as well as the UART Tx connect with the Rx on the Vaaman board that is the GPIOL_66.
    
     .. image:: _static/images/UART_CONNECTION.webp 

4. Synthesize the design, follow the Efinity programmer steps for loading the bitstream, and run the project on Vaaman board.

5. After programming the Vaaman board with the bitstream, the LED BLINK project's output is immediately displayed output through blinking the board's USER LEDs. For UART output, launch GTKTERM which is the serial communication tool, to view the data being transmitted and reflected in the serial terminal.

