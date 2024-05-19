from system_logic import Emulator
from telegram_logic import Telegram
from telegram_games import HarvestMoon, Blum, HamsterKombat
from time import sleep


def telegram_actions(emulator):
    GAMES = [
        HarvestMoon,
        Blum,
        HamsterKombat,
    ]
    CHATS = 3

    tg = Telegram(device=emulator.device)
    tg.start()
    tg.init_folder(index=0)

    folder = tg.folder
    folder.connect()
    for index in range(CHATS):
        folder.init_bot(index=index)

        bot = folder.bot
        bot.connect()
        bot.set_game(games=GAMES)

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
    emulator.stop()


if '__main__' == __name__:
    main()
