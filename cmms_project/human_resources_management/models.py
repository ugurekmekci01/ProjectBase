from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
