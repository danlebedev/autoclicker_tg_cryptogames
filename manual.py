from logic.system import Emulator
import json


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
        input('Press enter to continue: ')
        emulator.stop()


if '__main__' == __name__:
    main()
