import sqlite3 as sql

class DataBase:
    def __init__(self, db = 'DataBase.db'):
        self.database : str = db

    def connect_db(self, query : str, parameters : tuple = (),):
       # Make the connection according to he query you want to make  
        with sql.connect(self.database) as conn:
            cur = conn.cursor()
            result =  cur.execute(query, parameters)
            conn.commit()
        return result


    # CREATE
    def create_contact(self, name : str, number : int):
        self.connect_db('INSERT INTO CONTACT VALUES(NULL,?,?)', (name, number))

    # DELETE
    def delete_contact_name(self, name : str):
        self.connect_db('DELETE FROM CONTACT WHERE name LIKE ?', (name,))

    def delete_contact_id(self, id : int):
        self.connect_db('DELETE FROM CONTACT WHERE id=?', (id,))

    # VIEW
    def all_contacts(self):
        return  self.connect_db('SELECT * FROM CONTACT ORDER BY name, id', ).fetchall()

    # SEARCH
    def search_name_db(self, name : str):
        return self.connect_db('SELECT * FROM CONTACT WHERE name LIKE ?', (name, )).fetchall()
    
    def search_id_db(self, name : str):
        return self.connect_db('SELECT * FROM CONTACT WHERE id=?', (name, )).fetchall()

    # UPDATE
    def update_name(self, new_name : str, name : str):
        self.connect_db('UPDATE CONTACT SET name = ? WHERE name = ?', (new_name, name))

    def update_name_id(self, new_name : str, id : int):
        self.connect_db('UPDATE CONTACT SET name = ? WHERE id = ?', (new_name, id))

    def update_number(self, new_number : int, name : str):
        self.connect_db('UPDATE CONTACT SET number = ? WHERE name = ?', (new_number, name))

    def update_number_id(self, parameters):
        self.connect_db('UPDATE CONTACT SET number = ? WHERE id = ?', parameters)
