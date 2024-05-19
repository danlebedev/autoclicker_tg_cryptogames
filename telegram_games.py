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
        self.button = (0.500, 0.660)

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
        texts = ('Launch Blum', 'Claim')    # todo: add text choice.
        try:
            self.bot.session(className='android.widget.Button', text=texts[0]).click()
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
        self.clicks = 70

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
