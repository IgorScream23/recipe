from django.urls import path
from . import views  # Импортируем ваши представления

urlpatterns = [
    # Пример маршрута: замените `recipe_view` на вашу функцию
    path('', views.index, name='index'),  # Маршрут для пустого пути
    path('<str:recipe_name>/', views.recipe_view, name='recipe'),
]