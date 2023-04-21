from django.db import models
from project.models import ConstrProject
from customer.models import Customer

class Contracts(models.Model):
    number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Sut.Nr.")
    date = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sut.data')
    object_name = models.ForeignKey(ConstrProject, on_delete=models.SET_NULL, null=True, verbose_name='Objektas')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name='Užsakovas')
    contractor = models.CharField(max_length=150, default='UAB E', verbose_name='Rangovas')
    sum_obj = models.FloatField(null=True, blank=True, verbose_name='Sut.vertė')
    start_date = models.DateField(null=True, verbose_name='Pradžios data')
    end_date = models.DateField(null=True, verbose_name='Pabaigos data')
    ex_end_date = models.DateField(null=True, verbose_name='Pratęsta iki')
    description = models.TextField(null=True, blank=True, verbose_name='Kita info')

    class Meta:
        verbose_name = "Sutartys"
        verbose_name_plural = "Sutartys"

    def __str__(self):
        return self.object_name

