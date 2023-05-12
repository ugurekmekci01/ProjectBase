from django.db import models

# Create your models here.
class Inventory(models.Model):
    part_number = models.CharField(max_length=50)
    description = models.TextField()
    current_stock = models.IntegerField()
    minimum_stock = models.IntegerField()
    location = models.CharField(max_length=50)
