import os
from Manager import Manager
from db.DataBase import DataBase

query = 'CREATE TABLE IF NOT EXISTS CONTACT (NAME TEXT, NUMBER INTEGER)'
if __name__ == '__main__':
	os.system ("cls")
	DataBase( ).connect_db(query,)
	Manager()