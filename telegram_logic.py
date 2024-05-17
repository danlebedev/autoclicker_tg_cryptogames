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


class Folder():
    def __init__(self, index, session):
        self.parent_classname = 'androidx.recyclerview.widget.RecyclerView'
        self.classname = 'android.view.View'
        self.index = index
        self.session = session

    def connect(self):
        try:
            self.session(className=self.parent_classname) \
                .child(className=self.classname, index=self.index) \
                .click()
        finally:
            return self.is_connected()

    def is_connected(self):
        return self.session(className=self.classname, index=self.index, selected=True).exists
