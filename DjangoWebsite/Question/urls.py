from django.conf.urls import include, url
from Question import views
from django.contrib.auth import views as auth_view
from Question import forms

urlpatterns = [
    url(r'^(?P<page>[\d]*)/?$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<page>[\d]+)/(?P<sortby>[\w\-]+)$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>[\w\-\_]+)/(?P<page>[\d]+)/(?P<sortby>[\w\-]*)$', views.IndexView.as_view(), name='index'),
    url(r'^categories/(?P<page>[\d]*)', views.CategoriesView.as_view(), name='categories'),
    url(r'^question/(?P<pk>[\d]+)', views.QuestionView.as_view(), name='question'),
    url(r'^question/add', views.NewQuestionView.as_view(), name='newQuestion'),
    url(r'^edit/answer/(?P<pk>[\d]+)', views.EditAnswerView.as_view(), name='edit_answer'),
    url(r'^delete/answer/(?P<pk>[\d]+)', views.DeleteAnswerView.as_view(), name='delete_answer'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html', 'authentication_form': forms.LoginForm}),
    url(r'^logout/$', auth_view.logout, kwargs={'next_page': '/'}),
    url(r'^register/$', views.RegisterView.as_view()),
]
