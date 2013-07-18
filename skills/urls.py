from django.conf.urls import patterns, url


urlpatterns = patterns('',
     
    #list all companies
    url(r'^list/$', 'skills.views.list_all'),
    url(r'^edit/$', 'skills.views.edit'),
    url(r'^adduserskills/$', 'skills.views.addUserSkills'),
    url(r'^add/$', 'skills.views.add'),
    url(r'^search/(?P<text>...|\w+)', 'skills.views.search'),
)
  
