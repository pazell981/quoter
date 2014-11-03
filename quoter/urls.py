from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quoter.views.index', name='index'),
    url(r'^quotes/', 'quoter.views.quotes', name='quotes'),
    url(r'^register/$', 'quoter.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
