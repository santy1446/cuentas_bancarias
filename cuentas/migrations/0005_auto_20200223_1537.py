# Generated by Django 3.0.2 on 2020-02-23 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_auto_20200223_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balance',
        ),
        migrations.AlterField(
            model_name='account',
            name='creation_day',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 15, 36, 58, 364624)),
        ),
    ]
