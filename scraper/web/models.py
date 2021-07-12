from django.db import models

# Create your models here.
class Car (models.Model):
    year=models.IntegerField()
    make=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    mileage=models.IntegerField()
