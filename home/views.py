from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from desserts.models import Category
from .forms import CategoryForm


def index(request):
    """
    View to render index.html template
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/index.html', context)


def add_category(request):
    """Add Category"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form = category_form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add category. Please try again.')
    else:
        category_form = CategoryForm()

    template = 'home/add_category.html'
    context = {
        'category_form': category_form,
    }

    return render(request, template, context)


def update_category(request, pk_id):
    """Update Category"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, id=pk_id)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        if category_form.is_valid():
            category_form = category_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update category. Please try again.')
    else:
        category_form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'home/update_category.html'
    context = {
        'category_form': category_form,
        'category': category,
    }

    return render(request, template, context)


def delete_category(request, pk_id):
    """Delete Category"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    # get category id
    category = get_object_or_404(Category, id=pk_id)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category successfully deleted!')
        return redirect('home')

    template = 'home/delete_category.html'

    context = {
        'category': category,
    }

    return render(request, template, context)