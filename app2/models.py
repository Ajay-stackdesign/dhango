  from django.db import models

# Create your models here.

class employee(models.Model):
    name= models.charField(max_length= 30)
    address= models.charField(max_length= 40)
    salary= models.IntegerField()
    status=models.BooleanField()
