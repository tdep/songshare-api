from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from users.models import Artist
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


User = get_user_model()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve, update, or delete a user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
