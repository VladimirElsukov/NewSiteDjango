from django import template
import flowers.views as views
from flowers.models import Category, TagPost

register = template.Library()

@register.inclusion_tag('flowers/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('flowers/list_tags.html')
def show_all_tags():
    return {'tag': TagPost.objects.all()}