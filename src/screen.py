import os
import cv2 # pip install opencv-python
import time
import numpy
import mouse
import pyautogui

def get_pics(directory: str) -> list:
    """Grabs the images from /media/<directory> and returns their file names.

    Args:
        dir ([type]): The subfolder (/media/<directory>) for the images to load

    Returns:
        list[any]: A OpenCV image data list 
    """

    loading_screens = []
    for entry in os.scandir(os.getcwd() + f'/media/{directory}'):
        if entry.is_file():
            file_path = os.getcwd().replace('\\', '/') + f'/media/{directory}/' + entry.name
            loading_screens.append({'data': cv2.imread(file_path, 0), 'file': file_path})
    return loading_screens

def check(sh: numpy.ndarray, template, threshold: float) -> bool:
    """Scans the screen and returns if it found the template

    Args:
        sh (numpy.ndarray): Image of the current screen
        template ([type]): Image of what to find
        threshold (float): Detection threshold

    Returns:
        bool: If it found the template given on screen
    """

    res = cv2.matchTemplate(sh, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if loc[0].size != 0:
        return True
    return False

def screen_loop(threshold: float, dir_content: dict) -> None:
    """Returns when found the screen

    Args:
        dir_name (str): Directory of training pictures
        threshold (float): [description]
    
    Returns:
        str: Path of the image that was found
    """

    while True:
        time.sleep(0.2)
        screenshot = numpy.asarray(pyautogui.screenshot().convert(mode='L'))

        for folder in [d for d in os.listdir() if d.isdir()]:
            for screen in get_pics(folder):
                if check(screenshot, screen['data'], threshold):
                    return screen['file']

def click(image: str, timeout, left=True):
    """Click the location of the image (if found)

    Args:
        image (str): Image path to click
        timeout (int or float): Time in seconds to hold the mouse down

    Returns:
        bool: If the location could be found
    """

    try:
        click_location = pyautogui.locateOnScreen(image)
        x, y = pyautogui.center(click_location)

    except:
        return False
    
    else:
        mouse.move(x, y)
        mouse.press(button=mouse.LEFT if left else mouse.RIGHT)
        time.sleep(timeout)
        return True