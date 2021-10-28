# Generated by Django 3.1.6 on 2021-10-13 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211013_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='FooterContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='FooterTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='middlesection',
            old_name='HeadContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='middlesection',
            old_name='HeadTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offerfive',
            old_name='OfferFiveContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='offerfive',
            old_name='OfferFiveTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offerfour',
            old_name='OfferFourContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='offerfour',
            old_name='OfferFourTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offerone',
            old_name='OfferOneContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='offerone',
            old_name='OfferOneTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offerthree',
            old_name='OfferThreeContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='offerthree',
            old_name='OfferThreeTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offertwo',
            old_name='OfferTwoTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='offertwo',
            old_name='OfferTwoContent',
            new_name='oContent',
        ),
        migrations.RenameField(
            model_name='pansionneretva',
            old_name='Content1',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='pansionneretva',
            old_name='Link1',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='pansionneretva',
            old_name='Title1',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='quadadvantures',
            old_name='Content2',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='quadadvantures',
            old_name='Link2',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='quadadvantures',
            old_name='Title2',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='raftingadrenaline',
            old_name='Content3',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='raftingadrenaline',
            old_name='Link3',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='raftingadrenaline',
            old_name='Title3',
            new_name='Title',
        ),
    ]