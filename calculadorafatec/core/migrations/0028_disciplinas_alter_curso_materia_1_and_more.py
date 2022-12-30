# Generated by Django 4.1.1 on 2022-12-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_curso_destaque_curso_sugestao_cursos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(blank=True, max_length=20, null=True, verbose_name='Disciplina')),
                ('sigla', models.CharField(blank=True, max_length=4, null=True, verbose_name='Sigla')),
                ('cor', models.CharField(blank=True, max_length=7, null=True, verbose_name='Cor')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('quantidade_questoes', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Diciplina da proba',
                'verbose_name_plural': 'Disciplinas da Prova',
                'ordering': ('disciplina',),
            },
        ),
        migrations.AlterField(
            model_name='curso',
            name='materia_1',
            field=models.CharField(blank=True, choices=[('BIO', 'BIOLOGIA'), ('FIS', 'FÍSICA'), ('GEO', 'GEOGRAFIA'), ('HIST', 'HISTÓRIA'), ('ING', 'INGLÊS'), ('MAT', 'MATEMÁTICA'), ('MULT', 'MULTIDISCIPLINAR'), ('PORT', 'PORTUGUÊS'), ('RLOG', 'RACIOCÍNIO LÓGICO'), ('QUI', 'QUÍMICA')], max_length=4, verbose_name='Materia peso 2 (1ª)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='materia_2',
            field=models.CharField(blank=True, choices=[('BIO', 'BIOLOGIA'), ('FIS', 'FÍSICA'), ('GEO', 'GEOGRAFIA'), ('HIST', 'HISTÓRIA'), ('ING', 'INGLÊS'), ('MAT', 'MATEMÁTICA'), ('MULT', 'MULTIDISCIPLINAR'), ('PORT', 'PORTUGUÊS'), ('RLOG', 'RACIOCÍNIO LÓGICO'), ('QUI', 'QUÍMICA')], max_length=4, verbose_name='Materia peso 2 (2ª)'),
        ),
    ]
