from settings import settings, clear
from db.DataBase import DataBase as db


class ViewContacts:

	def all_contacts(self):
		clear.Clear()
		a = True
		while a:
			all_contacts = db().all_contacts()
				
			try:
				if all_contacts != []:
					self.view_all_contacts( all_contacts)

				else:	
					settings.view_empty_agenda()

				go_back = int(input('| 0 para regresar >> '))
				if go_back != 0:
					clear.Clear()
					print('Opción incorrecta'.center(settings.SPACE, settings.CARACTER))
					continue
				clear.Clear()
				break

			except ValueError:
				clear.Clear()
				print('Introduce solo números'.center(settings.SPACE, settings.CARACTER))



	def view_all_contacts(self, database ):
		print("+--------------------------------------+")
		print("|               AGENDA                 |")
		print("+----+--------------------+------------+")
		print("|ID  |Nombre              |Número      |")
		print("+----+--------------------+------------+")

		for id, name, number in database:
			print("|{:<4}|{:<20}|{:<12}|".format(id,name, number))

		print("+----+--------------------+------------+")




