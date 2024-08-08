from time import sleep
from games.tools import TimerMixin, LoadMixin
from computer_vision.cv import locateCenterOnScreen


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
            sleep(5)
            self.bot.session.send_keys(key)
            sleep(5)
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
                sleep(5)

            playground = locateCenterOnScreen(
                template=self.templates['playground'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if playground:
                self.bot.session.click(*playground)
                sleep(5)
                match key.split('-')[0]:
                    case 'CLONE':
                        key_clone = locateCenterOnScreen(
                            template=self.templates['key_clone'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_clone:
                            self.bot.session.click(*key_clone)
                            sleep(5)
                            self.send_key(key)
                    case 'CUBE':
                        key_cube = locateCenterOnScreen(
                            template=self.templates['key_cube'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_cube:
                            self.bot.session.click(*key_cube)
                            sleep(5)
                            self.send_key(key)
                    case 'TRAIN':
                        key_train = locateCenterOnScreen(
                            template=self.templates['key_train'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_train:
                            self.bot.session.click(*key_train)
                            sleep(5)
                            self.send_key(key)
                    case 'BIKE':
                        key_bike = locateCenterOnScreen(
                            template=self.templates['key_bike'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if key_bike:
                            self.bot.session.click(*key_bike)
                            sleep(5)
                            self.send_key(key)

            self.bot.stop()
