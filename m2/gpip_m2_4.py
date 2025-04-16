#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep

leds = [LED(pin) for pin in [20, 21, 23, 24]]
btn = Button(25, pull_up=True)
counter = 0

while True:
    btn.wait_for_press()            # 버튼이 눌릴 때까지 대기
    counter = (counter + 1) % 16    # 카운터 증가 (0~15, 4비트)
    for led, bit in zip(leds, format(counter, '04b')):
        led.value = int(bit)        # 각 LED를 비트에 따라 설정
    btn.wait_for_release()          # 버튼이 떼어질 때까지 대기
    sleep(0.1)
