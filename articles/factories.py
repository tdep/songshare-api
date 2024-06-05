import factory
from factory.django import DjangoModelFactory

from .models import Article
from users.factories import UserFactory


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker(
        "sentence",
        nb_words=5,
        variable_nb_words=True,
        )
    author = factory.SubFactory(UserFactory)
    description = factory.Faker(
        "sentence",
        nb_words=10,
        variable_nb_words=True
    )
    article_image = "https://picsum.photos/200/300"
    content = factory.Faker("paragraph")
