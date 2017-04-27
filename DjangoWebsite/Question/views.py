from django.shortcuts import render
from django.views import generic
from Question import models

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_questions'
    model = models.Question
    paginate_by = 10

    def get_queryset(self):
        sortType = self.request.GET.get('sortby', 'date-desc')

        if sortType == 'date-asc': return self.querySorted('askDate')
        elif sortType == 'date-desc': return self.querySorted('askDate', True)
        elif sortType == 'votes-asc': return self.querySorted('votes')
        elif sortType == 'votes-desc': return self.querySorted('votes', True)
        elif sortType == 'views-asc': return self.querySorted('views')
        elif sortType == 'views-desc': return self.querySorted('views', True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def querySorted(self, sortField, toReverse = False):
        query = super(IndexView, self).get_queryset().order_by(sortField)
        if toReverse: query = query.reverse()
        return query

