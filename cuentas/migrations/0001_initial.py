# Generated by Django 3.0.2 on 2020-02-15 14:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('creation_day', models.DateTimeField(default=datetime.datetime(2020, 2, 15, 9, 25, 26, 376615))),
                ('activate', models.BooleanField(default=True)),
                ('state_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuentas.StateAccount')),
                ('type_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuentas.TypeAccount')),
            ],
        ),
    ]