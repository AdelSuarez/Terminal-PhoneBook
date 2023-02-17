import os
from db.Create_contact import Create_contact
from db.View_contacts import View_contacts
from db.Delete_contact import Delete_contact
from db.Edit_contact import Edit_contact
import settings.settings as setting
from components.components import Components

class Manager:
    is_view = False
    is_message = '' 
    
    def __init__(self):
        self._views()

    def _views(self):

        self._view_welcome()

        while True:
            while True:
                self._view_options()
                try:
                    self._option = int(input('Selecciona una opción >> '))
                    if not(0 <= self._option < 6):
                        Manager.is_view = True
                        Manager.is_message = 'La opcion no existe'
                        os.system ("cls")
                        continue

                    break
                except ValueError:
                    Manager.is_view = True
                    Manager.is_message = 'Introduce solo números'
                    print('Introduce solo números'.center(setting.SPACE, setting.CARACTER))
                    os.system ("cls")


            if self._option == 1:
                Create_contact().create()

            elif self._option == 2:
                View_contacts().contacts()

            elif self._option == 3:
                Delete_contact().delete()

            elif self._option == 4:
                Edit_contact()

            elif self._option == 0:
                break


    def _view_welcome(self) -> None:
        print('')
        print(''.center(setting.SPACE, '*'))
        print(' AGENDA DE CONTACTOS '.center(setting.SPACE, '*'))
        print(''.center(setting.SPACE, '*'))
        print('')

    def _view_options(self) -> None:
        Components.view_message(Manager.is_view, Manager.is_message)
        print('Inicio'.center(setting.SPACE, setting.CARACTER))
        print('* Crear contacto     | presione 1\n* Ver contactos      | Presione 2\n* Borrar contacto    | Presione 3\n* Editar contacto    | Presione 4\n* Salir              | Presione 0\n')
        Manager.is_view = False

