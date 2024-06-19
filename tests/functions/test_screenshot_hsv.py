from pyautogui import screenshot as screenshot_pg
from computer_vision.tools import screenshot_hsv
from cv2 import cvtColor, COLOR_RGB2HSV
from numpy import array
import json
from os.path import join


save_path = 'tests/output'
region = (10, 10, 15, 15)

def do_screenshot_pg_rgb(region):
    image = screenshot_pg(region=region)
    return array(image)


def do_screenshot_pg_hsv(region):
    image = do_screenshot_pg_rgb(region=region)
    hsv_image = cvtColor(
        image,
        COLOR_RGB2HSV,
    )
    return array(hsv_image)


def do_screenshot_my_hsv(region):
    image = screenshot_hsv(bbox=region)
    return array(image)


def saver(arr, name):
    with open(join(save_path, f'{name}.json'), 'w') as f:
        json.dump(arr.tolist(), f)


saver(do_screenshot_pg_rgb(region), 'rgb')
saver(do_screenshot_pg_hsv(region), 'pg_hsv')
saver(do_screenshot_my_hsv(region), 'my_hsv')
