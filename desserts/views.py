from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Recipe, Category, Ingredient, Linked_recipes
from .forms import RecipeForm, IngredientForm


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


def full_recipe(request, pk_id):
    """
    Renders product_detail.html to display
    all info regarding each specific product
    """
    recipe = get_object_or_404(Recipe, id=pk_id)

    recipes = Recipe.objects.all()

    links = Linked_recipes.objects.all().filter(recipe=recipe)

    ingredients = Ingredient.objects.all().filter(recipe=recipe)

    context = {
        'recipe': recipe,
        'recipes': recipes,
        'ingredients': ingredients,
        'links': links,
    }

    return render(request, 'recipes/full_recipe.html', context)


def add_recipe(request):
    """Add Recipe"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect(reverse('recipes'))
        else:
            messages.error(request, 'Failed to add recipe. Please try again.')
    else:
        recipe_form = RecipeForm()

    template = 'recipes/add_recipe.html'
    context = {
        'recipe_form': recipe_form,
    }

    return render(request, template, context)


def update_recipe(request, pk_id):
    """Update Recipe"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, id=pk_id)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        ingredient_form = IngredientForm(request.POST, request.FILES)
        if all([recipe_form.is_valid(), ingredient_form.is_valid]):
            parent = recipe_form.save(commit=False)
            parent.save()
            child = ingredient_form.save(commit=False)
            if not child.ingredient_name:
                messages.success(request, 'Successfully updated recipe!')
                return redirect(reverse('full_recipe', args=[recipe.id]))
            else:
                child.recipe = parent
                child.save()
                messages.success(request, 'Successfully updated recipe!')
                return redirect(reverse('full_recipe', args=[recipe.id]))
        else:
            messages.error(request, 'Failed to update recipe. Please try again.')
    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientForm()
        messages.info(request, f'You are editing {recipe.name}')

    template = 'recipes/update_recipe.html'
    context = {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'recipe': recipe,
    }

    return render(request, template, context)


def delete_recipe(request, pk_id):
    """Delete Recipe"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    # get recipe id
    recipe = get_object_or_404(Recipe, id=pk_id)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, f'{recipe.name} successfully deleted!')
        return redirect('recipes')

    template = 'recipes/delete_recipe.html'

    context = {
        'recipe': recipe,
    }

    return render(request, template, context)


def delete_ingredient(request, pk_id):
    """Delete Ingredient"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    # get recipe id
    ingredient = get_object_or_404(Ingredient, id=pk_id)

    recipe = ingredient.recipe

    if request.method == 'POST':
        ingredient.delete()
        messages.success(request, f'"{ingredient.ingredient_name}" successfully deleted!')
        return redirect(reverse('full_recipe', args=[recipe.id]))

    template = 'recipes/recipes.html'

    context = {
        'ingredient': ingredient,
    }

    return render(request, template, context)


def delete_linked_recipe(request, pk_id):
    """Delete Linked Recipe"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    # get linked_recipe id
    linked_recipe = get_object_or_404(Linked_recipes, id=pk_id)

    recipe = linked_recipe.recipe

    if request.method == 'POST':
        linked_recipe.delete()
        messages.success(request, f'"{linked_recipe.linked_recipe}" link removed successfully!')
        return redirect(reverse('full_recipe', args=[recipe.id]))

    template = 'recipes/recipes.html'

    context = {
        'linked_recipe': linked_recipe,
    }

    return render(request, template, context)

