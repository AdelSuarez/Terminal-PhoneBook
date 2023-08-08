from settings import settings, clear
from db.DataBase import DataBase as db
from components import name_checker, message
from . import view, View_contacts

class EditContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
         
        self.view_options = {
            'Presione 1': 'Editar nombre',
            'Presione 2': 'Editar número',
            'Presione 3': 'Ver contactos',
            'Presione 0': 'Regresar',
        }


    def mian_edit(self):
        self.is_view = False
        if db().all_contacts() != []:
            while True:
                while True:
                    ViewOptionsEditContact(self.is_view, self.is_message, self.view_options).options_edit_contact()
                    try:
                        self.option = int(input('| Introduce la opcion >> '))
                        if not(0 <= self.option < len(self.view_options)):
                            self.is_view = True
                            self.is_message = 'Opción incorrecta'
                            continue
                        break
                    except ValueError:
                        self.is_view = True
                        self.is_message = 'Introduce solo números'

                if self.option == 1:
                    ViewEditName(self.is_view, self.is_message).edit_name()

                elif self.option == 2:
                    ViewEditNumber(self.is_view, self.is_message).edit_number()

                elif self.option == 3:

                    View_contacts.ViewContacts().all_contacts()
                    
                elif self.option == 0:
                    clear.Clear()
                    break
        else:
            clear.Clear()
            print('Agenda vacía'.center(settings.SPACE, settings.CARACTER))


class ViewEditName(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def edit_name(self):
        self.is_view = False
        while True:
            clear.Clear()
            message.Message(self.is_view, self.is_message)
            self.name = name_checker.NameChecker(self.is_view, self.is_message).name_checker('EDITAR NOMBRE').strip()

            if self.name == '0':
                break
            
            contact = db().search_name_db(self.name)

            if contact  != []:
                if len(contact) > 1:
                    View_contacts.ViewContacts().view_all_contacts(db().search_name_db(self.name))
                    id_contacto = int(input('| ID:  DESARROLLO'))
                else:
                    is_corret = False
                    self.is_view = False

                    while True:
                        if self.is_view:
                            clear.Clear()
                            message.Message(self.is_view, self.is_message)

                        print('Introduce el nuevo nombre:')
                        self._new_name = input('>> ')
                        if (len(self._new_name) == 0):
                            self.is_view = True
                            self.is_message = 'Por Favor introduce el nombre'
                            break
                        is_corret = True
                        break

                    if is_corret:
                        self._parameters = (self._new_name.strip(), self.name)
                        db().update_name(self._parameters)
                        self.is_view = True
                        self.is_message = 'Nombre actualizado con exito'
                        break
            else:
                self.is_view = True
                self.is_message = 'No existe el contacto'


class ViewEditNumber(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def edit_number(self):
        is_corret = False

        self.is_view = False
        while True:
            clear.Clear()
            message.Message(self.is_view, self.is_message)
            self.name = name_checker.NameChecker(self.is_view, self.is_message).name_checker('EDITAR NUMERO').strip()

            if db().search_name_db(self.name) != []:
                self.is_view = False
                while True:
                    if self.is_view:
                        clear.Clear()
                        message.Message(self.is_view, self.is_message)
                    try:
                        print('Introduce el nuevo número:')
                        self.new_number = int(input('>> '))
                        is_corret = True
                        break
                    except Exception:
                        self.is_view = True
                        self.is_message = 'Introduce un numero'
                        break
                    
                if is_corret:
                    self.parameters = (self.new_number, self.name)
                    db().update_number(self.parameters)
                    self.is_view = True
                    self.is_message = 'Número actualizado con exito'
                    break

            else:
                self.is_view = True
                self.is_message = 'No existe el contacto'

class ViewOptionsEditContact(view.View):
    def __init__(self, is_view, is_message, options) -> None:
        super().__init__(is_view, is_message)
        self.options = options

    def options_edit_contact(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message)
        print("+--------------------------------------+")
        print('|           EDITAR CONTACTO            |')
        self.view_option_menu(self.options)
