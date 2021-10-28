# Generated by Django 3.1.6 on 2021-10-15 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20211015_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='PansionGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pansion1', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion2', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion3', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion4', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion5', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion6', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion7', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion8', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion9', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion10', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion11', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion12', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion13', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion14', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion15', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion16', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion17', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion18', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
                ('Pansion19', models.ImageField(blank=True, null=True, upload_to='Pansion/')),
            ],
        ),
        migrations.CreateModel(
            name='QuadGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quad1', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad2', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad3', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad4', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad5', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad6', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad7', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad8', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad9', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad10', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad11', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad12', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad13', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad14', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad15', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad16', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad17', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad18', models.ImageField(blank=True, null=True, upload_to='Quad/')),
                ('Quad19', models.ImageField(blank=True, null=True, upload_to='Quad/')),
            ],
        ),
        migrations.RemoveField(
            model_name='raftinggallery',
            name='rafting',
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting1',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting10',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting11',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting12',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting13',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting14',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting15',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting16',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting17',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting18',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting19',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting2',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting3',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting4',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting5',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting6',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting7',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting8',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
        migrations.AddField(
            model_name='raftinggallery',
            name='rafting9',
            field=models.ImageField(blank=True, null=True, upload_to='rafting/'),
        ),
    ]
