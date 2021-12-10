from django.db import models

# create your models here

class employee(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=40)
    salary=models.IntegerField()
    status=models.BooleanField()