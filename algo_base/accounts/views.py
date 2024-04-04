from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from algo import views
from algo.models import *
from .models import *


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


def profile(request, username):
    user = User.objects.get(username=username)
    problems = user.profile.problems.all()
    problems_count = Problem.objects.count()
    algorithms = Algorithm.objects.all()

    data = {
        'title': views.TITLE,
        'user': user,
        'page': 'profile',
        'problems': problems,
        'algorithms': algorithms,
        'problems_count': problems_count,
        'percent': int(len(problems)/problems_count * 100)
    }

    # Алгоритм Евклида: 10
    # Бинарный поиск по массиву: 5
    # Алгоритм Карацубы: 1

    # Algorithm понадобится однозначно, чтобы взять название
    # Также понадобятся проблемы, чтобы посчитать их количество
    # Значит их нужно как-то соединить, например джоином

    return render(request, 'profile.html', data)

