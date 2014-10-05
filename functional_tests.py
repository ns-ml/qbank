from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_show_a_question(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Welcome to qbank', self.browser.title)
		self.fail('Finish the test')

# Student arrives at qbank website


# A wild question appears! with four potential answers

# A first attempt at an answer is made, wrong answer!

# A second attmept, correct answer. Text changes to green and an explination appears below

# Click on next button, which has been enabled

# Student moves on to the next question

if __name__ == '__main__':
	unittest.main(warnings='ignore')