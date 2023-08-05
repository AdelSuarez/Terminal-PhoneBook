from settings import settings
from view.view import View

class Message(View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
        self.message()

    def message(self):
        if self.is_view:
            print(self.is_message.center(settings.SPACE, settings.CARACTER))





        