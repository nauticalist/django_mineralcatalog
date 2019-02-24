from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .models import Mineral


def home(request):
    """
    Display all minerals on home page
    """
    data = Mineral.objects.filter(
        Q(name__startswith='A')
    )
    context = {
        'current': 'A',
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
            'minerals': data,
            'current': initial,
        }
    return render(request, 'minerals/home.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    data = Mineral.objects.filter(
        Q(name__icontains=keyword) |
        Q(image_caption__icontains=keyword) |
        Q(category__icontains=keyword) |
        Q(formula__icontains=keyword) |
        Q(strunz_classification__icontains=keyword) |
        Q(crystal_system__icontains=keyword) |
        Q(unit_cell__icontains=keyword) |
        Q(color__icontains=keyword) |
        Q(crystal_symmetry__icontains=keyword) |
        Q(cleavage__icontains=keyword) |
        Q(mohs_scale_hardness__icontains=keyword) |
        Q(luster__icontains=keyword) |
        Q(streak__icontains=keyword) |
        Q(diaphaneity__icontains=keyword) |
        Q(optical_properties__icontains=keyword) |
        Q(group__icontains=keyword) |
        Q(refractive_index__icontains=keyword) |
        Q(crystal_habit__icontains=keyword) |
        Q(specific_gravity__icontains=keyword)
    )
    context = {
        'keyword': keyword,
        'minerals': data,
    }
    return render(request, 'minerals/home.html', context)


def filter_by(request):
    if request.method == 'POST':
        filter_field = request.POST.get('filter_field')
        if not filter_field:
            return HttpResponseRedirect(reverse('minerals:home'))

        group = request.POST.get('groups')
        category = request.POST.get('categories')
        color = request.POST.get('colors')
        if filter_field == 'groups' and group is not None:
            data = Mineral.objects.filter(
                Q(group=group))
        elif filter_field == 'categories' and category is not None:
            data = Mineral.objects.filter(
                Q(category=category))
        elif filter_field == 'colors' and color:
            data = Mineral.objects.filter(
                Q(color=color))
        context = {
            'filter': filter_field,
            'group': group,
            'category': category,
            'color': color,
            'minerals': data,
        }
        return render(request, 'minerals/home.html', context)
    else:
        return HttpResponseRedirect(reverse('minerals:home'))
