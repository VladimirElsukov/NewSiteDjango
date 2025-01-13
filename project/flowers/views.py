from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Страница приложения flowers</h1>")

def categories(request, cat_id):
    return HttpResponse(f"<h3>Категории</h3> <p>id: {cat_id}</p>")

def categories_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    else:
        print("Данных нет")
    return HttpResponse(f"<h3>Категории</h3> <p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2025:
        raise Http404
    return HttpResponse(f"<h3>Архив по годам</h3> <p>{year}</p>")
# Create your views here.


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h2>")