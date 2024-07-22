from django.shortcuts import render, reverse
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'lavash_pizza': {
        'лаваш армянский, шт': 0.5,
        'яйца, шт': 2,
        'помидоры, шт': 1,
        'кетчуп': 'по вкусу',
        'колбаса, кг': 0.1,
        'сыр моцарелла, кг': 0.05,
        'как приготовить': 'руками =)'
    }
    # можете добавить свои рецепты ;)
}


# def omlet(request):
#     count = request.GET('servings')
#     return HttpResponse(f'')
#
#
# def pasta(request):
#     count = request.GET('servings')
#     return HttpResponse(f'')
#
#
# def buter(request):
#     count = request.GET('servings')
#     return HttpResponse(f'')


def recipe(request, recipe):
    if recipe:
        context = {'recipe': ''}
        for name_recipe, ingredients in DATA.items():
            if recipe == name_recipe:
                text_recipe = {}
                for name_ingredient, count in ingredients.items():
                    servings = request.GET.get('servings')
                    if servings and not isinstance(count, str):
                        servings = int(servings)
                        if servings >= 1:
                            count = round((count * int(servings)), 1)
                            if isinstance(count, float) and count.is_integer():
                                count = int(count)
                        else:
                            return HttpResponse('кажется, вы не голодны :)')
                    text_recipe[name_ingredient] = count
                context['recipe'] = text_recipe
        return render(request, 'calculator/index.html', context)



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
