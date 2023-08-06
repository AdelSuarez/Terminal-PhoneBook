from Manager import Manager
from db.DataBase import DataBase
from settings import clear

query = '''CREATE TABLE IF NOT EXISTS CONTACT (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME TEXT NOT NULL, 
			NUMBER INTEGER NOT NULL)'''

if __name__ == '__main__':
	clear.Clear()
	DataBase( ).connect_db(query,)
	Manager().manager()