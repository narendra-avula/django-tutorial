from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import login, logout


__author__ = 'narendra'


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.user_profile, name='user_profile')
]