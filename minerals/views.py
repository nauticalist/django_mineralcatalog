from django.shortcuts import render, get_object_or_404

from .models import Mineral


def home(request):
    """
    Display all minerals on home page
    """
    data = Mineral.objects.all()
    context = {
        'minerals': data,
    }
    return render(request, 'minerals/home.html', context)


def mineral_view(request, pk):
    """
    Display requested minerals details
    """
    data = get_object_or_404(Mineral, pk=pk)
    context = {
        'mineral': data,
    }
    return render(request, 'minerals/view.html', context)

def random_mineral(request):
    data = Mineral.get_random()
    context = {
        'mineral': data,
    }
    return render(request, 'minerals/view.html', context)
