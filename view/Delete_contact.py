from db.DataBase import DataBase as db
from components import name_checker, message
from settings import settings, clear
from . import view

class DeleteContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def delete(self):
        if db().all_contacts() != []:

            while True:
                while True:
                    if ViewOptionsDeleteContact(self.is_view, self.is_message).options_delete():
                        self.is_view = False
                    try:
                        self._option = int(input('Introduce la opcion >> '))
                        if not(0 <= self._option < 2 ):
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
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def options_delete(self):
        clear.Clear()
        message.Message(self.is_view, self.is_message)
        print('Borrar cotacto'.center(settings.SPACE, settings.CARACTER))
        print('\n* Borrar contacto | Presione 1\n* Regresar        | Presione 0\n')
        return True


class ViewDeleteContact(view.View):
    def __init__(self, is_view, is_message) -> None:
        super().__init__(is_view, is_message)

    def delete_contact(self):
        while True:
            if db().all_contacts() != []:
                clear.Clear()
                message.Message(self.is_view, self.is_message)
                self.name = name_checker.NameChecker.name_checker('BORRAR CONTACTO').strip()
                
                if db().search_name_db(self.name) != []:
                    db().delete_contact((self.name, ))
                    return True
                else:
                    self.is_view = True
                    self.is_message = 'No existe el contacto'

            else:
                settings.message_empty_calendar()


        
