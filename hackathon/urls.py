from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
admin.autodiscover()
from django.views.generic import RedirectView
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'deroubaix/login.html'}),
    url(r'^deroubaix/$', register),
    url(r'^deroubaix/success/$', register_success),
    url(r'^home/$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^real_page/$', RedirectView.as_view(url='https://www.ppolive.com/deroubaix/')),
)