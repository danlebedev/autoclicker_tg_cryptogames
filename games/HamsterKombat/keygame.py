from time import sleep
from games.tools import TimerMixin, LoadMixin
from computer_vision.cv import locateCenterOnScreen


PAUSE1 = 2
PAUSE2 = 2


class HamsterKombat(TimerMixin, LoadMixin):
    name = 'Hamster Kombat'

    def __init__(self, bot):
        self.bot = bot
        self.thanks = (0.500, 0.830)
        self.hamster = (440, 990)
        self.templates = self._load_templates()

    def send_key(self, keys):
        key_field = locateCenterOnScreen(
            template=self.templates['key_field'],
            screenshotIm=self.bot.session.screenshot(),
            confidence=0.95,
        )
        if key_field:
            self.bot.session.click(*key_field)
            sleep(PAUSE1)
            for key in keys:
                self.bot.session.send_keys(key)
                sleep(PAUSE1)
                key_activate = locateCenterOnScreen(
                    template=self.templates['key_activate'],
                    screenshotIm=self.bot.session.screenshot(),
                    confidence=0.95,
                )
                if key_activate:
                    self.bot.session.click(*key_activate)
                sleep(2)

    def play(self, keys):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(15)
            thanks = locateCenterOnScreen(
                template=self.templates['thanks'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if thanks:
                self.bot.session.click(*thanks)
                sleep(PAUSE1)
                key_game = locateCenterOnScreen(
                    template=self.templates['key_game'],
                    screenshotIm=self.bot.session.screenshot(),
                    confidence=0.95,
                )
                if key_game:
                    self.bot.session.click(*key_game)
                    sleep(PAUSE2)
                    self.send_key(keys)

            sleep(10)
            self.bot.stop()
