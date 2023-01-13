from django.shortcuts import render
from .models import Recipe


def all_desserts(request):
    """
    Renders products.html and displays
    all products on website. Search and
    filter option will also be included.
    """
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)
