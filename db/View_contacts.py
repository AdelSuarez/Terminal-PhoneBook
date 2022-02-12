from db.DataBase import DataBase

class View_contacts:
	def __init__(self):
		self.contacts()

	def contacts(self):
		self._query = 'SELECT * FROM CONTACTOS'
		self._result = DataBase(self._query, ).fetchall()

		if self._result != []:
			print('\n		*AGENDA*')
			for name, number in self._result:
				print(f'Nombre: {name} | Número: {number}')
				
		else:	
			print('\n		*AGENDA* \n-Vacía-')



