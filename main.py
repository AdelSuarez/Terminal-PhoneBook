from Manager import Manager
from db.DataBase import DataBase
from settings import clear

query = '''CREATE TABLE IF NOT EXISTS CONTACT (
				ID INTEGER,
				NAME TEXT NOT NULL, 
				NUMBER INTEGER NOT NULL,
				PRIMARY KEY("ID" AUTOINCREMENT)
			)'''

if __name__ == '__main__':
	clear.Clear()
	DataBase( ).connect_db(query,)
	Manager().manager()