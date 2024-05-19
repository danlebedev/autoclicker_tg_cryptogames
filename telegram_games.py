from time import sleep
from threading import Thread
from random import randint


def clicker(d, x, y, count):
    y += randint(-50, +50) / 1000
    for _ in range(count):
        d.click(x, y)


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
        self.hamster = [0.200, 0.630]

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            self.bot.session.click(*self.thanks)
            self.multi_threads(10)
            self.bot.run()

    def multi_threads(self, thread_count=0):
        threads = []
        for _ in range(thread_count):
            threads.append(Thread(
                target=clicker,
                args=(self.bot.session, *self.hamster, 80)
            ))
            self.hamster[0] += 0.6 / thread_count
        for thread in threads:
            sleep(0.17)
            thread.start()
        for thread in threads:
            thread.join()
