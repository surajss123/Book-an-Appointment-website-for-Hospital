from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class appointment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField(max_length=20)
    Department = models.CharField(max_length=100)
    Doctor = models.CharField(max_length=100)
    Date = models.DateField()
    Message = models.TextField(max_length=1000)