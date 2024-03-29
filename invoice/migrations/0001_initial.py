# Generated by Django 4.0.4 on 2022-12-20 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('customer', '0001_initial'),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(default='ELM', max_length=3, verbose_name='Serija')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='Numeris')),
                ('date', models.DateField(verbose_name='Data')),
                ('seller', models.CharField(default='UAB E', max_length=100, verbose_name='Pardavėjas')),
                ('sum_ex_vat', models.FloatField(verbose_name='Vertė be PVM')),
                ('vat', models.FloatField(verbose_name='PVM')),
                ('sum_with_vat', models.FloatField(verbose_name='Vertė su PVM')),
                ('reverse_payment', models.BooleanField()),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer', verbose_name='Pirkėjas')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.contracts', verbose_name='Sutartis')),
                ('proj_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.constrproject', verbose_name='Objektas')),
            ],
            options={
                'verbose_name': 'PVM sąskaita faktūra',
                'verbose_name_plural': 'PVM sąskaita faktūra',
            },
        ),
    ]
