from logic.system_logic import ADB, Emulator


def menu(emulator):
    while True:
        key = input(
        """Send key and press enter:
1) Single screenshot: s
2) Multiple screenshot: m
3) Quit: q
"""
    )
        if key == 's':
            pass
        elif key == 'm':
            multi_screenshots(emulator=emulator)
        elif key == 'q':
            break
        else:
            pass


def multi_screenshots(emulator):
    input('Press enter to start screenshots record: ')
    screenshots = []
    for _ in range(10):
        screenshots.append(emulator.make_screenshot())

    for screenshot in screenshots:
        emulator.save_screenshot(*screenshot)


def main():
    adb = ADB()
    adb.start()

    emulator = Emulator(
        index=0,
        device_id='emulator-5554',
    )
    emulator.start()
    emulator.connect()
    menu(emulator=emulator)


if '__main__' == __name__:
    main()
