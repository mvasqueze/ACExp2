# Generated by Django 3.2.8 on 2021-11-14 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco_preguntas',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('enunciado', models.CharField(max_length=500)),
                ('id_banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.banco_preguntas')),
            ],
        ),
        migrations.CreateModel(
            name='Incorrecta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_equivocada', models.CharField(max_length=50)),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.plantilla')),
            ],
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('dni', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_estudiantes',
            fields=[
                ('dni', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('id_estudiante', models.CharField(max_length=10)),
                ('nombre_estudiante', models.CharField(max_length=20)),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.grupos')),
            ],
        ),
        migrations.CreateModel(
            name='Correcta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=50)),
                ('respuesta', models.CharField(max_length=50)),
                ('id_pregunta', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.plantilla')),
            ],
        ),
        migrations.AddField(
            model_name='banco_preguntas',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.curso'),
        ),
    ]