from db.DataBase import DataBase as db
from components import name_checker, message
from settings import settings, clear
from . import view, View_contacts, View_contacts

class DeleteContact(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)
        
        self.view_options : dict[str:str] = {
            'Presione 1': 'Borrar',
            'Presione 2': 'Ver contactos',
            'Presione 0': 'Regresar',
        }

    def delete(self):
        if db().all_contacts() != []:

            while True:
                while True:
                    
                    if self.view_options_menu(self.view_options, 'BORRAR CONTACTO'):
                        self.is_view = False

                    try:
                        self.option = int(input('| Introduce la opcion >> '))
                        if not(0 <= self.option < len(self.view_options) ):

                            self.message_variables(True, 'Opcíon incorrecta', 'warning')
                            clear.Clear()
                            continue
                        break
                    except Exception:

                        self.message_variables(True, 'Introduce solo números', 'error')
                        clear.Clear()

                if self.option == 1:
                    if ViewDeleteContact(self.is_view, self.is_message, self.type_message).delete_contact():
                        
                        self.message_variables(True, 'Contacto borrado con éxito', 'approved')
                        clear.Clear()


                elif self.option == 2:

                    View_contacts.ViewContacts(self.is_view, self.is_message, self.type_message).all_contacts()
                
                elif self.option == 0:
                    clear.Clear()
                    break
        else:
            clear.Clear()
            print('Agenda vacía'.center(settings.SPACE, settings.CARACTER))


class ViewDeleteContact(view.View):
    def __init__(self, is_view, is_message, type_message) -> None:
        super().__init__(is_view, is_message, type_message)

    def delete_contact(self) -> bool:
        while True:
            if db().all_contacts() != []:
                clear.Clear()
                message.Message(self.is_view, self.is_message, self.type_message)


                self.name = name_checker.NameChecker(self.is_view, self.is_message, self.type_message).name_checker('BORRAR CONTACTO')
                
                if self.name =='0':
                    clear.Clear()
                    break

                contact = db().search_name_db(self.name)

                if  contact != []:
                    if len(contact) > 1:

                        self.is_view = False
                        View_contacts.ViewContacts(self.is_view, self.is_message, self.type_message).view_all_contacts(db().search_name_db(self.name))
                        
                        try:
                            id_contacto = int(input('| ID: '))
                            
                            if id_contacto == 0:
                                clear.Clear()
                                break

                            if db().search_id_db(id_contacto, self.name) != []:
                                db().delete_contact_id(id_contacto, self.name)
                                return True
                            
                            else:
                                self.message_variables(True, 'No existe el ID', 'warning')
                                
                        except ValueError:
                            self.message_variables(True, 'Introduce solo números', 'error')
                        
                    else:
                        db().delete_contact_name(self.name)
                        return True
                else:
                    self.message_variables(True, 'No existe el contacto', 'warning')

            else:
                clear.Clear()
                print('Agenda vacía'.center(settings.SPACE, settings.CARACTER))
                break


        
