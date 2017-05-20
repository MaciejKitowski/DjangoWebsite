from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from Question import models, forms
from django.contrib.auth import authenticate, login

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

class CategoriesView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categories'
    model = models.Category
    paginate_by = 21

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        return context

class RegisterView(generic.edit.FormView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context
