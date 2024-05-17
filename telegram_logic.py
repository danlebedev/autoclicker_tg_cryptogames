class Telegram():
    def __init__(self):
        self.name = 'org.telegram.messenger'
        self.session = None

    def start(self, d):
        try:
            self.session = d.session(self.name)
        except:
            self.session = None

    def is_started(self) -> bool:
        if self.session:
            return self.session.running()
