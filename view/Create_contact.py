from db.DataBase import DataBase as db
from settings import clear, settings
from components import name_checker, message
from . import view

class CreateContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)     

    def view_new_contact(self):
        while True:
            while True:
                if  ViewOptionsNewContact(self.is_view, self.is_message).view_welcome():
                    self.is_view = False
                try:
                    self.option = int(input('| Introduce la opcion >> '))
                    if not(0 <= self.option < 2 ):
                        self.is_view = True
                        self.is_message = 'Opción incorrecta'                        
                        continue
                    break
                except Exception:
                    self.is_view = True
                    self.is_message = 'Introduce solo números'

            if self.option == 1:
                if ViewCreateNewContact(self.is_view, self.is_message).new_contact():
                    self.is_view = True
                    self.is_message = 'Contacto creado con exito'

            elif self.option == 0:
                clear.Clear()
                break

            else:
                # It should never be executed, it is only there to check if a new error happens
                print('Ocurrio un error'.center(settings.SPACE, settings.CARACTER))
                break


class ViewOptionsNewContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
        self.options = {
            'Presione 1': 'Crear contacto',
            'Presione 0': 'Regresar'
        }

    def view_welcome(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message)
        print("+--------------------------------------+")
        print('|            NUEVO CONTACTO            |')
        self.view_option_menu(self.options)
        return True



class ViewCreateNewContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
        
    def new_contact(self):
        go_back = True
        while True:
            try:
                clear.Clear()
                message.Message(self.is_view, self.is_message)
                self.name = name_checker.NameChecker(self.is_view, self.is_message).name_checker('CREAR CONTACTO').strip()
                if self.name == '0':
                    go_back = False
                    break

                self.number = int(input('| Número: '))
                break

            except ValueError:
                self.is_view = True
                self.is_message = 'Introduce solo números'

        if go_back:
            db().create_contact(self.name, self.number)
            return True

