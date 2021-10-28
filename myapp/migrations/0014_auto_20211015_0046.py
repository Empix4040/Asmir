# Generated by Django 3.1.6 on 2021-10-14 22:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211013_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerfive',
            name='Price',
            field=models.CharField(default=datetime.datetime(2021, 10, 14, 22, 45, 53, 376960, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Price',
            field=models.CharField(default=datetime.datetime(2021, 10, 14, 22, 45, 58, 711879, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerone',
            name='Price',
            field=models.CharField(default=datetime.datetime(2021, 10, 14, 22, 46, 4, 625564, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Price',
            field=models.CharField(default=datetime.datetime(2021, 10, 14, 22, 46, 10, 303490, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Price',
            field=models.CharField(default=datetime.datetime(2021, 10, 14, 22, 46, 16, 227236, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]