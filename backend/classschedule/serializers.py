from rest_framework import serializers

from core.models import ClassSchedule


class ClassScheduleSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClassSchedule
        fields = '__all__'
        read_only_fields = ('id', )
