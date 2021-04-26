from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Users

from users import serializers


USERS_URL = reverse('users:users-list')


""" def create_users(**params):
    return get_user_model().objects.create_users(**params) """


def detail_url(users_id):
    """Return detail URL"""
    return reverse('users:users-detail', args=[users_id])


def sample_users(
    name='mateus',
    avatar='blahblah',
    whatsapp=123456789,
    bio='blah blah'
):
    return Users.objects.create(
        name=name, avatar=avatar, whatsapp=whatsapp, bio=bio
    )


class PublicUsersApiTests(TestCase):
    """Test privated users API"""

    def setUp(self):
        self.client = APIClient()


class PrivateUsersApiTests(TestCase):
    """Test to users private"""

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='test',
            email='test@email.com',
            password='test12345'
        )
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

    def test_to_create_new_users_failed(self):
        """Test create new users failed"""
        payload = {
            'name': '',
            'avatar': 'https://avatars.githubusercontent.com/u/14567480?v=4',
            'whatsapp': '123456789',
            'bio': '',
        }
        response = self.client.post(USERS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_to_viewer_users_registrated(self):
        """Test to see users registrated"""
        users = sample_users(self.user)

        url = detail_url(users.id)
        response = self.client.get(url)

        serializer = serializers.UsersSerializer(users)
        self.assertEqual(response.data, serializer.data)

    def test_partial_update_users(self):
        """Test to partial updated users"""
        users = sample_users(self.user)
        payload = {
            'name': 'Henrique',
        }

        url = detail_url(users.id)
        self.client.patch(url, payload)

        users.refresh_from_db()
        self.assertEqual(users.name, payload['name'])

    def test_full_update_users(self):
        """Test to upload all dates in users"""
        users = sample_users(self.user)
        payload = {
            'name': 'Cardoso',
            'avatar': 'https://avatars.githubusercontent.com/u/14567480?v=4',
            'whatsapp': 987654321,
            'bio': 'the best professor from amarican solth Irra'
        }

        url = detail_url(users.id)
        self.client.put(url, payload)

        users.refresh_from_db()
        self.assertEqual(users.name, payload['name'])
        self.assertEqual(users.avatar, payload['avatar'])
        self.assertEqual(users.whatsapp, payload['whatsapp'])
        self.assertEqual(users.bio, payload['bio'])
