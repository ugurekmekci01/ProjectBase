from django.db import models
from ..inventory_management.models import Inventory

class WorkOrder(models.Model):
    work_order_number = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    assigned_to = models.CharField(max_length=50)
    due_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    related_equipment = models.ForeignKey(Inventory, on_delete=models.CASCADE)
