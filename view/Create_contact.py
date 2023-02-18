import os
from db.DataBase import DataBase as db
from components.components import Components as com
import settings.settings as setting

class Create_contact:
    is_view = False
    is_message = ''       

    def create(self):
        while True: # main cicle
            while True:
                self._view_welcome()
                try:
                    self._option = int(input('Introduce la opcion >> '))
                    if not(0 <= self._option < 2 ):
                        Create_contact.is_view = True
                        Create_contact.is_message = 'Opción incorrecta'                        
                        continue
                    break
                except Exception:
                    Create_contact.is_view = True
                    Create_contact.is_message = 'Introduce solo números'

            if self._option == 1:
                self._options_create()

            elif self._option == 0:
                os.system ("cls")
                break

            else:
                print('Ocurrio un error'.center(setting.SPACE, setting.CARACTER))
                break


    def _options_create(self):
        while True:
            try:
                os.system ("cls") 
                com.view_message(Create_contact.is_view, Create_contact.is_message) 
                self._name = com.varify_name('CREAR CONTACTO').strip()
                self._number = int(input('Número: '))
                Create_contact.is_view = False
                break
            except Exception as e:
                Create_contact.is_view = True
                Create_contact.is_message = 'Introduce solo números'

        db().create_contact(self._name, self._number)
        Create_contact.is_view = True
        Create_contact.is_message = 'Contacto creado con exito'

    def _view_welcome(sefl):
        os.system ("cls")
        com.view_message(Create_contact.is_view, Create_contact.is_message)
        print('Nuevo cotacto'.center(setting.SPACE, setting.CARACTER))
        print('\n* Crear contacto | Presione 1\n* Regresar       | Presione 0\n')
        Create_contact.is_view = False
