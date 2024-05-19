from time import sleep


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
            self.bot.run()


class Blum():
    name = 'Blum'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.500, 0.870)

    def play(self):
        texts = ('Launch Blum', 'Claim')    # todo: add text choice.
        try:
            self.tg.session(className='android.widget.Button', text=texts[0]).click()
        except:
            pass
        else:
            sleep(10)
            self.tg.session.click(*self.button)
            sleep(5)
            self.tg.session.click(*self.button)
            sleep(5)
            self.tg.session.press('back')
