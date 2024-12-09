from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/index.html', context={
        'recipes': recipes
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes
    })

def recipes(request, id):
    return render(request, 'recipes/pages/recipes-views.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })