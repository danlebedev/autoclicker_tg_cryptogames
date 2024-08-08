from logic.system import Emulator, ADB
from logic.telegram import Telegram
from time import sleep
import json
from uiautomator2.exceptions import AdbShellError
from games.HamsterKombat.keygame import HamsterKombat


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


def emulator_connect():
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
        sleep(5)
        if tg.is_started():
            for index in FOLDERS:
                tg.init_folder(index=index)
                folder_connect(tg.folder, FOLDERS[index])
            break
        else:
            pass    # TODO: add logging.


def folder_connect(folder, CHATS):
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
    # Add try-except for pass bug. Need fix in the future.
    try:
        bot.connect()
        sleep(2)
        #screenshot(emulator=emulator)
        bot.set_game(games=GAMES)
        if bot.game is not None:
            game_actions(bot.game)
        else:
            bot.session.press('back')
            sleep(SLEEP_OUT)
    except:
        bot.session.press('back')
        sleep(SLEEP_OUT)


def game_actions(game):
    game.play(key)
    game.bot.session.press('back')
    sleep(SLEEP_OUT)


def main():
    global key
    for index, key in zip(list(EMULATORS)*4, KEYS):
        try:
            print(index)
            global emulator
            emulator = Emulator(
                index=int(index),
                device_id=EMULATORS[index],
            )
            emulator.start()
            emulator_connect()
        #FIXME: Временное решение пропускать краш.
        except AdbShellError:
            pass
        except Exception as err:
            pass
        finally:
            emulator.stop()


if __name__ == '__main__':
    ADB_PROCESS.start()
    main()
