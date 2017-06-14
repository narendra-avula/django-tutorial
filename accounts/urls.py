from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import login

__author__ = 'narendra'


urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'})
]