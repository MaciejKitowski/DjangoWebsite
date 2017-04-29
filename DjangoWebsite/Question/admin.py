from django.contrib import admin
from Question.models import *

import sys

class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'countReferences' )

    def countReferences(self, obj):
        counter = 0
        for ques in Question.objects.all():
            for cat in ques.categories.all():
                if(cat.id == obj.id):
                    counter += 1
        return counter
    #countReferences.admin_order_field  = 'References'
    countReferences.short_description = 'References'

class QuestionDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'askDate', 'views', 'votes')

class AnswerDisplay(admin.ModelAdmin):
    list_display = ('getTitle', 'author', 'answerDate', 'votes')

    def getTitle(self, obj):
        return obj.question.title
    getTitle.admin_order_field  = 'question'
    getTitle.short_description = 'Question'

admin.site.register(Category, CategoryDisplay)
admin.site.register(Question, QuestionDisplay)
admin.site.register(Answer, AnswerDisplay)