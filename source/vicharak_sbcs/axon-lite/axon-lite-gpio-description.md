---
orphan: true
---

(axon-lite-gpio-description)=

# Axon Lite GPIO Description

Vicharak Axon Lite board features a 40-pin GPIO (General-Purpose Input/Output)
header that provides flexible options for connecting and controlling external
devices. Through software settings, you can configure these pins as either
input or output, making them adaptable for various applications.

Out of the 40 pins on the header, 27 are dedicated GPIO pins. These GPIO pins 
can be used as digital inputs or outputs to control or read from external 
hardware. 

The remaining pins are dedicated to other functions, such as: 
- Power supply (3.3V and 5V) 
- Ground (GND) 
- Specific interfaces (I2C, SPI, UART, PWM, etc.) 
- ADC (Analog-to-Digital Converter) inputs 
- DAC (Digital-to-Analog Converter) outputs 
- I2S (Inter-IC Sound) 
- CAN (Controller Area Network) 
- eDP (Embedded DisplayPort) 
- PCIe (Peripheral Component Interconnect Express) 
- MIPI CSI/DSI 
- USB 
- Debug headers 
- UART debug (Pin 8 and 10) 
- Buttons (Power, Reset, Recovery, Maskrom)

<!-- TODO: Update Vicharak config to be suitable for Axon Lite -->
## GPIO Voltage Level
RK3576 SoC has three multiple GPIO voltage levels. Below table shows the
voltage level of Axon Lite GPIOs.

:::{list-table}
:widths: 40 40
:header-rows: 1

-
  - GPIO
  - Voltage Level

-
  - UART debug (Pin 2 and 4)
  - 3.3V

-
  - SARADC
  - 1.8V

-
  - Other GPIOs
  - 3.3V

:::

## Available GPIOs on Axon Lite

Vicharak Axon Lite board has total **40 GPIOs** available for user which
are accessible on `pin header`.
Below table shows the GPIOs available on Axon Lite board.

:::{warning}
Not all functions can be used at the same time. Only one function can be used
or assigned to a GPIO at a time.
:::

### Axon Lite GPIOs Header

| GPIO number | Function7 | Function6 | Function5 | Function4 | Function3 | Function2 | Function1 | PWR/GND | GPIO | Pin# | Pin# | GPIO | PWR/GND | Function1 | Function2 | Function3 | Function4 | Function5 | Function6 | Function7 | GPIO number |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  |  |  |  | 3.3V |  | <div class='red'>1</div> | <div class='red'>2</div> |  | 5V |  |  |  |  |  |  |  |  |
| 129 |  |  |  |  |  | I2C7_SDA_M2 | UART3_RX_M1 |  | GPIO4_A1 | <div class='green'>3</div> | <div class='red'>4</div> |  | 5V |  |  |  |  |  |  |  |  |
| 128 |  |  |  |  |  | I2C7_SCL_M2 | UART3_TX_M1 |  | GPIO4_A0 | <div class='green'>5</div> | <div class='black'>6</div> |  | GND |  |  |  |  |  |  |  |  |
| 77 |  |  |  | SAI0_MCLK_M0 |  |  | UART7_RTSN_M0 |  | GPIO2_B5 | <div class='green'>7</div> | <div class='orange'>8</div> | Debug |  | UART0_TX_M0 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | GND |  | <div class='black'>9</div> | <div class='green'>10</div> |  |  | UART0_RX_M0 |  |  |  |  |  |  |  |
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

<!-- TODO: Update Vicharak config and serial console suitable for Axon Lite -->
:::{note}

- The default function of pins marked in <span class="orange">orange</span> are
  specific to this board. For example, Pins 27, 28, 29 and 30 cannot be used as GPIOs
  as they are SARADC pins.
- All pins, except those for power supply, are directly connected to the
  System-on-Chip (SoC).
