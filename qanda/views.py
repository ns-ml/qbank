from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from qanda.models import Answer, Question, Explination
import django.contrib
django.contrib.admin.AdminSite.site_header = "Qbank Administration"
django.contrib.admin.AdminSite.site_title = "Qbank Administration"

# Create your views here.
def home_page(request):
	return render (request, 'home.html')

def view_answer(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	next_question_id = int(question_id)+1
	explination_text = get_object_or_404(Explination, question=question_stem)
	correct_answer = Answer.objects.filter(question=question_stem, correct=True)
	return render (request, 'view_answer.html', {
		'correct_answer': correct_answer,
		'question_stem': question_stem,
		'next_question_id':next_question_id,
		'explination_text':explination_text,
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