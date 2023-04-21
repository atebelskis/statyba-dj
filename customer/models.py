from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Pavadinimas")
    code = models.CharField(max_length=20, unique=True, verbose_name="Įmonės kodas")
    vat_code = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="PVM kodas")
    address = models.CharField(max_length=200, verbose_name='Adresas')
    bank_code = models.CharField(max_length=20, null=True, blank=True, verbose_name='Banko kodas')
    invoice_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Sąskaita')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Tel.')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='El. paštas')
    ceo_person = models.CharField(max_length=50, null=True, blank=True, verbose_name='Vadovas/atstovaujantis asmuo')

    class Meta:
        verbose_name = "Užsakovai"
        verbose_name_plural = "Užsakovai'"

    def __str__(self):
        return self.name

