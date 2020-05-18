from django.db import models
from django.utils import timezone

class event(models.Model):
    event_name = models.CharField(max_length = 200)
    event_location = models.CharField(max_length = 200)
    event_date = models.CharField(max_length = 200)
    event_remarks = models.TextField()
    event_pricing = models.CharField(max_length = 200)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.event_name