from django.db import models

# Create your models here.
from django.db import models
from ..work_order_management.models import WorkOrder

class QualityManagement(models.Model):
    issue_date = models.DateField()
    issue_description = models.TextField()
    corrective_action = models.TextField()
    status = models.CharField(max_length=20)
    assigned_to = models.CharField(max_length=50)
    due_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    related_work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f"Quality Management {self.id}"
