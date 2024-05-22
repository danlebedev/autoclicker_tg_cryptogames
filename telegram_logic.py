class Telegram():
    def __init__(self, device):
        self.name = 'org.telegram.messenger'
        self.session = None
        self.device = device

    def start(self):
        try:
            self.session = self.device.session(self.name)
        except:
            self.session = None
        else:
            # If we start session, session.setting are reset.
            # That why we need assign previous settings.
            self.session.settings = self.device.settings

    def is_started(self) -> bool | None:
        if self.session:
            return self.session.running()

    def init_folder(self, index):
        self.folder = Folder(index, self.session)


class Folder():
    def __init__(self, index, session):
        self.parent_classname = 'androidx.recyclerview.widget.RecyclerView'
        self.classname = 'android.view.View'
        self.index = index
        self.session = session

    def connect(self) -> bool:
        try:
            self.session(className=self.parent_classname) \
                .child(className=self.classname, index=self.index) \
                .click()
        finally:
            return self.is_connected()

    def is_connected(self) -> bool:
        return self.session(className=self.classname, index=self.index, selected=True).exists()

    def init_bot(self, index):
        self.bot = Bot(index, self.session)


class MessageMixin():
    message_classname = 'android.view.ViewGroup'
    inline_button_classname = 'android.widget.Button'


class Chat(MessageMixin):
    def __init__(self, index, session):
        self.parent_classname = 'androidx.recyclerview.widget.RecyclerView'
        self.classname = 'android.view.ViewGroup'
        self.index = index
        self.session = session

    def connect(self) -> bool:
            try:
                self.session(className=self.parent_classname) \
                    .child(className=self.classname, index=self.index) \
                    .click()
                self._set_name()
            finally:
                return self.is_connected()

    def is_connected(self) -> bool:
        return self.session(className='android.widget.EditText', longClickable=True).exists()

    def _set_name(self):
        self.name = self.session(className='android.widget.TextView')[0].get_text()

    def get_last_message(self):
        return self.session(className=self.message_classname)[-1]
    
    def click_inline_button(self, index):
        self.get_last_message() \
            .child(
                className=self.inline_button_classname,
                index=index,
            ).click()


class Bot(Chat):
    def __init__(self, index, session):
        self.menu = 'Меню бота'
        super().__init__(index, session)

    def is_connected(self) -> bool:
        return self.session(description=self.menu).exists()

    def run(self):
        self.session(description=self.menu).click()
        self._run_accept()

    def stop(self):
        self.run()

    def click_inline_button(self, index):
        super().click_inline_button(index)
        self._run_accept()

    def _run_accept(self):
        if self.session(className='android.widget.TextView', text='Начать', clickable=True).exists():
            self.session(className='android.widget.TextView', text='Начать', clickable=True).click()

    def set_game(self, games):
        for game in games:
            if game.name == self.name:
                self.game = game(self)
                break
        else:
            self.game = None
