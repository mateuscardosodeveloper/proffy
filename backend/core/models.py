from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    whatsapp = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name
