import os
from db.DataBase import DataBase as db
from components.components import Components as com
import settings.settings as setting

class Delete_contact:
    is_view = False
    is_message = ''

    def delete(self):

        while True:
            while True:
                self._view_welcome()
                try:
                    self._option = int(input('Introduce la opcion >> '))
                    if not(0 <= self._option < 2 ):
                        Delete_contact.is_view = True
                        Delete_contact.is_message = 'Opción incorrecta'                        
                        continue
                    break
                except Exception:
                    Delete_contact.is_view = True
                    Delete_contact.is_message = 'Introduce solo números'
            
            if self._option == 1:
                self._delete_contact()
            elif self._option == 0:
                os.system ("cls")
                break


    def _delete_contact(self):
        if db().all_contacts() != []:
            os.system ("cls")
            com.view_message(Delete_contact.is_view, Delete_contact.is_message) 
            print('BORRAR CONTACTO'.center(setting.SPACE, setting.CARACTER))
            self._name = com.varify_name().strip()
            
            if db().search_name_db(self._name) != []:
                db().delete_contact((self._name, ))
                Delete_contact.is_view = True
                Delete_contact.is_message = 'Contacto borrado con éxito'
            else:
                Delete_contact.is_view = True
                Delete_contact.is_message = 'No existe el contacto'

        else:
            setting.message_empty_calendar()
    
    def _view_welcome(sefl):
        os.system ("cls")
        com.view_message(Delete_contact.is_view, Delete_contact.is_message)
        print('Borrar cotacto'.center(setting.SPACE, setting.CARACTER))
        print('\n* Borrar contacto | Presione 1\n* Regresar        | Presione 0\n')
        Delete_contact.is_view = False


        
