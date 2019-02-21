from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import Http404
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


def list_by_initial(request, initial):
    """
    List minerals by first letter
    """
    try:
        data = Mineral.objects.filter(
            Q(name__startswith=initial))
    except Mineral.DoesNotExist:
        raise Http404
    else:
        context = {
            'minerals': data
        }
    return render(request, 'minerals/home.html', context)
