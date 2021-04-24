from rest_framework import serializers

from core.models import Users


class UsersSerializer(serializers.ModelSerializer):
    """Serializer for users objects"""

    class Meta:
        model = Users
        fields = '__all__'
