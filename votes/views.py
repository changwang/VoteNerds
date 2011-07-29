from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from votes.models import Game, Vote

@require_POST
@login_required
def add_game(request, template_name='index.html'):
    if request.method == 'POST':
        messages.info(request, "Game Added Successfully!")
        url = urlresolvers.resolve('index')
        return HttpResponseRedirect(url)
    else:
        render_to_response(template_name, locals(), context_instance=RequestContext(request))

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
    vote_list = Vote.objects.filter(game__owned=0).order_by('-count')
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def owned(request, template_name="owned.html"):
    owned_list = Game.objects.owned_list()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def thumb_up(request):
    pass
