import sqlite3 as sql

class DataBase:
    def __init__(self, db = 'DataBase.db'):
        self.database = db

    def connect_db(self, query, parameters = (),):
        with sql.connect(self.database) as conn:
            self.cur = conn.cursor()
            result =  self.cur.execute(query, parameters)
            conn.commit()
        return result

    def fetchall(self):
        return self.connect_db().fetchall()

    def create_contact(self, name, number):
        parameters = (name, number)
        query = 'INSERT INTO CONTACT VALUES(NULL,?,?)'
        self.connect_db(query, parameters)

    def delete_contact_name(self, parameters):
        query = 'DELETE FROM CONTACT WHERE name LIKE ?'
        self.connect_db(query, parameters)

    def delete_contact_id(self, parameters):
        query = 'DELETE FROM CONTACT WHERE id=?'
        self.connect_db(query, parameters)

    def all_contacts(self):
        query = 'SELECT * FROM CONTACT ORDER BY name'
        return  self.connect_db(query, ).fetchall()

    def search_name_db(self, name):
        parameters = (name, )
        query = 'SELECT * FROM CONTACT WHERE name LIKE ?'
        return self.connect_db(query, parameters).fetchall()

    def update_name(self, parameters):
        query = 'UPDATE CONTACT SET name = ? WHERE name = ?'
        self.connect_db(query, parameters)

    def update_number(self, parameters):
        query = 'UPDATE CONTACT SET number = ? WHERE name = ?'
        self.connect_db(query, parameters)


