from django.conf.urls.defaults import patterns, url
from views import home, ticket_list, ticket_detail

urlpatterns = patterns('',
    url(u'^home$', home, name="home"),
    url(u'^home/(\w+)$', home, name="home"),
    url(u'^list/(\w+)$', ticket_list, name="list"),
    url(u'^detail/(\d+)$', ticket_detail, name="detail")
)
