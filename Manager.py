from view import Create_contact, View_contacts, Delete_contact, Edit_contact, view_main
from settings import clear
from view.view import View

class Manager(View):
    def __init__(self, is_view = False, is_message = '', type_message = '') -> None:
        super().__init__(is_view, is_message, type_message)

    def manager(self):

        while True:
            self.option = view_main.ViewMain(self.is_view, self.is_message, self.type_message).views_main()

            if self.option == 1:
                Create_contact.CreateContact(self.is_view, self.is_message, self.type_message).view_new_contact()

            elif self.option == 2:
                View_contacts.ViewContacts().all_contacts()

            elif self.option == 3:
                clear.Clear()
                Delete_contact.DeleteContact(self.is_view, self.is_message, self.type_message).delete()

            elif self.option == 4:
                Edit_contact.EditContact(self.is_view, self.is_message, self.type_message).mian_edit()

            elif self.option == 0:
                break



