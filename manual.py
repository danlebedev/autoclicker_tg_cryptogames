from system_logic import Emulator, ADB
from telegram_games import HarvestMoon, Blum, HamsterKombat, \
    PocketFi, Vertus, PocketRocketGame, QappiMiner, GleamAquaProtocol
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
FOLDERS = {
    1: (0, 1, 2, 3, 4),
    2: (0, 1, 2)
}
SLEEP_OUT = 5
RETRY = 3


def main():
    for emulator in EMULATORS:
        print(EMULATORS.index(emulator))
        emulator = Emulator(
            index=EMULATORS.index(emulator),
            device_id=emulator,
        )
        emulator.start()
        emulator.connect()
        input()
        emulator.stop()


if '__main__' == __name__:
    ADB_PROCESS.start()
    main()
