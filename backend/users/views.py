from rest_framework import generics

from users import serializers


class CreateUsersView(generics.CreateAPIView):
    """Create a new users in the system"""
    serializer_class = serializers.UsersSerializer
