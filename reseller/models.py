from django.db import models

# Create your models here.
class ajax_image(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)