from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'articles']

# The user serializer might work for all types of users, but we may need specific views for users of different types
