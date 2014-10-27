from django import forms

class QuestionForm(forms.Form):
	answers = forms.ChoiceField(widget=forms.RadioSelect)
	