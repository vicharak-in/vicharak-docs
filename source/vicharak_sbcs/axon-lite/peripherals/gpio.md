## GPIO

GPIO stands for General Purpose Input/Output. It refers to configurable digital pins on microcontrollers or embedded systems that can act as either inputs or outputs, allowing them to read signals (like button presses) or control devices (like LEDs). They serve as the basic interface for interacting with external hardware.

Axon Lite has **40-pin GPIO header pins** which can support multiple interfaces like UART, I2C etc.


### Axon Lite GPIOs Header

| GPIO number | Function7 | Function6 | Function5 | Function4 | Function3 | Function2 | Function1 | PWR/GND | GPIO | Pin# | Pin# | GPIO | PWR/GND | Function1 | Function2 | Function3 | Function4 | Function5 | Function6 | Function7 | GPIO number |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  |  |  |  | 3.3V |  | <div class='red'>1</div> | <div class='red'>2</div> |  | 5V |  |  |  |  |  |  |  |  |
| 129 |  |  |  |  |  | I2C7_SDA_M2 | UART3_RX_M1 |  | GPIO4_A1 | <div class='green'>3</div> | <div class='red'>4</div> |  | 5V |  |  |  |  |  |  |  |  |
| 128 |  |  |  |  |  | I2C7_SCL_M2 | UART3_TX_M1 |  | GPIO4_A0 | <div class='green'>5</div> | <div class='black'>6</div> |  | GND |  |  |  |  |  |  |  |  |
| 77 |  |  |  | SAI0_MCLK_M0 |  |  | UART7_RTSN_M0 |  | GPIO2_B5 | <div class='green'>7</div> | <div class='orange'>8</div> | Debug |  | UART0_TX_M0 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | GND |  | <div class='black'>9</div> | <div class='orange'>10</div> | Debug |  | UART0_RX_M0 |  |  |  |  |  |  |  |
| 112 |  |  |  | SAI1_SDO3_M1 |  | I2C4_SCL_M3 | UART2_TX_M2 / UART3_RTSN_M1 |  | GPIO3_C0 | <div class='green'>11</div> | <div class='green'>12</div> | GPIO3_A0 |  | UART3_TC_M0 | I2C7_SCL_M1 | SPI3_CLK_M0 | SAI3_SCLK_M2 |  |  |  | 96 |
| 111 |  |  |  | SAI1_SDI0_M1 |  | I2C4_SDA_M3 | UART2_RX_M2 / UART3_CTSN_M1 |  | GPIO3_B7 | <div class='green'>13</div> | <div class='black'>14</div> |  | GND |  |  |  |  |  |  |  |  |
| 71 |  |  |  | SAI0_SDO1_M0 |  | I2C4_SDA_M2 | UART8_RX_M1 |  | GPIO2_A7 | <div class='green'>15</div> | <div class='green'>16</div> | GPIO0_C1 |  | UART8_TX_M2 | I2C0_SCL_M1 |  |  |  | I3C0_SCL_M0 |  | 17 |
|  |  |  |  |  |  |  |  | 3.3V |  | <div class='red'>17</div> | <div class='green'>18</div> | GPIO0_C2 |  | UART8_RX_M2 | I2C0_SDA_M1 |  |  |  | I3C0_SDA_M0 |  | 18 |
| 126 |  |  | PWM2_CH6_M3 | SAI1_SDI3_M1 | SPI3_MOSI_M1 |  | UART5_CTSN_M0 |  | GPIO3_D6 | <div class='green'>19</div> | <div class='black'>20</div> |  | GND |  |  |  |  |  |  |  |  |
| 125 |  |  |  | SAI1_SDI2_M1 | SPI3_MISO_M1 | I2C3_SDA_M2 | UART5_TX_M0 |  | GPIO3_D5 | <div class='green'>21</div> | <div class='green'>22</div> | GPIO2_B4 |  | UART7_CTSN_M0 |  |  | SAI0_SDI3_M0 |  |  |  | 76 |
| 124 |  |  |  | SAI1_SDI1_M1 | SPI3_CLK_M1 | I2C3_SCL_M2 | UART5_RX_M0 |  | GPIO3_D4 | <div class='green'>23</div> | <div class='green'>24</div> | GPIO3_D7 |  | UART5_RTSN_M0 |  | SPI3_CSN1_M1 |  | PWM2_CH7_M3 |  |  | 127 |
|  |  |  |  |  |  |  |  | GND |  | <div class='black'>25</div> | <div class='green'>26</div> | GPIO2_A6 |  | UART8_TX_M1 | I2C4_SCL_M2 |  | SAI0_SDO0_M0 |  |  |  | 70 |
| 117 |  |  | PWM2_CH2_M3 | SAI1_SDO0_M1 | SPI1_MISO_M2 |  | UART8_RX_M0 |  | GPIO3_C5 | <div class='green'>27</div> | <div class='green'>28</div> | GPIO2_B6 |  | UART7_TX_M0 / UART8_RTSN_M1 | I2C8_SCL_M2 |  | SAI0_SCLK_M0 |  |  |  | 78 |
| 118 |  |  |  | SAI1_LRCK_M1 | SPI1_MOSI_M2 |  | UART8_TX_M0 |  | GPIO3_C6 | <div class='green'>29</div> | <div class='black'>30</div> |  | GND |  |  |  |  |  |  |  |  |
| 119 |  |  |  | SAI1_SCLK_M1 | SPI1_CLK_M2 |  | UART8_RTSN_M0 |  | GPIO3_C7 | <div class='green'>31</div> | <div class='green'>32</div> | GPIO2_D5 |  | UART6_CTSN_M1 | I2C9_SCL_M2 |  |  | PWM2_CH5_M2 |  |  | 93 |
| 120 |  |  | PWM2_CH3_M3 | SAI1_MCLK_M1 | SPI1_CSN0_M2 |  | UART8_CTSN_M0 |  | GPIO3_D0 | <div class='green'>33</div> | <div class='black'>34</div> |  | GND |  |  |  |  |  |  |  |  |
| 97 |  |  |  | SAI3_LRCK_M2 | SPI3_MOSI_M0 | I2C7_SDA_M1 | UART3_RX_M0 |  | GPIO3_A1 | <div class='green'>35</div> | <div class='green'>36</div> | GPIO2_D4 |  |  | I2C9_SDA_M2 |  |  | PWM2_CH4_M2 |  |  | 92 |
| 79 |  |  |  | SAI0_LRCK_M0 |  | I2C8_SDA_M2 | UART7_RX_M0 / UART8_CTSN_M1 |  | GPIO2_B7 | <div class='green'>37</div> | <div class='green'>38</div> | GPIO3_A3 |  | UART3_RTSN_M0 |  | SPI3_CSN0_M0 | SAI3_SDI_M2 |  |  | CAN_RX_M3 | 99 |
|  |  |  |  |  |  |  |  | GND |  | <div class='black'>39</div> | <div class='green'>40</div> | GPIO3_A2 |  | UART3_CTSN_M0 |  | SPI3_MISO_M0 | SAI3_SDO_M2 |  |  | CAN_TX_M3 | 98 |

