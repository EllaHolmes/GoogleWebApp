from .base import ToDoFunctionalTest
from selenium import webdriver

class DeleteItemsTest(ToDoFunctionalTest):

    def select_item_to_delete(self, delete_text):
        item_list = self.browser.find_element_by_id('id_list_table')
        items = item_list.find_elements_by_tag_name('tr')

        for item in items:
            if delete_text in item.text:
                #she then click the delete button
                item.find_element_by_tag_name('a').click()
                return


    def test_can_start_list_and_delete_items(self):
        #mary opens a new browser
        self.browser.get(self.live_server_url)

        # she enters in two items
        self.enter_a_new_item('Dont delete me')
        self.enter_a_new_item('Delete me')

        #we check if the items are there
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Dont delete me', page_text)
        self.assertIn('Delete me', page_text)

        #mary decides that she want to delete one item so she clicks
        #on the checkbox for 'delete me'
        self.select_item_to_delete('Delete me')

        #check if the item is there
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Dont delete me', page_text)
        self.assertNotIn('Delete me', page_text)
