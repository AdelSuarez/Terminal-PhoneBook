class View:
    def __init__(self, is_view, is_message) -> None:
        self.is_view = is_view
        self.is_message = is_message

    def view_option_menu(self, options):
        print("+-----------------------+--------------+")

        for command, description in options.items():
            print('| {:<22}| {:<12} |'.format(description,command))
            
        print("+-----------------------+--------------+")
        