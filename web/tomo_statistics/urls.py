from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_view, name='main_view'),
    url(r'^(?P<course_pk>\d+)/$', views.test_view, name = 'main_view')
    
]
