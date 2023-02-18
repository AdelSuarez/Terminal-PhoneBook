import os
from db.DataBase import DataBase as db
from components.components import Components as com
import settings.settings as setting


class Edit_contact:
    is_view = False
    is_message = ''

    def __init__(self):
        self._mian_edit()

    def _mian_edit(self):
        Edit_contact.is_view = False
        if db().all_contacts() != []:
            while True:
                while True:
                    self._view_welcome()
                    try:
                        self._option = int(input('Introduce la opcion >> '))
                        if not(0 <= self._option < 3):
                            Edit_contact.is_view = True
                            Edit_contact.is_message = 'Opción incorrecta'
                            continue
                        break
                    except ValueError:
                        Edit_contact.is_view = True
                        Edit_contact.is_message = 'Introduce solo números'

                if self._option == 1:
                    self._edit_name()

                elif self._option == 2:
                    self._edit_number()
                    
                elif self._option == 0:
                    os.system ("cls")
                    break
        else:
            os.system ("cls")
            setting.message_empty_calendar()




    def _edit_name(self):
        Edit_contact.is_view = False
        while True:
            os.system ("cls")
            com.view_message(Edit_contact.is_view, Edit_contact.is_message)
            self._name = com.varify_name('EDITAR NOMBRE').strip()

            if db().search_name_db(self._name) != []:
                is_corret = False
                Edit_contact.is_view = False
                while True:
                    if Edit_contact.is_view:
                        os.system ("cls")
                        com.view_message(Edit_contact.is_view, Edit_contact.is_message)

                    print('Introduce el nuevo nombre:')
                    self._new_name = input('>> ')
                    if (len(self._new_name) == 0):
                        Edit_contact.is_view = True
                        Edit_contact.is_message = 'Por Favor introduce el nombre'
                        break
                    is_corret = True
                    break

                if is_corret:
                    self._parameters = (self._new_name.strip(), self._name)
                    db().update_name(self._parameters)
                    Edit_contact.is_view = True
                    Edit_contact.is_message = 'Nombre actualizado con exito'
                    break
            else:
                Edit_contact.is_view = True
                Edit_contact.is_message = 'No existe el contacto'

    def _edit_number(self):
        is_corret = False

        Edit_contact.is_view = False
        while True:
            os.system ("cls")
            com.view_message(Edit_contact.is_view, Edit_contact.is_message)
            self._name = com.varify_name('EDITAR NUMERO').strip()
            if db().search_name_db(self._name) != []:
                Edit_contact.is_view = False
                while True:
                    if Edit_contact.is_view:
                        os.system ("cls")
                        com.view_message(Edit_contact.is_view, Edit_contact.is_message)
                    try:
                        print('Introduce el nuevo número:')
                        self._new_number = int(input('>> '))
                        is_corret = True
                        break
                    except Exception:
                        Edit_contact.is_view = True
                        Edit_contact.is_message = 'Introduce un numero'
                        break


                if is_corret:
                    self._parameters = (self._new_number, self._name)
                    db().update_number(self._parameters)
                    Edit_contact.is_view = True
                    Edit_contact.is_message = 'Número actualizado con exito'
                    break

            else:
                Edit_contact.is_view = True
                Edit_contact.is_message = 'No existe el contacto'

    def _view_welcome(sefl):
        os.system ("cls")
        com.view_message(Edit_contact.is_view, Edit_contact.is_message)
        print('Editar contacto'.center(setting.SPACE, setting.CARACTER))
        print('\n* Editar Nombre | Presione 1\n* Editar Número | Presione 2\n* Regresar      | Presione 0\n')