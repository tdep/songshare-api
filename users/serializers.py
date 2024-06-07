from django.utils.timezone import now
from rest_framework import serializers
from .models import SongShareUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = SongShareUser
        fields = ['id', 'user_type', 'is_staff',
                  'is_superuser', 'username', 'email',
                  'phone_number', 'first_name', 'last_name',
                  'created_at', 'bio', 'avatar', 'articles']
        read_only_fields = ['id', 'created_at']

    def get_days_since_joined(self, obj):
        return (now() - obj.created_at).days


