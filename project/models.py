from django.db import models
from customer.models import *



WORKS = (
    ("E", "Electrical"),
    ("SST", 'Low current networks'),
    ('PVA', "Automatisation"),
    ('Oth', 'Other'),
)

class ConstrProject(models.Model):
    proj_name = models.CharField(max_length=200, verbose_name='Objekto pavadinimas')
    address = models.CharField(max_length=200, verbose_name='Adresas')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name='Užsakovas')
    start_date = models.DateField(verbose_name='Pradžia')
    end_date = models.DateField(verbose_name='Pabaiga')
    works_part = models.CharField(max_length=20, choices=WORKS, verbose_name='Darbai')
    description = models.TextField(null=True, blank=True, verbose_name='Aprašymas')

    class Meta:
        verbose_name = "Objektai"
        verbose_name_plural = "Objektai"

    def __str__(self):
        return self.proj_name


