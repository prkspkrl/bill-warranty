# Generated by Django 3.0.7 on 2023-11-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printbill', '0002_auto_20231120_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='watch_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='delivey_fee',
            field=models.IntegerField(blank=True, default='Free', null=True),
        ),
    ]
