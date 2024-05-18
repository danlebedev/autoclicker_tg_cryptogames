from system_logic import Emulator
from telegram_logic import Telegram
from telegram_games import HarvestMoon
from time import sleep


def telegram_actions(emulator):
    tg = Telegram(device=emulator.device)
    tg.start()
    tg.init_folder(index=0)

    folder = tg.folder
    folder.connect()
    folder.init_bot(index=0)

    bot = folder.bot
    bot.connect()
    games = [
        HarvestMoon,
    ]
    bot.set_game(games)

    game = bot.game
    game.play()
    emulator.device.press('back')
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
