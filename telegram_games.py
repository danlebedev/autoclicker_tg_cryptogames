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
