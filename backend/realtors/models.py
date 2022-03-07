from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.CharField(blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, black=True)


    def __str__(self):
        return self.name
