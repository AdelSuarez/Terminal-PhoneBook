import os
from db.DataBase import DataBase
from components.components import Components
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
                os.system ("cls") 
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
                Components.view_message(Create_contact.is_view, Create_contact.is_message) 
                self._name = Components.varify_name().strip()
                self._number = int(input('Número: '))
                Create_contact.is_view = False
                break
            except ValueError:
                Create_contact.is_view = True
                Create_contact.is_message = 'Introduce solo números'

        self._createUser(self._name, self._number)
        print('Contacto creado con éxito'.center(setting.SPACE, setting.CARACTER))
        print(f'Nombre: {self._name} | Número: {self._number}\n')

    def _view_welcome(sefl):
        os.system ("cls") 
        Components.view_message(Create_contact.is_view, Create_contact.is_message)
        print('Nuevo cotacto'.center(setting.SPACE, setting.CARACTER))
        print('\n* Crear contacto | Presione 1\n* Regresar       | Presione 0\n')
        Create_contact.is_view = False

    def _createUser(self, name, number):
        self._parameters = (name, number)
        self._query = 'INSERT INTO CONTACT VALUES(?,?)'
        DataBase(self._query,self._parameters).db()
        os.system ("cls") 


