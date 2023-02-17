from db.DataBase import DataBase
from components.components import Components
import settings.settings as setting

class Delete_contact:

    def delete(self):

        while True:
            if Components.all_contacts() != []:
                print('')
                print('BORRAR CONTACTO'.center(setting.SPACE, setting.CARACTER))
                self.name = Components.varify_name().strip()
                
                if Components.search_name(self.name) != []:
                    self._query = 'DELETE FROM CONTACT WHERE NAME like ?'
                    DataBase(self._query, (self.name, )).db()
                    print('')
                    print('Contacto borrado con éxito'.center(setting.SPACE, setting.CARACTER))
                    break
                else:
                    print('No existe el contacto'.center(setting.SPACE, setting.CARACTER))

            else:
                setting.message_empty_calendar()
                break


        
