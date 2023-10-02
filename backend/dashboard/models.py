from django.db import models


# Create your models here.

class Item(models.Model):
    icons = models.ImageField(required=False)
    name = models.CharField(max_length=256)
    url = models.URLField(max_length=512)
