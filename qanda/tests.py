from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from qanda.views import home_page
from qanda.models import Answer, Question

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		address = resolve('/')
		self.assertEqual(address.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class QuestionandAnswerModelTest(TestCase):
	
	def test_save_and_retrieve_an_answer(self):
		question_stem = Question()
		question_stem.save()

		first_answer = Answer()
		first_answer.text = "First answer ever"
		first_answer.question = question_stem
		first_answer.save()

		second_answer = Answer()
		second_answer.text = "Second answer!"
		second_answer.question = question_stem
		second_answer.save()

		saved_answers = Answer.objects.all()
		self.assertEqual(saved_answers.count(), 2)

		first_saved_answer = saved_answers[0]
		second_saved_answer = saved_answers[1]
		self.assertEqual('First answer ever', first_saved_answer.text)
		self.assertEqual(first_answer.question, question_stem)
		self.assertIn('Second', second_saved_answer.text)
		self.assertEqual(second_answer.question, question_stem)

class QandAViewTest (TestCase):

	def test_uses_view_template(self):
		question_stem = Question.objects.create()
		response = self.client.get('/questions/%d/' % (question_stem.id,))
		self.assertTemplateUsed(response, 'view_question.html')

