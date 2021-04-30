from django.urls import path, include
from rest_framework.routers import DefaultRouter

from classes import views


route = DefaultRouter()
route.register('classes', views.ClassesViewSets)

app_name = 'classes'

urlpatterns = [
    path('', include(route.urls))
]
