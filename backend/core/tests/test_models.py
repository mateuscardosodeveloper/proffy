from django.test import TestCase

from core import models


def sample_users(name='Cardoso',
                 avatar='foto.url',
                 whatsapp=123456789,
                 bio='blah blah'
                 ):
    """Create sample users"""
    return models.Users.objects.create(
        name=name,
        avatar=avatar,
        whatsapp=whatsapp,
        bio=bio
    )


def sample_classes(users, subject='Matemática', price=100.00):
    """Create sample classes"""
    return models.Classes.objects.create(subject=subject,
                                         price=price, users=users)


class ModelsTests(TestCase):
    """Test for creates new dates in database"""

    def test_users_str(self):
        """Test the Users string representation"""
        self.users = models.Users.objects.create(
            name='Mateus Cardoso',
            avatar='https://avatars.githubusercontent.com/u/14567480?v=4',
            whatsapp='123456789',
            bio='Great proffessor in programation using language Python',
        )
        self.assertEqual(str(self.users), self.users.name)

    def test_classes_str(self):
        """Test the Classes string representation"""
        classes = models.Classes.objects.create(
            subject='História',
            price=50.00,
            users=sample_users()
        )

        self.assertEqual(str(classes), classes.subject)


"""     def test_classshedule_int(self):
        Test the ClassSchedule integer representation
        class_schedule = models.ClassSchedule.objects.create(
            week_day=1,
            initial_hour_lesson=10.00,
            final_hour_lesson=11.00,
            classes=sample_classes()
        ) """
