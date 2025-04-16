#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep

btn = Button(25)
leds = [LED(p) for p in (20, 21, 23, 24)]

while True:
    btn.wait_for_press()
    for led in leds:
        led.on()
        sleep(1)
        led.off()
    btn.wait_for_release()
