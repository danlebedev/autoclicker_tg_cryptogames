from time import sleep
from games.tools import TimerMixin, LoadMixin
from computer_vision.cv import locateCenterOnScreen


PAUSE1 = 2
PAUSE2 = 10


class HamsterKombat(TimerMixin, LoadMixin):
    name = 'Hamster Kombat'

    def __init__(self, bot):
        self.bot = bot
        self.thanks = (0.500, 0.830)
        self.hamster = (440, 990)
        self.templates = self._load_templates()

    def send_key(self, key):
        key_field = locateCenterOnScreen(
            template=self.templates['key_field'],
            screenshotIm=self.bot.session.screenshot(),
            confidence=0.95,
        )
        if key_field:
            self.bot.session.click(*key_field)
            sleep(PAUSE1)
            self.bot.session.send_keys(key)
            sleep(PAUSE1)
            key_activate = locateCenterOnScreen(
                template=self.templates['key_activate'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if key_activate:
                self.bot.session.click(*key_activate)
                sleep(10)

    def play(self, key):
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

            playground = locateCenterOnScreen(
                template=self.templates['playground'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if playground:
                self.bot.session.click(*playground)
                sleep(PAUSE1)
                match key.split('-')[0]:
                    case 'MERGE':
                        key_merge = locateCenterOnScreen(
                            template=self.templates['key_merge'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_merge:
                            self.bot.session.click(*key_merge)
                            sleep(PAUSE2)
                            self.send_key(key)
                    case 'CLONE':
                        key_clone = locateCenterOnScreen(
                            template=self.templates['key_clone'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_clone:
                            self.bot.session.click(*key_clone)
                            sleep(PAUSE2)
                            self.send_key(key)
                    case 'CUBE':
                        key_cube = locateCenterOnScreen(
                            template=self.templates['key_cube'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_cube:
                            self.bot.session.click(*key_cube)
                            sleep(PAUSE2)
                            self.send_key(key)
                    case 'TRAIN':
                        key_train = locateCenterOnScreen(
                            template=self.templates['key_train'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_train:
                            self.bot.session.click(*key_train)
                            sleep(PAUSE2)
                            self.send_key(key)
                    case 'BIKE':
                        key_bike = locateCenterOnScreen(
                            template=self.templates['key_bike'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_bike:
                            self.bot.session.click(*key_bike)
                            sleep(PAUSE2)
                            self.send_key(key)

            sleep(10)
            self.bot.stop()
