from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    login = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    def __str__ (self):
        return self.login
class CustomUser(AbstractUser):

    def __str__ (self):
        return self.username
# Create your models here.
# Create your models here.
# class User(models.Model):
#     login = models.CharField(max_length=25)
#     password = models.CharField(max_length = 25)
#
#     def __str__(self):
#         return self.login

class UserHistory(models.Model):
    user_id = models.IntegerField(null = True, blank = False)
    age = models.PositiveIntegerField(null=True, blank=False)
    height = models.FloatField(null=True, blank=False)
    weight = models.FloatField(null=True, blank=False)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', blank=False)
    date = models.DateTimeField(auto_now=True)
    bmr = models.FloatField(null = True, blank=False)
    body_mass_index = models.FloatField(null = True, blank=False)
    effectiv_weight = models.FloatField(null=True, blank=False)
    protein = models.FloatField(null=True, blank=False)
    fats = models.FloatField(null=True, blank=False)
    carbohydrates = models.FloatField(null=True, blank=False)

    def __str__(self):
        return str(self.date)