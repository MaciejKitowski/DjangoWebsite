from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
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

class CategoriesView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categories'
    model = models.Category
    paginate_by = 21

class QuestionView(generic.DetailView):
    template_name = 'question.html'
    model = models.Question

    def post(self, request, *args, **kwargs):
        if 'answer' in request.POST:
            ans = models.Answer.objects.create(author=request.user, content = request.POST['answer'])
            models.Question.objects.get(pk=self.kwargs['pk']).answers.add(ans)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        return context

class NewQuestionView(generic.edit.FormView):
    template_name = 'newQuestion.html'
    form_class = forms.NewQuestionForm
    success_url = '/'
    
    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.author = self.request.user
        candidate.save()
        form.save_m2m()
        return super(NewQuestionView, self).form_valid(candidate)

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
