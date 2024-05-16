from subprocess import Popen, run


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
    def __init__(self):
        self.cwd = r'C:\Users\spirit\Desktop\platform-tools'
        self.name = 'adb'

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
    def __init__(self):
        self.cwd = r'C:\LDPlayer\LDPlayer9'
        self.name = 'dnconsole'

    def set_index(self, index):
        self.index = index

    def start(self):
        self.args = f'{self.name} launch --index {self.index}'
        self.start_process()

    def stop(self):
        self.args = f'{self.name} quit --index {self.index}'
        self.start_process()
