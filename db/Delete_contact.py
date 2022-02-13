from db.DataBase import DataBase
from components.components import Components

class Delete_contact:
    def __init__(self):
        self.delete()

    def delete(self):
        while True:
            if Components.all_contacts() != []:

                print('\n     *BORRAR CONTACTO*')
                self.name = Components.varify_name().strip()
                
                if Components.search_name(self.name) != []:
                    self._query = 'DELETE FROM CONTACTOS WHERE NOMBRE=?'
                    DataBase(self._query, (self.name, ))
                    print('\n *Contacto borrado con éxito*')
                    break
                else:
                    print('*No existe el contacto*')

            else:
                print('\n     *Agenda* \n-vacia-')
                break


        
