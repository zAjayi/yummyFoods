from django.db import models

class Starters(models.Model):
    name = models.CharField(max_length=400)
    ingredients = models.CharField(max_length=1000)
    price = models.CharField(max_length=400)
    imageUrl = models.CharField(max_length=1000)
