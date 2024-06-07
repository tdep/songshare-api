from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # to make this a hyperlink, change to Hyperlinked

    class Meta:
        model = Article
        fields = ['id', 'published', 'title', 'author', 'description', 'article_image', 'content', 'shares']
        read_only_fields = ['id', 'published', 'author', 'shares']


class FavoriteArticleSerializer(serializers.ModelSerializer):
    # Logic for user likes goes here
    pass
