import time
import pynput
import random
import pyautogui

mouse = pynput.mouse.Controller()

def hotbar():
    return \
    {
        # 'name': slot,
        'sword': 1,         
    }

# HUGE thanks to https://stackoverflow.com/a/58043888
def look(x: int, y: int, duration: float=1):
    t = duration/60
    for i in range(duration*60):
        if i < t/2:
            h = i
        else:
            h = t - i
        mouse.move(h*x, h*y)
        time.sleep(1/60)

def random_look(): 
    return random.randint(-1, 1)/10

def look_around():
    look(random_look(), random_look(), duration=random.randint(1, 3))

def walk(direction='w', duration: float=):
    pyautogui.press()
    pyautogui.releas

def wait_attack(sword: bool=True):
    t = 1.25
    if sword:
        t = 0.625

    time.sleep(t)
    return t

def press(left=True):
    pyautogui.click(button=pyautogui.LEFT if left else pyautogui.RIGHT)

def slot(name=None, number: str=None):
    if name:
        number = hotbar()[name]
    pyautogui.press(number)
    time.sleep(.1)
    pyautogui.release(number)

def attack(critical=True):
    if critical:
        pyautogui.press('space')
        time.sleep(0.6)
    press()