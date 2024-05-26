from system_logic import Emulator, ADB
import json


ADB_PROCESS = ADB()
with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)


def main():
    for emulator in EMULATORS:
        print(EMULATORS.index(emulator))
        emulator = Emulator(
            index=EMULATORS.index(emulator),
            device_id=emulator,
        )
        emulator.start()
        emulator.connect()
        input()
        emulator.stop()


if '__main__' == __name__:
    ADB_PROCESS.start()
    main()
