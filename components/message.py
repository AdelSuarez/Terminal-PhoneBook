from settings import settings


class Message:
    def __init__(self, is_view, is_message) -> None:
        self.is_message = is_message
        self.is_view = is_view
        self.message()

    def message(self):
        if self.is_view:
            print(self.is_message.center(settings.SPACE, settings.CARACTER))





        