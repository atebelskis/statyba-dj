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

WORKS = (
    ("E", "Electrical"),
    ("SST", 'Low current networks'),
    ('PVA', "Automatisation")
)


class ConstProject(models.Model):
    obj_name = models.CharField(max_length=200)
    addresss = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    works_part = models.CharField(max_length=20, choices=WORKS)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.obj_name