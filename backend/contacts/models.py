from django.db import models
from datetime import datetime

# Create your models here.
class Contacts(models.Model):
    email = models.EmailField(max_length=25)
    name = models.CharField(max_length=25)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=500)
    contact_data = models.DateField(default=datetime.now, blank=True)


    def __str__(self):
        return self.email