:::{note}
You can find [ GPIO Number Translation: ](#axon-lite-gpio-transaction) for Axon Lite.
:::

Before going to configure GPIOs, Need to know some basics:

Let's take one ``GPIO2_B6`` Pin,

|  Pin   |  GPIO    |  GPIO Number  |
| :----: | :------: | :-----------: |
|  28    | GPIO2_B6 |     78        |

- What is GPIO Pin ?
  It is a Pin which locates on GPIO Header on Axon Lite. Axon Lite has 40 Pins on GPIO header.

- What is GPIO Number ?
  You can get GPIO Number from Axon Lite GPIOs Header Table.

- What is GPIO Chip Num ?
  In ``GPIO2_B6``, 2 means GPIO Chip Number.

- What is GPIO Base Number ?
  It depends on GPIO Chip Number, For example, GPIOCHIP2 has base number = 64

- What is GPIO Line ?
  You can get GPIO Line number by substracting GPIO Base Number from GPIO Number. 


### How GPIO Pins can be configured ?

GPIO Pins can be configured in many ways. For example, you can ``write program`` to function pins according to your
requirement or you can simply run command using ``gpiod`` Command line and you can also use GPIO Pins as UART or I2C
Functionality.

:::{warning}
As mention in table, you can use only one function at a time of GPIO Pin.

Let's take one ``GPIO1_D1`` Pin, You have 3 Function to use this GPIO Pin. Like, UART, I2C, SPI
You can only use any of the above one at a time.
:::


Now, Using ``sudo gpioinfo``, you can figure out which pin is located on which gpiochip and gpio_line.

:::{note}
For GPIO2_B6,

GPIO Pin  = 28

GPIO Line = 14 ( GPIO_NUM - GPIO_BASE_NUMBER for CHIP2 ) ( 78 - 64 ) 

GPIO Chip = 2
:::

:::{code}
    vicharak@vicharak:~$ sudo gpioinfo

    gpiochip0 - 32 lines:
            line   0:      unnamed "bt_default_wake_host" input active-high [used]
            line   1:      unnamed       unused   input  active-high 
            line   2:      unnamed       unused   input  active-high 
            line   3:      unnamed       unused   input  active-high 
            line   4:      unnamed       unused   input  active-high 
            line   5:      unnamed  "interrupt"   input  active-high [used]
            line   6:      unnamed  "interrupt"   input  active-high [used]
            line   7:      unnamed       unused   input  active-high 
            line   8:      unnamed       unused   input  active-high 
            line   9:      unnamed       unused   input  active-high 
            line  10:      unnamed       unused   input  active-high 
            line  11:      unnamed       unused   input  active-high 
            line  12:      unnamed       unused   input  active-high 
            line  13:      unnamed       unused   input  active-high 
            line  14:      unnamed       unused   input  active-high 
            line  15:      unnamed       unused   input  active-high 
            line  16:      unnamed       unused   input  active-high 
            line  17:      unnamed       unused   input  active-high 
            line  18:      unnamed "bt_default_wake" output active-high [used]
            line  19:      unnamed       unused   input  active-high 
            line  20:      unnamed       unused  output  active-high 
            line  21:      unnamed       unused   input  active-high 
            line  22:      unnamed       unused   input  active-high 
            line  23:      unnamed       unused   input  active-high 
            line  24:      unnamed     "enable"  output  active-high [used]
            line  25:      unnamed       unused   input  active-high 
            line  26:      unnamed       unused   input  active-high 
            line  27:      unnamed       unused   input  active-high 
            line  28:      "PIN_8"       unused   input  active-high 
            line  29:     "PIN_10"       unused   input  active-high 
            line  30:      unnamed       unused   input  active-high 
            line  31:      unnamed       unused   input  active-high 

:::

:::{note}
If It shows `gpioinfo` not found, you need to install `gpiod`.

sudo apt update

sudo apt gpiod
:::

### Using C Language

Below Program will configure GPIO Header Pin 10 (GPIO_NUM 78) using gpiod library.

Make sure, you have installed ``libgpiod-dev`` in Axon Lite.

:::{code}

    sudo apt update
    sudo apt-get install -y libgpiod-dev
:::


This code will high GPIO-Pin 10 for 5 sec and again put it in Low.

:::{code}

#include <stdio.h>
#include <gpiod.h>
#include <unistd.h>

#define GPIO_CHIP "/dev/gpiochip2"  // Specify the correct GPIO chip device
#define GPIO_NUMBER 78             // Global GPIO number
#define GPIO_CHIP_BASE 64          // The base GPIO number for gpiochip2 

int main()
{
    struct gpiod_chip *chip;
    struct gpiod_line *line;
    int ret;
    int gpio_line = GPIO_NUMBER - GPIO_CHIP_BASE;  // Local GPIO line number

    // Open the GPIO chip
    chip = gpiod_chip_open(GPIO_CHIP);
    if (!chip)
    {
        perror("Failed to open GPIO chip");
        return EXIT_FAILURE;
    }

    // Get the GPIO line (based on the offset calculated)
    line = gpiod_chip_get_line(chip, gpio_line);
    if (!line)
    {
        perror("Failed to get GPIO line");
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Request the GPIO line as an output and set the initial value to low (0)
    ret = gpiod_line_request_output(line, "gpioset", 0);
    if (ret < 0)
    {
        perror("Failed to request GPIO line as output");
        gpiod_line_release(line);  // Ensure the line is released in case of error
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Set GPIO line 135 to high (enable)
    printf("Setting GPIO %d to high (enabled)\n", GPIO_NUMBER);
    ret = gpiod_line_set_value(line, 1);  // Set value to 1 (high)
    if (ret < 0)
    {
        perror("Failed to set GPIO value");
        gpiod_line_release(line);
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Sleep for a while to keep the pin enabled (you can modify the delay as needed)
    sleep(5);  // Keep the GPIO high for 5 seconds

    // Optionally: Set GPIO line to low (disable) after sleep
    printf("Disabling GPIO %d (set to low)\n", GPIO_NUMBER);
    gpiod_line_set_value(line, 0);  // Set value to 0 (low)

    // Release the GPIO line and close the GPIO chip
    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
:::

1. Compile above code using ``gcc <Code_File_Name.c> -o <Executable_File_Name> -lgpiod``
2. Run executable file using `sudo` as it requires privileges, ``sudo ./<Executable_File_Name>``


### Using gpiod Command Line Tool in Linux

- Install ``gpiod`` Command Line Tool

:::{code}

    sudo apt update
    sudo apt install gpiod
:::

- ``gpiodetect`` - List all GPIO chips present on the system, their names, labels and number of GPIO lines.

- ``gpioinfo`` - List all lines of specified GPIO chips, their names, consumers, direction, active state and additional flags.

- ``gpioget`` - Read values of specified GPIO lines.

- ``gpioset`` - Set values of specified GPIO lines, and potentially keep the lines exported and wait until timeout, user input or signal.

:::{note}
For ``GPIO2_B6``, To set GPIO as High X=1 and Low X=0,

``sudo gpioset gpiochip2 14=<X>``

where, 14 is GPIO Line ( 78 - 64 )
:::

- ``gpiofind`` - Find the GPIO chip name and line offset given the line name.

- ``gpiomon`` - Wait for events on GPIO lines, specifying which events to watch, how many events to process before exiting or if the events should be reported to the console.

### How to change Functionality of GPIO Pin Like, UART, I2C etc  ?

For that, we will soon provide `overlay`, on `vicharak-config`.



:::{seealso}
https://en.wikipedia.org/wiki/General-purpose_input/output
:::
