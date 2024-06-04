from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=False, default='', unique=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    is_staff = models.BooleanField(default=False)
    email = models.CharField(max_length=256, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    bio = models.TextField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']


class Artist(User):  # To be expanded
    pass


class Subscriber(User):
    pass


class Admin(User):
    pass
