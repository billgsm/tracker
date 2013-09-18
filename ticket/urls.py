from django.conf.urls.defaults import patterns, url
from views import home

urlpatterns = patterns('',
    url(u'^home$', home, name="home"),
    url(u'^home/(\w+)$', home, name="home")
)
