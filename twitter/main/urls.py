from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
	url(r'^$','main.views.home', name='home'),
	url(r'^add/$', 'main.views.add_tweet', name='add'),
	url(r'^register/$', 'main.views.register', name='register'),
	url(r'^login/$', 'main.views.login', name='login'),
	url(r'^login_process/$', 'main.views.login_process', name='login_process'),
	url(r'^tweet/(?P<pk>\d+)/delete$', 'main.views.delete_tweet', name='delete_tweet'),
	
)
