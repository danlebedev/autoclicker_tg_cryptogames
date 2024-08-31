from time import sleep

class Proxy():
    def __init__(self, device):
        self.name = 'org.proxydroid'
        self.session = None
        self.device = device

    def start(self):
        try:
            self.session = self.device.session(self.name)
        except:
            self.session = None
        else:
            self.session.settings = self.device.settings
            sleep(5)
            self.run()

    def is_started(self) -> bool | None:
        if self.session:
            return self.session.running()

    def run(self):
        self.session(className='android.widget.Switch').click()