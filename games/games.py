from time import sleep
from games.tools import click_generator


class HarvestMoon():
    name = 'HarvestMoonBot'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.16, 0.34)

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
            self.bot.send_message_start()
            sleep(5)
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
            self.bot.session.shell(click_generator(
                *self.hamster,
                count=10,
                x_rand=20,
                y_rand=20,
            ))


class PocketFi():
    name = 'PocketFi'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.75, 0.645)

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
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
            self.bot.send_message_start()
            sleep(5)
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
        self.rocket = (450, 400)
        self.clicks = 50

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.clicker()
            self.bot.session.press('back')
            self.bot._stop_accept()

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(
                *self.rocket,
                count=10,
                x_rand=350,
                y_rand=50,
            ))


class QappiMiner():
    name = 'Qappi Miner'

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.500, 0.740)
        self.rocket = (0.515, 0.515)

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.claim)
            sleep(10)
            self.bot.session.press('back')


class Gleam():
    name = 'GLEAM'

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
            self.bot.stop()


class EmpiresBattle():
    name = "Empire's Battle Bot"

    def __init__(self, bot):
        self.bot = bot
        self.hero = (440, 990)
        self.clicks = 260

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            self.clicker()
            self.bot.session.press('back')
            self.bot._stop_accept()

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(
                *self.hero,
                count=10,
                x_rand=20,
                y_rand=20,
            ))