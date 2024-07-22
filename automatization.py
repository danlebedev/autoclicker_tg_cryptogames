from logic.system import Emulator, ADB
from logic.telegram import Telegram
from games.games import HarvestMoon, Blum, HamsterKombat, \
    PocketFi, Vertus, PocketRocketGame, QappiMiner, Gleam, \
    HotWallet, EmpiresBattle, AnonSpace, PixelTap, Tomarket, \
    MemeFi, OKX, PikeMan
from tools import screenshot, load_state, save_state, load_times, save_times
from time import sleep
import json
from uiautomator2.exceptions import AdbShellError


ADB_PROCESS = ADB()
with open('emulators.json', 'r') as f:
    EMULATORS = json.load(f)
GAMES = [
    HarvestMoon,
    Blum,
    HamsterKombat,
    PocketFi,
    Vertus,
    PocketRocketGame,
    QappiMiner,
    #Gleam,
    HotWallet,
    #EmpiresBattle,
    AnonSpace,
    #PixelTap,
    MemeFi,
    Tomarket,
    OKX,
    PikeMan,
]
FOLDERS = {
    1: (0, 1, 2, 3, 4),
    2: (0, 1, 2, 3, 4),
    3: (0, 1, 2, 3, 4),
}
SLEEP_OUT = 5
RETRY = 3
LAST_STATE = load_state()
NEW_STATE = {}
TIMES = load_times()


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
    if game.timer is not None:
        last_time = EMULATOR_TIMES.setdefault(game.__class__.__name__, 0)
        new_time = game.check_time(last_time)
        if new_time is not None:
            EMULATOR_TIMES[game.__class__.__name__] = new_time
            game.play()
    else:
        game.play()
    game.bot.session.press('back')
    sleep(SLEEP_OUT)


def main():
    for index in EMULATORS:
        if LAST_STATE:
            if not LAST_STATE['device_id'] == EMULATORS[index]:
                continue
            else:
                LAST_STATE.clear()
        try:
            NEW_STATE['device_id'] = EMULATORS[index]
            print(index)
            save_state(NEW_STATE)
            global EMULATOR_TIMES
            EMULATOR_TIMES = TIMES.setdefault(EMULATORS[index], {})
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
            save_times(TIMES)
            save_state(NEW_STATE)
            emulator.stop()


if __name__ == '__main__':
    ADB_PROCESS.start()
    while True:
        main()
