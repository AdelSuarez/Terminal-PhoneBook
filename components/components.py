from db.DataBase import DataBase
import settings.settings as setting

class Components:

    def varify_name():
            while True:
                print('Introduce el nombre del contacto')
                name = input('Nombre: ')
                if (len(name) == 0):

                    print('Por Favor introduce el nombre'.center(setting.SPACE, setting.CARACTER))
                    print('')
                    continue
                break
            return name

    def view_message(is_view, is_message):
        if is_view:
            print(is_message.center(setting.SPACE, setting.CARACTER))

            
