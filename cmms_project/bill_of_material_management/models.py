from django.db import models

# Create your models here.
from django.db import models
from ..inventory_management.models import Inventory

class BillOfMaterial(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    part_number = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
