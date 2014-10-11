from django.contrib import admin
from qanda.models import Question, Answer, Explination

class AnswersInline(admin.TabularInline):
	model= Answer
	extra=0

class ExplinationInline(admin.StackedInline):
	model= Explination
	extra=0
		

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text',)
	fieldsets = [
	(None, {'fields': ['text']}),]
	inlines=[AnswersInline, ExplinationInline]
	search_fields = ['text']


admin.site.register(Question, QuestionAdmin)