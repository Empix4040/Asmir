# Generated by Django 3.1.6 on 2021-10-08 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('titleDescription', models.CharField(max_length=120)),
                ('middleTitle', models.CharField(max_length=120)),
                ('middleDescription', models.CharField(max_length=240)),
            ],
        ),
    ]