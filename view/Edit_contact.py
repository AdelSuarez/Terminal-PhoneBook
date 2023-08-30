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

                self.menu_edit()
                self.is_view = False

                if self.option == 1:

                    if ViewEditName(self.is_view, self.is_message, self.type_message).edit_name():
                        self.message_variables(True, 'Contacto actualizado con exito', 'approved')

                elif self.option == 2:
                    
                    if ViewEditNumber(self.is_view, self.is_message, self.type_message).edit_number():
                        self.message_variables(True, 'Contacto actualizado con exito', 'approved')

                elif self.option == 3:

                    self.is_view = False
                    View_contacts.ViewContacts(self.is_view, self.is_message, self.type_message).all_contacts()
                    
                elif self.option == 0:
                    clear.Clear()
                    break
        else:
            clear.Clear()
            print('Agenda vacía'.center(settings.SPACE, settings.CARACTER))



    def menu_edit(self):
        while True:            

            self.view_options_menu(self.view_options, 'EDITAR CONTACTO')


            try:
                self.option = int(input('| Introduce la opcion >> '))

                if not(0 <= self.option < len(self.view_options)):

                    self.message_variables(True, 'Opción incorrecta', 'warning')
                    continue
                break

            except ValueError:
                self.message_variables(True, 'Introduce solo números', 'error')




class ViewEditName(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)


    def edit_name(self):
        self.is_view = False
        while True:
            self.name = ViewNameChecker(self.is_view, self.is_message, self.type_message).view('EDITAR NOMBRE')

            if self.name == '0':
                break
            
            contact = db().search_name_db(self.name)

            if contact  != []:
                if len(contact) > 1:
                    
                    self.is_view = False
                    View_contacts.ViewContacts(self.is_view, self.is_message, self.type_message).view_all_contacts(db().search_name_db(self.name))

                    try:
                        id_contacto = int(input('| ID: '))

                        if id_contacto == 0:
                            break
                        
                        if db().search_id_db(id_contacto, self.name) != []:
                            self.new_name, self.is_correct =  InputNewData(self.is_view, self.is_message, self.type_message).input_new_name('name')

                            if self.is_correct and self.new_name != '0':
                                db().update_name_id(self.new_name, id_contacto)
                                return True
                            elif self.new_name == '0':
                                break
                        else:
                            self.message_variables(True, 'No existe el ID', 'warning')



                    except ValueError:
                        self.message_variables(True, 'Introduce solo números', 'error')

                else:

                    self.is_view = False

                    self.new_name, self.is_correct =  InputNewData(self.is_view, self.is_message, self.type_message).input_new_name('name')
                    

                    if self.is_correct and self.new_name != '0':
                        db().update_name(self.new_name, self.name)
                        return True
                    elif self.new_name == '0':
                        break
            else:
                self.message_variables(True, 'No existe el contacto', 'warning')
                
class ViewEditNumber(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

    def edit_number(self):

        self.is_view = False
        while True:
            self.name = ViewNameChecker(self.is_view, self.is_message, self.type_message).view('EDITAR NUMERO')

            if self.name == '0':
                break
            
            contact = db().search_name_db(self.name)

            if contact != []:
                if len(contact) > 1:
                    self.is_view = False
                    View_contacts.ViewContacts(self.is_view, self.is_message, self.type_message).view_all_contacts(db().search_name_db(self.name))
                    
                    try:
                        id_contacto = int(input('| ID: '))
                        if id_contacto == 0:
                                break
                        if db().search_id_db(id_contacto, self.name) != []:

                            self.new_number, self.is_correct = InputNewData(self.is_view, self.is_message, self.type_message).input_new_name('number')

                            if self.new_number == '0':
                                break

                            elif self.is_correct and self.new_number != '0':
                                db().update_number_id((int(self.new_number), id_contacto))
                                return True
                        else:
                            self.message_variables(True, 'No existe el ID', 'warning')

                        
                    except ValueError:
                        self.message_variables(True, 'Introduce solo números', 'error')
                    
                else:
                    self.is_view = False

                    self.new_number, self.is_correct = InputNewData(self.is_view, self.is_message, self.type_message).input_new_name('number')

                    try:
                        if self.is_correct and self.new_number != '0':
                            db().update_number(int(self.new_number), self.name)
                            return True
                        
                        elif self.new_number == '0':
                            break
                            
                    except ValueError:
                        self.message_variables(True, 'Introduce solo números', 'error')
            else:
                self.message_variables(True, 'No existe el contacto', 'warning')



class InputNewData(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)
        

    def input_new_name(self, option : str) -> tuple:

        is_view_go_back = False
        while True:

            if self.is_view:
                clear.Clear()
                message.Message(self.is_view, self.is_message, self.type_message)
            print("+--------------------------------------+")
            
            if is_view_go_back:
                print('| > 0 Regresar                         |')

            if option == 'name':
                print('| ° Introduce el nuevo nombre:         |')

            elif option == 'number':
                print('| Introduce el nuevo número:           |')
                
            print("+--------------------------------------+")

            new_data = input('| >> ')

            if (len(new_data) == 0):
                self.message_variables(True, 'Por Favor introduce el dato', 'warning')
                is_view_go_back = True
                continue

            return (new_data.strip(), True)
        
class ViewNameChecker(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

        
    def view(self, title : str):
        clear.Clear()
        message.Message(self.is_view, self.is_message, self.type_message)

        name = name_checker.NameChecker(self.is_view, self.is_message, self.type_message).name_checker(title)

        return name