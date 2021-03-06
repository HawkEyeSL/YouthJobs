from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
     
    url(r'postjob/$', views.post_job, name='post_job'),
    url(r'vacancies_list/$', views.vacancies_list, name='vacancies_list'),
    url(r'^(?P<vacancy_id>\d+)/$', views.view_vacancy, name='view_vacancy'),
    url(r'apply/$', views.apply, name='apply'),
    
)