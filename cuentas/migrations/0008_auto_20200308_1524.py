# Generated by Django 3.0.2 on 2020-03-08 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_auto_20200308_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_day',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 8, 15, 24, 42, 979093)),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
