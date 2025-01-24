from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


flower_dict = [
    {
        'id': 1,
        'title': 'Роза',
        'content': 'Роза – королева цветов, символ красоты и любви.',
        'published': True
    },
    {
        'id': 2,
        'title': 'Тюльпан',
        'content': 'Тюльпаны – яркие весенние цветы, символизирующие возрождение и начало новой жизни.',
        'published': False
    },
    {
        'id': 3,
        'title': 'Лилия',
        'content': 'Лилии – элегантные цветы, часто используемые в свадебных букетах и символизирующие чистоту и благородство.',
        'published': True
    },
    {
        'id': 4,
        'title': 'Ромашка',
        'content': 'Ромашки – простые, но милые цветы, ассоциирующиеся с летом и детством.',
        'published': False
    },
    {
        'id': 5,
        'title': 'Пион',
        'content': 'Пионы – пышные цветы, символизирующие богатство, честь и счастье.',
        'published': True
    },
]


def index(request):
    # t = render_to_string('flowers/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': flower_dict,
            }
    return render(request, 'flowers/index.html', context=data)

def about(request):
    return render(request, 'flowers/about.html', {'title': 'О нас'})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id: {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")



def page_not_found(request, exception):
     return HttpResponseNotFound("<h1>Страница не найдена</h2>")








# def categories(request, cat_id):
#     return HttpResponse(f"<h3>Категории</h3> <p>id: {cat_id}</p>")
#
# def categories_slug(request, cat_slug):
#     if request.GET:
#         print(request.GET)
#     else:
#         print("Данных нет")
#     return HttpResponse(f"<h3>Категории</h3> <p>slug: {cat_slug}</p>")
#
# def archive(request, year):
#     if year > 2025:
#         return redirect('cats', 'buket')
#     return HttpResponse(f"<h3>Архив по годам</h3> <p>{year}</p>")
# # Create your views here.
#
#
#