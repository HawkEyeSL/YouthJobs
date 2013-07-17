from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     
    #User auth urls
    url(r'^$', 'youthjob.views.index'),
    url(r'^login/$', 'youthjob.views.login'),
   	url(r'^auth/$', 'youthjob.views.auth_view'),
    url(r'^logout/$', 'youthjob.views.logout'),
    url(r'^loggedin/$', 'youthjob.views.loggedin'),
    url(r'^invalid/$', 'youthjob.views.invalid_login'),
    url(r'^wall/$', 'youthjob.views.wall'),
    url(r'^check_username/$', 'youthjob.views.check_username'),

    #for vacancies views
    url(r'^vacancies/', include('vacancies.urls')),    

    #for generate CV
    url(r'^gencv/', include('gencv.urls')),    

    #User registration urls
    url(r'^register/$', 'youthjob.views.register_user'),
    url(r'^register_success/$', 'youthjob.views.register_success'),
    
    #company views
    url(r'^companies/', include('companies.urls')),

    #generate pdf
    url(r'^pdf/$', 'youthjob.views.some_view'),
    
    
    #skills views
    url(r'^skills/', include('skills.urls')),
    
    #maching algorithm views
    url(r'^match/', include('match.urls')),
    
    
    
    
)
