from django.shortcuts import render


def index(request):
    """
    View to render index.html template
    Finds and sends reviews data to index.html
    """
    context = {}

    return render(request, 'home/index.html', context)
