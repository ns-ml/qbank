from django.contrib import admin
from qanda.models import Question, Answer, Explanation, Reference, UserProfile

class AnswersInline(admin.TabularInline):
	model= Answer
	extra=0

class ExplanationInline(admin.StackedInline):
	model= Explanation
	extra=0

class ReferencesInline(admin.StackedInline):
	model = Reference
	extra = 0
		

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text',)
	fieldsets = [
	(None, {'fields': ['text']}),]
	inlines=[AnswersInline, ExplanationInline, ReferencesInline]
	search_fields = ['text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)