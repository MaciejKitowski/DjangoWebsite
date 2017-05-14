from django.conf.urls import include, url
from Question import views

urlpatterns = [
    url(r'^(?P<page>[\d]*)/?$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<page>[\d]+)/(?P<sortby>[\w\-]+)$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<category>[\w\-\_]+)/(?P<page>[\d]+)/(?P<sortby>[\w\-]*)$', views.IndexView.as_view(), name='index'),
]
