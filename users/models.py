from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, GroupManager, Permission
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from articles.permissions import IsAdminOrReadOnly


class BasicUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'subscriber')
        if not email:
            raise ValueError('The Email field must not be empty')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(username, email, password, **extra_fields)


class SongShareUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('subscriber', 'Subscriber'),
        ('artist', 'Artist'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists.",
        }
    )
    email = models.CharField(
        max_length=256,
        blank=False,
        unique=True,
        help_text='Required, 256 characters or fewer.',
        validators=[],
        error_messages={
            'unique': "An account using that email address already exists."
        }
    )
    phone_number = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "An account using that phone number already exists."
        }
    )
    first_name = models.CharField(
        max_length=20,
        blank=True
    )
    last_name = models.CharField(
        max_length=20,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=2000)
    avatar = ResizedImageField(
        size=[640, 640],
        crop=['middle', 'center'],
        upload_to='images/',
        force_format='PNG')

    def is_subscriber(self):
        return self.user_type == 'subscriber'

    def is_artist(self):
        return self.user_type == 'artist'

    def is_admin(self):
        return self.user_type == 'admin'

    objects = BasicUserManager()


class BasicSongShareUserGroupManager(GroupManager):
    def create_artist_group(self):
        group = Group.objects.create(name="Artist Group")
        group.permissions.add(IsAdminOrReadOnly)


class SongShareUserGroup(Group):
    description = models.TextField(blank=True)
    # Articles
    # Events
    # Songs
    # Num_Subscribers
    # Messages
    # Permissions: [
    #   view/create/update/delete: profile/songs/events/messages;
    #   view: subscribers/articles; ]
    pass


class Subscriber(BasicUserManager):
    # Favorite Songs
    # Events Attended/ing
    # Messages
    # Permissions: [
    #   view/create/update/delete: profile(self);
    #   view/update: events/songs/articles/artists (favs/seats/follows); ]
    pass


class Admin(BasicUserManager):
    # Articles (Author)
    # Events
    # Permissions: [
    #   view/create/update/delete: profile(self)/articles/events;
    #   view/update/delete: profile (as admin)/messages;
    pass
