from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from .forms import RegistrationForm
from users.models import SongShareUser

# =================================================Admin Views====================================================


class UserViewSet(viewsets.ViewSet):
    """
    List or retrieve users.
    """
    serializer_class = UserSerializer
    queryset = SongShareUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = SongShareUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SongShareUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# =================================================User Views====================================================

