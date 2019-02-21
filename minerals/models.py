from django.db import models
from django.db.models import Max

import random


class Mineral(models.Model):
    name = models.CharField(max_length=100)
    image_filename = models.CharField(max_length=255, null=True, blank=True)
    image_caption = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    formula = models.CharField(max_length=500, null=True, blank=True)
    strunz_classification = models.CharField(
        max_length=255, null=True, blank=True)
    crystal_system = models.CharField(max_length=255, null=True, blank=True)
    unit_cell = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    crystal_symmetry = models.CharField(max_length=255, null=True, blank=True)
    cleavage = models.CharField(max_length=255, null=True, blank=True)
    mohs_scale_hardness = models.CharField(
        max_length=255, null=True, blank=True)
    luster = models.CharField(max_length=255, null=True, blank=True)
    streak = models.CharField(max_length=255, null=True, blank=True)
    diaphaneity = models.CharField(max_length=255, null=True, blank=True)
    optical_properties = models.CharField(
        max_length=255, null=True, blank=True)
    refractive_index = models.CharField(max_length=255, null=True, blank=True)
    crystal_habit = models.CharField(max_length=255, null=True, blank=True)
    specific_gravity = models.CharField(max_length=255, null=True, blank=True)
    group = models.CharField(max_length=255, null=True, blank=True)

    def __repr__(self):
        return self.name

    @classmethod
    def get_random(cls):
        max_id = cls.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            mineral = Mineral.objects.filter(pk=pk).first()
            if mineral:
                return mineral
