from django.shortcuts import render
from django.views import generic
from Question import models

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_questions'
    model = models.Question
    paginate_by = 10

    def get_queryset(self):
        sortbyColumn = {'date-asc':'askDate', 'date-desc':'-askDate', 'votes-asc':'votes', 'votes-desc':'-votes', 'views-asc':'views', 'views-desc':'-views' }
        qr = super(IndexView, self).get_queryset().order_by(sortbyColumn[self.__getSortType()])

        return qr

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

#**********************************************************************************

    def __getSortType(self):
        try:
            buffer = self.kwargs['sortby']
            return buffer
        except:
            return 'date-desc'

    def __getQuerySorted(self, sortField, toReverse = False):
        query = super(IndexView, self).get_queryset().order_by(sortField)
        if toReverse: query = query.reverse()
        return query

