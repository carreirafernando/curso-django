from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe


# Create your views here.
def index(request):
    return render(request, 'recipes/pages/index.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })

def recipes(request, id):
    return render(request, 'recipes/pages/recipes-views.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })