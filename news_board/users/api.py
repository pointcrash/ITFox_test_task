from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token

from .models import FoxToken
from .serializers import UserSerializer, CreateSuperUserSerializer
from rest_framework import mixins


class RegistrationView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        token = Token.objects.create(user=user)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class CreateSuperuserView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateSuperUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        token = Token.objects.create(user=user)

        return Response(CreateSuperUserSerializer(user).data, status=status.HTTP_201_CREATED)
