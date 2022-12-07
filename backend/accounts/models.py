from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    refresh_token = models.CharField(max_length=513, blank=True, default='')