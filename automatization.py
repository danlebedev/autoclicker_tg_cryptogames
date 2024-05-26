from system_logic import Emulator, ADB
from telegram_logic import Telegram
from telegram_games import HarvestMoon, Blum, HamsterKombat, \
    PocketFi, Vertus, PocketRocketGame, QappiMiner, GleamAquaProtocol
from time import sleep
import json


ADB_PROCESS = ADB()
with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)
GAMES = [
    #HarvestMoon,
    Blum,
    HamsterKombat,
    PocketFi,
    Vertus,
    PocketRocketGame,
    #QappiMiner,
    GleamAquaProtocol,
]
FOLDERS = [
    1,
    2,
]
CHATS = [
    0,
    1,
    2,
    3,
    4,
]
SLEEP_OUT = 5
RETRY = 3


def emulator_connect(emulator):
        for _ in range(RETRY):
            emulator.connect()
            if emulator.is_connected():
                tg = Telegram(device=emulator.device)
                telegram_start(tg=tg)
                break
            else:
                ADB_PROCESS.reconnect()
                sleep(SLEEP_OUT)
                # TODO: add logging.


def telegram_start(tg):
    for _ in range(RETRY):
        tg.start()
        if tg.is_started():
            for index in FOLDERS:
                tg.init_folder(index=index)
                folder_connect(tg.folder)
            break
        else:
            pass    # TODO: add logging.


def folder_connect(folder):
    for _ in range(RETRY):
        folder.connect()
        if folder.is_connected():
            for index in CHATS:
                folder.init_bot(index=index)
                bot_actions(folder.bot)
            break
        else:
            pass    # TODO: add logging.


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
    for emulator in EMULATORS:
        emulator = Emulator(
            index=EMULATORS.index(emulator),
            device_id=emulator,
        )
        emulator.start()
        emulator_connect(emulator=emulator)
        emulator.stop()


if '__main__' == __name__:
    ADB_PROCESS.start()
    while True:
        main()
