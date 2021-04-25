from rest_framework import generics, viewsets

from users import serializers

from core.models import Users


class CreateUsersView(generics.CreateAPIView):
    """Create a new users in the system"""
    queryset = Users.objects.all()
    serializer_class = serializers.UsersSerializer
