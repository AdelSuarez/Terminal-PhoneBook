from db.DataBase import DataBase

class Create_contact:
    def __init__(self):
        self.create()


    def create(self):
        '''   
            observation: two loops are created for each input, so that when the 
            number is incorrectly entered it does not start from the name
        '''
        while True:
            self.name = input('Nombre: ')
            if (len(self.name) == 0):
                print('*Por Favor introduce un nombre*')
                continue
            break
        while True:
            try: 
                self.number = int(input('Número: '))
                break
            except ValueError:
                print('*Introduce solo números*')

        self._parameters = (self.name.strip(), self.number)
        self._query = 'INSERT INTO CONTACTOS VALUES(?,?)'
        DataBase(self._query,self._parameters)

    def __repr__(self) -> str:
        return f'''
    * Contacto creado con éxito *
    Nombre: {self.name} | Número: {self.number}
        '''
