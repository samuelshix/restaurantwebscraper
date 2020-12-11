from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    food_type = models.CharField(max_length=50)