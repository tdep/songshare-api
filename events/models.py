from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()
    seats = models.IntegerField(default=0)
    event_date = models.DateField(auto_now_add=False)

    class Meta:
        ordering = ['event_date']
