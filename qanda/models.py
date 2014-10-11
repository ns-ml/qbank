from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):
	text = models.TextField(default='')

class Answer(models.Model):
	text = models.TextField(default='')
	correct = models.BooleanField(default='')
	question = models.ForeignKey(Question, default=None)

class Explination(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)

class AnswerForm(forms.Form):
	user_answer = forms.CharField(label='Answer') 

