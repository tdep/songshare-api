from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # to make this a hyperlink, change to Hyperlinked

    class Meta:
        model = Article
        fields = ['id', 'owner', 'published', 'title', 'content', 'shares']
