from django.shortcuts import render
from qanda.models import Answer, Question

# Create your views here.
def home_page(request):
	return render (request, 'home.html')

def view_question(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	answers = Answer.objects.filter(question=question_stem)
	return render (request, 'view_question.html', {
		'answers': answers
		})