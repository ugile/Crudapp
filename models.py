from django.db import models

# Create your models here.


class Hospital(models.Model):
    name=models.CharField(max_length=200)
    doctor=models.IntegerField()
    patient=models.IntegerField()
    city=models.CharField(max_length=60)
    contact=models.IntegerField()