from db.DataBase import DataBase
from components.components import Components

class Create_contact:
    def __init__(self):
        self.create()


    def create(self):

        self.name = Components.varify_name().strip()
        
        while True:
            try: 
                self.number = int(input('Número: '))
                break
            except ValueError:
                print('*Introduce solo números*')

        self._parameters = (self.name, self.number)
        self._query = 'INSERT INTO CONTACTOS VALUES(?,?)'
        DataBase(self._query,self._parameters)

    def __repr__(self) -> str:
        return f'\n* Contacto creado con éxito *\nNombre: {self.name} | Número: {self.number}'
