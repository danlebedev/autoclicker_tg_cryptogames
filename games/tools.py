from random import randint
from os import scandir
from os.path import join, splitext
from settings import GAMES_DIR
from PIL import Image
import json
from time import time


def click_generator(x, y, count=1, x_rand=0, y_rand=0):
    commands = []
    for _ in range(count):
        new_x = randint(-x_rand, x_rand) + x
        new_y = randint(-y_rand, y_rand) + y
        commands.append(f"input tap {new_x} {new_y}")
    return ' && '.join(commands)


def load_templates(classname):
    templates = {}
    path = join(GAMES_DIR, classname, 'templates')
    for template in scandir(path):
        template_name = splitext(template.name)[0]
        templates[template_name] = Image.open(template.path)
    return templates


class TimerMixin:
    timer = None

    def check_time(self, last_time):
        time_now = int(time())
        if time_now - last_time > self.timer:
            return time_now
        else:
            return None


class LoadMixin:

    @classmethod
    def _load_templates(cls):
        return load_templates(cls.__name__)
