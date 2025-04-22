#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [8, 7, 16, 20]]
button = Button(25, pull_up=True)

button.when_pressed = lambda: [led.toggle() for led in leds]
pause()
