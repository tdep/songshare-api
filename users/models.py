from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=256, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    bio = models.TextField()
