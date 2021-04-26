from rest_framework import viewsets

from users import serializers

from core.models import Users


""" class CreateUsersView(generics.CreateAPIView):
    Create a new users in the system
    queryset = Users.objects.all()
    serializer_class = serializers.UsersSerializer """


class UsersViewSet(viewsets.ModelViewSet):
    """Manage Users in the database"""
    serializer_class = serializers.UsersSerializer
    queryset = Users.objects.all()

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]
