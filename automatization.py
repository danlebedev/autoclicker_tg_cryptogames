from system_logic import Emulator, ADB
from telegram_logic import Telegram
from telegram_games import HarvestMoon, Blum, HamsterKombat, \
    PocketFi
from time import sleep
import json


ADB_PROCESS = ADB()
with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)
GAMES = [
    Blum,
    HamsterKombat,
    PocketFi,
]
FOLDERS = [
    0,
]
CHATS = [
    0,
    1,
    2,
    4,
]
SLEEP_OUT = 5
RETRY = 3


def emulator_actions():
    for emulator in EMULATORS:
        emulator = Emulator(
            index=EMULATORS.index(emulator),
            device_id=emulator,
        )
        emulator.start()
        for _ in range(RETRY):
            emulator.connect()
            if emulator.is_connected():
                telegram_actions(emulator=emulator)
                break
            else:
                ADB_PROCESS.reconnect()
                sleep(SLEEP_OUT)
                emulator.connect()
        emulator.stop()


def telegram_actions(emulator):
    tg = Telegram(device=emulator.device)
    tg.start()
    for index in FOLDERS:
        tg.init_folder(index=index)
        folder_actions(tg.folder)


def folder_actions(folder):
    folder.connect()
    for index in CHATS:
        folder.init_bot(index=index)
        bot_actions(folder.bot)


def bot_actions(bot):
    bot.connect()
    bot.set_game(games=GAMES)
    if bot.game is not None:
        game_actions(bot.game)
    else:
        bot.session.press('back')
        sleep(SLEEP_OUT)


def game_actions(game):
    game.play()
    game.bot.session.press('back')
    sleep(SLEEP_OUT)


def main():
    ADB_PROCESS.start()
    emulator_actions()


if '__main__' == __name__:
    main()
