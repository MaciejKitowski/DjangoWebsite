from django.conf.urls import include, url
from Question import views
from django.contrib.auth import views as auth_view
from Question import forms

urlpatterns = [
    url(r'^(?P<page>[\d]*)/?$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<page>[\d]+)/(?P<sortby>[\w\-]+)$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<category>[\w\-\_]+)/(?P<page>[\d]+)/(?P<sortby>[\w\-]*)$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html', 'authentication_form': forms.LoginForm}), 
]
