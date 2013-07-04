from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     
    #User auth urls
    url(r'^login/$', 'youthjob.views.login'),
   	url(r'^auth/$', 'youthjob.views.auth_view'),
    url(r'^logout/$', 'youthjob.views.logout'),
    url(r'^loggedin/$', 'youthjob.views.loggedin'),
    url(r'^invalid/$', 'youthjob.views.invalid_login'),

    #User registration urls
    url(r'^register/$', 'youthjob.views.register_user'),
    url(r'^register_success/$', 'youthjob.views.register_success'),
)
