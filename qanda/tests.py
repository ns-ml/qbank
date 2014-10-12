from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from qanda.views import home_page, check_answer
from qanda.models import Answer, Question, Explination, Reference
from django.shortcuts import get_object_or_404

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

class QuestionViewTest (TestCase):

	def test_uses_view_template(self):
		question_stem = Question.objects.create()
		Answer.objects.create(text='',question=question_stem, correct=True)
		response = self.client.get('/questions/%d/' % (question_stem.id,))
		self.assertTemplateUsed(response, 'view_question.html')

	def test_displays_answers_only_for_that_question(self):
		correct_question = Question.objects.create(text="Question #1: This is the first question ever")
		Answer.objects.create(text="Answer 1", question=correct_question, correct=True)
		Answer.objects.create(text="Answer 2", question=correct_question, correct=False)
		Explination.objects.create(text='Explination #1', question=correct_question)
		Reference.objects.create(text='Reference #1', question=correct_question)	

		other_question = Question.objects.create()
		Answer.objects.create(text="Other Answer 1", question=other_question)
		Answer.objects.create(text="Other Answer 2", question=other_question)
		
		response = self.client.get('/questions/%d/' % (correct_question.id,))

		saved_answers = Answer.objects.all()

		self.assertContains(response, 'Answer 1')
		self.assertContains(response, 'Question #1')
		self.assertNotContains(response, 'Other Answer')
		self.assertTrue(saved_answers[0])

	def test_question_view_page_can_save_a_POST_request(self):
		question_stem = Question.objects.create()
		correct_answer = Answer.objects.create(text='Test radio answer',question=question_stem, correct=True)

		request = HttpRequest()
		request.method = 'POST'
		request.POST['radio_answer'] = 'Test radio answer'
		user_answer = request.POST['radio_answer']

		response = check_answer(request, '1')

		self.assertEqual(correct_answer.text, user_answer)

class AnswerViewTest (TestCase):
	
	def test_uses_view_template(self):
		question_stem = Question.objects.create()
		Explination.objects.create(text='Correct explination', question=question_stem)
		response = self.client.get('/questions/%d/answer' % (question_stem.id,))
		self.assertTemplateUsed(response, 'view_answer.html')

	def test_displays_question_stem_and_correct_answer_only(self):
		correct_question = Question.objects.create(text="Question #1: This is the first question ever")
		Answer.objects.create(text="Answer 1", question=correct_question, correct=True)
		Answer.objects.create(text="Answer 2", question=correct_question, correct=False)
		Explination.objects.create(text='Correct explination', question=correct_question)
		
		response = self.client.get('/questions/%d/answer' % (correct_question.id,))

		self.assertContains(response, 'Answer 1')
		self.assertNotContains(response, 'Answer 2')

	def test_displays_correct_explination(self):
		correct_question = Question.objects.create(text="Q1")
		wrong_question = Question.objects.create(text="Q2")
		Answer.objects.create(text='Answer 1', question=correct_question)
		Answer.objects.create(text='Answer 2', question=correct_question)
		Answer.objects.create(text='Other answer 1', question=wrong_question)
		Explination.objects.create(text='Correct explination', question=correct_question)
		Explination.objects.create(text='Wrong explination', question=wrong_question)

		explination_text = Explination.objects.get(question=correct_question)
		self.assertEqual('Correct explination', explination_text.text)

	def test_retrieve_correct_reference(self):
		correct_question = Question.objects.create(text="Q1")
		Reference.objects.create(text='Reference #1', question=correct_question)

		reference_text = get_object_or_404(Reference, question=correct_question)
		
		self.assertEqual('Reference #1', reference_text.text)



