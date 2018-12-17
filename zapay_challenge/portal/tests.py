import pytest
from django.test import TestCase
from portal.views import *

# Create your tests here.
class TestPages(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_access_last_lanches_page(request):
        url = reverse('last')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'last.html')

    def test_access_next_lanches_page(request):
      url = reverse('next')
      response = self.client.get(url)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'next.html')
    def test_access_past_lanches_page(request):
      url = reverse('past')
      response = self.client.get(url)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'past.html')
