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
    """
    creates a new game record with given title
    """
    game = Game.objects.create(title=title, owned=False)
    game.save()
    # each time user creates a new game record,
    # it means this game is voted once.
    vote = Vote.objects.create(game=game)
    vote.count = 1
    vote.save()
    return game

@require_POST
@login_required
def add_game(request):
    """
    add a new game record according to the given form,
    if it is not in the weekday, do nothing;
    if it happens within one day, do nothing;
    user login is required.
    """
    response = redirect('wishes')
    # if it is weekend, directly display the flash message
    if weekend():
        messages.info(request, "Give me a break, do it on workdays!")
    else:
        postdata = request.POST.copy()
        title = postdata.get("game", "")
        # if add game cookie is set and the consecutive operation is within one day,
        # display the flash message
        # if user doesn't type anything, display the flash message
        if (settings.COOKIE_ADD_GAME_TIME in request.COOKIES) and \
                (one_day_limit(datetime.datetime.strptime(request.COOKIES[settings.COOKIE_ADD_GAME_TIME], settings.COOKIE_TIME_FORMAT))):
            messages.info(request, "One day's limit, try it tomorrow, or buy me a coffee!")
        else:
            # if user doens't type anything, display the flash message
            if title == "":
                messages.info(request, "Game title cannot be empty, try something meaningful!")
            else:
                try:
                    # if the game existed, case insensitively compare
                    game = Game.objects.get(title__iexact=title)
                except Game.DoesNotExist:
                    # if the game doesn't exist, create a new record, with title case
                    game = new_game(title.title())
                    messages.info(request, "Game '%s' has been added successfully!" % game.title)
                    # set cookie expiration is one day
                    response.set_cookie(settings.COOKIE_ADD_GAME_TIME, datetime.datetime.now(), expires=settings.COOKIE_EXPIRATION)
                else:
                    # otherwise display the game has been added
                    messages.info(request, "Game '%s' already existed! You don't want to buy it twice, don't you?" % game.title)
    return response
    
def vote_plus(game_id):
    """
    add one more vote to the given game votes
    """
    v = Vote.objects.get(game__id=game_id)
    v.count += 1
    v.save()

@login_required
def thumb_up(request, game_id):
    """
    add one vote to the given game,
    if it is not in the weekday, do nothing;
    if it happens within one day, do nothing;
    """
    response = redirect("wishes")
    # if it is weekend, directly display the flash message
    if weekend():
        messages.info(request, "Give me a break, do it on workdays!")
    else:
        # if add game cookie is set and the consecutive operation is within one day,
        # display the flash message
        if (settings.COOKIE_VOTE_GAME_TIME in request.COOKIES) and \
                (one_day_limit(datetime.datetime.strptime(request.COOKIES[settings.COOKIE_ADD_GAME_TIME], settings.COOKIE_TIME_FORMAT))):
            messages.info(request, "One day's limit, try it tomorrow, or buy me a coffee!")
        else:
            vote_plus(game_id)
            messages.info(request, "Vote has been submitted, stay tuned!")
            response.set_cookie(settings.COOKIE_VOTE_GAME_TIME, datetime.datetime.now(), expires=settings.COOKIE_EXPIRATION)
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
