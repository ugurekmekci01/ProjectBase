from django.db import models

# Create your models here.

class DocumentManagement(models.Model):
    title = models.CharField(max_length=100)
    document_type = models.CharField(max_length=20)
    description = models.TextField()
    file_path = models.CharField(max_length=255)
    uploaded_date = models.DateField()
    uploaded_by = models.CharField(max_length=50)
