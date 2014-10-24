from base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from qanda.models import Question, Answer, Explanation, Reference

class NewVisitorTest(FunctionalTest):
# Background database setup
	def test_can_show_a_question(self):
		self.browser.get(self.server_url)
		
		first_question = Question.objects.create(text="question #1: This is the first question ever")
		Answer.objects.create(text="Answer #1 (correct)", question=first_question, correct=True)
		Answer.objects.create(text="Answer 2 (incorrect)", question=first_question, correct=False)
		Explanation.objects.create(text="Explanation for question #1", question=first_question)
		Reference.objects.create(text="Reference #1", question=first_question)
		first_question.save()

		second_question = Question.objects.create(text="Question #2: El secundo")
		Answer.objects.create(text="Second question answer #1", question=second_question, correct=True)
		Answer.objects.create(text="Second question answer #2", question=second_question, correct=False)
		Explanation.objects.create(text="Explanation for question #2", question=second_question)
		second_question.save()
# Student clicks the start button and is taken to the first question

		self.browser.find_element_by_id("submit_id").click()
		current_url = self.browser.current_url
		self.assertRegex(current_url, '.+/questions/1/')
		# time.sleep (20)

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