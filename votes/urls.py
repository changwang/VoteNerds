from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('votes.views',

    # votes
    url(r'^$', 'index', { 'template_name': 'index.html' }, 'index'),

    url(r'^register/$', 'register', { 'template_name': 'registration/register.html' }, 'register'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$', 'login', { 'template_name': 'registration/login.html' }, 'login'),
	url(r'^logout/$', 'logout', { 'template_name': 'registration/logout.html', 'next_page': '/' }, 'logout'),
)
