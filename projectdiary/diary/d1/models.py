from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
    dates=models.DateField()
    heading = models.CharField(max_length=50)
    diarys=models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)