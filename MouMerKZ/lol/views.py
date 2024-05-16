from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from lol.models import FlashGames

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


def index(request):
    posts = Lol.objects.all()
    return render(request, 'lol/index.html',
                  {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0})


def about(request):
    return render(request, 'lol/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render(request, 'lol/contact.html', {'menu': menu, 'title': 'Обратная связь'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Lol, slug=post_slug)
    flash_games = post.flash_games.all()

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
        'flash_games': flash_games,
    }

    return render(request, 'lol/post.html', context=context)


def show_category(request, cat_id):
    posts = Lol.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'lol/index.html', context=context)


def game_view(request):
    flash_games = FlashGames.objects.all()
    return render(request, 'lol/game.html', {'flash_games': flash_games})


