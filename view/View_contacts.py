from settings import settings, clear
from db.DataBase import DataBase as db


class ViewContacts:

	def contacts(self):
		clear.Clear()
		while True:
			if db().all_contacts() != []:
				print('AGENDA'.center(settings.SPACE, settings.CARACTER))
				print("+--------------------+------------+")
				print("|Nombre              |Número      |")
				print("+--------------------+------------+")

				for name, number in db().all_contacts():
					print("|{:<20}|{:<12}|".format(name, number))
					
				
				print("+--------------------+------------+")

			else:	
				settings.message_empty_calendar()
			try:
				go_back = int(input('\n0 para regresa >> '))
				if go_back != 0:
					clear.Clear()
					print('Opción incorrecta'.center(settings.SPACE, settings.CARACTER))
					continue
				clear.Clear()
				break
			except ValueError:
				clear.Clear()
				print('Introduce solo números'.center(settings.SPACE, settings.CARACTER))



