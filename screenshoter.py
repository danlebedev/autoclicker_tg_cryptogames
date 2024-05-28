from logic.system_logic import ADB, Emulator


count = 0


def multi_screenshots(emulator):
    input('Press enter to start screenshots record: ')
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
    multi_screenshots(emulator=emulator)


if '__main__' == __name__:
    main()
