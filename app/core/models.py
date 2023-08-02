"""
Define all models here
"""
from django.db import models


class Event(models.Model):
    EVENT_TYPES = [
        ("conference", "conference"),
        ("seminar", "seminar"),
        ("company party or meeting", "company party or meeting"),
        ("product or service launch", "product or service launch"),
        ("wedding", "wedding"),
        ("festival", "festival"),
        ("exhibition", "exhibition"),
        ("charity event", "charity event"),
        ("sport and competition", "sport and competition"),
    ]
    event_title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_date = models.DateTimeField()
    event_description = models.TextField()

    def __str__(self):
        return self.event_title
