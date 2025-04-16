# 🧪 Raspberry Pi GPIO 실습 – 버튼과 LED 제어

이 프로젝트는 Raspberry Pi와 `gpiozero`를 사용하여 버튼과 LED를 제어하는 예제 모음입니다. 총 4가지 문제를 통해 다양한 제어 방식을 익힐 수 있습니다.

---

## 🔌 회로 구성

![회로 이미지](./image3.jpeg)

| 구성 요소 | GPIO 핀 번호 |
|-----------|--------------|
| LED1 (파랑) | 20 |
| LED2 (빨강) | 21 |
| LED3 (빨강) | 23 |
| LED4 (노랑) | 24 |
| 버튼 | 25 |
| 저항 | 330Ω x 4 |

- 버튼은 **풀업(pull_up=True)** 설정으로 사용됩니다.
- LED는 각각 GND를 공유하며, 저항을 통해 연결됩니다.

---
# 문제 1 – 버튼을 누르면 모든 LED가 켜짐

## gpiozero 활용 설명

- `LEDBoard`를 사용하여 여러 개의 LED(GPIO 20, 21, 23, 24)를 하나의 객체로 묶어 제어합니다.
- `Button` 객체는 GPIO 25번에 연결되며 `pull_up=True`로 설정되어 있습니다.
- `button.when_pressed = leds.on` 과 `button.when_released = leds.off` 으로 이벤트 기반으로 LED 제어를 합니다.
- `pause()`를 사용하여 코드가 종료되지 않도록 유지합니다.

## 주요 메서드/클래스
- `LEDBoard(...)`
- `Button(..., pull_up=True)`
- `.when_pressed`, `.when_released`
- `.on()`, `.off()`

# 문제 2 – 버튼을 누를 때마다 LED 상태 토글

## gpiozero 활용 설명

- 각 LED(GPIO 20, 21, 23, 24)는 개별 `LED` 객체로 생성됩니다.
- 버튼은 `Button(25, pull_up=True)`로 설정됩니다.
- 버튼이 눌렸을 때 실행되는 `lambda` 함수를 통해 모든 LED에 대해 `.toggle()` 메서드를 실행하여 상태를 반전시킵니다.
- 이벤트 기반으로 상태를 전환하므로 루프 없이도 동작합니다.

## 주요 메서드/클래스
- `LED(pin)`
- `Button(..., pull_up=True)`
- `.when_pressed`
- `.toggle()`

# 문제 3 – 버튼을 누르면 LED가 순차적으로 켜졌다 꺼짐

## gpiozero 활용 설명

- LED들은 리스트 컴프리헨션으로 `LED(pin)` 객체 배열로 생성됩니다.
- 버튼은 `Button(25)`로 설정되어, `wait_for_press()`와 `wait_for_release()`를 사용해 루프 안에서 동기적으로 작동합니다.
- 각 LED에 대해 `.on()`, `sleep(1)`, `.off()` 순으로 실행되어 순차 제어를 구현합니다.
- 이벤트 기반이 아닌 polling 방식으로 버튼 입력을 기다립니다.

## 주요 메서드/클래스
- `LED(pin)`
- `Button(pin)`
- `.wait_for_press()`, `.wait_for_release()`
- `.on()`, `.off()`





# 문제 4 – 버튼을 누를 때마다 4비트 카운트 출력

## gpiozero 활용 설명

- 4개의 `LED(pin)` 객체를 리스트로 생성합니다.
- 버튼은 `pull_up=True`로 설정된 `Button` 객체를 사용합니다.
- 버튼을 누를 때마다 `counter` 변수를 1씩 증가시키고, 이 값을 4비트 이진수 문자열로 변환합니다.
- `zip()`을 사용하여 각 LED의 `value`를 이진수에 따라 `0` 또는 `1`로 설정합니다.
- `.value` 속성은 불리언 혹은 `0`/`1`을 직접 설정하여 LED ON/OFF 제어가 가능합니다.

## 주요 메서드/클래스
- `LED(pin)`
- `Button(..., pull_up=True)`
- `.value = int(bit)`
- `zip()`, `format(counter, '04b')`
