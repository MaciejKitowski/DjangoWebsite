from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.SlugField('Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
    
    def countReferences(obj):
        counter = 0
        for ques in Question.objects.all():
            for cat in ques.categories.all():
                if(cat.id == obj.id):
                    counter += 1
        return counter
    countReferences.short_description = 'References'

class Answer(models.Model):
    author = models.ForeignKey(User)
    answerDate = models.DateTimeField('Answer Date', auto_now_add=True)
    content = models.TextField('Content')
    votes = models.IntegerField('Votes', default=0)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answerDate.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.content

class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField('Title', max_length = 255)
    askDate = models.DateTimeField('Ask Date', auto_now_add=True)
    content = models.TextField('Content')
    views = models.PositiveIntegerField('Views', default=0)
    votes = models.IntegerField('Votes', default=0)
    categories = models.ManyToManyField(Category, verbose_name = 'Categories', blank = True)
    answers = models.ManyToManyField(Answer, verbose_name = 'Answers', blank = True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.title


