import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from votes.models import Game, Vote
from votes.utilities import one_day_limit, weekend

def new_game(title):
    game = Game.objects.create(title=title, owned=False)
    game.save()
    vote = Vote.objects.create(game=game)
    vote.count += 1
    vote.save()
    return game

@require_POST
@login_required
def add_game(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    postdata = request.POST.copy()
    title = postdata.get("game", "")
    added_today = False
    response = redirect('wishes')

    if title == "":
        messages.info(request, "Game title cannot be empty, try something meaningful!")
    else:
        if settings.COOKIE_ADD_GAME_TIME in request.COOKIES:
            added_today = True
        try:
            game = Game.objects.get(title__iexact=title)
        except Game.DoesNotExist:
            if added_today:
                added_time = datetime.datetime.strptime(request.COOKIES[settings.COOKIE_ADD_GAME_TIME], settings.COOKIE_TIME_FORMAT)
                if one_day_limit(added_time) or weekend():
                    messages.info(request, "One day's limit, try it tomorrow, or buy me a coffee!")
                else:
                    game = new_game(title)
                    messages.info(request, "Game '%s' has been added successfully!" % game.title)
                    response.set_cookie(settings.COOKIE_ADD_GAME_TIME, datetime.datetime.now())
            else:
                game = new_game(title)
                messages.info(request, "Game '%s' has been added successfully!" % game.title)
                response.set_cookie(settings.COOKIE_ADD_GAME_TIME, datetime.datetime.now())
        else:
            messages.info(request, "Game '%s' already existed! You don't want to buy it twice, don't you?" % game.title)
    return response

def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('index')
                messages.info(request, "Successfully Registered!")
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def wishes(request, template_name="wishes.html"):
    vote_list = Vote.objects.filter(game__owned=0).order_by('-count', 'created')
    return render_to_response(template_name, { "vote_list": vote_list }, context_instance=RequestContext(request))

def owned(request, template_name="owned.html"):
    owned_list = Game.objects.owned_list()
    return render_to_response(template_name, { "owned_list": owned_list }, context_instance=RequestContext(request))

def vote_plus(game_id):
    v = Vote.objects.get(game__id=game_id)
    v.count += 1
    v.save()

@login_required
def thumb_up(request, game_id):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    voted_today = False
    response = redirect("wishes")
    if settings.COOKIE_VOTE_GAME_TIME in request.COOKIES:
        voted_today = True
    if voted_today:
        voted_time = datetime.datetime.strptime(request.COOKIES[settings.COOKIE_VOTE_GAME_TIME], settings.COOKIE_TIME_FORMAT)
        if one_day_limit(voted_time) or weekend():
            messages.info(request, "One day's limit, try it tomorrow, or buy me a coffee!")
        else:
            vote_plus(game_id)
            messages.info(request, "Vote has been submitted, stay tuned!")
            response.set_cookie(settings.COOKIE_VOTE_GAME_TIME, datetime.datetime.now())
    else:
        vote_plus(game_id)
        messages.info(request, "Vote has been submitted, stay tuned!")
        response.set_cookie(settings.COOKIE_VOTE_GAME_TIME, datetime.datetime.now())
    return response