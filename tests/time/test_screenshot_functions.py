from PIL import Image, ImageGrab
from tests.tools import check_time
from computer_vision.tools import screenshot_hsv
from pyautogui import screenshot


def without_transform():
    image = ImageGrab.grab()

def with_transform():
    image = ImageGrab.grab()
    image = image.convert(mode='HSV')

def hsv_screenshot():
    image = screenshot_hsv(0)

def pg_screenshot():
    image = screenshot()

check_time(without_transform, iterations=100)
check_time(with_transform, iterations=100)
check_time(hsv_screenshot, iterations=100)
check_time(pg_screenshot, iterations=100)
