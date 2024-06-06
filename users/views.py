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


def registration(request):
    if request.method == 'POST':
        # Create a form that has request.POST
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set user's password securely
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

            if password1 == password2:
                user.set_password(password1)
                user.save()

                messages.success(request, f'Your Account has been created {username} ! Proceed to log in.')
                return redirect('login')
            else:
                form.add_error('password2', 'Passwords do not match')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
