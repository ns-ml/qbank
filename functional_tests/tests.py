from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest
import time
from qanda.models import Question, Answer, Explanation, Reference
import sys

class NewVisitorTest(StaticLiveServerTestCase):
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

# Student arrives at qbank website and notices how nice it looks awesome

	def test_layout_and_styling(self):
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		inputbox = self.browser.find_element_by_id('submit_id')
		self.assertAlmostEqual(
			inputbox.size['width'], 224, delta=5
			)

	def test_can_show_a_question(self):
		self.browser.get(self.server_url)
		self.assertIn('Neurosurgery', self.browser.title)
		
# Background database setup
		first_question = Question.objects.create(text="question #1: This is the first question ever")
		Answer.objects.create(text="Answer #1 (correct)", question=first_question, correct=True)
		Answer.objects.create(text="Answer 2 (incorrect)", question=first_question, correct=False)
		Explanation.objects.create(text="Explanation for question #1", question=first_question)
		Reference.objects.create(text="Reference #1", question=first_question)

		second_question = Question.objects.create(text="Question #2: El secundo")
		Answer.objects.create(text="Second question answer #1", question=second_question, correct=True)
		Answer.objects.create(text="Second question answer #2", question=second_question, correct=False)
		Explanation.objects.create(text="Explanation for question #2", question=second_question)



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


# Click on next button, which has been enabled
		self.browser.find_element_by_id("submit_id").click()
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Question #2', page_text)
# Student moves on to the next question
		self.fail('Finish the test')