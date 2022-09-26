from django.db import models

# Create your models here.

class Users(models.Model):
    nome = models.CharField(blank=False, max_length=300)
    idade = models.PositiveIntegerField(blank=False, max_length=3)
    cidade = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=300)
    password = models.CharField(blank=False, max_length=300)