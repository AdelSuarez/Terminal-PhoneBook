from view.Create_contact import CreateContact
from view.View_contacts import ViewContacts
from view.Delete_contact import DeleteContact
from view.Edit_contact import EditContact
from view import view_main
from settings import clear

class View:
    def __init__(self, is_view, is_message) -> None:
        self.is_view = is_view
        self.is_message = is_message

class Manager(View):
    def __init__(self, is_view = False, is_message = '') -> None:
        super().__init__(is_view, is_message)

    def manager(self):

        while True:
            self.option = view_main.ViewMain(self.is_view, self.is_message).views_main()

            #for option, view in views.items():
                #if self.option == option:
                 #   print(view)   

            if self.option == 1:
                CreateContact(self.is_view, self.is_message).view_new_contact()

            elif self.option == 2:
                ViewContacts().all_contacts()

            elif self.option == 3:
                clear.Clear()
                DeleteContact(self.is_view, self.is_message).delete()

            elif self.option == 4:
                EditContact(self.is_view, self.is_message).mian_edit()

            elif self.option == 0:
                break
#views = {1:CreateContact().view_new_contact(),
 #        2:View_contacts().contacts(),
  #       3:Delete_contact().delete(),
   #      4:Edit_contact(),
    #     }
views = {1:'1',
         2:'2',
         3:'3',
         4: '4'}