- `UART2` has a default baudrate to **115200 bps**, Need to change baudrate to **1500000 bps**.
  Here, you can find instructions to use UART2 in [Serial Console](#axon-lite-linux-uart-serial-console), 
  and you can also use another UART provided on GPIO Pin, refer to [Vicharak Config Device tree  overlays](/vicharak_sbcs/axon-lite/peripherals/uart) section.
:::

<!-- TODO: FPGA LVDS guide -->
(axon-lite-gpio-transaction)=

## GPIO Numbers translation

|            GPIO0             | Number |     |            GPIO1            | Number |     |           GPIO2            | Number |     |           GPIO3           | Number |     |            GPIO4             | Number |
| :--------------------------: | :----: | :-: | :-------------------------: | :----: | :-: | :------------------------: | :----: | :-: | :-----------------------: | :----: | :-: | :--------------------------: | :----: |
| <div class="yellow">A0</div> |   0    |     | <div class="green">A0</div> |   32   |     | <div class="blue">A0</div> |   64   |     | <div class="red">A0</div> |   96   |     | <div class="orange">A0</div> |  128   |
| <div class="yellow">A1</div> |   1    |     | <div class="green">A1</div> |   33   |     | <div class="blue">A1</div> |   65   |     | <div class="red">A1</div> |   97   |     | <div class="orange">A1</div> |  129   |
| <div class="yellow">A2</div> |   2    |     | <div class="green">A2</div> |   34   |     | <div class="blue">A2</div> |   66   |     | <div class="red">A2</div> |   98   |     | <div class="orange">A2</div> |  130   |
| <div class="yellow">A3</div> |   3    |     | <div class="green">A3</div> |   35   |     | <div class="blue">A3</div> |   67   |     | <div class="red">A3</div> |   99   |     | <div class="orange">A3</div> |  131   |
| <div class="yellow">A4</div> |   4    |     | <div class="green">A4</div> |   36   |     | <div class="blue">A4</div> |   68   |     | <div class="red">A4</div> |  100   |     | <div class="orange">A4</div> |  132   |
| <div class="yellow">A5</div> |   5    |     | <div class="green">A5</div> |   37   |     | <div class="blue">A5</div> |   69   |     | <div class="red">A5</div> |  101   |     | <div class="orange">A5</div> |  133   |
| <div class="yellow">A6</div> |   6    |     | <div class="green">A6</div> |   38   |     | <div class="blue">A6</div> |   70   |     | <div class="red">A6</div> |  102   |     | <div class="orange">A6</div> |  134   |
| <div class="yellow">A7</div> |   7    |     | <div class="green">A7</div> |   39   |     | <div class="blue">A7</div> |   71   |     | <div class="red">A7</div> |  103   |     | <div class="orange">A7</div> |  135   |
| <div class="yellow">B0</div> |   8    |     | <div class="green">B0</div> |   40   |     | <div class="blue">B0</div> |   72   |     | <div class="red">B0</div> |  104   |     | <div class="orange">B0</div> |  136   |
| <div class="yellow">B1</div> |   9    |     | <div class="green">B1</div> |   41   |     | <div class="blue">B1</div> |   73   |     | <div class="red">B1</div> |  105   |     | <div class="orange">B1</div> |  137   |
| <div class="yellow">B2</div> |   10   |     | <div class="green">B2</div> |   42   |     | <div class="blue">B2</div> |   74   |     | <div class="red">B2</div> |  106   |     | <div class="orange">B2</div> |  138   |
| <div class="yellow">B3</div> |   11   |     | <div class="green">B3</div> |   43   |     | <div class="blue">B3</div> |   75   |     | <div class="red">B3</div> |  107   |     | <div class="orange">B3</div> |  139   |
| <div class="yellow">B4</div> |   12   |     | <div class="green">B4</div> |   44   |     | <div class="blue">B4</div> |   76   |     | <div class="red">B4</div> |  108   |     | <div class="orange">B4</div> |  140   |
| <div class="yellow">B5</div> |   13   |     | <div class="green">B5</div> |   45   |     | <div class="blue">B5</div> |   77   |     | <div class="red">B5</div> |  109   |     | <div class="orange">B5</div> |  141   |
| <div class="yellow">B6</div> |   14   |     | <div class="green">B6</div> |   46   |     | <div class="blue">B6</div> |   78   |     | <div class="red">B6</div> |  110   |     | <div class="orange">B6</div> |  142   |
| <div class="yellow">B7</div> |   15   |     | <div class="green">B7</div> |   47   |     | <div class="blue">B7</div> |   79   |     | <div class="red">B7</div> |  111   |     | <div class="orange">B7</div> |  143   |
| <div class="yellow">C0</div> |   16   |     | <div class="green">C0</div> |   48   |     | <div class="blue">C0</div> |   80   |     | <div class="red">C0</div> |  112   |     | <div class="orange">C0</div> |  144   |
| <div class="yellow">C1</div> |   17   |     | <div class="green">C1</div> |   49   |     | <div class="blue">C1</div> |   81   |     | <div class="red">C1</div> |  113   |     | <div class="orange">C1</div> |  145   |
| <div class="yellow">C2</div> |   18   |     | <div class="green">C2</div> |   50   |     | <div class="blue">C2</div> |   82   |     | <div class="red">C2</div> |  114   |     | <div class="orange">C2</div> |  146   |
| <div class="yellow">C3</div> |   19   |     | <div class="green">C3</div> |   51   |     | <div class="blue">C3</div> |   83   |     | <div class="red">C3</div> |  115   |     | <div class="orange">C3</div> |  147   |
| <div class="yellow">C4</div> |   20   |     | <div class="green">C4</div> |   52   |     | <div class="blue">C4</div> |   84   |     | <div class="red">C4</div> |  116   |     | <div class="orange">C4</div> |  148   |
| <div class="yellow">C5</div> |   21   |     | <div class="green">C5</div> |   53   |     | <div class="blue">C5</div> |   85   |     | <div class="red">C5</div> |  117   |     | <div class="orange">C5</div> |  149   |
| <div class="yellow">C6</div> |   22   |     | <div class="green">C6</div> |   54   |     | <div class="blue">C6</div> |   86   |     | <div class="red">C6</div> |  118   |     | <div class="orange">C6</div> |  150   |
| <div class="yellow">C7</div> |   23   |     | <div class="green">C7</div> |   55   |     | <div class="blue">C7</div> |   87   |     | <div class="red">C7</div> |  119   |     | <div class="orange">C7</div> |  151   |
| <div class="yellow">D0</div> |   24   |     | <div class="green">D0</div> |   56   |     | <div class="blue">D0</div> |   88   |     | <div class="red">D0</div> |  120   |     | <div class="orange">D0</div> |  152   |
| <div class="yellow">D1</div> |   25   |     | <div class="green">D1</div> |   57   |     | <div class="blue">D1</div> |   89   |     | <div class="red">D1</div> |  121   |     | <div class="orange">D1</div> |  153   |
| <div class="yellow">D2</div> |   26   |     | <div class="green">D2</div> |   58   |     | <div class="blue">D2</div> |   90   |     | <div class="red">D2</div> |  122   |     | <div class="orange">D2</div> |  154   |
| <div class="yellow">D3</div> |   27   |     | <div class="green">D3</div> |   59   |     | <div class="blue">D3</div> |   91   |     | <div class="red">D3</div> |  123   |     | <div class="orange">D3</div> |  155   |
| <div class="yellow">D4</div> |   28   |     | <div class="green">D4</div> |   60   |     | <div class="blue">D4</div> |   92   |     | <div class="red">D4</div> |  124   |     | <div class="orange">D4</div> |  156   |
| <div class="yellow">D5</div> |   29   |     | <div class="green">D5</div> |   61   |     | <div class="blue">D5</div> |   93   |     | <div class="red">D5</div> |  125   |     | <div class="orange">D5</div> |  157   |
| <div class="yellow">D6</div> |   30   |     | <div class="green">D6</div> |   62   |     | <div class="blue">D6</div> |   94   |     | <div class="red">D6</div> |  126   |     | <div class="orange">D6</div> |  158   |
| <div class="yellow">D7</div> |   31   |     | <div class="green">D7</div> |   63   |     | <div class="blue">D7</div> |   95   |     | <div class="red">D7</div> |  127   |     | <div class="orange">D7</div> |  159   |

<!-- TODO: Update Vicharak config to be suitable for Axon Lite -->

:::{seealso}
[Configure 40-Pin header using vicharak-config utility](#)
**(Will be available soon)**
:::
