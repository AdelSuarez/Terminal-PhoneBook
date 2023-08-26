from settings import clear
from components import message
from . import view

class ViewMain(view.View):

    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)
        
        self.view_options : dict[str : str] = {
            'Presione 1': 'Nuevo contacto',
            'Presione 2': 'Ver contactos',
            'Presione 3': 'Borrar contacto',
            'Presione 4': 'Editar contacto',
            'Presione 0': 'Salir'
        }

    def views_main(self) -> int:

        while True:
            if not ViewOptions(self.is_view, self.is_message,self.type_message, self.view_options).view_options():
                self.is_view = False
                
            try:
                option = int(input('| Selecciona una opción >> '))
                if not(0 <= option < len(self.view_options)):

                    self.message_variables(True, 'La opcion no existe', 'warning')
                    clear.Clear()

                    continue

                self.type_message = ''
                return option

            except ValueError:
                
                self.message_variables(True, 'Introduce solo números', 'error')
                clear.Clear()

        
class ViewOptions(view.View):
    def __init__(self, is_view, is_message, type_message, options) -> None:
        super().__init__(is_view, is_message, type_message)
        self.options = options

    def view_options(self) -> bool:
        message.Message(self.is_view, self.is_message, self.type_message)
        print("+--------------------------------------+")
        print('|          AGENDA DE CONTACTOS         |')
        print('|----------------INICIO----------------|')

        self.view_option_menu(self.options)
        return False