from db.DataBase import DataBase
from db.Delete_contact import Delete_contact

class Edit_contact:
    def __init__(self):
        self.edit()

    def edit(self):
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
                        print('*Opcion incorrecta*')
                        continue
                    break
                except ValueError as e:
                    print('*Introduce solo números*')

            if self.option == 1:
                self.edit_name()

            elif self.option == 2:
                self.edit_number()
                
            elif self.option == 0:
                break


    def validation_name(self):
        while True:
            name = input('Introduce el nombre: ')
            if (len(name) == 0):
                print('*Por Favor introduce el nombre')
                continue
            break
        return name

    def edit_name(self):
        while True:
            print('')
            self.name = self.validation_name()

            n =  Delete_contact.search(self, self.name.strip())

            if n != []:
                while True:
                    self.new_name = input('Introduce el nuevo nombre: ')
                    if (len(self.new_name) == 0):
                        print('*Por Favor introduce el nombre')
                        continue
                    break

                self._parameters = (self.new_name.strip(), self.name.strip())
                self._query = 'UPDATE CONTACTOS SET NOMBRE = ? WHERE NOMBRE = ?'
                DataBase(self._query, self._parameters)
                print('')
                print('*Contacto actualizado con éxito*')
                break
            elif n == []:
                print('')
                print('*No existe el contacto*')

    def edit_number(self):
        while True:
            print('')
            self.name = self.validation_name()

            n = Delete_contact.search(self, self.name.strip())
            if n != []:
                while True:
                    try:
                        self.new_number = int(input('Introduce el nuevo numero: '))
                        break
                    except ValueError as e:
                        print('*Se a producido un error*')

                self._parameters = (self.new_number, self.name.strip())
                self._query = 'UPDATE CONTACTOS SET NUMERO = ? WHERE NOMBRE = ?'
                DataBase(self._query, self._parameters)
                print('')
                print('*Contacto actualizado con éxito*')
                break

            elif n == []:
                print('')
                print('*No existe el contacto*')