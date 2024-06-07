from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import SongShareUser


class SongShareTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(SongShareTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=SongShareUser.objects.all())]
    )
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SongShareUser
        fields = ('username', 'password1', 'password2', 'email', 'phone_number', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': False},
            'phone_number': {'required': True},
            'bio': {'required': False},
            'avatar': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields don't match."})

        return attrs

    def create(self, validated_data):
        user = SongShareUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SongShareUser
        fields = ('old_password', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields don't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.id != instance.pk:
            raise serializers.ValidationError({"authorize": "You do not have permission for this user."})

        instance.set_password(validated_data['password1'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = SongShareUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'bio', 'avatar')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': False},
            'email': {'required': True},
            'phone_number': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if SongShareUser.objects.exclude(pk=user.id).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if SongShareUser.objects.exclude(pk=user.id).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def validate_phone_number(self, value):
        user = self.context['request'].user
        if SongShareUser.objects.exclude(pk=user.id).filter(phone_number=value).exists():
            raise serializers.ValidationError({"phone_number": "This phone number is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.id != instance.pk:
            raise serializers.ValidationError({"authorize": "You do not have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.phone_number = validated_data['phone_number']
        instance.bio = validated_data['bio']
        instance.avatar = validated_data['avatar']

        instance.save()

        return instance
