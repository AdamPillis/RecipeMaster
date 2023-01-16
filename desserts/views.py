from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
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
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                recipes = recipes.annotate(lower_name=Lower('name'))
                # sort by name rather than id, using double under score to
                # gain access into related object model
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            recipes = recipes.order_by(sortkey)
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
                print('not found')
                messages.add_message(
                    request,
                    messages.ERROR,
                    "No search criteria recognized, please try again.")
                return redirect(reverse('recipes'))

            queries = Q(name__icontains=query) | Q(
                step_guide__icontains=query)
            recipes = recipes.filter(queries)

    chosen_sorting = f'{sort}_{direction}'

    context = {
        'recipes': recipes,
        'search_word': query,
        'chosen_categories': categories,
        'chosen_sorting': chosen_sorting,
    }

    return render(request, 'recipes/recipes.html', context)
