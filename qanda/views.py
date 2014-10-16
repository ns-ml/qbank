from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from qanda.models import Answer, Question, Explanation, Reference
import django.contrib
from django.db.models import Max

# Create your views here.
def home_page(request):
	return render (request, 'home.html')

def view_answer(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	next_question_id = int(question_id)+1
	explanation_text = get_object_or_404(Explanation, question=question_stem)
	references = Reference.objects.filter(question=question_stem)
	correct_answer = Answer.objects.filter(question=question_stem, correct=True)
	return render (request, 'view_answer.html', {
		'correct_answer': correct_answer,
		'question_stem': question_stem,
		'next_question_id':next_question_id,
		'explanation_text':explanation_text,
		'references': references,
		})

def check_answer(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	question_number = int(question_stem.id)
	answers = Answer.objects.filter(question=question_stem)
	correct_answer = Answer.objects.get(question=question_stem, correct=True)

	if request.method == 'POST':
		user_answer = request.POST['radio_answer']
		if user_answer == correct_answer.text:
			return HttpResponseRedirect('/questions/%d/answer' % (question_number,))
		else:
			return render (request, 'view_question.html', {
		'answers': answers,
		'question_stem': question_stem,
		'try_again': 'Sorry, try again.'
		})

	return render (request, 'view_question.html', {
		'answers': answers,
		'question_stem': question_stem,
		})