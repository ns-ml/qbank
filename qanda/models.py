from django.db import models

# Create your models here.
class Question(models.Model):
	pass

class Answer(models.Model):
	text = models.TextField(default='')
	question = models.ForeignKey(Question, default=None)
