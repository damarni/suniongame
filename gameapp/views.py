from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.conf import settings
from django.utils import timezone

from . import forms, models

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home.html')

    level = request.user.level
    if level >= len(settings.LEVEL_SOLUTIONS):
        return render(request, 'congrats.html')

    wrong_solution = False
    if request.method == 'POST':
        form = forms.SolutionForm(request.POST)
        if form.is_valid():
            solution = form.cleaned_data['solution']
            if solution in settings.LEVEL_SOLUTIONS[level]:
                request.user.level += 1
                request.user.level_date = timezone.now()
                request.user.save()
                return HttpResponseRedirect("/")
            else:
                wrong_solution = True
    else:
        form = forms.SolutionForm()

    return render(request, 'level.html', {
        'form': form.as_p(),
        'level': level,
        'template': 'levels/{}.html'.format(level),
        'wrong_solution': wrong_solution
    })

def ranking(request):
    users = models.User.objects.filter(level__gt=0).order_by('-level', 'level_date')
    return render(request, 'ranking.html', {'users': users, 'levellength': len(settings.LEVEL_SOLUTIONS)})


def login(request):
    # if this is a POST request we need to process the form data
    bad_login = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                bad_login = True
    else:
        form = forms.LoginForm()

    return render(request, 'login.html', {'form': form.as_p(), 'bad_login': bad_login})

def register(request):
    # if this is a POST request we need to process the form data
    bad_username = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if models.User.objects.filter(username=username).first() is not None:
                bad_username = True
            else:
                user = models.User.objects.create_user(username=username, password=password)
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = forms.LoginForm()

    return render(request, 'register.html', {'form': form.as_p(), 'bad_username': bad_username})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return HttpResponseRedirect("/")
