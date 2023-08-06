from settings import settings, clear
from components.name_checker import NameChecker
from . import view

class ViewMain(view.View):

    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def views_main(self):


        while True:
            ViewWelcome().view_welcome()
            if not ViewOptions(self.is_view, self.is_message).view_options():
                self.is_view = False
                
            try:
                self.option = int(input('Selecciona una opción >> '))
                if not(0 <= self.option < 6):
                    self.is_view = True
                    self.is_message = 'La opcion no existe'
                    clear.Clear()
                    continue
                return self.option

            except ValueError:
                self.is_view = True
                self.is_message = 'Introduce solo números'
                print('Introduce solo números'.center(settings.SPACE, settings.CARACTER))
                clear.Clear()


class ViewWelcome:
    def view_welcome(self) -> None:
        print(''.center(settings.SPACE, '*'))
        print(' AGENDA DE CONTACTOS '.center(settings.SPACE, '*'))
        print(''.center(settings.SPACE, '*'))


class ViewOptions(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def view_options(self) -> None:
        NameChecker.view_message(self.is_view, self.is_message)
        print('Inicio'.center(settings.SPACE, settings.CARACTER))
        print('| Crear contacto     | presione 1 |\n| Ver contactos      | Presione 2 |\n| Borrar contacto    | Presione 3 |\n| Editar contacto    | Presione 4 |\n| Salir              | Presione 0 |')
        print(''.center(settings.SPACE, settings.CARACTER))

        return False