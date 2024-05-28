from logic.system_logic import ADB, Emulator


COUNT = 0

def massive_screenshots(emulator):
    input('Press enter to start screenshots record: ')
    screenshots = []
    for count in range(count):
        image = emulator.device.screenshot()
        screenshots.append(image)

    for image in screenshots:
        image.save(f'screenshots/{count}', format='PNG')


def main():
    adb = ADB()
    adb.start()

    emulator = Emulator(
        index=0,
        device_id='emulator-5554',
    )
    emulator.start()
    emulator.connect()
    massive_screenshots(emulator=emulator)


if '__main__' == __name__:
    main()
