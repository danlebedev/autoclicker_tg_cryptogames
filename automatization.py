from system_logic import Emulator
from telegram_logic import Telegram
from time import sleep


def telegram_actions(emulator):
    tg = Telegram(emulator.device)
    tg.start()
    sleep(5)


def main():
    emulator = Emulator(
        index=0,
        device_id='emulator-5554',
    )
    emulator.start()
    emulator.connect()
    telegram_actions(emulator)


if '__main__' == __name__:
    main()
