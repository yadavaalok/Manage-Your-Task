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

    def test_get_create_event(self):
        url = reverse('addevent')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_create_event(self):
        url = reverse('addevent')
        payload = {
            "title" : "Sample Event Title",
            "eventtype" : "Exhibition",
            "datetime": "2023-08-04T04:00",
            "description": "Sample Description"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)

"""    def test_list_event(self):
        event1 = {
            "title" : "Event 1",
            "eventtype" : "Festival",
            "datetime": "2023-08-04T04:00",
            "description": "Event 1 Description"
        }
        event2 = {
            "title" : "Event 2",
            "eventtype" : "Exhibition",
            "datetime": "2023-10-04T05:00",
            "description": "Event 2 Description"
        }

        url1 = reverse('addevent')
        r1 = self.client.post(url1, event1)
        r2 = self.client.post(url1, event2)

        url = reverse('allevents')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)"""