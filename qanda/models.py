from django.db import models
from django import forms
import datetime

# Create your models here.
class Question(models.Model):
	text = models.TextField(default='')
	created = models.DateTimeField(editable=False, default=datetime.datetime.now)
	modified = models.DateTimeField(default=datetime.datetime.now)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = datetime.datetime.today()
		self.modified = datetime.datetime.today()
		return super(Question, self).save(*args, **kwargs)

class Answer(models.Model):
	text = models.TextField(default='')
	correct = models.BooleanField(default='')
	question = models.ForeignKey(Question, default=None)

class Explanation(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)

class Reference(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)
