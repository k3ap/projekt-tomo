from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from attempts.rest import AttemptViewSet
from problems.rest import ProblemViewSet
from courses.rest import ProblemSetViewSet, CourseViewSet
from courses.views import homepage
from utils.views import help, terms_of_service
from users.views import mobile_app_token
import courses.urls
import django.contrib.auth.views
from django.conf import settings

router = DefaultRouter()
router.register(r'attempts', AttemptViewSet, base_name='attempts')
router.register(r'problems', ProblemViewSet, base_name='problems')
router.register(r'problem_sets', ProblemSetViewSet, base_name='problem_sets')
router.register(r'courses', CourseViewSet, base_name='courses')


urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^terms_of_service$', terms_of_service, name='terms_of_service'),
    url(r'^help$', help, name='help'),
    url(r'^help/students$', help, {'special': 'students'}, name='help_students'),
    url(r'^help/teachers$', help, {'special': 'teachers'}, name='help_teachers'),
    url('', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include([
        url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login.html'}, name='login'),
        url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
    ])),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/mobile-app-token/', mobile_app_token, name='mobile_app_token'),
    url(r'^api/', include(router.urls)),
    url(r'^problems/', include('problems.urls')),
    url(r'^tomo_statistics/', include('tomo_statistics.urls')),
]

urlpatterns += courses.urls.urlpatterns

if 'silk' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^silk/', include('silk.urls', namespace='silk')),
    ]
