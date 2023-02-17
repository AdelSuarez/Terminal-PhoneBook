from db.DataBase import DataBase
from components.components import Components
import settings.settings as setting


class Edit_contact:
    def __init__(self):
        self._mian_edit()

    def _mian_edit(self):
        if Components.all_contacts() != []:
            while True:
                print('Editar contacto'.center(setting.SPACE, setting.CARACTER))
                print('\n* Editar Nombre | Presione 1\n* Editar Número | Presione 2\n* Regresar      | Presione 0\n')
                while True:
                    try:
                        self._option = int(input('Introduce la opcion >> '))
                        if not(0 <= self._option < 3):
                            print('Opción incorrecta'.center(setting.SPACE, setting.CARACTER))
                            continue
                        break
                    except ValueError:
                        print('Introduce solo números'.center(setting.SPACE, setting.CARACTER))

                if self._option == 1:
                    self._edit_name()

                elif self._option == 2:
                    self._edit_number()
                    
                elif self._option == 0:
                    break
        else:
            setting.message_empty_calendar()




    def _edit_name(self):
        while True:
            print('')
            self._name = Components.varify_name().strip()

            if Components.search_name(self._name) != []:
                while True:
                    
                    self._new_name = input('Introduce el nuevo nombre >> ')
                    if (len(self._new_name) == 0):
                        print('Por Favor introduce el nombre'.center(setting.SPACE, setting.CARACTER))
                        continue
                    break

                self._parameters = (self._new_name.strip(), self._name)
                self._query = 'UPDATE CONTACT SET NAME = ? WHERE NAME = ?'
                self._database_process(self._query, self._parameters)
                break
            else:
                print('')
                print('No existe el contacto'.center(setting.SPACE, setting.CARACTER))

    def _edit_number(self):
        while True:
            print('')
            self._name = Components.varify_name().strip()

            if Components.search_name(self._name) != []:
                while True:
                    try:
                        self._new_number = int(input('Introduce el nuevo número >> '))
                        break
                    except ValueError:
                        print('*Se a producido un error*')

                self._parameters = (self._new_number, self._name)
                self._query = 'UPDATE CONTACT SET NUMBER = ? WHERE NAME = ?'
                self._database_process(self._query, self._parameters)
                break

            else:
                print('No existe el contacto'.center(setting.SPACE, setting.CARACTER))

    def _database_process(self, query, parameters):
        DataBase(query, parameters).db()
        print('')
        print('Contacto actualizado con éxito'.center(setting.SPACE, setting.CARACTER))
