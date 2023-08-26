from db.DataBase import DataBase as db
from settings import clear, settings
from components import name_checker, message
from . import view

class CreateContact(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

        self.view_options : dict[str : str]  = {
            'Presione 1': 'Crear contacto',
            'Presione 0': 'Regresar'
        }

    def view_new_contact(self):
        while True:
            while True:

                if self.view_options_menu(self.view_options, 'NUEVO CONTACTO'):
                    self.is_view = False

                try:
                    self.option = int(input('| Introduce la opcion >> '))

                    if not(0 <= self.option < len(self.view_options) ):
                        
                        self.message_variables(True, 'Opción incorrecta', 'warning')
                        continue

                    break
                except Exception:
                    self.message_variables(True, 'Introduce solo números', 'error')

            if self.option == 1:
                if ViewCreateNewContact(self.is_view, self.is_message, self.type_message).new_contact():

                    self.message_variables(True, 'Contacto creado con exito', 'approved')

            elif self.option == 0:
                clear.Clear()
                break

            else:
                # It should never be executed, it is only there to check if a new error happens
                print('Ocurrio un error'.center(settings.SPACE, settings.CARACTER))
                break


class ViewCreateNewContact(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)
        
    def new_contact(self) -> bool:
        go_back : bool = False

        while True:
            try:
                clear.Clear()
                message.Message(self.is_view, self.is_message, self.type_message)

                self.name = name_checker.NameChecker(self.is_view, self.is_message, self.type_message).name_checker('CREAR CONTACTO')

                if self.name == '0':
                    go_back = True
                    break

                self.number = int(input('| Número: '))

                if self.number == 0:
                    go_back = True
                    break

                break

            except ValueError:
                self.message_variables(True, 'Introduce solo números', 'error')


        if not go_back:
            db().create_contact(self.name, self.number)
            return True

