from db.DataBase import DataBase
from db.Create_contact import Create_contact
from db.View_contacts import View_contacts
from db.Delete_contact import Delete_contact
from db.Edit_contact import Edit_contact

class Manager:
    def __init__(self):
        self.views()

    def views(self):
        print('''        *********************
        *AGENDA DE CONTACTOS*
        *********************''')
        while True:
            print('''
            *OPCIONES*
    * Crear agenda nueva | Presione 1
    * Crear contacto     | presione 2
    * Ver contactos      | Presione 3
    * Borrar contacto    | Presione 4
    * Editar contacto    | Presione 5
    * Salir              | Presione 0
        ''')
            while True:
                try:
                    option = int(input('Selecciona una opción: '))
                    if not(-1 < option < 6):
                        print('Opcion incorrecta')
                        continue
                    break
                except ValueError:
                    print('*Introduce solo números*')


            if option == 1:
                try:
                    self.create_agenda()
                except:
                    print('\n*Ya existe una agenda*')

            elif option == 2:
                contact = Create_contact()
                print(repr(contact))

            elif option == 3:
                View_contacts()

            elif option == 4:
                Delete_contact()

            elif option == 5:
                Edit_contact()

            elif option == 0:
                break


    def create_agenda(self):
        self._query = 'CREATE TABLE CONTACTOS (NOMBRE VARCHAR(15), NUMERO INTEGER)'
        if DataBase(self._query, ):
            print('\n*Agenda creada*')