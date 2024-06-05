from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType
from django_resized import ResizedImageField


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        max_length=100,
        blank=False,
        default='',
        unique=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    is_staff = models.BooleanField(default=False)
    email = models.CharField(
        max_length=256,
        blank=False,
        default='',
        unique=True)
    phone_number = models.CharField(
        max_length=20,
        blank=False,
        default='',
        unique=True)
    bio = models.TextField(max_length=2000)
    avatar = ResizedImageField(
        size=[640, 640],
        crop=['middle', 'center'],
        upload_to='images/',
        force_format='PNG')

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ['last_name']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Artist(User):  # To be expanded
    # Articles
    # Events
    # Songs
    # Num_Subscribers
    # Messages
    # Permissions: [
    #   view/create/update/delete: profile/songs/events/messages;
    #   view: subscribers/articles; ]
    pass


class Subscriber(User):
    # Favorite Songs
    # Events Attended/ing
    # Messages
    # Permissions: [
    #   view/create/update/delete: profile(self);
    #   view/update: events/songs/articles/artists (favs/seats/follows); ]
    pass


class Admin(User):
    # Articles (Author)
    # Events
    # Permissions: [
    #   view/create/update/delete: profile(self)/articles/events;
    #   view/update/delete: profile (as admin)/messages;
    pass
