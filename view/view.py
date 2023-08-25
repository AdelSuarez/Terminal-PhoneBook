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
    
        