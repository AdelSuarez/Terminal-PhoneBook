from db.DataBase import DataBase as db
from components import name_checker, message
from settings import settings, clear
from . import view, View_contacts

class DeleteContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)
        self.options = {
            'Presione 1': 'Borrar',
            'Presione 0': 'Regresar'
        }

    def delete(self):
        if db().all_contacts() != []:

            while True:
                while True:
                    if ViewOptionsDeleteContact(self.is_view, self.is_message, self.options).options_delete():
                        self.is_view = False
                    try:
                        self._option = int(input('| Introduce la opcion >> '))
                        if not(0 <= self._option < len(self.options) ):
                            self.is_view = True
                            self.is_message = 'Opción incorrecta'                        
                            continue
                        break
                    except Exception:
                        self.is_view = True
                        self.is_message = 'Introduce solo números'
                
                if self._option == 1:
                    if ViewDeleteContact(self.is_view, self.is_message).delete_contact():
                        self.is_view = True
                        self.is_message = 'Contacto borrado con éxito'
                
                elif self._option == 0:
                    clear.Clear()
                    break
        else:
            clear.Clear()
            settings.message_empty_calendar()

class ViewOptionsDeleteContact(view.View):
    def __init__(self, is_view, is_message, options) -> None:
        super().__init__(is_view, is_message)
        self.options = options

    def options_delete(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message)
        print("+--------------------------------------+")
        print('|           BORRAR CONTACTO            |')
        self.view_option_menu(self.options)
        return True


class ViewDeleteContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def delete_contact(self):
        while True:
            if db().all_contacts() != []:
                clear.Clear()
                message.Message(self.is_view, self.is_message)
                self.name = name_checker.NameChecker(self.is_view, self.is_message).name_checker('BORRAR CONTACTO').strip()
                
                if self.name =='0':
                    break
                contact = db().search_name_db(self.name)
                if  contact != []:
                    if len(contact) > 1:
                        View_contacts.ViewContacts().view_all_contacts(db().search_name_db(self.name)) 
                        id_contacto = int(input('| ID: '))
                        if id_contacto == 0:
                            break

                        db().delete_contact_id((id_contacto,))
                        return True

                    else:
                        db().delete_contact_name((self.name, ))
                        return True
                else:
                    self.is_view = True
                    self.is_message = 'No existe el contacto'

            else:
                settings.message_empty_calendar()


        
