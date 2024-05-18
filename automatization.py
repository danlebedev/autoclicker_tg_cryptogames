from system_logic import Emulator
from telegram_logic import Telegram
from time import sleep


def telegram_actions(emulator):
    tg = Telegram(device=emulator.device)
    tg.start()
    tg.connect_folder(index=0)
    tg.folder.connect_bot(index=0)
    sleep(5)


def main():
    emulator = Emulator(
        index=0,
        device_id='emulator-5554',
    )
    emulator.start()
    emulator.connect()
    telegram_actions(emulator=emulator)


if '__main__' == __name__:
    main()
