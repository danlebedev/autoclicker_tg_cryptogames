from time import sleep
from games.tools import click_generator, TimerMixin, LoadMixin
from computer_vision.cv import locateCenterOnScreen
from random import choice, randint
from computer_vision.cv import search_pixel_with_getpixel
from pyautogui import screenshot
from pygetwindow import getActiveWindow
from pynput.mouse import Controller, Button


class HarvestMoon(TimerMixin, LoadMixin):
    name = 'HarvestMoonBot'
    timer = 16 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.16, 0.34)
        self.center = (450, 800)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(15)
            close = locateCenterOnScreen(
                template=self.templates['close'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if close:
                self.bot.session.click(*close)
                sleep(5)
            self.bot.session.click(*self.button)
            sleep(10)
            self.bot.session.click(*self.center)
            sleep(5)
            self.bot.session.click(*self.center)
            sleep(5)
            self.bot.stop()


class Blum(TimerMixin, LoadMixin):
    name = 'Blum'
    timer = 8 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.500, 0.870)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(20)
            daily = locateCenterOnScreen(
                template=self.templates['daily'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if daily:
                self.bot.session.click(*daily)
                sleep(5)
            for _ in range(2):
                claim = locateCenterOnScreen(
                    template=self.templates['claim'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if claim:
                    self.bot.session.click(*claim)
                    sleep(5)
            for _ in range(2):
                start = locateCenterOnScreen(
                    template=self.templates['start'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if start:
                    self.bot.session.click(*start)
                    sleep(5)
            self.bot.stop()


class Blum2(TimerMixin, LoadMixin):
    name = 'Blum'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.500, 0.870)
        self.templates = self._load_templates()

    def minigame(self):        
        mouse = Controller()
        drop_min = (153, 201, 0)
        drop_max = (213, 255, 50)
        spins = 0
        SPINS_MAX = randint(20, 25)

        while True:
            last_click = None
            # Хранит количество сделанных скриншотов
            count = 0
            while True:
                count += 1
                window = getActiveWindow()
                region = (window.left, window.top, window.width, window.height)
                image = screenshot(region=region)
                drop_region_coordinates = search_pixel_with_getpixel(
                    image=image,
                    color_min=drop_min,
                    color_max=drop_max,
                    step_string=13,
                    step_pixel=13,
                    reverse=True
                )

                if drop_region_coordinates:
                    drop_coordinates = (
                        window.left + drop_region_coordinates[0],
                        window.top + drop_region_coordinates[1],
                    )

                    if drop_coordinates != last_click:
                        mouse.position = drop_coordinates
                        mouse.click(Button.left)
                        last_click = drop_coordinates

                # Делаем проверку кнопки play каждые 50 скринов.
                if count > 50:
                    count = 0
                    wrong = locateCenterOnScreen(
                        template=self.templates['wrong'],
                        screenshotIm=image,
                        confidence=0.90,
                    )
                    if wrong:
                        self.bot.stop()
                        self.bot.send_message_start()
                        sleep(5)
                        self.bot.click_inline_button(index=0)

                    collapse = locateCenterOnScreen(
                        template=self.templates['collapse'],
                        screenshotIm=image,
                        confidence=0.90,
                    )
                    if collapse:
                        collapse = (
                            window.left + collapse[0],
                            window.top + collapse[1],
                        )
                        mouse.position = collapse
                        mouse.click(Button.left)
                        sleep(5)

                    locate_play = locateCenterOnScreen(
                        template=self.templates['play_minigame1'],
                        screenshotIm=image,
                        confidence=0.90,
                    )
                    if locate_play:
                        if SPINS_MAX <= spins:
                            return
                        locate_play = (
                            window.left + locate_play[0],
                            window.top + locate_play[1],
                        )
                        mouse.position = locate_play
                        mouse.click(Button.left)
                        spins += 1
                    locate_play = locateCenterOnScreen(
                        template=self.templates['play_minigame2'],
                        screenshotIm=image,
                        confidence=0.90,
                    )
                    if locate_play:
                        if SPINS_MAX <= spins:
                            return
                        locate_play = (
                            window.left + locate_play[0],
                            window.top + locate_play[1],
                        )
                        mouse.position = locate_play
                        mouse.click(Button.left)
                        spins += 1

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(20)
            daily = locateCenterOnScreen(
                template=self.templates['daily'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if daily:
                self.bot.session.click(*daily)
                sleep(5)
            self.minigame()
        self.bot.stop()


class HamsterKombat(TimerMixin, LoadMixin):
    name = 'Hamster Kombat'

    def __init__(self, bot):
        self.bot = bot
        self.thanks = (0.500, 0.830)
        self.hamster = (440, 990)
        self.clicks = 60
        self.time_between_clicks = 0.3
        self.templates = self._load_templates()
        self.scripts = self._load_scripts()
        self.morze = {
            "A": "sl",
            "B": "lsss",
            "C": "lsls",
            "D": "lss",
            "E": "s",
            "F": "ssls",
            "G": "lls",
            "H": "ssss",
            "I": "ss",
            "J": "slll",
            "K": "lsl",
            "L": "slss",
            "M": "ll",
            "N": "ls",
            "O": "lll",
            "P": "slls",
            "Q": "llsl",
            "R": "sls",
            "S": "sss",
            "T": "l",
            "U": "ssl",
            "V": "sssl",
            "W": "sll",
            "X": "lssl",
            "Y": "lsll",
            "Z": "llss",
            "1": "sllll",
            "2": "sslll",
            "3": "sssll",
            "4": "ssssl",
            "5": "sssss",
            "6": "lssss",
            "7": "llsss",
            "8": "lllss",
            "9": "lllls",
            "0": "lllll",
        }
        self.minigame_coords = {
            "1_1": (80, 615),
            "1_2": (215, 615),
            "1_3": (350, 615),
            "1_4": (485, 615),
            "1_5": (620, 615),
            "1_6": (755, 615),
            "2_1": (80, 750),
            "2_2": (215, 750),
            "2_3": (350, 750),
            "2_4": (485, 750),
            "2_5": (620, 750),
            "2_6": (755, 750),
            "3_1": (80, 885),
            "3_2": (215, 885),
            "3_3": (350, 885),
            "3_4": (485, 885),
            "3_5": (620, 885),
            "3_6": (755, 885),
            "4_1": (80, 1020),
            "4_2": (215, 1020),
            "4_3": (350, 1020),
            "4_4": (485, 1020),
            "4_5": (620, 1020),
            "4_6": (755, 1020),
            "5_1": (80, 1155),
            "5_2": (215, 1155),
            "5_3": (350, 1155),
            "5_4": (485, 1155),
            "5_5": (620, 1155),
            "5_6": (755, 1155),
            "6_1": (80, 1290),
            "6_2": (215, 1290),
            "6_3": (350, 1290),
            "6_4": (485, 1290),
            "6_5": (620, 1290),
            "6_6": (755, 1290),
        }

    def minigame(self):
        try:
            self.bot.session.settings['operation_delay'] = (0, 0)
            self.bot.session.settings['operation_delay_methods'] = ["click", "swipe"]
            for item in self.scripts['minigame']:
                self.bot.session.swipe_points(
                    [
                        self.minigame_coords[item[0]],
                        self.minigame_coords[item[1]],
                    ],
                    0.1,
                )
        finally:
            self.bot.session.settings['operation_delay'] = (2, 2)
            self.bot.session.settings['operation_delay_methods'] = [
                'click',
                'press',
                'exists',
                'get_text',
                'set_text',
                'swipe_ext',
            ]

    def daily_minigame(self):
        minigame_daily = locateCenterOnScreen(
            template=self.templates['minigame_daily'],
            screenshotIm=self.bot.session.screenshot(),
        )
        if minigame_daily:
            self.bot.session.click(*minigame_daily)
            sleep(5)
            minigame_play = locateCenterOnScreen(
                template=self.templates['minigame_play'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if minigame_play:
                self.bot.session.click(*minigame_play)
                sleep(5)
                minigame_start = locateCenterOnScreen(
                    template=self.templates['minigame_start'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if minigame_start:
                    self.bot.session.click(*minigame_start)
                    sleep(2)
                    self.minigame()
                    sleep(5)
            else:
                self.bot.session.press('back')

    def cipher(self):
        for k in self.scripts["cipher"]:
            for click_type in self.morze[k]:
                if click_type == "s":
                    self.bot.session.shell(f"input tap {' '.join(map(str, self.hamster))}")
                elif click_type == "l":
                    self.bot.session.shell(f"input swipe {' '.join(map(str, self.hamster))} {' '.join(map(str, self.hamster))} 1000")
                sleep(self.time_between_clicks)
            sleep(3)

    def daily_cipher(self):
        cipher_daily = locateCenterOnScreen(
            template=self.templates['cipher_daily'],
            screenshotIm=self.bot.session.screenshot(),
        )
        if cipher_daily:
            self.bot.session.click(*cipher_daily)
            sleep(5)
            self.cipher()
            sleep(5)
            cipher_claim = locateCenterOnScreen(
                template=self.templates['cipher_claim'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if cipher_claim:
                self.bot.session.click(*cipher_claim)
                sleep(5)

    def daily_reward(self):
        reward_daily = locateCenterOnScreen(
            template=self.templates['reward_daily'],
            screenshotIm=self.bot.session.screenshot(),
        )
        if reward_daily:
            self.bot.session.click(*reward_daily)
            sleep(5)

            reward = locateCenterOnScreen(
                template=self.templates['reward'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if reward:
                self.bot.session.click(*reward)
                sleep(5)
                reward_claim = locateCenterOnScreen(
                    template=self.templates['reward_claim'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if reward_claim:
                    self.bot.session.click(*reward_claim)
                    sleep(5)

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(15)
            reward_claim = locateCenterOnScreen(
                template=self.templates['reward_claim'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if reward_claim:
                self.bot.session.click(*reward_claim)
                sleep(5)
                
            thanks = locateCenterOnScreen(
                template=self.templates['thanks'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if thanks:
                self.bot.session.click(*thanks)
                sleep(5)

            cipher_claimed = locateCenterOnScreen(
                template=self.templates['cipher_claimed'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if not cipher_claimed:
                self.daily_cipher()

            """minigame_claimed = locateCenterOnScreen(
                template=self.templates['minigame_claimed'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if not minigame_claimed:
                self.daily_minigame()"""

            reward_claimed = locateCenterOnScreen(
                template=self.templates['reward_claimed'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if not reward_claimed:
                self.daily_reward()

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


class HamsterKombat2(TimerMixin, LoadMixin):
    name = 'Hamster Kombat'

    def __init__(self, bot):
        self.bot = bot
        self.thanks = (0.500, 0.830)
        self.hamster = (440, 990)
        self.first_game = (0.190, 0.270)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(20)
            thanks = locateCenterOnScreen(
                template=self.templates['thanks'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if thanks:
                self.bot.session.click(*thanks)
                sleep(5)

            sleep(10)
            self.bot.stop()


class PocketFi(TimerMixin, LoadMixin):
    name = 'PocketFi'

    def __init__(self, bot):
        self.bot = bot
        self.button = (0.5, 0.59)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            quests = locateCenterOnScreen(
                template=self.templates['quests'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if quests:
                self.bot.session.click(*quests)
                sleep(5)
                everyday = locateCenterOnScreen(
                    template=self.templates['everyday'],
                    screenshotIm=self.bot.session.screenshot(),
                    confidence=0.95,
                )
                if everyday:
                    self.bot.session.click(*everyday)
                    sleep(5)
                    claim_everyday = locateCenterOnScreen(
                        template=self.templates['claim_everyday'],
                        screenshotIm=self.bot.session.screenshot(),
                        confidence=0.95,
                    )
                    if claim_everyday:
                        self.bot.session.click(*claim_everyday)
                        sleep(5)
                        self.bot.session.click(0.5, 0.2)
                        sleep(5)
                mining = locateCenterOnScreen(
                    template=self.templates['mining'],
                    screenshotIm=self.bot.session.screenshot(),
                    confidence=0.95,
                )
                if mining:
                    self.bot.session.click(*mining)
                    sleep(5)

            self.bot.session.click(*self.button)
            sleep(5)
            self.bot.stop()


class Vertus(TimerMixin, LoadMixin):
    name = 'Vertus'
    timer = 2 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.storage = (0.700, 0.460)
        self.collect = (0.840, 0.780)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
            # Skip daily reward.
            # TODO: rewrite this to check screenshot with opencv later.
            sleep(20)
            collect = locateCenterOnScreen(
                template=self.templates['collect'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if collect:
                self.bot.session.click(*collect)
            self.bot.session.press('back')
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
            self.bot.stop()


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


class PocketRocketGame(TimerMixin, LoadMixin):
    name = 'Pocket Rocket Game'
    timer = 4 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.rocket = (450, 400)
        self.clicks = 10
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            for _ in range(2):
                start_continue = locateCenterOnScreen(
                    template=self.templates['start_continue'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if start_continue:
                    self.bot.session.click(*start_continue)
                    sleep(5)

            roulette = locateCenterOnScreen(
                template=self.templates['roulette'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if roulette:
                self.bot.session.click(*roulette)
                sleep(5)

                roulette_spin = locateCenterOnScreen(
                    template=self.templates['roulette_spin'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if roulette_spin:
                    self.bot.session.click(*roulette_spin)
                    sleep(10)
                
                    roulette_claim = locateCenterOnScreen(
                        template=self.templates['roulette_claim'],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if roulette_claim:
                        self.bot.session.click(*roulette_claim)
                        sleep(5)
            
            daily = locateCenterOnScreen(
                template=self.templates['daily'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if daily:
                self.bot.session.click(*daily)
                sleep(5)

                daily_claim = locateCenterOnScreen(
                    template=self.templates['daily_claim'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if daily_claim:
                    self.bot.session.click(*daily_claim)
                    sleep(5)
                    self.bot.session.press('back')

            for _ in range(3):
                for _ in range(5):
                    boosts = locateCenterOnScreen(
                        template=self.templates['boosts'],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if boosts:
                        self.bot.session.click(*boosts)
                        sleep(5)

                        turbo = locateCenterOnScreen(
                            template=self.templates['turbo'],
                            screenshotIm=self.bot.session.screenshot(),
                        )
                        if turbo:
                            self.bot.session.click(*turbo)
                            sleep(5)

                            turbo_claim = locateCenterOnScreen(
                                template=self.templates['turbo_claim'],
                                screenshotIm=self.bot.session.screenshot(),
                            )
                            if turbo_claim:
                                self.bot.session.click(*turbo_claim)
                                sleep(5)
                            else:
                                self.bot.session.press('back')
                        break

            self.clicker()
            self.bot.stop()

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
            self.bot.stop()


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


class HotWallet(TimerMixin, LoadMixin):
    name = 'HOT Wallet'
    timer = 2 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=2)
            sleep(10)

            follow = locateCenterOnScreen(
                template=self.templates['follow'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if follow:
                self.bot.session.click(0.5, 0.3)
                sleep(5)
            if locateCenterOnScreen(
                template=self.templates['start'],
                screenshotIm=self.bot.session.screenshot(),
            ):
                follow = locateCenterOnScreen(
                    template=self.templates['follow'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if follow:
                    self.bot.session.click(0.5, 0.3)
                    sleep(5)

                home = locateCenterOnScreen(
                    template=self.templates['home'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if home:
                    self.bot.session.click(*home)
                    self.bot.session.swipe_ext("up")
                
                storage = locateCenterOnScreen(
                    template=self.templates['storage'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if storage:
                    self.bot.session.click(*storage)

                check_news = locateCenterOnScreen(
                    template=self.templates['check_news'],
                    screenshotIm=self.bot.session.screenshot(),
                    confidence=0.95
                )
                if check_news:
                    self.bot.session.click(*check_news)
                    sleep(2)
                    self.bot.expand()

                for _ in range(2):
                    claim_hot = locateCenterOnScreen(
                        template=self.templates['claim_hot'],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if claim_hot:
                        self.bot.session.click(*claim_hot)
                        sleep(5)
                        if self.bot.get_name() != self.name:
                            self.bot.session.press('back')
                            sleep(5)
                sleep(15)
                self.bot.session.press('back')

            self.bot.stop()
        except:
            pass


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
            self.bot.stop()

    def clicker(self):
        for _ in range(self.clicks):
            self.bot.session.shell(click_generator(
                *self.hero,
                count=10,
                x_rand=20,
                y_rand=20,
            ))


class Gleam(TimerMixin, LoadMixin):
    name = 'Gleam Bot'
    timer = 8 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.800, 0.645)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(10)
            menu = locateCenterOnScreen(
                template=self.templates['menu'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if menu:
                self.bot.session.click(*menu)
                sleep(5)

                while True:
                    project_claim = locateCenterOnScreen(
                        template=self.templates['project_claim'],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if project_claim:
                        self.bot.session.click(*project_claim)
                        sleep(5)
                    else:
                        close = locateCenterOnScreen(
                            template=self.templates['close'],
                            screenshotIm=self.bot.session.screenshot(),
                        )
                        if close:
                            self.bot.session.click(*close)
                        break

            self.bot.session.click(*self.claim)
            sleep(10)
            self.bot.stop()


class AnonSpace(TimerMixin, LoadMixin):
    name = 'ANON Space: Onboarding'
    timer = 8 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.send_message_start()
            sleep(5)
            self.bot.click_inline_button(index=0)
        except:
            pass
        else:
            sleep(20)
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
        self.bot.stop()


class PixelTap(TimerMixin, LoadMixin):
    name = 'PixelTap by Pixelverse'

    def __init__(self, bot):
        self.bot = bot
        self.templates = self._load_templates()
    
    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(60)
            close = locateCenterOnScreen(
                template=self.templates['close'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if close:
                self.bot.session.click(*close)
                sleep(5)
            close = locateCenterOnScreen(
                template=self.templates['close'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if close:
                self.bot.session.click(*close)
                sleep(5)
            claim = locateCenterOnScreen(
                template=self.templates['claim'],
                screenshotIm=self.bot.session.screenshot(),
                confidence=0.95,
            )
            if claim:
                self.bot.session.click(*claim)
                sleep(20)
            self.bot.stop()


class MemeFi(TimerMixin, LoadMixin):
    name = 'MemeFi Coin'

    def __init__(self, bot):
        self.bot = bot
        self.templates = self._load_templates()
        self.closes = self.load_closes()
        self.scripts = self._load_scripts()
        self.time_between_clicks = 0.3
        self.coordinates = {
            "1": (450, 720),
            "2": (450, 850),
            "3": (450, 980),
            "4": (450, 1100),
        }

    def load_closes(self):
        lst = []
        for template in self.templates.items():
            if 'close_quest' in template[0]:
                lst.append(template[1])
        return lst

    def daily_cipher(self):
        for k in self.scripts["cipher"]:
            self.bot.session.shell(f"input tap {' '.join(map(str, self.coordinates[k]))}")
            sleep(self.time_between_clicks)
        sleep(5)
        close = locateCenterOnScreen(
            template=self.templates['close'],
            screenshotIm=self.bot.session.screenshot(),
        )
        if close:
            self.bot.session.click(*close)
            sleep(5)

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(15)
            for _ in range(6):
                for template in self.closes:
                    close_quest = locateCenterOnScreen(
                        template=template,
                        screenshotIm=self.bot.session.screenshot(),
                        confidence=0.8,
                    )
                    if close_quest:
                        self.bot.session.click(*close_quest)
                        sleep(5)
                sleep(1)
            accept_terms = locateCenterOnScreen(
                template=self.templates['accept_terms'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if accept_terms:
                self.bot.session.click(*accept_terms)
                sleep(5)
            spin = locateCenterOnScreen(
                template=self.templates['spin'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if spin:
                self.bot.session.click(*spin)
                sleep(5)

            continue_game = locateCenterOnScreen(
                template=self.templates['continue_game'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if continue_game:
                self.bot.session.click(*continue_game)
                sleep(5)

            close = locateCenterOnScreen(
                template=self.templates['close'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if close:
                self.bot.session.click(*close)
                sleep(5)

            self.daily_cipher()
            boosters = locateCenterOnScreen(
                template=self.templates['boosters'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if boosters:
                self.bot.session.click(*boosters)
                sleep(5)
                tapbot = locateCenterOnScreen(
                    template=self.templates['tapbot'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                for _ in range(2):
                    if tapbot:
                        self.bot.session.click(*tapbot)
                        sleep(5)
                        tapbot_claim = locateCenterOnScreen(
                            template=self.templates['tapbot_claim'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if tapbot_claim:
                            self.bot.session.click(*tapbot_claim)
                            sleep(5)
                        tapbot_activate = locateCenterOnScreen(
                            template=self.templates['tapbot_activate'],
                            screenshotIm=self.bot.session.screenshot(),
                            confidence=0.95,
                        )
                        if tapbot_activate:
                            self.bot.session.click(*tapbot_activate)
                            sleep(5)
                            break
            self.bot.stop()


class Tomarket(TimerMixin, LoadMixin):
    name = 'Tomarket App'
    timer = 3 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.claim = (0.480, 0.855)
        self.templates = self._load_templates()
        self.scripts = self._load_scripts()
        self.time_between_clicks = 0.3
        self.coordinates = {
            "h": (85, 1180),
            "t": (665, 1048),
            "c": (450, 800),
        }

    def daily_cipher(self):
        for k in self.scripts["cipher"]:
            self.bot.session.shell(f"input tap {' '.join(map(str, self.coordinates[k]))}")
            sleep(self.time_between_clicks)
        sleep(5)
        cipher_close = locateCenterOnScreen(
            template=self.templates['cipher_close'],
            screenshotIm=self.bot.session.screenshot(),
        )
        if cipher_close:
            self.bot.session.click(*cipher_close)
            sleep(5)

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(15)
            login = locateCenterOnScreen(
                template=self.templates['login'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if login:
                self.bot.session.click(*login)
                sleep(5)
            daily = locateCenterOnScreen(
                template=self.templates['daily'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if daily:
                self.bot.session.click(*daily)
                sleep(5)
            login = locateCenterOnScreen(
                template=self.templates['login'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if login:
                self.bot.session.click(*login)
                sleep(5)
            #self.daily_cipher()
            self.bot.session.click(*self.claim)
            sleep(5)
            self.bot.session.click(*self.claim)
            sleep(5)
            self.bot.stop()


class OKX(TimerMixin, LoadMixin):
    name = 'OKX Racer'

    def __init__(self, bot):
        self.bot = bot
        self.spins = 25
        self.templates = self._load_templates()
        self.choice = ('moon', 'doom')

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            continue_racing = locateCenterOnScreen(
                template=self.templates['continue_racing'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if continue_racing:
                self.bot.session.click(*continue_racing)
                sleep(5)
            for _ in range(self.spins):
                empty = locateCenterOnScreen(
                    template=self.templates['empty'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if empty:
                    sleep(5)
                    break
                button = locateCenterOnScreen(
                    template=self.templates[choice(self.choice)],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if button:
                    self.bot.session.click(*button)
                    sleep(3.5)
            tasks = locateCenterOnScreen(
                template=self.templates["tasks"],
                screenshotIm=self.bot.session.screenshot(),
            )
            if tasks:
                self.bot.session.click(*tasks)
                sleep(5)
                daily = locateCenterOnScreen(
                    template=self.templates["daily"],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if daily:
                    self.bot.session.click(*daily)
                    sleep(5)
                    daily_checkin = locateCenterOnScreen(
                        template=self.templates["daily_checkin"],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if daily_checkin:
                        self.bot.session.click(*daily_checkin)
                        sleep(5)
            self.bot.stop()

class PikeMan(TimerMixin, LoadMixin):
    name = 'pike_man'
    timer = 4 * 60 * 60 + 120

    def __init__(self, bot):
        self.bot = bot
        self.spins = 12
        self.click = (0.500, 0.700)
        self.templates = self._load_templates()

    def play(self):
        try:
            self.bot.run()
        except:
            pass
        else:
            sleep(10)
            for _ in range(self.spins):
                self.bot.session.click(*self.click)
            quests = locateCenterOnScreen(
                template=self.templates['quests'],
                screenshotIm=self.bot.session.screenshot(),
            )
            if quests:
                self.bot.session.click(*quests)
                sleep(5)
                daily = locateCenterOnScreen(
                    template=self.templates['daily'],
                    screenshotIm=self.bot.session.screenshot(),
                )
                if daily:
                    self.bot.session.click(*daily)
                    sleep(5)
                    daily_accept = locateCenterOnScreen(
                        template=self.templates['daily_accept'],
                        screenshotIm=self.bot.session.screenshot(),
                    )
                    if daily_accept:
                        self.bot.session.click(*daily_accept)
                        sleep(5)
            self.bot.stop()
