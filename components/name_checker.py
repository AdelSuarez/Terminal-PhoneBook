from settings import settings, clear
from . import message
from view.view import View 

class NameChecker(View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

    def name_checker(self, title : str = '') -> str:
        while True:

            if self.is_view:
                clear.Clear()

            message.Message(self.is_view, self.is_message,self.type_message)

            if title != '':
                print(title.center(settings.SPACE, settings.CARACTER))
                print('| > 0 Regresar                         |')


            print('| ° Introduce el nombre del contacto   |')
            print("+--------------------------------------+")

            name = input('| Nombre: ')
            
            if (len(name) == 0):

                self.message_variables(True,'Por Favor introduce el nombre', 'warning' )
                continue
            
            break

        self.is_view = False

        return name


            
