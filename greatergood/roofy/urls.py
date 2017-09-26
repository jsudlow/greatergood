from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notes/(\d+)/', views.roofy_notes_view, name='roofy_notes_view'),
    url(r'^notes/(?P<project_id>[0-9]+)/', views.roofy_notes_test, name='roofy_notes_test'),
    url(r'^$', views.index, name='index'),
]