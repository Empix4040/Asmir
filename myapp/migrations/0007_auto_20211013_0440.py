# Generated by Django 3.1.6 on 2021-10-13 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_maincontent_titlesmall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerfive',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='offerfour',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='offerone',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='offerthree',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='offertwo',
            name='oContent',
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content1',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content2',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content3',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content4',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content5',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content6',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content7',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfive',
            name='Content8',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content1',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content2',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content3',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content4',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content5',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content6',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content7',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerfour',
            name='Content8',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content1',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content2',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content3',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content4',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content5',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content6',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content7',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerone',
            name='Content8',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content1',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content2',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content3',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content4',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content5',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content6',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content7',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offerthree',
            name='Content8',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content1',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content2',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content3',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content4',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content5',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content6',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content7',
            field=models.TextField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='offertwo',
            name='Content8',
            field=models.TextField(default=None, max_length=40),
        ),
    ]
