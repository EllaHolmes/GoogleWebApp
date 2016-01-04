from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Ella goes to check out a cool new website
        #She goes to the home page

        self.browser.get('http://localhost:8000')

        #She notices the the page title and the header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)

        #she is inivted to enter a to-do list item straight away

        #she types water the plants into a text box

        #when she hits enter the page refreashes and displays a list
        # "1 : Water the plants"

        #There is still a text box prompting Ella to enter in another item
        #she enters "Run a mile" into the text box and presses enter

        #the homepage refreshed again and displays both items on her list

        #eidith realizes that there is a unique URL for her

        # she revisits this URL and her todo list is still there

        #happy, Ella goes back to watching protlandia

if __name__ == '__main__':
    unittest.main()
