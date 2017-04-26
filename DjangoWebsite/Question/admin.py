from django.contrib import admin
from Question.models import *

class QuestionDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'askDate', 'views', 'rate')
    

admin.site.register(Category)
admin.site.register(Question, QuestionDisplay)