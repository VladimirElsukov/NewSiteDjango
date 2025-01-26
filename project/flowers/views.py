from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {
        'id': 1,
        'title': 'Розы',
        'content': '''Роза – цветок, который символизирует любовь, красоту и благородство. Это одно из самых древних растений, известных человеку. Род роз насчитывает около 150 видов, произрастающих в разных уголках мира. Их разнообразие поражает: от миниатюрных до крупных кустарников, от нежного белого цвета до насыщенного бордового оттенка. Розы выращивают как для украшения садов, так и для создания парфюмерии. Аромат розы используется в производстве духов, кремов и других косметических средств. В культуре многих народов роза занимает особое место, символизируя страсть, чистоту и вечную молодость.''',
        'is_published': True
    },
    {
        'id': 2,
        'title': 'Тюльпаны',
        'content': 'Тюльпаны – яркие весенние цветы, символизирующие возрождение и начало новой жизни.',
        'is_published': False
    },
    {
        'id': 3,
        'title': 'Лилии',
        'content': 'Лилии – элегантные цветы, часто используемые в свадебных букетах и символизирующие чистоту и благородство.',
        'is_published': True
    },
    {
        'id': 4,
        'title': 'Ромашки',
        'content': 'Ромашки – простые, но милые цветы, ассоциирующиеся с летом и детством.',
        'is_published': False
    },
    {
        'id': 5,
        'title': 'Пионы',
        'content': 'Пионы – пышные цветы, символизирующие богатство, честь и счастье.',
        'is_published': True
    },
]

cats_db = [
    {'id': 1, 'name': 'Цветы'},
    {'id': 2, 'name': 'Букеты'},
    {'id': 3, 'name': 'Композиции'},
    {'id': 4, 'name': 'Корзины с цветами'},
    {'id': 5, 'name': 'Упаковка и аксессуары'},
]

def index(request):
    data = {
        'title': 'Доставка цветов Москва',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'flowers/index.html', context=data)


def about(request):
    return render(request, 'flowers/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



