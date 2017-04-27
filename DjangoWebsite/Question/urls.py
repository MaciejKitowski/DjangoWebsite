from django.conf.urls import include, url
from Question import views

urlpatterns = [
    url(r'^(?P<page>[\d]*)$', views.IndexView.as_view(), name='index'),
]