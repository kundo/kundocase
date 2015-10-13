from django.contrib import admin
from kundocase.forum.models import Question, Answer

admin.site.register(Question, admin.ModelAdmin)
admin.site.register(Answer, admin.ModelAdmin)
