from unittest import skip
from .base import ToDoFunctionalTest

class ItemValidationTest(ToDoFunctionalTest):

    def test_cannot_add_empty_list_item(self):
        #Ella goes to the home page
        #and accidentally enters an empty list item
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        #the home page refreshes and there is an error messages
        #saying the the list item cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #she tries to enter a second blank item again
        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('1: Buy milk')

        self.enter_a_new_item('')

        #she recives a similar wanring on the list page.
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # self.enter_a_new_item('make tea')

        #And she can correct it but filling in the blakn
        # self.fail('Finish the test!')
