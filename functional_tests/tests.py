from selenium import webdriver
from django.test import LiveServerTestCase
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

# Student arrives at qbank website

	def test_can_show_a_question(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Welcome to Q Bank', self.browser.title)

# Student clicks the start button and is taken to the first question

		self.browser.find_element_by_id("submit").click()
		current_url = self.browser.current_url
		self.assertEqual(current_url, 'http://localhost:8081/the_only_question/')

		
# A wild question appears! with four potential answers



# A first attempt at an answer is made, wrong answer!

# A second attmept, correct answer. Text changes to green and an explination appears below

# Click on next button, which has been enabled

# Student moves on to the next question
		self.fail('Finish the test')