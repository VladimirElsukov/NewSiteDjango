from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from .models import Flowers, Category, TagPost



menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},

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


def index(request):
    posts = Flowers.published.all()
    data = {
        'title': 'Доставка цветов Москва',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'flowers/index.html', context=data)


def about(request):
    return render(request, 'flowers/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Flowers, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'flowers/post.html', data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    post = Flowers.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': post,
        'cat_selected': category.pk,
    }
    return render(request, 'flowers/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Flowers.Status.PUBLISHED)

    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'flowers/index.html', context=data)










