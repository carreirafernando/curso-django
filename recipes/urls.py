from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipes, name='recipes'),
]
