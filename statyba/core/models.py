from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    vat_code = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    bank_code = models.CharField(max_length=20, null=True, blank=True)
    invoice_number = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
