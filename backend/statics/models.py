from django.db import models

# Create your models here.
class Machine(models.Model):
    # override email field as unique
    name = models.CharField(max_length=20, blank=True, default='')
    image = models.ImageField(upload_to='machine/', blank=True)
    description = models.TextField()

class School(models.Model):
    # override email field as unique
    name = models.CharField(max_length=20, blank=True, default='')
    logo = models.ImageField(upload_to='school/', blank=True)