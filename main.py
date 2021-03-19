from machine import Pin, ADC
from time import sleep

builtin_led = Pin(25, Pin.OUT)
led = Pin(22, Pin.OUT)
water_level_sensor = ADC(Pin(28))

while True:
    sleep(1)
    water_value = water_level_sensor.read_u16()
    if water_value < 22000:
        print("Brak wody")
        builtin_led.value(1)
        led.value(1)
    else:
        print("Jest woda")
        builtin_led.value(0)
        led.value(0)

