# Generated by Django 4.0.4 on 2022-07-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Įmonės kodas')),
                ('vat_code', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='PVM kodas')),
                ('address', models.CharField(max_length=200, verbose_name='Adresas')),
                ('bank_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Banko kodas')),
                ('invoice_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sąskaita')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tel.')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='El. paštas')),
                ('ceo_person', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vadovas/atstovaujantis asmuo')),
            ],
            options={
                'verbose_name': 'Užsakovai',
                'verbose_name_plural': "Užsakovai'",
            },
        ),
    ]
