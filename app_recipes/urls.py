from django.contrib import admin
from django.urls import path

from app_recipes.views import contato, fotos, home, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('fotos/', fotos)
]
