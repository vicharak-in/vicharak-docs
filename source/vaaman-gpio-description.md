---
orphan: true
---

(vaaman-gpio-description)=

# Vaaman GPIO Description

## GPIO Voltage Level

RK3399 SoC has three multiple GPIO voltage levels. Below table shows the
voltage level of vaaman GPIOs.

:::{list-table}
:widths: 20 40 80
:header-rows: 1

- - GPIO
  - Voltage Level
  - Tolerance

- - ADC_IN0
  - 1.8V
  - ~1.98V

- - GPIO3_C0 (Pin 32)
  - 3.3V
  - ~3.46V

- - Other GPIOs
  - 3.0V
  - ~3.15V

:::

## Available GPIOs on Vaaman

Vicharak Vaaman board has total **80 GPIOs** available for user. **40 GPIOs**
are accessible on `40 pin header` and **40 GPIOs** are accessible from `FPGA`.
Below table shows the GPIOs available on Vaaman board.

:::{warning}
Not all functions can be used at the same time. Only one function can be used
or assigned to a GPIO at a time.
:::

| GPIO number | Function2 |  Function1   |   GPIO   |             Pin#             |            Pin#             |   GPIO   |              Function1              | Function2  | GPIO number |
| :---------: | :-------: | :----------: | :------: | :--------------------------: | :-------------------------: | :------: | :---------------------------------: | :--------: | :---------: |
|             |           |    +3.3V     |          | <div class='yellow'>1</div>  |  <div class='red'>2</div>   |          |                +5.0V                |            |             |
|     71      |           |   I2C7_SDA   | GPIO2_A7 |  <div class='green'>3</div>  |  <div class='red'>4</div>   |          |                +5.0V                |            |             |
|     72      |           |   I2C7_SCL   | GPIO2_B0 |  <div class='green'>5</div>  | <div class='black'>6</div>  |          |                 GND                 |            |             |
|     75      |           |   SPI2_CLK   | GPIO2_B3 |  <div class='green'>7</div>  | <div class='green'>8</div>  | GPIO4_C4 | <div class='orange'>UART2_TXD</div> |            |     148     |
|             |           |     GND      |          |  <div class='black'>9</div>  | <div class='green'>10</div> | GPIO4_C3 | <div class='orange'>UART2_RXD</div> |            |     147     |
|     146     |           |     PWM0     | GPIO4_C2 | <div class='green'>11</div>  | <div class='green'>12</div> | GPIO4_A3 |              I2S1_SCLK              |            |     131     |
|     150     |           |     PWM1     | GPIO4_C6 | <div class='green'>13</div>  | <div class='black'>14</div> |          |                 GND                 |            |             |
|     149     |           |   SPDIF_TX   | GPIO4_C5 | <div class='green'>15</div>  | <div class='green'>16</div> | GPIO4_D2 |                                     |            |     154     |
|             |           |    +3.3V     |          | <div class='yellow'>17</div> | <div class='green'>18</div> | GPIO4_D4 |                                     |            |     156     |
|     40      |           |     +5V      |          |  <div class='red'>19</div>   | <div class='black'>20</div> |          |                 GND                 |            |             |
|     39      |           |     GND      |          | <div class='black'>21</div>  | <div class='green'>22</div> | GPIO4_D5 |                                     |            |     157     |
|     41      |           |     +5V      |          |  <div class='red'>23</div>   | <div class='green'>24</div> | GPIO1_B2 | <div class='orange'>SPI1_CSn</div>  |            |     42      |
|             |           |     GND      |          | <div class='black'>25</div>  | <div class='green'>26</div> |          |               ADC_IN0               |            |             |
|     64      |           |   I2C2_SDA   | GPIO2_A0 |  <div class='blue'>27</div>  | <div class='blue'>28</div>  | GPIO2_A1 |              I2C2_CLK               |            |     65      |
|     74      | I2C6_SCL  |   SPI2_TXD   | GPIO2_B2 | <div class='green'>29</div>  | <div class='black'>30</div> |          |                 GND                 |            |             |
|     73      | I2C6_SDA  |   SPI2_RXD   | GPIO2_B1 | <div class='green'>31</div>  | <div class='green'>32</div> | GPIO3_C0 |              SPDIF_TX               | UART3_CTSn |     112     |
|     76      |           |   SPI2_CSn   | GPIO2_B4 | <div class='green'>33</div>  | <div class='black'>34</div> |          |                 GND                 |            |             |
|     133     |           | I2S1_LRCK_TX | GPIO4_A5 | <div class='green'>35</div>  | <div class='green'>36</div> | GPIO4_A4 |            I2S1_LRCK_RX             |            |     132     |
|     158     |           |              | GPIO4_D6 | <div class='green'>37</div>  | <div class='green'>38</div> | GPIO4_A6 |              I2S1_SDI               |            |     134     |
|             |           |     GND      |          | <div class='black'>39</div>  | <div class='green'>40</div> | GPIO4_A7 |              I2S1_SDO               |            |     135     |

:::{note}

- The default function of pins marked in <span class="orange">orange</span> is specific to this board.
- All pins, except those for power supply, are directly connected to the
  System-on-Chip (SoC).
- **Pins 3, 5, 27, 28, 29, and 31** are connected to a **3.0V** supply through
  a `4.7K` pull-up resistor.
- **Pin 7** is directly connected to the `MIPI CSI` pin on the board.
- `UART2` is enabled as U-boot and Linux serial console by default.
  Instructions to use UART2 as serial console can be found in
  [Serial Console](#serial-console), and to disable it, refer to
  [Vicharak Config Device tree overlays](#vicharak-config-device-tree-overlays)
  section.
- Both `UART2` and `UART4` support a wide range of baud rates, including
  **115200bps, 500000bps, 1500000bps,** and more.

:::

## GPIO Numbers translation

```{csv-table}
:file: _static/files/vaaman_gpio_numbers_translation_rev0.1.csv
:header: >
: "GPIO0",,,"GPIO1",,,"GPIO2",,,"GPIO3",,,"GPIO4",
:align: left
:width: 50%
```
