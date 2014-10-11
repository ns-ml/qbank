from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time
from qanda.models import Question, Answer, Explination

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

# Student arrives at qbank website

	def test_can_show_a_question(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Welcome to Q Bank', self.browser.title)

		first_question = Question.objects.create(text="Question #1: This is the first question ever")
		Answer.objects.create(text="Answer 1 (correct)", question=first_question, correct=True)
		Answer.objects.create(text="Answer 2 (incorrect)", question=first_question, correct=False)
		Explination.objects.create(text="Explination for question #1", question=first_question)

		second_question = Question.objects.create(text="Question #2: El secundo")
		Answer.objects.create(text="Second question answer #1", question=second_question, correct=True)
		Answer.objects.create(text="Second question answer #2", question=second_question, correct=False)
		Explination.objects.create(text="Explination for question #2", question=second_question)


# Student clicks the start button and is taken to the first question

		self.browser.find_element_by_id("submit").click()
		current_url = self.browser.current_url
		self.assertEqual(current_url, 'http://localhost:8081/questions/1/')
		# time.sleep (20)

# A wild (first) question appears!

		question_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Question #1', question_text)

# # Two potential answers
# 		self.browser.get('/questions/%d/' % (first_question.id,))
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Answer 1', page_text)

# A first attempt at an answer is made, wrong answer!
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		inputbox.send_keys(Keys.DOWN)
		
		self.browser.find_element_by_id("submit").click()
		page_text = self.browser.find_element_by_tag_name('body').text

		self.assertIn('try again', page_text)
		
# A second attmept, correct answer. User is taken to the answer explination page
		inputbox = self.browser.find_element_by_tag_name('input')
		inputbox.send_keys(Keys.TAB)
		inputbox.send_keys(Keys.SPACE)
		self.browser.find_element_by_id("submit").click()

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('Explination for question #1', page_text)

# Click on next button, which has been enabled
		self.browser.find_element_by_id("submit").click()
		page_text = self.browser.find_element_by_tag_name('body').text

		print(page_text)
		self.assertIn('secundo', page_text)
# Student moves on to the next question
		self.fail('Finish the test')