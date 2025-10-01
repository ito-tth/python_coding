import serial
import time
import pyautogui
import keyboard
import time

arduino = serial.Serial('COM7', 9600)  # COMポートは環境に合わせて変更

time.sleep(2)

arduino.write(b'press\n')  # 左キー押して

while not keyboard.is_pressed('a'):
    try:
        p = pyautogui.locateOnScreen(r"C:\Users\ito_t\Videos\Captures\judge.png", confidence=0.5)
        if p is not None:
            x, y = pyautogui.center(p)
            pyautogui.click(x, y)
            pyautogui.click(x, y)
    except pyautogui.ImageNotFounException:
        pass  # 見つからなかったら何もしない
    time.sleep(0.01)

arduino.write(b'release\n')  # 左キー離して