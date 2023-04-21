from django.db import models
from contract.models import *
from project.models import *


class Form3(models.Model):
    number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Nr.")
    date = models.DateField(verbose_name='Laikotarpis')
    contractor = models.CharField(max_length=100, default='UAB E', verbose_name='Rangovas')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Užsakovas')
    object = models.ForeignKey(ConstrProject, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Objektas')
    contract = models.ForeignKey(Contracts, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sutartis')
    contract_price = models.FloatField(verbose_name='Sutarties vertė')
    sum_from_begining = models.FloatField(verbose_name='Atlikta nuo pradžios')
    sum_before_month = models.FloatField(verbose_name='Atlikta be ataskaitinio')
    sum_p_month = models.FloatField(verbose_name='Atlikta per mėn.')

    class Meta:
        verbose_name = "Forma 3"
        verbose_name_plural = "Forma 3"

    def __str__(self):
        return self.date, self.object



