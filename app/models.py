from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 255, blank=True, null=True)
    def __str__(self):
            return self.name

class County(models.Model):
    city =  models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
            return self.name