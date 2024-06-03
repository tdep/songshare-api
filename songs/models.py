from django.db import models


class Song(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    soundcloud_url = models.CharField(max_length=256, blank=True, default='')
    favorites = models.IntegerField(default=0)
