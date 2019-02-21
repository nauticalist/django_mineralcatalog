from django import template

from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('minerals/nav_mineral_groups.html')
def mineral_groups():
    """
    Returns distinct dictionay of mineral groups
    """
    groups = Mineral.objects.values(
        'group'
    ).order_by().distinct()

    return {'groups': groups}
