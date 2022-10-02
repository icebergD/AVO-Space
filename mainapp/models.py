from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coins = models.IntegerField()

class Merch(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

class Donate(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.IntegerField()