from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClassScheduleViewSets

route = DefaultRouter()
route.register('class_schedule', ClassScheduleViewSets)

app_name = 'class_schedule'

urlpatterns = [
    path('', include(route.urls)),
]
