from .serializers import SongShareTokenObtainPairSerializer, RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import SongShareUser


class SongShareObtainTokenPairView(TokenObtainPairView):

    permission_classes = (AllowAny,)
    serializer_class = SongShareTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):

    queryset = SongShareUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):

    queryset = SongShareUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = SongShareUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

