from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from classes import serializers
from core.models import Users, Classes

CLASSES_URL = reverse('classes:classes-list')


def sample_users(name='test', avatar='foto.url', whatsapp=123, bio='blah'):
    """Create simple users"""
    return Users.objects.create(name=name, avatar=avatar,
                                whatsapp=whatsapp, bio=bio)


def sample_classes(users, subject='Ciências', price=90.00):
    """Create sample classes"""
    return Classes.objects.create(subject=subject, price=price, users=users)


def detail_url(classes_id):
    """See details urls"""
    return reverse('classes:classes-detail', args=[classes_id])


class PrivateClassesTests(TestCase):
    """Test private Classes"""

    def setUp(self):
        self.users = Users.objects.create(
            name='Mateus Cardoso',
            avatar='https://avatars.githubusercontent.com/u/14567480?v=4',
            whatsapp=123456789,
            bio='Great proffessor in programation using language Python'
        )
        self.client = APIClient()

    def test_created_new_classes_successful(self):
        """Test create new classes success"""
        users1 = sample_users()
        payload = {
            'subject': 'Português',
            'price': '100.00',
            'users': [users1.id]
        }
        response = self.client.post(CLASSES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_created_new_classes_failed(self):
        """Test create new classes to failed"""
        payload = {
            'subject': '',
        }
        response = self.client.post(CLASSES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_classes_registrated(self):
        """Test to see dates registrated in classes"""
        classes = sample_classes(self.users)

        url = detail_url(classes.id)
        response = self.client.get(url)

        serializer = serializers.ClassSerializers(classes)
        self.assertEqual(response.data, serializer.data)

    def test_update_partial_classes(self):
        """Test to update partial classes"""
        classes = sample_classes(self.users)
        payload = {
            'subject': 'Artes'
        }

        url = detail_url(classes.id)
        self.client.patch(url, payload)

        classes.refresh_from_db()
        self.assertEqual(classes.subject, payload['subject'])

    def test_full_update_classes(self):
        """Test to update full classes """
        classes = sample_classes(self.users)
        payload = {
            'subject': 'Artes',
            'price': 50.00,
            'users': self.users.id
        }

        url = detail_url(classes.id)
        self.client.put(url, payload)

        classes.refresh_from_db()
        self.assertEqual(classes.subject, payload['subject'])
        self.assertEqual(classes.price, payload['price'])
        self.assertEqual(classes.users.id, payload['users'])
