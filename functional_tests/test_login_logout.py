from .base import FunctionalTest
from django.contrib.auth.models import User
# from selenium.webdriver.common.keys import Keys
import time


class LoginTest(FunctionalTest):

    #Required to get to the registration page
    def set_up_database_and_get_to_login_page(self):
        self.generate_two_questions()
        User.objects.create_user('testusr', 'testemail',
            'testpswd')
        loginurl = self.server_url + '/login/'
        return self.browser.get(loginurl)

    # User gets to the login pages and types in the wrong credentials
    def test_wrong_login(self):
        self.set_up_database_and_get_to_login_page()
        inputbox = self.browser.find_element_by_name('username')
        inputbox.send_keys('wrongusr')
        inputbox = self.browser.find_element_by_name('password')
        inputbox.send_keys('wrongpswd')
        self.browser.find_element_by_name('submit').click()
        # time.sleep(10)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Invalid login', page_text)

    def test_correct_login(self):
        self.set_up_database_and_get_to_login_page()
        inputbox = self.browser.find_element_by_name('username')
        inputbox.send_keys('testusr')
        inputbox = self.browser.find_element_by_name('password')
        inputbox.send_keys('testpswd')
        self.browser.find_element_by_name('submit').click()
        # time.sleep(10)

        current_url = self.browser.current_url
        self.assertRegex(current_url, '.+/questions/1/')
