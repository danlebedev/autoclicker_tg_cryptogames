from logic.system import ADB, Emulator
from keyboard import is_pressed


def menu(emulator):
    while True:
        key = input(
        """Send key and press enter:
1) Single screenshot: s
2) Multiple screenshot: m
3) Quit: q

Input your choice: """
    )
        if key == 's':
            single_screenshot(emulator=emulator)
        elif key == 'm':
            multi_screenshots(emulator=emulator)
        elif key == 'q':
            break



def single_screenshot(emulator):
    print("Start: ctrl\nStop: q")
    while True:
        if is_pressed('ctrl'):
            emulator.make_and_save_screenshot()
        elif is_pressed('q'):
            break


def multi_screenshots(emulator):
    print("Start: ctrl\nStop: q")
    screenshots = []
    while True:
        if is_pressed('ctrl'):
            while True:
                if is_pressed('q'):
                    break
                screenshots.append(emulator.make_screenshot())
            break
        elif is_pressed('q'):
            break
    key = input("""Screenshots is done.
1) Save: s
2) Don't save: q

Input your choice: """)
    if key == 's':
        print("Wait for saving...")
        for screenshot in screenshots:
            emulator.save_screenshot(*screenshot)


def main():
    adb = ADB()
    adb.start()

    emulator = Emulator(
        index=3,
        device_id='emulator-5560',
    )
    emulator.start()
    emulator.connect()
    menu(emulator=emulator)


if __name__ == '__main__':
    main()
