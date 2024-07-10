from time import sleep
from games.tools import click_generator, load_templates, TimerMixin
from computer_vision.cv import locateCenterOnScreen


class HarvestMoon(TimerMixin):
    name = 'HarvestMoonBot'
    timer = 12 * 60 * 60 + 120

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


class Blum(TimerMixin):
    name = 'Blum'
    timer = 8 * 60 * 60 + 120

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


class HamsterKombat(TimerMixin):
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
            #self.clicker()
            self.bot.stop()

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(
                *self.hamster,
                count=10,
                x_rand=20,
                y_rand=20,
            ))


class PocketFi(TimerMixin):
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


class Vertus(TimerMixin):
    name = 'Vertus'
    timer = 2 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.storage = (0.700, 0.460)
        self.collect = (0.840, 0.780)
        self.templates = self._load_templates()
    
    @classmethod
    def _load_templates(cls):
        return load_templates(cls.__name__)

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
            # Skip daily reward.
            # TODO: rewrite this to check screenshot with opencv later.
            sleep(20)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(20)
            okx = locateCenterOnScreen(
                template=self.templates['okx'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if okx:
                self.bot.session.click(*okx)
                self.bot.session.press('back')
            sleep(5)
            collect = locateCenterOnScreen(
                template=self.templates['collect'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if collect:
                self.bot.session.click(*collect)
            sleep(5)
            okx = locateCenterOnScreen(
                template=self.templates['okx'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if okx:
                self.bot.session.click(*okx)
                self.bot.session.press('back')
            sleep(5)
            self.bot.session.click(*self.storage)
            sleep(5)
            self.bot.session.click(*self.collect)
            claim = locateCenterOnScreen(
                template=self.templates['claim'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if claim:
                self.bot.session.click(*claim)
            sleep(5)
            self.bot.session.press('back')
            self.bot.session.press('back')


class HoldWallet(TimerMixin):
    name = 'HOLD Wallet 💎'

    def play(self):
        try:
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            pass
            # TODO: WRITE THIS CLASS


class PocketRocketGame(TimerMixin):
    name = 'Pocket Rocket Game'
    timer = 5 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.rocket = (450, 400)
        self.clicks = 10

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


class QappiMiner(TimerMixin):
    name = 'Qappi Miner'

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.500, 0.740)
        self.rocket = (0.500, 0.500)

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
            self.bot.session.click(*self.rocket)
            self.bot.session.press('back')


class Aqua(TimerMixin):
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


class HotWallet(TimerMixin):
    name = 'HOT Wallet'
    timer = 2 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.templates = self._load_templates()

    @classmethod
    def _load_templates(cls):
        return load_templates(cls.__name__)

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=2)
            sleep(10)

            if locateCenterOnScreen(
                template=self.templates['start'],
                screenshotIm=self.bot.session.screenshot(),
            ):
                self.bot.session.click(*locateCenterOnScreen(
                    template=self.templates['home'],
                    screenshotIm=self.bot.session.screenshot(),
                ))
                self.bot.session.swipe_ext("up")
                self.bot.session.click(*locateCenterOnScreen(
                    template=self.templates['storage'],
                    screenshotIm=self.bot.session.screenshot(),
                ))

                if locateCenterOnScreen(
                    template=self.templates['check_news'],
                    screenshotIm=self.bot.session.screenshot(),
                ):
                    self.bot.session.click(*locateCenterOnScreen(
                        template=self.templates['check_news'],
                        screenshotIm=self.bot.session.screenshot(),
                    ))
                    self.bot.session.press('back')
                if locateCenterOnScreen(
                    template=self.templates['claim_hot'],
                    screenshotIm=self.bot.session.screenshot(),
                ):
                    self.bot.session.click(*locateCenterOnScreen(
                        template=self.templates['claim_hot'],
                        screenshotIm=self.bot.session.screenshot(),
                    ))
                sleep(15)
                self.bot.session.press('back')

            sleep(5)
            self.bot.session.press('back')
            self.bot._stop_accept()
        except:
            raise


class EmpiresBattle(TimerMixin):
    name = "Empire's Battle Bot"

    def __init__(self, bot):
        self.bot = bot
        self.hero = (440, 990)
        self.clicks = 320

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(20)
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


class Gleam(TimerMixin):
    name = 'Gleam Bot'
    timer = 3 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.800, 0.645)

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


class AnonSpace(TimerMixin):
    name = 'ANON Space: Onboarding'
    timer = 8 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            daily = locateCenterOnScreen(
                template=self.templates['daily'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if daily:
                self.bot.session.click(*daily)
            sleep(5)
            claim = locateCenterOnScreen(
                template=self.templates['claim'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if claim:
                self.bot.session.click(*claim)
            sleep(10)
            self.bot.session.press('back')
