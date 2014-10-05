from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render (request, 'home.html')

def view_question(request, question_id):
	return render (request, 'view_question.html')