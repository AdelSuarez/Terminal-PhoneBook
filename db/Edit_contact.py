from db.DataBase import DataBase
from components.components import Components

class Edit_contact:
    def __init__(self):
        self.edit()

    def edit(self):
        if Components.all_contacts() != []:
            while True:
                print('''
                *OPCION EDITAR*
        * Editar Nombre | Presione 1
        * Editar Número | Presione 2
        * Regresar      | Presione 0
                ''')
                while True:
                    try:
                        self.option = int(input('Introduce la opcion: '))
                        if not(-1 < self.option < 3):
                            print('*Opción incorrecta*')
                            continue
                        break
                    except ValueError:
                        print('*Introduce solo números*')

                if self.option == 1:
                    self.edit_name()

                elif self.option == 2:
                    self.edit_number()
                    
                elif self.option == 0:
                    break
        else:
            print('\n     *Agenda* \n-vacía-')



    def edit_name(self):
        while True:
            print('')
            self.name = Components.varify_name().strip()

            if Components.search_name(self.name) != []:
                while True:
                    self.new_name = input('Introduce el nuevo nombre: ')
                    if (len(self.new_name) == 0):
                        print('*Por Favor introduce el nombre')
                        continue
                    break

                self._parameters = (self.new_name.strip(), self.name)
                self._query = 'UPDATE CONTACTOS SET NOMBRE = ? WHERE NOMBRE = ?'
                DataBase(self._query, self._parameters)
                print('\n*Contacto actualizado con éxito*')
                break
            else:
                print('\n*No existe el contacto*')

    def edit_number(self):
        while True:
            print('')
            self.name = Components.varify_name().strip()

            if Components.search_name(self.name) != []:
                while True:
                    try:
                        self.new_number = int(input('Introduce el nuevo número: '))
                        break
                    except ValueError:
                        print('*Se a producido un error*')

                self._parameters = (self.new_number, self.name)
                self._query = 'UPDATE CONTACTOS SET NUMERO = ? WHERE NOMBRE = ?'
                DataBase(self._query, self._parameters)
                print('\n*Contacto actualizado con éxito*')
                break

            else:
                print('\n*No existe el contacto*')