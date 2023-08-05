from db.DataBase import DataBase as db
from settings import clear, settings
from components import name_checker, message

class CreateContact:
    is_view = False
    is_message = ''       

    def view_new_contact(self):
        while True:
            while True:
                if not ViewOptionsNewContact(CreateContact.is_view, CreateContact.is_message).view_welcome():
                    CreateContact.is_view = False
                try:
                    self.option = int(input('Introduce la opcion >> '))
                    if not(0 <= self.option < 2 ):
                        CreateContact.is_view = True
                        CreateContact.is_message = 'Opción incorrecta'                        
                        continue
                    break
                except Exception:
                    CreateContact.is_view = True
                    CreateContact.is_message = 'Introduce solo números'

            if self.option == 1:
                if ViewCreateNewContact(CreateContact.is_view, CreateContact.is_message).new_contact():
                    CreateContact.is_view = True
                    CreateContact.is_message = 'Contacto creado con exito'

            elif self.option == 0:
                clear.Clear()
                break

            else:
                # It should never be executed, it is only there to check if a new error happens
                print('Ocurrio un error'.center(settings.SPACE, settings.CARACTER))
                break


class ViewOptionsNewContact:
    def __init__(self, is_view, is_message) -> None:
        self.is_view = is_view
        self.is_message = is_message

    def view_welcome(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message)
        print('Nuevo cotacto'.center(settings.SPACE, settings.CARACTER))
        print('\n* Crear contacto | Presione 1\n* Regresar       | Presione 0\n')
        return False



class ViewCreateNewContact:
    def __init__(self, is_view, is_message) -> None:
        self.is_view = is_view
        self.is_message = is_message
        
    def new_contact(self):
        while True:
            try:
                clear.Clear()
                message.Message(self.is_view, self.is_message)
                self.name = name_checker.NameChecker().name_checker('CREAR CONTACTO').strip()
                self.number = int(input('Número: '))
                #self.is_view = False
                break

            except ValueError:
                self.is_view = True
                self.is_message = 'Introduce solo números'

        db().create_contact(self.name, self.number)
        return True
