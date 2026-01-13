
[Amlogic.md](Amlogic.md)
```cf
/ # cd sys/class/gpio/
/sys/class/gpio # ls
export       gpiochip431  gpiochip439  unexport

```
```c
mount -t debugfs debugfs /tmp

cat /tmp/gpio
```
```c
gpiochip1: GPIOs 431-438, parent: platform/soc:pinctrl@fe08e700, aobus-banks:
 gpio-431 (GPIOAO_0            |fixed@vddq_reg      ) out hi
 gpio-432 (GPIOAO_1            )
 gpio-433 (GPIOAO_2            |sdio_wifi           ) in  hi
 gpio-434 (GPIOAO_3            )
 gpio-435 (GPIOAO_4            |fixed@v_12v         ) out lo ACTIVE LOW
 gpio-436 (GPIOAO_5            )
 gpio-437 (GPIOAO_6            )
 gpio-438 (GPIO_TEST_N         |fixed@vddio3v3_reg  ) out hi

gpiochip0: GPIOs 439-511, parent: platform/fe000000.apb4:pinctrl@4000, periphs-banks:
 gpio-439 (GPIOE_0             )
 gpio-440 (GPIOE_1             )
 gpio-441 (GPIOD_0             )
 gpio-442 (GPIOD_1             )
 gpio-443 (GPIOD_2             )
 gpio-444 (GPIOD_3             )
 gpio-445 (GPIOD_4             )
 gpio-446 (GPIOD_5             )
 gpio-447 (GPIOD_6             |fe03a020.crgphy20   ) out hi
 gpio-448 (GPIOD_7             )
 gpio-449 (GPIOD_8             )
 gpio-450 (GPIOD_9             |tas5707-reset-pin   ) out hi
 gpio-451 (GPIOD_10            |fe03a000.crgphy21   ) out lo
 gpio-452 (GPIOD_11            |avout_mute          ) out hi
 gpio-453 (GPIOD_12            )
 gpio-454 (GPIOD_13            )
 gpio-455 (GPIOD_14            )
 gpio-456 (GPIOD_15            )
 gpio-457 (GPIOB_0             )
 gpio-458 (GPIOB_1             )
 gpio-459 (GPIOB_2             )
 gpio-460 (GPIOB_3             )
 gpio-461 (GPIOB_4             )
 gpio-462 (GPIOB_5             )
 gpio-463 (GPIOB_6             )
 gpio-464 (GPIOB_7             )
 gpio-465 (GPIOB_8             )
 gpio-466 (GPIOB_9             )
 gpio-467 (GPIOB_10            )
 gpio-468 (GPIOB_11            )
 gpio-469 (GPIOB_12            )
 gpio-470 (GPIOB_13            )
 gpio-471 (GPIOX_0             )
 gpio-472 (GPIOX_1             )
 gpio-473 (GPIOX_2             )
 gpio-474 (GPIOX_3             )
 gpio-475 (GPIOX_4             )
 gpio-476 (GPIOX_5             )
 gpio-477 (GPIOX_6             |sdio_wifi           ) out hi
 gpio-478 (GPIOX_7             )
 gpio-479 (GPIOX_8             )
 gpio-480 (GPIOX_9             )
 gpio-481 (GPIOX_10            )
 gpio-482 (GPIOX_11            )
 gpio-483 (GPIOX_12            )
 gpio-484 (GPIOX_13            )
 gpio-485 (GPIOX_14            )
 gpio-486 (GPIOX_15            )
 gpio-487 (GPIOX_16            |bt_rfkill           ) out hi
 gpio-488 (GPIOX_17            )
 gpio-489 (GPIOT_0             )
 gpio-490 (GPIOT_1             )
 gpio-491 (GPIOT_2             )
 gpio-492 (GPIOT_3             )
 gpio-493 (GPIOT_4             )
 gpio-494 (GPIOT_5             )
 gpio-495 (GPIOT_6             )
 gpio-496 (GPIOT_7             )
 gpio-497 (GPIOT_8             )
 gpio-498 (GPIOT_9             )
 gpio-499 (GPIOT_10            )
 gpio-500 (GPIOT_11            )
 gpio-501 (GPIOT_12            )
 gpio-502 (GPIOT_13            )
 gpio-503 (GPIOT_14            )
 gpio-504 (GPIOT_15            )
 gpio-505 (GPIOT_16            )
 gpio-506 (GPIOT_17            )
 gpio-507 (GPIOT_18            )
 gpio-508 (GPIOT_19            )
 gpio-509 (GPIOT_20            )
 gpio-510 (GPIOT_21            )
 gpio-511 (GPIOT_22            )

```
[Amlogic.md](Amlogic.md)