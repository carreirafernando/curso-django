from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:id>/', views.recipes, name='recipes')
]
