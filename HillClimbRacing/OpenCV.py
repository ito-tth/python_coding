import pyautogui
import keyboard

pyautogui.press('left')

while not keyboard.is_pressed('a'):
    p = pyautogui.locateOnScreen(r"C:\Users\ito_t\Videos\Captures\judge.png")
    if p != None:
        x,y = pyautogui.center(p)
        pyautogui.click(x,y)