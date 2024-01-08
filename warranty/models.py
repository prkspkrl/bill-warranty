from django.db import models
from datetime import datetime


# Create your models here.
class WarrantyCard(models.Model):
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True) 
    watch_model = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer_name
