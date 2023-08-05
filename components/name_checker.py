from settings import settings, clear
from . import message

class NameChecker:
    is_view = False
    is_message = ''

    def name_checker(self, title = ''):
        while True:

            if NameChecker.is_view:
                clear.Clear()

            message.Message(NameChecker.is_view, NameChecker.is_message)

            if title != '':
                print(title.center(settings.SPACE, settings.CARACTER))

            print('Introduce el nombre del contacto')
            name = input('Nombre: ')
            
            if (len(name) == 0):
                NameChecker.is_view = True
                NameChecker.is_message = 'Por Favor introduce el nombre'
                continue
            break

        NameChecker.is_view = False

        return name

    def view_message(is_view, is_message):
        if is_view:
            print(is_message.center(settings.SPACE, settings.CARACTER))

            
