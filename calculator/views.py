from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 100,
    },
}

def index(request):
    recipes = DATA.keys()
    return render(request, 'calculator/index.html', {'recipes': recipes})

def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))  # Получаем порции из параметров запроса
    recipe = DATA.get(recipe_name)
    if recipe:
        recipe = {key: value * servings for key, value in recipe.items()}
        return render(request, 'calculator/recipe.html', {'recipe': recipe})
    else:
        return render(request, 'calculator/recipe.html', {'error': 'Рецепт не найден'})