from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from classschedule import serializers
from core.models import Users, Classes, ClassSchedule

CLASS_SCHEDULE_URL = reverse('class_schedule:classschedule-list')


def sample_users(name='test', avatar='test.url', whatsapp=123, bio='blah'):
    """Create sample users"""
    return Users.objects.create(
        name=name,
        avatar=avatar,
        whatsapp=whatsapp,
        bio=bio
    )


def sample_class_shedule(classes, week_day=2, initial_hour_lesson=12,
                         final_hour_lesson=13):
    """Create sample class schedule"""
    return ClassSchedule.objects.create(
        week_day=week_day,
        initial_hour_lesson=initial_hour_lesson,
        final_hour_lesson=final_hour_lesson,
        classes=classes
    )


def detail_url(class_schedule_id):
    """Detail url for ClassSchedule"""
    return reverse(
        'class_schedule:classschedule-detail',
        args=[class_schedule_id]
    )


class PrivateClassScheduleTests(TestCase):
    """Test private ClassSchedule"""

    def setUp(self):
        self.classes = Classes.objects.create(
            subject='Português',
            price=90.00,
            users=sample_users()
        )
        self.client = APIClient()

    def test_new_class_schedule_successful(self):
        """Test to create new ClassSchedule success"""
        payload = {
            'week_day': 2,
            'initial_hour_lesson': 12,
            'final_hour_lesson': 13,
            'classes': self.classes.id
        }
        response = self.client.post(CLASS_SCHEDULE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_new_class_schedule_failed(self):
        """Test to create new ClassSchedule failed"""
        payload = {
            'week_day': ''
        }
        response = self.client.post(CLASS_SCHEDULE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_viewer_class_schedule(self):
        """Test to see ClassSchedule registrated"""
        class_schedule = sample_class_shedule(self.classes)

        url = detail_url(class_schedule.id)
        response = self.client.get(url)

        serializer = serializers.ClassScheduleSerializers(class_schedule)
        self.assertEqual(response.data, serializer.data)

    def test_update_partial_class_schedule(self):
        """Test to updated partial ClassSchedule"""
        class_schedule = sample_class_shedule(self.classes)
        payload = {
            'week_day': 7
        }

        url = detail_url(class_schedule.id)
        self.client.patch(url, payload)

        class_schedule.refresh_from_db()
        self.assertEqual(class_schedule.week_day, payload['week_day'])

    def test_full_update_class_schedule(self):
        """Test full updated ClassSchedule"""
        class_schedule = sample_class_shedule(self.classes)
        payload = {
            'week_day': 6,
            'initial_hour_lesson': 8,
            'final_hour_lesson': 11,
            'classes': self.classes.id
        }

        url = detail_url(class_schedule.id)
        self.client.put(url, payload)

        class_schedule.refresh_from_db()
        self.assertEqual(class_schedule.week_day, payload['week_day'])
        self.assertEqual(class_schedule.initial_hour_lesson,
                         payload['initial_hour_lesson'])
        self.assertEqual(class_schedule.final_hour_lesson,
                         payload['final_hour_lesson'])
        self.assertEqual(class_schedule.classes.id, payload['classes'])
