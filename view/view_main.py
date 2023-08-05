from settings import settings, clear
from components.name_checker import NameChecker

class ViewMain:
    is_view = False
    is_message = '' 

    def views_main(self):


        while True:
            ViewWelcome().view_welcome()
            ViewOptions(ViewMain.is_view, ViewMain.is_message).view_options()
            try:
                self.option = int(input('Selecciona una opción >> '))
                if not(0 <= self.option < 6):
                    ViewMain.is_view = True
                    ViewMain.is_message = 'La opcion no existe'
                    clear.Clear()
                    continue
                return self.option

            except ValueError:
                ViewMain.is_view = True
                ViewMain.is_message = 'Introduce solo números'
                print('Introduce solo números'.center(settings.SPACE, settings.CARACTER))
                clear.Clear()


class ViewWelcome:
    def view_welcome(self) -> None:
        print('')
        print(''.center(settings.SPACE, '*'))
        print(' AGENDA DE CONTACTOS '.center(settings.SPACE, '*'))
        print(''.center(settings.SPACE, '*'))
        print('')


class ViewOptions:
    def __init__(self, is_view, is_message) -> None:
        self.is_view = is_view
        self.is_message = is_message

    def view_options(self) -> None:
        NameChecker.view_message(self.is_view, self.is_message)
        print('Inicio'.center(settings.SPACE, settings.CARACTER))
        print('* Crear contacto     | presione 1\n* Ver contactos      | Presione 2\n* Borrar contacto    | Presione 3\n* Editar contacto    | Presione 4\n* Salir              | Presione 0\n')
        self.is_view = False