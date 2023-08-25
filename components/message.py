from settings import settings
from view.view import View

class Message(View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

        self.message_colors : dict[str : str] = {
            'error': settings.RED,
            'warning': settings.YELLOW,
            'approved': settings.GREEN,
        }

        self.message()

    def message(self):
        if self.is_view:

            for type, color in self.message_colors.items():
                if type == self.type_message:
                    print(f'{color}', end='')
                    
            print(self.is_message.center(settings.SPACE, settings.CARACTER))
            print(f'{settings.RESET}', end='')





        