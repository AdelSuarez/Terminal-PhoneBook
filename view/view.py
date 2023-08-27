from components import message
from settings import clear

class View:
    # class whose function is to be inherited, in order to control messages and menus
    def __init__(self, is_view, is_message, type_message) -> None:
        self.is_view : bool = is_view
        self.is_message : str = is_message
        self.type_message : str = type_message

    def view_option_menu(self, options):
        # Function that prints the options menu on the console depending on the number of options provided by parameter
        print("+-----------------------+--------------+")

        for command, description in options.items():
            print('| {:<22}| {:<12} |'.format(description,command))
            
        print("+-----------------------+--------------+")

    def message_variables(self, view : bool , message : str, type : str):
        # Function that stores the variables used by the message component, to avoid calling the functions at all times
        self.is_view = view
        self.is_message = message
        self.type_message = type
        

    def view_options_menu(self, options : dict, title : str) -> bool:
        # Function that prints to the console the title of the selected view, and then calls the function that prints the options of that view
        clear.Clear()
        message.Message(self.is_view, self.is_message, self.type_message)
        
        print("+--------------------------------------+")
        print('|', end='')
        print(f'{title}'.center(38, ' '), end='')
        print('|')

        self.view_option_menu(options)

        return True
    
        