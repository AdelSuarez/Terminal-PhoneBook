from settings import settings, clear
from db.DataBase import DataBase as db
from components import name_checker, message
from . import view, View_contacts

class EditContact(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)
         
        self.view_options : dict[str : str] = {
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
                    ViewOptionsEditContact(self.is_view, self.is_message, self.type_message, self.view_options).view_options()
                    try:
                        self.option = int(input('| Introduce la opcion >> '))
                        if not(0 <= self.option < len(self.view_options)):

                            self.message_variables(True, 'Opción incorrecta', 'warning')
                            continue
                        break
                    except ValueError:
                        self.message_variables(True, 'Introduce solo números', 'error')

                if self.option == 1:
                    #try:
                        if ViewEditName(self.is_view, self.is_message, self.type_message).edit_name():
                            self.message_variables(True, 'Nombre actualizado con exito', 'approved')

                    #except TypeError:
                    #    self.is_view = False

                elif self.option == 2:
                    self.is_message, self.is_view = ViewEditNumber(self.is_view, self.is_message, self.type_message).edit_number()

                elif self.option == 3:
                    self.is_view = False
                    View_contacts.ViewContacts().all_contacts()
                    
                elif self.option == 0:
                    clear.Clear()
                    break
        else:
            clear.Clear()
            print('Agenda vacía'.center(settings.SPACE, settings.CARACTER))


class ViewEditName(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

        self.successful_change_message = ('Nombre actualizado con exito', True)

    def edit_name(self):
        self.is_view = False
        while True:
            clear.Clear()
            message.Message(self.is_view, self.is_message, self.type_message)

            self.name = name_checker.NameChecker(self.is_view, self.is_message, self.type_message).name_checker('EDITAR NOMBRE').strip()

            if self.name == '0':
                break
            
            contact = db().search_name_db(self.name)

            if contact  != []:
                if len(contact) > 1:
                    
                    self.is_view = False
                    View_contacts.ViewContacts().view_all_contacts(db().search_name_db(self.name))

                    
                    try:
                        id_contacto = int(input('| ID: '))

                        if id_contacto == 0:
                            break

                        self.new_name, self.is_correct =  self.input_new_name()

                        if self.is_correct:
                            db().update_name_id(self.new_name.strip(), id_contacto)
                            return True
                        


                    except ValueError:
                        self.message_variables(True, 'Introduce solo números', 'error')

                else:

                    self.is_view = False

                    self.new_name, self.is_correct =  self.input_new_name()


                    if self.is_correct:
                        db().update_name(self.new_name.strip(), self.name)
                        return True
                    
            else:
                self.message_variables(True, 'No existe el contacto', 'warning')

    def input_new_name(self) -> tuple:

        while True:

            if self.is_view:
                clear.Clear()
                message.Message(self.is_view, self.is_message, self.type_message)
            print("+--------------------------------------+")
            print('| Introduce el nuevo nombre:           |')
            print("+--------------------------------------+")

            new_name = input('| >> ')

            if (len(new_name) == 0):
                self.message_variables(True, 'Por Favor introduce el nombre', 'warning')
                continue

            return (new_name, True)
        


class ViewEditNumber(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

    def edit_number(self):

        self.is_view = False
        while True:
            clear.Clear()
            message.Message(self.is_view, self.is_message, self.type_message)

            self.name = name_checker.NameChecker(self.is_view, self.is_message, self.type_message).name_checker('EDITAR NUMERO').strip()

            if self.name == '0':
                break
            
            contact = db().search_name_db(self.name)

            if contact != []:
                if len(contact) > 1:
                    View_contacts.ViewContacts().view_all_contacts(db().search_name_db(self.name))
                    id_contact = input()
                    
                else:
                    self.is_view = False

                    self.new_number, self.is_correct = self.input_new_number()
                        
                    if self.is_correct:
                        db().update_number(self.new_number, self.name)
                        return ('Número actualizado con exito', True)

            else:
                self.message_variables(True, 'No existe el contacto', 'warning')

    def input_new_number(self) -> tuple:
        while True:
            if self.is_view:
                clear.Clear()
                message.Message(self.is_view, self.is_message)
            try:
                print("+--------------------------------------+")
                print('| Introduce el nuevo número:           |')
                print("+--------------------------------------+")
                new_number = int(input('| >> '))
                return (new_number, True)
            
            except ValueError:
                
                self.is_view = True
                self.is_message = 'Introduce el número'

class ViewOptionsEditContact(view.View):
    def __init__(self, is_view, is_message, type_message, options) -> None:
        super().__init__(is_view, is_message, type_message)
        self.options = options

    def view_options(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message, self.type_message)
        print("+--------------------------------------+")
        print('|           EDITAR CONTACTO            |')
        self.view_option_menu(self.options)
