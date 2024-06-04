SCREENSHOTS = 'last_session/screenshots'


def screenshot(emulator):
    # TODO: add checking folder exists.
    emulator.make_and_save_screenshot(folder=SCREENSHOTS)
