from system_logic import Emulator


def main():
    emulator = Emulator(
        index=0,
        device_id='emulator-5554',
    )
    emulator.start()
    emulator.connect()


if '__main__' == __name__:
    main()
