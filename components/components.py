from db.DataBase import DataBase

class Components:
    def varify_name():
            while True:
                name = input('Nombre: ')
                if (len(name) == 0):
                    print('\n*Por Favor introduce el nombre')
                    continue
                break
            return name

    def search_name(contact):
        parameters = (contact, )
        query = 'SELECT * FROM CONTACTOS WHERE NOMBRE=?'
        return DataBase(query, parameters ).fetchall()

    def all_contacts():
        query = 'SELECT * FROM CONTACTOS'
        return DataBase(query, ).fetchall()
