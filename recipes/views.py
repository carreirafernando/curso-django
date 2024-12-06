from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'recipes/index.html', context={'name': 'Fernando Carreira'})

def contato(request):
    return render(request, 'recipes/contato.html')