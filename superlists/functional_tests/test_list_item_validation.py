from unittest import skip
from .base import ToDoFunctionalTest

class ItemValidationTest(ToDoFunctionalTest):
    @skip("Haven't implemented this yet")
    def test_cannot_add_empty_list_item(self):
        #Ella goes to the home page
        #and accidentally enters an empty list item

        #the home page refreshes and there is an error messages
        #saying the the list item cannot be blank

        #she tries to enter a second blank item again

        #she recives a similar wanring on the list page.

        #And she can correct it but filling in the blakn
        self.fail('Finish the test!')
