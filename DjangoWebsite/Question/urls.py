from django.conf.urls import include, url
from Question import views
from django.contrib.auth import views as auth_view
from Question import forms

urlpatterns = [
    url(r'^(?P<page>[\d]*)/?$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<page>[\d]+)/(?P<sortby>[\w\-]+)$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>[\w\-\_]+)/(?P<page>[\d]+)/(?P<sortby>[\w\-]*)$', views.IndexView.as_view(), name='index'),
    url(r'^categories/(?P<page>[\d]*)', views.CategoriesView.as_view(), name='categories'),
    url(r'^question/(?P<questionID>[\d]+)', views.QuestionView.as_view(), name='question'),
    url(r'^question/add', views.NewQuestionView.as_view(), name='newQuestion'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html', 'authentication_form': forms.LoginForm}),
    url(r'^logout/$', auth_view.logout, kwargs={'next_page': '/'}),
    url(r'^register/$', views.RegisterView.as_view()),
]
