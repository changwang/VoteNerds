from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from votes.models import Game

urlpatterns = patterns('votes.views',

    # votes
    url(r'^$', ListView.as_view(model=Game,
                                queryset=Game.objects.owned_list(),
                                context_object_name="game_list",
                                template_name='index.html'), name="index"),

    url(r'^wishes/$', 'wishes', {}, 'wishes'),
    url(r'^owned/$', 'owned', {}, 'owned'),
    url(r'^add-game/$', 'add_game', {}, 'add_game'),
    url(r'^thumb-up/(?P<game_id>\d+)/$', 'thumb_up', {}, 'thumb_up'),
    url(r'^buy/$', 'buy_game', {}, 'buy_game'),
    url(r'^register/$', 'register', {}, 'register'),
)

urlpatterns += patterns('django.contrib.auth.views',
    # use django's auth framework
    url(r'^login/$', 'login', { 'template_name': 'registration/login.html' }, 'login'),
    url(r'^logout/$', 'logout', { 'next_page': '/' }, 'logout'),
)
