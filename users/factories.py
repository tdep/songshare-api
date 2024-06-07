import factory
from factory.django import DjangoModelFactory

from .models import SongShareUser, SongShareUserGroup


class UserFactory(DjangoModelFactory):
    class Meta:
        model = SongShareUser

    username = factory.Faker('words', unique=True)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False
    user_type = 'subscriber'
    email = factory.Faker('safe_email')
    phone_number = factory.Faker('phone_number')
    bio = factory.Faker('catch_phrase')
    avatar = "https://picsum.photos/200/300"


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = SongShareUserGroup

    name = "Artist Group"
    description = "This is the artist group."
