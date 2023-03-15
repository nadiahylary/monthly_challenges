from django.db import models

# Create your models here.


class Challenge(models.Model):
    month = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
