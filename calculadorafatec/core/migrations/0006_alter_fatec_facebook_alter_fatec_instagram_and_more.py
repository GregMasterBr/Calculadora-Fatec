# Generated by Django 4.1.1 on 2022-11-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_fatec_googlemaps_alter_fatec_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatec',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='fatec',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='fatec',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='fatec',
            name='youtube',
            field=models.URLField(blank=True),
        ),
    ]