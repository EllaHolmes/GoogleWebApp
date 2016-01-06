from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text , [row.text for row in rows])

    def enter_a_new_item(self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(todo_text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Ella goes to check out a cool new website
        #She goes to the home page
        self.browser.get(self.live_server_url)

        #She notices the the page title and the header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #she is inivted to enter a to-do list item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #she types water the plants into a text box

        self.enter_a_new_item('Water the plants')

        ella_list_url = self.browser.current_url
        self.assertRegexpMatches(ella_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Water the plants')

        #There is still a text box prompting Ella to enter in another item
        #she enters "Run a mile" into the text box and presses enter
        self.enter_a_new_item('Run a mile')

        #the homepage refreshed again and displays both items on her list
        self.check_for_row_in_list_table('1: Water the plants')
        self.check_for_row_in_list_table('2: Run a mile')

        #now a new user, Oren comes along,

        ##We use a new browser session to make sure no information
        ##of Ella's comes along (eg. cookies, localSrotage)
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        self.browser = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Water the plants', page_text)
        self.assertNotIn('Run a mile', page_text)

        #he starts a new list by entering an item
        self.enter_a_new_item('Buy milk')

        #oren gets his own url
        oren_list_url = self.browser.current_url
        self.assertRegexpMatches(oren_list_url, '/lists/.+')
        self.assertNotEqual(oren_list_url, ella_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Water the plants', page_text)
        self.assertIn('Buy milk', page_text)
