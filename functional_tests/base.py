from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from qanda.models import Question, Answer, Explanation, Reference
import sys

class FunctionalTest(StaticLiveServerTestCase):
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

	def generate_two_questions(self):
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

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')