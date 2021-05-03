from rest_framework import viewsets

from classschedule import serializers

from core.models import ClassSchedule


class ClassScheduleViewSets(viewsets.ModelViewSet):
    """Manage ClassSchedule in database"""
    serializer_class = serializers.ClassScheduleSerializers
    queryset = ClassSchedule.objects.all()
