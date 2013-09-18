from django.conf.urls import patterns, include, url
from django.contrib import admin, databrowse

from ticket.databrowse_config import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    url(r'^ticket/', include('ticket.urls')),
    url(r'^databrowse/(.*)', databrowse.site.root),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
