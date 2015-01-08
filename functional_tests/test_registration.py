from .base import FunctionalTest
# from selenium.webdriver.common.keys import Keys
# import time


class RegistrationTest(FunctionalTest):

    #Required to get to the registration page
    def set_up_database_and_get_to_registration_page(self):
        self.generate_two_questions()
        registerurl = self.server_url + '/register/'
        return self.browser.get(registerurl)

    def test_registration_setup(self):
    #User arrives at the registration page
        self.set_up_database_and_get_to_registration_page()
        current_url = self.browser.current_url
        self.assertRegex(current_url, ".+/register/")

    #User enters all her information
    def test_data_input(self):
        self.set_up_database_and_get_to_registration_page()
        inputbox = self.browser.find_element_by_id("id_username")
        inputbox.send_keys('test')
        inputbox = self.browser.find_element_by_id("id_email")
        inputbox.send_keys('test@test.com')
        inputbox = self.browser.find_element_by_id("id_password")
        inputbox.send_keys('testing')
        inputbox = self.browser.find_element_by_id("id_program")
        inputbox.send_keys('test program')
        # time.sleep(10)

        self.browser.find_element_by_name('submit').click()

        page_text = self.browser.find_element_by_tag_name('strong').text
        self.assertEqual(page_text, 'Thank you for registering!')
