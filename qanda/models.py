from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):
	text = models.TextField(default='')

class Answer(models.Model):
	text = models.TextField(default='')
	correct = models.BooleanField(default='')
	question = models.ForeignKey(Question, default=None)

class Explanation(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)

class Reference(models.Model):
	text= models.TextField(default='')
	question = models.ForeignKey(Question, default=None)
