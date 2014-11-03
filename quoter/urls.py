from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quoter.views.index', name='index'),
    url(r'^quoutes/', 'quoter.views.quotes', name='quotes'),
    url(r'^user/', 'quoter.views.user', name='user'),
    url(r'^admin/', include(admin.site.urls)),
)
