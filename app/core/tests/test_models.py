"""
Test for Models.
"""
from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test Models"""

    def test_create_event(self):
        """Test creating event successfully"""
        event = models.Event.objects.create(
            event_title = "Sample Event Title",
            event_type = "festival",
            event_date = "2023-08-25 16:00",
            event_description = "Sample Event Description"
        )

        self.assertEqual(str(event), event.event_title)
