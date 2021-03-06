# Generated by Django 3.0.2 on 2020-02-23 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_auto_20200223_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='id_account',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='balance',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='creation_day',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 15, 5, 1, 863859)),
        ),
    ]
