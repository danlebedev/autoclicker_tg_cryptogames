from time import sleep
from random import randint


def click_generator(x, y, count=10):
    commands = []
    for _ in range(count):
        x += randint(-20, 20)
        y += randint(-20, 20)
        commands.append(f"input tap {x} {y}")
    return ' && '.join(commands)


class HarvestMoon():
    name = 'HarvestMoonBot'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.225, 0.390)

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.button)
            sleep(10)
            self.bot.stop()


class Blum():
    name = 'Blum'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.500, 0.870)

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.button)
            sleep(5)
            self.bot.session.click(*self.button)
            sleep(5)
            self.bot.session.press('back')


class HamsterKombat():
    name = 'Hamster Kombat'

    def __init__(self, bot):
        self.bot = bot
        self.thanks = (0.500, 0.830)
        self.hamster = (440, 990)
        self.clicks = 60

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.thanks)
            self.clicker()
            self.bot.stop()

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(*self.hamster))


class PocketFi():
    name = 'PocketFi'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.75, 0.645)

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.button)
            sleep(5)
            self.bot.session.press('back')


class Vertus():
    name = 'Vertus'

    def __init__(self, bot):
        self.bot = bot
        self.storage = (0.700, 0.460)
        self.collect = (0.840, 0.780)

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
            # Skip daily reward.
            # TODO: rewrite this to check screenshot with opencv later.
            sleep(10)
            self.bot.session.press('back')
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.storage)
            sleep(5)
            self.bot.session.click(*self.collect)
            self.bot.session.press('back')
            self.bot.session.press('back')


class HoldWallet():
    name = 'HOLD Wallet 💎'

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            pass
            # TODO: WRITE THIS CLASS


class PocketRocketGame():
    name = 'Pocket Rocket Game'

    def __init__(self, bot):
        self.bot = bot
        self.rocket = (0.500, 0.730)
        self.clicks = 100

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.clicker()
            self.bot.session.press('back')

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(*self.rocket))


class QappiMiner():
    name = 'Qappi Miner'

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.500, 0.740)
        self.rocket = (0.515, 0.515)

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.claim)
            sleep(10)
            self.bot.session.press('back')


class GleamAquaProtocol():
    name = 'Gleam~AquaProtocol'

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.500, 0.610)

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.claim)
            sleep(5)
            self.bot.session.click(*self.claim)
            sleep(5)
            self.bot.session.press('back')
