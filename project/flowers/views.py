from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Страница приложения flowers</h1>")

def categories(request, cat_id):
    return HttpResponse(f"<h3>Категории</h3> <p>id: {cat_id}</p>")

def categories_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h3>Категории</h3> <p>slug: {cat_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h3>Архив по годам</h3> <p>{year}</p>")
# Create your views here.
