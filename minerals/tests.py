from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral

from load_fixtures import load_data


class MineralViewTests(TestCase):
    def setUp(self):
        load_data()
        self.mineral1 = Mineral.objects.get(pk=3)
        self.randmineral = Mineral.get_random()

    def test_home_view(self):
        resp = self.client.get(reverse('minerals:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.randmineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/home.html')

    def test_mineral_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={
            'pk': self.mineral1.pk
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral1, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/view.html')

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={
            'pk': self.randmineral.pk
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.randmineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/view.html')
