from base import FunctionalTest
from qanda.views import WRONG_ANSWER_ERROR
from qanda.models import Question
import time

class AnswerValidationTest(FunctionalTest):
	def test_shows_error_message_with_wrong_answer(self):
		self.generate_two_questions()
		qandaurl = self.server_url + '/questions/%d/' % (Question.objects.first().id)
		self.browser.get(qandaurl)
		
