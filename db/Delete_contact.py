from db.DataBase import DataBase

class Delete_contact:
    def __init__(self):
        self.delete()

    def delete(self):
        while True:
            print('')
            print('     *BORRAR CONTACTO*')
            while True:
                self.name = input('Introduce el nombre: ')
                if (len(self.name) == 0):
                    print('*Por favor Introduce un nombre*')
                    continue
                break
            c = self.search(self.name.strip())
            if c != []:
                self._query = 'DELETE FROM CONTACTOS WHERE NOMBRE=?'
                DataBase(self._query, (self.name.strip(), ))
                print('')
                print(' *Contacto borrado con éxito*')
                break
            elif c == []:
                print('*No existe el contacto*')

    def search(self, e):
        self._parameters = (e, )
        self._query = 'SELECT * FROM CONTACTOS WHERE NOMBRE=?'
        return DataBase(self._query, self._parameters ).fetchall()

        
