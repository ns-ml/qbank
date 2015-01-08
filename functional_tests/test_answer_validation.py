from .base import FunctionalTest
from qanda.views import WRONG_ANSWER_ERROR
from selenium.webdriver.common.keys import Keys
from qanda.models import Question
import time

class AnswerValidationTest(FunctionalTest):
	def set_up_database_and_get_to_qanda_page(self):
		self.generate_two_questions()
		qandaurl = self.server_url + '/questions/%d/' % (Question.objects.first().id)
		return self.browser.get(qandaurl)
	
	def test_shows_error_message_with_wrong_answer(self):
		self.set_up_database_and_get_to_qanda_page()
		#wrong answer is picked
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		inputbox.send_keys(Keys.DOWN)
		
		self.browser.find_element_by_id("submit_id").click()

		#Error message appears
		error = self.get_error_element()
		self.assertEqual(error.text, WRONG_ANSWER_ERROR)

	def test_error_messages_clear_with_mouse_click(self):
		self.set_up_database_and_get_to_qanda_page()
		
		#wrong answer is picked
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		inputbox.send_keys(Keys.DOWN)
		
		self.browser.find_element_by_id("submit_id").click()
		error = self.get_error_element()
		self.assertTrue(error.is_displayed())

		#user clicks on any answer choice
		self.browser.find_element_by_tag_name('input').click()
		error = self.get_error_element()
		#error message disappears
		self.assertFalse(error.is_displayed())

