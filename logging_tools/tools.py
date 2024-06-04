import json

SCREENSHOTS = 'last_session/screenshots'
SESSION = 'last_session/state.json'


def screenshot(emulator):
    # TODO: add checking folder exists.
    emulator.make_and_save_screenshot(folder=SCREENSHOTS)


def write_state(state: dict):
    # TODO: add checking folder exists.
    with open(SESSION, 'w') as f:
        json.dump(state, f)


def read_state():
    # TODO: add checking folder exists.
    try:
        with open(SESSION, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
