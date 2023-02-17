from components.components import Components
import settings.settings as setting
import os


class View_contacts:

	def contacts(self):
		os.system ("cls")
		while True:
			if Components.all_contacts() != []:
				print('\n	*AGENDA*')
				for name, number in Components.all_contacts():
					print(f'Nombre: {name} | Número: {number}')

			else:	
				setting.message_empty_calendar()
			try:
				go_back = int(input('\n0 para regresa >> '))
				if go_back != 0:
					os.system ("cls")
					print('Opción incorrecta'.center(setting.SPACE, setting.CARACTER))
					continue
				os.system ("cls")
				break
			except ValueError:
				os.system ("cls")
				print('Introduce solo números'.center(setting.SPACE, setting.CARACTER))



