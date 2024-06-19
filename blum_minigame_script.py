from keyboard import is_pressed
from computer_vision.cv import search_pixel_with_getpixel
from pyautogui import screenshot
from pygetwindow import getActiveWindow
from pynput.mouse import Controller, Button


def listen_keyboard():
    if is_pressed('s'):
        return True
    if is_pressed('q'):
        return False


def main():
    mouse = Controller()
    drop_min = (153, 201, 0)
    drop_max = (213, 255, 50)
    freeze_min = (80, 150, 200)
    freeze_max = (170, 250, 255)
    bomb_min = (90, 90, 70)
    bomb_max = (234, 200, 180)
    skip_pixels = (
        (0, 0, 0),
        (28, 117, 50),
        (24, 99, 42),
        (37, 157, 66),
    )

    last_click = None
    state = False
    while True:
        key = listen_keyboard()
        if key is not None:
            if state != key:
                state = key
                if state is True:
                    print('Start')
                elif state is False:
                    print('Stop')

        if state is True:
            window = getActiveWindow()
            region = (window.left, window.top, window.width, window.height)
            image = screenshot(region=region)
            drop_region_coordinates = search_pixel_with_getpixel(
                image=image,
                color_min=drop_min,
                color_max=drop_max,
                step_string=15,
                step_pixel=15,
                reverse=True
            )

            if drop_region_coordinates:
                drop_coordinates = (
                    window.left + drop_region_coordinates[0],
                    window.top + drop_region_coordinates[1],
                )

                if drop_coordinates != last_click:
                    mouse.position = drop_coordinates
                    mouse.click(Button.left)
                    last_click = drop_coordinates


if __name__ == '__main__':
    print("""To start press: s
To stop press: q""")
    while True:
        main()
