from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quoter.views.index', name='index'),
    url(r'^logout/', 'quoter.views.logout_view', name='logout'),
    url(r'^quotes/', 'quoter.views.quotes', name='quotes'),
    url(r'^register/$', 'quoter.views.register', name='register'),
    url(r'^update_profile/$', 'quoter.views.update_profile', name='update_profile'),
    # url(r'^admin/', include(admin.site.urls)),
)
