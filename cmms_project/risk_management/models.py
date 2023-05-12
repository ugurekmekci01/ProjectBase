from django.db import models

from work_order_management.models import WorkOrder

class Risk(models.Model):
    RISK_TYPE_CHOICES = (
        ('Health', 'Health'),
        ('Safety', 'Safety'),
        ('Environmental', 'Environmental'),
        ('Financial', 'Financial'),
        ('Reputation', 'Reputation'),
    )
    LIKELIHOOD_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    IMPACT_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    RISK_LEVEL_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    risk_type = models.CharField(max_length=50, choices=RISK_TYPE_CHOICES)
    description = models.TextField()
    likelihood = models.CharField(max_length=20, choices=LIKELIHOOD_CHOICES)
    impact = models.CharField(max_length=20, choices=IMPACT_CHOICES)
    risk_level = models.CharField(max_length=20, choices=RISK_LEVEL_CHOICES)
    risk_owner = models.CharField(max_length=50)
    due_date = models.DateField(null=True, blank=True)
    related_work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
