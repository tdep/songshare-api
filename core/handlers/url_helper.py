from django.contrib import admin

from users.models import SongShareUser
from articles.models import Article


def register_app_models():
    models = [SongShareUser, Article]
    for model in models:
        admin.site.register(model)
