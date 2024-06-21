from keyboard import is_pressed
from computer_vision.cv import search_pixel_with_getpixel
from pyautogui import screenshot
from pygetwindow import getActiveWindow
from pynput.mouse import Controller, Button
from computer_vision.cv import locateCenterOnScreen


PLAY_TEMPLATE = 'games/Blum/minigame/play.png'


def listen_keyboard():
    if is_pressed('s'):
        return True
    if is_pressed('q'):
        return False


def main(spins_max):
    print("""To start press: s
To stop press: q""")
    mouse = Controller()
    drop_min = (153, 201, 0)
    drop_max = (213, 255, 50)
    spins = 0

    while True:
        last_click = None
        state = False
        # Хранит количество сделанных скриншотов
        count = 0
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
                count += 1
                window = getActiveWindow()
                region = (window.left, window.top, window.width, window.height)
                image = screenshot(region=region)
                drop_region_coordinates = search_pixel_with_getpixel(
                    image=image,
                    color_min=drop_min,
                    color_max=drop_max,
                    step_string=13,
                    step_pixel=13,
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

                # Делаем проверку кнопки play каждые 50 скринов.
                if count > 50:
                    count = 0
                    locate_play = locateCenterOnScreen(
                        template=PLAY_TEMPLATE,
                        screenshotIm=image,
                        confidence=0.90,
                    )
                    if locate_play:
                        if spins_max <= spins:
                            return
                        locate_play = (
                            window.left + locate_play[0],
                            window.top + locate_play[1],
                        )
                        mouse.position = locate_play
                        mouse.click(Button.left)
                        spins += 1


if __name__ == '__main__':
    spins_max = input("Spins count: ")
    main(int(spins_max))
