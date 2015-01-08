from django.shortcuts import render, get_object_or_404, redirect
from qanda.models import Answer, Question, Explanation, Reference
from qanda.forms import UserForm, UserProfileForm
import django.contrib
from django.core.exceptions import ObjectDoesNotExist

WRONG_ANSWER_ERROR = 'Sorry, try again'

def home_page(request):
	first_question = Question.objects.first().id
	return render (request, 'home.html', {
		'first_question': first_question
		})

def view_answer(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	explanation_text = get_object_or_404(Explanation, question=question_stem)
	references = Reference.objects.filter(question=question_stem)
	correct_answer = Answer.objects.filter(question=question_stem, correct=True)
	
	#Look for the next question by date created. If one does not exist, go back to the first.
	try:
		next_question_id = question_stem.get_next_by_created().id
	except ObjectDoesNotExist:
		next_question_id = Question.objects.first().id

	return render (request, 'view_answer.html', {
		'correct_answer': correct_answer,
		'question_stem': question_stem,
		'next_question_id':next_question_id,
		'explanation_text':explanation_text,
		'references': references,
		})

def check_answer(request, question_id):
	question_stem = Question.objects.get(id=question_id)
	answers = Answer.objects.filter(question=question_stem)
	# correct_answer = Answer.objects.get(question=question_stem, correct=True)
	correct_answer = get_object_or_404(Answer, question=question_stem, correct=True)
	error = None

	if request.method == 'POST':
		user_answer = request.POST['radio_answer']
		if user_answer == correct_answer.text:
			return redirect('/questions/%d/answer' % (question_stem.id,))
		else:
			error = WRONG_ANSWER_ERROR

	return render (request, 'view_question.html', {
		'answers': answers,
		'question_stem': question_stem,
		'error': error
		})

def register(request):

	#Tell the template whether the regitration was sucessful, changes to True when regitration sucessful
	registered = False

	if request.method == 'POST':
		#Grab standard form raw data
		user_form = UserForm(data=request.POST)
		#Grab extra data in the profile
		profile_form = UserProfileForm(data=request.POST)

		#Validate
		if user_form.is_valid() and profile_form.is_valid():
			#Save the user's data to the database
			user = user_form.save()

			#Hash the password and update the object
			user.set_password(user.password)
			user.save()

			#sort out the UserProfile instance, comit set to False to delay saving the model until ready
			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			#update the variable to tell the template that registration was sucessful
			registered = True

		# Invalid form? Print problems to the terminal and show them to the user
		else:
			print (user_form.errors, profile_form.errors)

	#Not an HTTP pull means it must be a new form
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	#Render the template
	return render(request,
		'register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

