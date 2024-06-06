import random

from django.db import transaction
from django.core.management.base import BaseCommand

from articles.models import Article
from articles.factories import ArticleFactory
from users.models import SongShareUser
from users.factories import UserFactory

NUM_USERS = 20
NUM_ARTICLES = 10


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Article, SongShareUser]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create some users
        users = []
        for _ in range(NUM_USERS):
            user = UserFactory()
            users.append(user)

        # Create some articles
        articles = []
        for _ in range(NUM_ARTICLES):
            author = random.choice(users)
            article = ArticleFactory(author=author)
            articles.append(article)
