from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'user_type', 'is_staff',
                  'is_superuser', 'username', 'email',
                  'phone_number', 'first_name', 'last_name',
                  'created_at', 'bio', 'avatar', 'articles']
