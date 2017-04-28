from django.contrib import admin
from Question.models import *

class QuestionDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'askDate', 'views', 'votes')

class AnswerDisplay(admin.ModelAdmin):
    list_display = ('getTitle', 'author', 'answerDate', 'votes')

    def getTitle(self, obj):
        return obj.question.title
    getTitle.admin_order_field  = 'question'
    getTitle.short_description = 'Question'

admin.site.register(Category)
admin.site.register(Question, QuestionDisplay)
admin.site.register(Answer, AnswerDisplay)