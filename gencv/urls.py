from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     
    url(r'^$', 'gencv.views.index'), 
    url(r'^view_cv/$', 'gencv.views.view_cv'),
    url(r'^save_my_cv/$', 'gencv.views.save_my_cv'),
    
)