from .base import ToDoFunctionalTest

class ManyListsTest(ToDoFunctionalTest):

    def change_list_name(self, new_name):
        pass

    def test_can_create_and_view_multiple_lists(self):
        #Edith comes to the home page, creates a new List
        #and fills in her grociery ListViewTest
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy milk')
        self.enter_a_new_item('Buy cheese')
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Buy cheese')

        #she sees that she can change list name
        self.change_list_name('Groceries')

        #Edith goes back to the home page and sees her grocery List
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')

        #Edith creates a new list for her art history HW
        self.browser.enter_a_new_item('Read Camille')

        #Edith opens the home page later and sees both Lists
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')
        self.check_for_row_in_list_table('Read Camille')

        #Edith goes to the grocery list and sees what she needs to buy
        row = self.find_table_row('Groceries')
        row.find_element_by_tag_name('a').click()
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Buy cheese')
        pass
