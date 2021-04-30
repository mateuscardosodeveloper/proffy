from rest_framework import viewsets

from classes import serializers

from core.models import Classes


class ClassesViewSets(viewsets.ModelViewSet):
    """Manage Classes in database"""
    serializer_class = serializers.ClassSerializers
    queryset = Classes.objects.all()
