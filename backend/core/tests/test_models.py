from django.test import TestCase

from core import models


class ModelsTests(TestCase):
    """Test for creates new dates in database"""

    def test_users_str(self):
        """Test the users string representation"""
        users = models.Users.objects.create(
            name='Mateus Cardoso',
            avatar='https://avatars.githubusercontent.com/u/14567480?v=4',
            whatsapp='123456789',
            bio='Great proffessor in programation using language Python',
        )
        self.assertEqual(str(users), users.name)
