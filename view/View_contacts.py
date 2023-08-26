from settings import settings, clear
from db.DataBase import DataBase as db
from . import view
from components import message

class ViewContacts(view.View):
	def __init__(self, is_view, is_message, type_message) -> None:
		super().__init__(is_view, is_message, type_message)

	def all_contacts(self):
		clear.Clear()
		while True:
			all_contacts = db().all_contacts()
				
			try:
				
				if all_contacts != []:
					self.view_all_contacts( all_contacts)

				else:	
					settings.view_empty_agenda()

				go_back = int(input('| 0 para regresar >> '))
				if go_back != 0:

					clear.Clear()
					self.message_variables(True, 'Opción incorrecta', 'warning')
					continue

				clear.Clear()
				break

			except ValueError:
				clear.Clear()
				self.message_variables(True, 'Introduce solo números', 'error')


	def view_all_contacts(self, database ):
		message.Message(self.is_view, self.is_message, self.type_message)
		print("+--------------------------------------+")
		print("|               AGENDA                 |")
		print("+----+--------------------+------------+")
		print("|ID  |Nombre              |Número      |")
		print("+----+--------------------+------------+")

		for id, name, number in database:
			print("|{:<4}|{:<20}|{:<12}|".format(id,name, number))

		print("+----+--------------------+------------+")




