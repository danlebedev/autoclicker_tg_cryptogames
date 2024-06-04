import json

SCREENSHOTS = 'last_session/screenshots'
SESSION = 'last_session/session'


def screenshot(emulator):
    # TODO: add checking folder exists.
    emulator.make_and_save_screenshot(folder=SCREENSHOTS)


def write_state(state: dict):
    with open(f'{SESSION}/state.json', 'w') as f:
        json.dump(state, f)
