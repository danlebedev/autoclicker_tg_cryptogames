from system_logic import Emulator
from telegram_logic import Telegram
from telegram_games import HarvestMoon, Blum, HamsterKombat
from time import sleep


GAMES = [
    HarvestMoon,
    Blum,
    HamsterKombat,
]
CHATS = [
    0,
    1,
    2,
]


def telegram_actions(emulator):
    tg = Telegram(device=emulator.device)
    tg.start()
    tg.init_folder(index=0)
    folder_actions(tg.folder)


def folder_actions(folder):
    folder.connect()
    for index in CHATS:
        folder.init_bot(index=index)
        bot_actions(folder.bot)


def bot_actions(bot):
    bot.connect()
    bot.set_game(games=GAMES)
    game_actions(bot.game)


def game_actions(game):
    game.play()
    game.bot.session.press('back')
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
