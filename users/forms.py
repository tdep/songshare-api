from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from phonenumber_field.formfields import PhoneNumberField
from .models import SongShareUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password_strength = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )
    phone_number = PhoneNumberField()
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    bio = forms.Textarea()
    avatar = forms.ImageField()

    class Meta:
        model = SongShareUser
        fields = ('username', 'email', 'phone_number', 'user_type')
