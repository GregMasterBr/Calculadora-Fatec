# Generated by Django 4.1.1 on 2022-11-18 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagem',
            options={'verbose_name': 'imagem', 'verbose_name_plural': 'imagens'},
        ),
        migrations.RemoveField(
            model_name='imagem',
            name='fatec',
        ),
        migrations.AddField(
            model_name='fatec',
            name='imagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Imagem', to='core.imagem'),
        ),
    ]
