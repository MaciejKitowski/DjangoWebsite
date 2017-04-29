from django.contrib import admin
from Question.models import *

class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'countReferences' )

class QuestionDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'askDate', 'views', 'votes')

class AnswerDisplay(admin.ModelAdmin):
    list_display = ('author', 'answerDate', 'votes')

admin.site.register(Category, CategoryDisplay)
admin.site.register(Question, QuestionDisplay)
admin.site.register(Answer, AnswerDisplay)