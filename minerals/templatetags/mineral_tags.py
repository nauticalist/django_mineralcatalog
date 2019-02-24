from django import template

from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('minerals/filters.html')
def filter_by():
    """
    Returns distinct dictionay of mineral groups
    """
    groups = Mineral.objects.values_list(
        'group', flat=True
    ).order_by().distinct()
    categories = Mineral.objects.values_list(
        'category', flat=True
    ).order_by().distinct()
    colors = Mineral.objects.values_list(
        'color', flat=True
    ).order_by().distinct()
    context = {
        'groups': groups,
        'categories': categories,
        'colors': colors,
    }
    return context
