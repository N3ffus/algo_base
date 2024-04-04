from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.
TITLE = 'Алго-база'


def index(request):
    data = {
        'title': TITLE,
        'page': 'home',
        'auth': request.user.is_authenticated,
        'user': request.user,
        'algorithms': len(Algorithm.objects.all()),
        'data_structures': len(DataStructure.objects.all()),
        'articles': len(Article.objects.all()),
        'videos': len(Video.objects.all()),
        'problems': len(Problem.objects.all())
    }
    return render(request, 'index.html', data)


def algorithms(request):
    data = {
        'title': TITLE,
        'themes': AlgoTheme.objects.all(),
        'algorithms': Algorithm.objects.all(),
        'page': 'algorithms',
        'user': request.user
    }
    return render(request, 'algorithms.html', data)


def algorithm(request, id):
    data = {
        'title': TITLE,
        'algorithm': Algorithm.objects.get(id=id),
        'page': 'algorithms',
        'user': request.user
    }
    return render(request, 'algorithm.html', data)


def algorithm_practice(request, id):
    algorithm = Algorithm.objects.get(id=id)
    data = {
        'title': TITLE,
        'algorithm': algorithm,
        'sites': ProblemSite.objects.all(),
        'problems': Problem.objects.filter(tags_algo__in=[algorithm]),
        'page': 'algorithms',
        'user': request.user,
        'id': id,
        'user_problems': request.user.profile.problems.all(),
    }
    return render(request, 'algorithm_practice.html', data)


def algorithm_theory(request, id):
    algorithm = Algorithm.objects.get(id=id)
    data = {
        'title': TITLE,
        'algorithm': algorithm,
        'articles': Article.objects.filter(tag_algo=algorithm),
        'videos': Video.objects.filter(tag_algo=algorithm),
        'page': 'algorithms',
        'user': request.user
    }
    return render(request, 'algorithm_theory.html', data)


def data_structures(request):
    data = {
        'title': TITLE,
        'themes': DataStructureTheme.objects.all(),
        'data_structures': DataStructure.objects.all(),
        'page': 'data_structures',
        'user': request.user
    }
    return render(request, 'data_structures.html', data)


def data_structure(request, id):
    data = {
        'title': TITLE,
        'data_structure': DataStructure.objects.get(id=id),
        'page': 'data_structures',
        'user': request.user
    }
    return render(request, 'data_structure.html', data)


def data_structure_practice(request, id):
    data_structure = DataStructure.objects.get(id=id)
    data = {
        'title': TITLE,
        'data_structure': data_structure,
        'sites': ProblemSite.objects.all(),
        'problems': Problem.objects.filter(tags_ds__in=[data_structure]),
        'page': 'data_structures',
        'user': request.user,
        'user_problems': request.user.profile.problems.all(),
        'id': id
    }
    return render(request, 'data_structure_practice.html', data)


def data_structure_theory(request, id):
    data_structure = DataStructure.objects.get(id=id)
    data = {
        'title': TITLE,
        'data_structure': data_structure,
        'articles': Article.objects.filter(tag_ds=data_structure),
        'videos': Video.objects.filter(tag_ds=data_structure),
        'page': 'data_structures',
        'user': request.user,
    }
    return render(request, 'data_structure_theory.html', data)


def add(request):
    problem = request.POST['problem']
    id_ = int(request.POST['id'])
    page = request.POST['page']
    request.user.profile.problems.add(Problem.objects.get(name=problem))
    request.user.save()

    if page == 'algorithms':
        return algorithm_practice(request, id_)
    elif page == 'data_structures':
        return data_structure_practice(request, id_)


def delete(request):
    problem = request.POST['problem']
    id_ = int(request.POST['id'])
    page = request.POST['page']
    request.user.profile.problems.remove(Problem.objects.get(name=problem))
    request.user.save()

    if page == 'algorithms':
        return algorithm_practice(request, id_)
    elif page == 'data_structures':
        return data_structure_practice(request, id_)