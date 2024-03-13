from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    technology = models.CharField(max_length=50, default= '')