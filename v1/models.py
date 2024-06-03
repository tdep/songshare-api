from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    class GroupType(models.TextChoices):
        ADMIN = "AD", _("Admin")
        SUBSCRIBER = "SU", _("Subscriber")
        ARTIST = "AR", _("Artist")

    name = models.CharField(max_length=100, blank=False, default='')
    type = models.CharField(
        max_length=2,
        choices=GroupType,
        default=GroupType.SUBSCRIBER
    )


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=False, default='')
    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100, blank=False, default='')
    bio = models.TextField()
    # avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)  # Requires Pillow
    email = models.CharField(max_length=256, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    group = models.CharField(
        max_length=2,
        choices=Group.GroupType,
        blank=False,
        default=Group.GroupType.SUBSCRIBER,
    )


class Article(models.Model):
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    shares = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)
    artist = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        'auth.User',
        models.SET_NULL,
        related_name='articles',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



