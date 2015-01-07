from django.test import TestCase
from qanda.forms import QuestionForm, UserForm, UserProfileForm
from unittest import skip

class QuestionFormTest(TestCase):

	@skip
	def test_form_renders_question_stem(self):
		form = QuestionForm()
		self.fail(form.as_p())

class UserFormTest(TestCase):

	def test_form_renders_user_fields(self):
		form = UserForm()
		self.fail(form.as_p())