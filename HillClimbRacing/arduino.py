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
        p = pyautogui.locateOnScreen(r"C:\Users\ito_t\Videos\Captures\judge.png", confidence = 0.5)
        if p is not None:
            x, y = pyautogui.center(p)
            pyautogui.click(x, y)
            time.sleep(0.5)
            pyautogui.click(x, y)
    except pyautogui.ImageNotFoundException:
        pass  # 見つからなかったら何もしない
    
    try:
        p = pyautogui.locateOnScreen(r"C:\Users\ito_t\Videos\Captures\home.png", confidence = 1)
        if p is not None:
            pyautogui.click(1510,1170)
    except pyautogui.ImageNotFoundException:
        pass
    
    try:
        p = pyautogui.locateOnScreen(r"C:\Users\ito_t\Videos\Captures\start_button.png", confidence = 0.5)
        if p is not None:
            x, y = pyautogui.center(p)
            pyautogui.click(x, y)
    except pyautogui.ImageNotFoundException:
        pass
    
    time.sleep(0.1)

arduino.write(b'release\n')  # 左キー離して