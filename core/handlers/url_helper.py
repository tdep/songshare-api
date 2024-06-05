from django.contrib import admin

from users.models import User, Admin, Artist, Subscriber
from articles.models import Article


def register_app_models():
    models = [User, Admin, Artist, Subscriber, Article]
    for model in models:
        admin.site.register(model)
