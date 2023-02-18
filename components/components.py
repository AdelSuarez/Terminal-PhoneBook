import os
import settings.settings as setting

class Components:
    is_view = False
    is_message = ''

    def varify_name(title=''):
        while True:

            if Components.is_view:
                os.system ("cls") 
            Components.view_message(Components.is_view, Components.is_message)

            if title != '':
                print(title.center(setting.SPACE, setting.CARACTER))

            print('Introduce el nombre del contacto')
            name = input('Nombre: ')
            
            if (len(name) == 0):
                Components.is_view = True
                Components.is_message = 'Por Favor introduce el nombre'
                continue
            break
        Components.is_view = False

        return name

    def view_message(is_view, is_message):
        if is_view:
            print(is_message.center(setting.SPACE, setting.CARACTER))

            
