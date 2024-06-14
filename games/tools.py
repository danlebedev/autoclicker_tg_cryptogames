from random import randint


def click_generator(x, y, count=1, x_rand=0, y_rand=0):
    commands = []
    for _ in range(count):
        new_x = randint(-x_rand, x_rand) + x
        new_y = randint(-y_rand, y_rand) + y
        commands.append(f"input tap {new_x} {new_y}")
    return ' && '.join(commands)
