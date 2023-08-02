"""
Test for Views.
"""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """Testing Views"""

    def test_index_get(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
