from django.shortcuts import render, redirect, reverse, get_object_or_404

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
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form = category_form.save()
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
