import sqlite3 as sql

class DataBase:
    def __init__(self, query, parameters = ()):
        self._query = query
        self._parameters = parameters
        self._database = 'DataBase.db'
        self.db()

    def db(self):
        self.conn = sql.connect(self._database)
        self.cur = self.conn.cursor()
        result =  self.cur.execute(self._query, self._parameters)
        self.conn.commit()
        return result

    def fetchall(self):
        return self.db().fetchall()


    