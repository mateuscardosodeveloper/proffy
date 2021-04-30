from rest_framework import serializers

from core.models import Classes


class ClassSerializers(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = '__all__'
        read_only_fields = ('id', )
