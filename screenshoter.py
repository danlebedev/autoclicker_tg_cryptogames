from logic.system_logic import ADB, Emulator

adb = ADB()
adb.start()

emulator = Emulator(
    index=0,
    device_id='emulator-5554',
)
emulator.start()
emulator.connect()

input('Press enter to start screenshots record: ')
for count in range(1000):
    image = emulator.device.screenshot()
    image.save(f'screenshots/{count}.png', format='PNG')
