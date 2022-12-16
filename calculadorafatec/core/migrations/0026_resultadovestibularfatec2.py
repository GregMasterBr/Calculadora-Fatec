# Generated by Django 4.1.3 on 2022-12-07 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_resultadovestibularfatec_cod_curso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoVestibularFatec2',
            fields=[
                ('cod_resultado_fatec', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('periodo', models.CharField(max_length=10)),
                ('qtde_vagas', models.IntegerField()),
                ('qtde_inscrito', models.IntegerField()),
                ('demanda', models.FloatField()),
                ('nota_corte', models.FloatField()),
                ('nota_maxima', models.FloatField()),
                ('cod_curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.curso')),
                ('cod_instituicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.fatec')),
            ],
        ),
    ]