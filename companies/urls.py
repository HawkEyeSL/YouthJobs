from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
     
    #list all companies
    url(r'^list/$', 'companies.views.list_all'),
)

