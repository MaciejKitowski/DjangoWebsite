from django.shortcuts import render
from django.views import generic
from Question import models

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_questions'
    model = models.Question
    paginate_by = 10

    def get_queryset(self):
        sortType = self.__getSortType()

        if sortType == 'date-asc': return self.__getQuerySorted('askDate')
        elif sortType == 'date-desc': return self.__getQuerySorted('askDate', True)
        elif sortType == 'votes-asc': return self.__getQuerySorted('votes')
        elif sortType == 'votes-desc': return self.__getQuerySorted('votes', True)
        elif sortType == 'views-asc': return self.__getQuerySorted('views')
        elif sortType == 'views-desc': return self.__getQuerySorted('views', True)
        else: return self.__getQuerySorted('askDate', True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context



    def __getSortType(self):
        try:
            buffer = self.kwargs['sortby']
            return buffer
        except:
            return 'date-dest'

    def __getQuerySorted(self, sortField, toReverse = False):
        query = super(IndexView, self).get_queryset().order_by(sortField)
        if toReverse: query = query.reverse()
        return query

