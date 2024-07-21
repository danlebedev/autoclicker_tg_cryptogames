from logic.system import Emulator
import json


with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)


def main():
    for index in EMULATORS:
        print(index)
        emulator = Emulator(
            index=int(index),
            device_id=EMULATORS[index],
        )
        emulator.start()
        input('Press enter to continue: ')
        emulator.stop()


if __name__ == '__main__':
    main()
