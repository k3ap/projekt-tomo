from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<course_pk>\d+)/$', views.course_graphs, name = 'course_graphs'),
    url(r'^(?P<course_pk>\d+)/active/(?P<days>\d+)$', views.course_graphs_active,
        name = 'course_graphs_active'),
    url(r'^(?P<course_pk>\d+)/users$', views.user_success, name='user_success'),
]
