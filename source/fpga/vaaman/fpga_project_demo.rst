##########################
FPGA PROJECT DETAILS
##########################


1. LED blinking.
2. Pass the data using UART.


==========================================
STEPS FOR TESTING AND CLONING THE PROJECT
==========================================


1. git clone <git url> for cloning the project.


 ``git clone https://github.com/vicharak-in/LED_BLINKING_DEMO.git`` for cloning the LED blinking whole project.


 ``git clone https://github.com/vicharak-in/UART_RX_TX_DEMO.git`` for cloning the UART demo project.


2. Open the .xml file of the project and follow the steps of interface design to set the desired PLL clock.


Note: There is no need to set the GPIO pins in both projects, as there already exists a .peri.xml file in the repository that contains the input and output pins of the project.


3. Make the proper wire connection on the Vaaman. For that, follow `Download Pinouts <_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf>`_.


 In the led blinking, GPIOR_188 for clock, 4 user leds are used for checking output, that is, GPIOT_RXN27, GPIOT_RXP27, GPIOT_RXP24, and GPIOT_RXN24.


 .. image:: ../../_static/images/led_blink.webp 
 
 In the UART test, GPIOR_188 sets the clock to 100 MHz and connects the UART RX to the Tx on the Vaaman board, which is GPIOL_62, as well as the UART Tx to the Rx on the Vaaman board, which is GPIOL_66.
 
 .. image:: ../../_static/images/uart_connection.webp


4. Synthesize the design, follow the Efinity programmer steps for loading the bitstream, and run the project on the Vaaman board.


5. After programming the Vaaman board with the bitstream, the LED BLINK project's output is immediately displayed through blinking the board's user LEDs. For UART output, launch GTKTERM, which is the serial communication tool, to view the data being transmitted and reflected in the serial terminal.


