from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return HttpResponse('Sobre 3')

def contato(request):
    return HttpResponse('Contato 3')