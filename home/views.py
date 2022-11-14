from django.shortcuts import render
from desserts.models import Category


def index(request):
    """
    View to render index.html template
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/index.html', context)
