# Generated by Django 4.1.3 on 2022-12-01 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_resultadovestibularfatec_cod_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadovestibularfatec',
            name='cod_instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.fatec'),
        ),
    ]
