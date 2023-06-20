from django.forms import PasswordInput
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from config import super_password_conf


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CreateSuperUserSerializer(serializers.ModelSerializer):
    super_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'super_password']

    def validate_password(self, value):
        super_password = self.initial_data.get('super_password')
        if super_password != super_password_conf:
            raise ValidationError("Invalid super password.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        super_password = validated_data.pop('super_password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
