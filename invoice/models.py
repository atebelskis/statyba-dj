from django.db import models
from contract.models import *

from project.models import ConstrProject


class Invoice(models.Model):
    serie = models.CharField(max_length=3, default='ELM', verbose_name="Serija")
    number = models.CharField(max_length=10, unique=True, verbose_name="Numeris")
    date = models.DateField(verbose_name="Data")
    seller = models.CharField(max_length=100, default='UAB E', verbose_name="Pardavėjas")
    buyer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pirkėjas')
    proj_name = models.ForeignKey(ConstrProject, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Objektas')
    contract = models.ForeignKey(Contracts, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sutartis')
    sum_ex_vat = models.FloatField( verbose_name="Vertė be PVM")
    vat = models.FloatField(verbose_name='PVM')
    sum_with_vat = models.FloatField(verbose_name='Vertė su PVM')
    reverse_payment = models.BooleanField()

    class Meta:
        verbose_name = "PVM sąskaita faktūra"
        verbose_name_plural = "PVM sąskaita faktūra"

    def __str__(self):
        return self.serie, self.number, self.date

