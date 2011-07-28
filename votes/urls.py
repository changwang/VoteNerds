from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    # votes
    url(r'^$', 'votes.views.index'),
)