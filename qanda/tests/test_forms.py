from django.test import TestCase
from qanda.forms import QuestionForm
from unittest import skip

class QuestionFormTest(TestCase):

	@skip
	def test_form_renders_question_stem(self):
		form = QuestionForm()
		self.fail(form.as_p())