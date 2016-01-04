from selenium import webdriver

#Ella goes to check out a cool new website
#She goes to the home page
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#She notices the the page title and the header mention to-do lists.
assert 'To-Do' in browser.title

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
