
from django.db import models

# Create your models here.

class registration(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    phn=models.BigIntegerField(unique=True)
    address=models.TextField()
