from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.SlugField('Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name

class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField('Title', max_length = 255)
    askDate = models.DateTimeField('Ask Date', auto_now_add=True)
    content = models.TextField('Content')
    views = models.PositiveIntegerField('Views', default=0)
    rate = models.IntegerField('Rates', default=0)
    tags = models.ManyToManyField(Category, verbose_name = 'Tags')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.title
