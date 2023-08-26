from components import message
from settings import clear

class View:
    def __init__(self, is_view, is_message, type_message) -> None:
        self.is_view : bool = is_view
        self.is_message : str = is_message
        self.type_message : str = type_message

    def view_option_menu(self, options):
        print("+-----------------------+--------------+")

        for command, description in options.items():
            print('| {:<22}| {:<12} |'.format(description,command))
            
        print("+-----------------------+--------------+")

    def message_variables(self, view : bool , message : str, type : str):
        self.is_view = view
        self.is_message = message
        self.type_message = type
        

    def view_options_menu(self, options : dict, title : str) -> bool:
        clear.Clear()
        message.Message(self.is_view, self.is_message, self.type_message)
        
        print("+--------------------------------------+")
        print('|', end='')
        print(f'{title}'.center(38, ' '), end='')
        print('|')

        self.view_option_menu(options)

        return True
    
        