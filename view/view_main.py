from settings import settings, clear
from components import message
from . import view

class ViewMain(view.View):

    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
        
        self.options = {
            'Presione 1': 'Nuevo contacto',
            'Presione 2': 'Ver contactos',
            'Presione 3': 'Borrar contacto',
            'Presione 4': 'Editar contacto',
            'Presione 0': 'Salir'
        }

    def views_main(self):

        while True:
            if not ViewOptions(self.is_view, self.is_message, self.options).view_options():
                self.is_view = False
                
            try:
                self.option = int(input('| Selecciona una opción >> '))
                if not(0 <= self.option < len(self.options)):
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

        
class ViewOptions(view.View):
    def __init__(self, is_view, is_message, options) -> None:
        super().__init__(is_view, is_message)
        self.options = options

    def view_options(self) -> None:
        message.Message(self.is_view, self.is_message)
        print("+--------------------------------------+")
        print('|          AGENDA DE CONTACTOS         |')
        print('|----------------INICIO----------------|')

        self.view_option_menu(self.options)
        return False