# Generated by Django 3.1.6 on 2021-10-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20211013_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincontent',
            name='TitleSmall',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
