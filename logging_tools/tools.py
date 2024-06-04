import json

SCREENSHOTS = 'last_session/screenshots'
SESSION = 'last_session/session'


def screenshot(emulator):
    # TODO: add checking folder exists.
    emulator.make_and_save_screenshot(folder=SCREENSHOTS)


def write_state(state: dict):
    # TODO: add checking folder exists.
    # TODO: rewrite path generation in open() with os lib.
    with open(f'{SESSION}/state.json', 'w') as f:
        json.dump(state, f)


def read_state():
    # TODO: add checking folder exists.
    # TODO: rewrite path generation in open() with os lib.
    try:
        with open(f'{SESSION}/state.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
