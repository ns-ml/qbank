from django.db import models

# Create your models here.
class Question(models.Model):
	text = models.TextField(default='')

class Answer(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)
