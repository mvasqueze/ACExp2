# Generated by Django 3.2.8 on 2021-11-07 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0002_alter_grupos_dni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupo_estudiantes',
            old_name='id_curso',
            new_name='id_grupo',
        ),
    ]