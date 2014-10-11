from django.contrib import admin

# Register your models here.
from qanda.models import Question, Answer, Explination

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Explination)