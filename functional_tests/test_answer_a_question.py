from base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from qanda.views import WRONG_ANSWER_ERROR

class NewVisitorTest(FunctionalTest):

# Background database setup
	def test_can_show_a_question(self):
		self.generate_two_questions()
		self.browser.get(self.server_url)
# Student clicks the start button and is taken to the first question
		
		self.browser.find_element_by_id("submit_id").click()
		current_url = self.browser.current_url
		self.assertRegex(current_url, '.+/questions/1/')
		

# A wild (first) question appears!

		question_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('question #1', question_text)

# # Two potential answers
# 		self.browser.get('/questions/%d/' % (first_question.id,))
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Answer #1', page_text)

# A first attempt at an answer is made, wrong answer!
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		inputbox.send_keys(Keys.DOWN)
		
		self.browser.find_element_by_id("submit_id").click()
		page_text = self.browser.find_element_by_tag_name('body').text

		error = self.get_error_element()
		self.assertEqual(error.text, WRONG_ANSWER_ERROR)
		self.assertIn('try again', page_text)
		
# A second attmept, correct answer. User is taken to the answer Explanation page
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		self.browser.find_element_by_id("submit_id").click()

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Explanation for question #1', page_text)

# Explanation page also includes a reference to the answer
		self.assertIn('Reference #1', page_text)

# Click on next button
		self.browser.find_element_by_id("submit_id").click()
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Question #2', page_text)
# Student moves on to the next question
		self.fail('Finish the test')