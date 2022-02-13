from components.components import Components

class View_contacts:
	def __init__(self):
		self.contacts()

	def contacts(self):

		if Components.all_contacts() != []:
			print('\n		*AGENDA*')
			for name, number in Components.all_contacts():
				print(f'Nombre: {name} | Número: {number}')

		else:	
			print('\n		*AGENDA* \n-Vacía-')



