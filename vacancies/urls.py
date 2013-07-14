from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
     
    #list all companies
    url(r'^$', views.index, name='index'),
    
    )