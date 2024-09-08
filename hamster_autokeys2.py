from logic.system import Emulator, ADB
from logic.telegram import Telegram
from time import sleep
import json
from uiautomator2.exceptions import AdbShellError
from games.HamsterKombat.keygame import HamsterKombat
from queue import Queue
from os.path import join
from os import scandir
from settings import GAMES_DIR
from threading import Thread


ADB_PROCESS = ADB()
with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)

with open('keys.json', 'r') as f:
    KEYS = json.load(f)

GAMES = [
    HamsterKombat,
]
FOLDERS = {
    1: (2,)
}
SLEEP_OUT = 5
RETRY = 3


def load_keys():
    q = Queue()
    path = join(GAMES_DIR, 'HamsterKombat', 'keys')
    for keys in scandir(path):
        with open(keys.path, 'r') as f:
            for key in f:
                q.put(key.strip())
    return q


KEYS_Q = load_keys()


def load_emulators():
    q = Queue()
    for key in EMULATORS:
        q.put(key)
    return q


def emulator_connect(emulator, key):
    for _ in range(RETRY):
        emulator.connect()
        sleep(5)
        if emulator.is_connected():
            tg = Telegram(device=emulator.device)
            telegram_start(tg, key)
            break
        else:
            ADB_PROCESS.reconnect()
            sleep(SLEEP_OUT)
            # TODO: add logging.


def telegram_start(tg, key):
    for _ in range(RETRY):
        tg.start()
        sleep(5)
        if tg.is_started():
            for index in FOLDERS:
                tg.init_folder(index=index)
                folder_connect(tg.folder, FOLDERS[index], key)
            break
        else:
            pass    # TODO: add logging.


def folder_connect(folder, CHATS, key):
    for _ in range(RETRY):
        folder.connect()
        if folder.is_connected():
            for index in CHATS:
                folder.init_bot(index=index)
                bot_actions(folder.bot, key)
            break
        else:
            pass    # TODO: add logging.


def bot_actions(bot, key):
    # Add try-except for pass bug. Need fix in the future.
    try:
        bot.connect()
        sleep(2)
        #screenshot(emulator=emulator)
        bot.set_game(games=GAMES)
        if bot.game is not None:
            sleep(5)
            game_actions(bot.game, key)
        else:
            bot.session.press('back')
            sleep(SLEEP_OUT)
    except:
        bot.session.press('back')
        sleep(SLEEP_OUT)


def game_actions(game, key):
    game.play(key)
    game.bot.session.press('back')
    sleep(SLEEP_OUT)


def emulator_actions(KEYS_Q, emulators_q):
    key = KEYS_Q.get()
    
    index = emulators_q.get()
    try:
        print(index)
        emulator = Emulator(
            index=int(index),
            device_id=EMULATORS[index],
        )
        emulator.start()
        sleep(5)
        emulator_connect(emulator, key)
    #FIXME: Временное решение пропускать краш.
    except AdbShellError:
        pass
    except Exception as err:
        pass
    finally:
        emulator.stop()


def main():
    emulators_q = load_emulators()
    while not KEYS_Q.empty():
        if emulators_q.empty():
            emulators_q = load_emulators()
        
        threads = [Thread(target=emulator_actions, args=(KEYS_Q, emulators_q)) for _ in range(2)]

        for thread in threads:
            thread.start()
            sleep(5)

        for thread in threads:
            thread.join()


if __name__ == '__main__':
    ADB_PROCESS.start()
    main()