import json

SCREENSHOTS = 'last_session/screenshots'
SESSION = 'last_session/state.json'
TIMES = 'last_session/times.json'


def screenshot(emulator):
    # TODO: add checking folder exists.
    emulator.make_and_save_screenshot(folder=SCREENSHOTS)


def save_state(state: dict):
    # TODO: add checking folder exists.
    with open(SESSION, 'w') as f:
        json.dump(state, f)


def load_state():
    # TODO: add checking folder exists.
    try:
        with open(SESSION, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_times(data: dict):
    with open(TIMES, 'w') as f:
        json.dump(data, f)


def load_times():
    try:
        with open(TIMES, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
