from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.SlugField('Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
    
    def countReferences(obj):
        return Question.objects.filter(categories__in=[obj]).count()
    countReferences.short_description = 'References'

class Vote(models.Model):
    user = models.ForeignKey(User, blank = True)
    date = models.DateTimeField('Date', auto_now_add=True)
    useragent = models.TextField('User agent')
    ip = models.TextField("IP address")
    vote = models.IntegerField("Vote")

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.ip + " | " + ("{0}").format(self.vote)

class Answer(models.Model):
    author = models.ForeignKey(User)
    answerDate = models.DateTimeField('Answer Date', auto_now_add=True)
    content = models.TextField('Content')
    votes = models.ManyToManyField(Vote, verbose_name = 'Votes', blank = True)

    def getRating(self):
        return self.votes.all().aggregate(Sum('vote')).get('vote__sum', 0)

    getRating.short_description = 'Votes'

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answerDate.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.content

class View(models.Model):
    user = models.ForeignKey(User, blank = True)
    date = models.DateTimeField('Date', auto_now_add=True)
    useragent = models.TextField('User agent')
    ip = models.TextField("IP address")

    class Meta:
        verbose_name = 'View'
        verbose_name_plural = 'Views'
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.ip

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


