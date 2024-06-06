from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from users.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .forms import RegistrationForm

User = get_user_model()

# =================================================Admin Views====================================================


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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })

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
