from django.urls import reverse
from django.test import TestCase

from .models import Mineral

from load_fixtures import load_data


class MineralViewTests(TestCase):
    def setUp(self):
        load_data()
        self.mineral1 = Mineral.objects.get(pk=3)
        self.mineral_starts_with_c = Mineral.objects.get(name='Calaverite')
        self.randmineral = Mineral.get_random()

    def test_home_view(self):
        resp = self.client.get(reverse('minerals:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
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

    def test_list_by_initial_view(self):
        resp = self.client.get(reverse('minerals:list_by_initial', kwargs={
            'initial': 'c'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_starts_with_c, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/home.html')

    def test_search_view(self):
        resp = self.client.get(reverse('minerals:search'), {
            'keyword': 'calaver'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_starts_with_c, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/home.html')

    def test_filter_by_view(self):
        # Test group filters
        resp_group = self.client.post(reverse('minerals:filter_by'), {
            'filter_field': 'groups',
            'groups': 'Other',
        }, enforce_csrf_checks=True)
        self.assertEqual(resp_group.status_code, 200)
        self.assertIn(self.mineral_starts_with_c,
                      resp_group.context['minerals'])
        self.assertTemplateUsed(resp_group, 'minerals/home.html')
        # Test category filters
        resp_category = self.client.post(reverse('minerals:filter_by'), {
            'filter_field': 'categories',
            'categories': 'Halide',
        }, enforce_csrf_checks=True)
        self.assertEqual(resp_category.status_code, 200)
        self.assertIn(self.mineral1, resp_category.context['minerals'])
        self.assertTemplateUsed(resp_category, 'minerals/home.html')
        # Test color filters
        resp_color = self.client.post(reverse('minerals:filter_by'), {
            'filter_field': 'colors',
            'colors': 'Brass yellow to silver white',
        }, enforce_csrf_checks=True)
        self.assertEqual(resp_color.status_code, 200)
        self.assertIn(self.mineral_starts_with_c,
                      resp_color.context['minerals'])
        self.assertTemplateUsed(resp_color, 'minerals/home.html')
