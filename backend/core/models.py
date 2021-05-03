from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    whatsapp = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Classes(models.Model):
    subject = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class ClassSchedule(models.Model):
    week_day = models.IntegerField()
    initial_hour_lesson = models.IntegerField()
    final_hour_lesson = models.IntegerField()
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __repr__(self):
        return self.week_day
