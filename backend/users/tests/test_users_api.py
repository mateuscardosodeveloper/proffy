from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient


USERS_URL = reverse('users:create')


def create_users(**params):
    return get_user_model().objects.create_users(**params)


class PublicUsersApiTests(TestCase):
    """Test privated users API"""

    def setUp(self):
        self.client = APIClient()


class PrivateUsersApiTests(TestCase):
    """Test to users private"""

    def setUp(self):
        self.client = APIClient()

    def test_to_create_new_users_successful(self):
        """Test to created new users successful"""
        payload = {
            'name': 'Mateus Cardoso',
            'avatar': 'https://avatars.githubusercontent.com/u/14567480?v=4',
            'whatsapp': '999999999',
            'bio': 'Great proffessor in programation using language Python',
        }
        response = self.client.post(USERS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
