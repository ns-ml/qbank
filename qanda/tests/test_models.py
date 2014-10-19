from django.test import TestCase
from qanda.models import Answer, Question, Explanation, Reference

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
