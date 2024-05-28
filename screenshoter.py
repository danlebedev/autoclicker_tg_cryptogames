from logic.system_logic import ADB, Emulator


count = 0


def menu(emulator):
    while True:
        key = input(
        """Send key and press enter:
1) Single screen: s
2) Multiple screen: m
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
    global count
    screenshots = []
    for _ in range(100):
        image = emulator.device.screenshot()
        screenshots.append(image)

    for index in range(len(screenshots)):
        image = screenshots[index]
        image.save(f'screenshots/{index + count}.png', format='PNG')
    
    count += len(screenshots)


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
