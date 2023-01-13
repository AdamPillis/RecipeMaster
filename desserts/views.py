from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Recipe, Category


def all_desserts(request):
    """
    Renders products.html and displays
    all products on website. Search and
    filter option will also be included.
    """
    recipes = Recipe.objects.all()
    query = None

    if request.GET:
        # splitting into list after commas and filter list who's
        # category name is in the list
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # double underscore for django's built in search
            recipes = recipes.filter(category__name__in=categories)
            # category objects created from search
            # used to display them products.html
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request,
                    "No search criteria recognized, please try again.")
                return redirect(reverse('recipes'))

            queries = Q(name__icontains=query) | Q(
                step_guide__icontains=query)
            recipes = recipes.filter(queries)

    context = {
        'recipes': recipes,
        'search_word': query,
    }

    return render(request, 'recipes/recipes.html', context)
