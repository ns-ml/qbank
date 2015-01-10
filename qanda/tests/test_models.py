from django.test import TestCase
from qanda.models import Answer, Question, Explanation, Reference
from django.contrib.auth.models import User
from unittest import skip

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

	def test_retrieve_next_object_by_created_time(self):
		first_question = Question(text="#1")
		second_question = Question(text="#2")
		first_question.save()
		second_question.save()

		retrieved_question = first_question.get_next_by_created()

		self.assertEqual(retrieved_question.text, second_question.text)

	@skip
	def test_get_absolute_url_for_question(self):
		question = Question.objects.create()
		self.assertEqual(question.get_absolute_url(), '/questions/%d/' % (question.id,))
	@skip
	def test_get_absolute_url_for_answer(self):
		question = Question.objects.create()
		answer = Answer.objects.create(question=question)
		self.assertEqual(answer.get_absolute_url(), '/questions/%d/answer' % (answer.id,))

class UserProfileTest(TestCase):

    def test_create_and_retrieve_users(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.program = 'NMH'
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.program, 'NMH')
        # print (user.program)

