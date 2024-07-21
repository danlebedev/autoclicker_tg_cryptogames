from logic.system import Emulator, ADB
import json
from keyboard import is_pressed


ADB_PROCESS = ADB()
RETRY = 3
coords = {
    "1_1": (0.085, 0.385),
    "1_2": (0.240, 0.385),
    "1_3": (0.390, 0.385),
    "1_4": (0.535, 0.385),
    "1_5": (0.685, 0.385),
    "1_6": (0.845, 0.385),
    "2_1": (0.085, 0.465),
    "2_2": (0.240, 0.465),
    "2_3": (0.390, 0.465),
    "2_4": (0.535, 0.465),
    "2_5": (0.685, 0.465),
    "2_6": (0.845, 0.465),
    "3_1": (0.085, 0.555),
    "3_2": (0.240, 0.555),
    "3_3": (0.390, 0.555),
    "3_4": (0.535, 0.555),
    "3_5": (0.685, 0.555),
    "3_6": (0.845, 0.555),
    "4_1": (0.085, 0.635),
    "4_2": (0.240, 0.635),
    "4_3": (0.390, 0.635),
    "4_4": (0.535, 0.635),
    "4_5": (0.685, 0.635),
    "4_6": (0.845, 0.635),
    "5_1": (0.085, 0.720),
    "5_2": (0.240, 0.720),
    "5_3": (0.390, 0.720),
    "5_4": (0.535, 0.720),
    "5_5": (0.685, 0.720),
    "5_6": (0.845, 0.720),
    "6_1": (0.085, 0.810),
    "6_2": (0.240, 0.810),
    "6_3": (0.390, 0.810),
    "6_4": (0.535, 0.810),
    "6_5": (0.685, 0.810),
    "6_6": (0.845, 0.810),
}


with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)


with open('games/HamsterKombat/minigame.json', 'r') as f:
    script = json.load(f)


def main():
    for index in EMULATORS:
        print(index)
        emulator = Emulator(
            index=int(index),
            device_id=EMULATORS[index],
        )
        emulator.start()
        emulator.connect()
        for _ in range(RETRY):
            if emulator.is_connected():
                print("Connected")
                break
            else:
                ADB_PROCESS.reconnect()
        emulator.device.settings['operation_delay'] = (0, 0)
        emulator.device.settings['operation_delay_methods'] = ["click", "swipe"]
        game(emulator)
        input('Press enter to continue: ')
        emulator.stop()


def listen_keyboard():
    if is_pressed('s'):
        return True
    if is_pressed('q'):
        return False


def game(emulator):
    print("""To start press: s
To stop press: q
To break press: o""")

    state = False
    while True:
        key = listen_keyboard()
        if is_pressed('o'):
            break
        if key is not None:
            if state != key:
                state = key
                if state is True:
                    print('Start')
                elif state is False:
                    print('Stop')

        if state is True:
            for item in script:
                emulator.device.swipe_points(
                    [
                        coords[item[0]],
                        coords[item[1]],
                    ],
                    0.1,
                )
            state = False
            print('Stop')


if __name__ == '__main__':
    ADB_PROCESS.start()
    main()
