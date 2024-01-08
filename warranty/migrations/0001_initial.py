# Generated by Django 3.0.7 on 2023-11-19 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarrantyCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('watch_model', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]