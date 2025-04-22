#!/usr/bin/env python3
from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(8,7,16,20)
button = Button(25, pull_up=True)

# 버튼 상태가 변할 때마다 LED 켜고 끄기
button.when_pressed = leds.on
button.when_released = leds.off

pause()  # 프로그램이 계속 실행되도록 대기
