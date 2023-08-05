from view.Create_contact import CreateContact
from view.View_contacts import ViewContacts
from view.Delete_contact import DeleteContact
from view.Edit_contact import Edit_contact
from view import view_main



class Manager:

    def manager(self):

        while True:
            self.option = view_main.ViewMain().views_main()

            #for option, view in views.items():
                #if self.option == option:
                 #   print(view)   

            if self.option == 1:
                CreateContact().view_new_contact()

            elif self.option == 2:
                ViewContacts().contacts()

            elif self.option == 3:
                DeleteContact().delete()

            elif self.option == 4:
                Edit_contact()

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


