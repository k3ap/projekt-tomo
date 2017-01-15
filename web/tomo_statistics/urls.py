from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_view, name='main_view'),
    url(r'^(?P<course_pk>\d+)/$', views.test_view, name = 'test_view'),
    url(r'^graf_test/(?P<course_pk>\d+)/$', views.graph, name='graph'),
    url(r'^(?P<course_pk>\d+)/js$', views.graph_json, name='graph_json'),
]
