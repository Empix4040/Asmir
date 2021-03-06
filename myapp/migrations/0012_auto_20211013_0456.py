# Generated by Django 3.1.6 on 2021-10-13 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20211013_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offertwo',
            name='oContent',
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content1',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content2',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content3',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 55, 46, 456993, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content4',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 56, 1, 819690, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content5',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 56, 6, 161930, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content6',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 56, 9, 193569, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content7',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 56, 11, 112675, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content8',
            field=models.TextField(default=datetime.datetime(2021, 10, 13, 2, 56, 13, 215317, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
