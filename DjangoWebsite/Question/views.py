from django.shortcuts import render
from django.views import generic
from Question import models

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_questions'
    model = models.Question
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
