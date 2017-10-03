from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^notes/(\d+)/', views.roofy_notes_view, name='roofy_notes_view'),
    url(r'^notes/(?P<project_id>[0-9]+)/', views.roofy_notes_test, name='roofy_notes_test'),
    url(r'^notes/$', views.roofy_notes_generic_view.as_view(), name='roofy_notes_generic_view'),
    url(r'^notes/add/(?P<project_id>[0-9]+)/',views.roofy_add_note,name='roofy_add_note'),
    url(r'^$', views.index, name='index'),
]