from django.db import models
from datetime import datetime

PAYMENT_METHODS = (
    
    ('Esewa', 'Esewa'),
    ('Banktransfer', 'Banktransfer'),
    ('COD', 'COD'),

    )

# Create your models here.
class Bill(models.Model):
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    watch_name = models.CharField(max_length=100, blank=True, null=True)
    invoice = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    subtotal = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(blank=True, null=True)    
    grand_total = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    delivey_fee = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS, default='COD')    
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer_name
