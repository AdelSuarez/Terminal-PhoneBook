import os
from Manager import Manager
from db.DataBase import DataBase
import settings.settings as setting

query = 'CREATE TABLE IF NOT EXISTS CONTACT (NAME TEXT, NUMBER INTEGER)'
if __name__ == '__main__':
	os.system ("cls")
	DataBase(query, ).db()
	Manager()