from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]

def index(request):
    posts = Lol.objects.all()
    return render(request, 'lol/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'lol/about.html', {'menu': menu, 'title': 'О сайте'})


def contact (request):
    return HttpResponse("Обратная связь")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post (request, post_id):
    return HttpResponse(f"Отображение поста с id = {post_id}")
