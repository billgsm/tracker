from django.conf.urls.defaults import patterns, url
from views import home, ticket_listing

urlpatterns = patterns('',
    url(u'^home$', home, name="home"),
    url(u'^home/(\w+)$', home, name="home"),
    url(u'^$', ticket_listing, name="listing")
)
