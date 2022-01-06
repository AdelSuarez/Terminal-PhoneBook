from db.DataBase import DataBase

class View_contacts:
	def __init__(self):
		self.contacts()

	def contacts(self):
		self._query = 'SELECT * FROM CONTACTOS'
		self._result = DataBase(self._query, ).fetchall()

		if self._result != []:
			print('')
			print('		*AGENDA*')
			for name, number in self._result:
				print(f'Nombre: {name} | Número: {number}')
		else:
			print('')
			print('		*AGENDA*')
			print('-Vacía-')


