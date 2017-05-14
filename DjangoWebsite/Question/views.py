from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from Question import models

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'questions'
    model = models.Question
    paginate_by = 13

    def get_queryset(self):
        sortbyColumn = {'date-asc':'askDate', 'date-desc':'-askDate', 'votes-asc':'votes', 'votes-desc':'-votes', 'views-asc':'views', 'views-desc':'-views', 'answers-asc':'answersCount', 'answers-desc':'-answersCount' }
        qr = super(IndexView, self).get_queryset()
        qr = qr.annotate(answersCount=Count('answers'))

        if 'category' in self.kwargs:
            qr = qr.filter(categories__name__iexact = self.kwargs['category'])

        if 'sortby' in self.kwargs and self.kwargs['sortby'] in sortbyColumn:
            qr = qr.order_by(sortbyColumn[self.kwargs['sortby']])
        else:
            qr = qr.order_by(sortbyColumn['date-desc'])

        return qr

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
