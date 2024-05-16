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
