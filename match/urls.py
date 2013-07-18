from django.conf.urls import patterns, url


urlpatterns = patterns('',
     
    #list all companies
    url(r'^(?P<vacancy>\d+)/(?P<amount>\d+)', 'match.views.list_all'),
)
  
