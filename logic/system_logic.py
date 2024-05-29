from subprocess import Popen, run
from time import sleep
from datetime import datetime
import uiautomator2 as u2
from os.path import abspath


class Shell():
    def __init__(self, args=None, cwd=None, shell=True):
        self.process = None
        self.args = args
        self.cwd = cwd
        self.shell = shell

    def start_process(self):
        self.process = Popen(
            args=self.args,
            shell=self.shell,
            cwd=self.cwd
        )
    
    def kill_process(self):
        if self.process:
            self.process.kill()

    def run_command(self):
        run(
            args=self.args,
            shell=self.shell,
            cwd=self.cwd
        )


class ADB(Shell):
    def __init__(self, shell=True):
        self.cwd = abspath('platform-tools')
        self.name = 'adb'
        self.shell = shell

    def start(self):
        self.args = f'{self.name} start-server'
        self.run_command()

    def stop(self):
        self.args = f'{self.name} kill-server'
        self.run_command()

    def reconnect(self):
        self.args = f'{self.name} reconnect'
        self.run_command()


class Dnconsole(Shell):
    def __init__(self, shell=True):
        self.cwd = r'C:\LDPlayer\LDPlayer9'
        self.name = 'dnconsole'
        self.shell = shell

    def set_index(self, index):
        self.index = index

    def start(self):
        self.args = f'{self.name} launch --index {self.index}'
        self.start_process()

    def stop(self):
        self.args = f'{self.name} quit --index {self.index}'
        self.start_process()


class Emulator(Dnconsole):
    def __init__(self, index, device_id, shell=True):
        super().__init__(shell)
        self.set_index(index)
        self.device_id = device_id

    def start(self):
        super().start()
        sleep(30)

    def stop(self):
        super().stop()
        sleep(5)
    
    def connect(self):
        self.device = u2.connect(self.device_id)
        self.device.settings['operation_delay'] = (2, 2)
        self.device.settings['operation_delay_methods'] = [
            'click',
            'press',
            'exists',
            'get_text',
            'set_text',
        ]

    def is_connected(self) -> bool:
        if self.device:
            return True
        return False

    def make_screenshot(self, scr_format='pillow'):
        screenshot = self.device.screenshot(format=scr_format)
        date = datetime.now()
        return (screenshot, date)

    def save_screenshot(self, screenshot, name, save_format='PNG'):
        if isinstance(name, datetime):
            name = name.strftime('%d-%m-%Y_%H-%M-%S-%f')
        screenshot.save(f'screenshots/{name}.{save_format.lower()}')

    def make_and_save_screenshot(self, name=None, scr_format='pillow', save_format='PNG'):
        """
        Use this method only for single screenshots. Slow speed because it is saved
        immediately after taking a screenshot.
        For fast screenshots use methods make_screenshot() and append to list.
        After finishing screenshots iterate through the list and save images
        with method save_screenshot().
        """
        screenshot = self.make_screenshot(scr_format=scr_format)
        if not name:
            self.save_screenshot(
                *screenshot,
                save_format=save_format,
            )
        else:
            self.save_screenshot(
                screenshot=screenshot[1],
                name=name,
                save_format=save_format,
            )