# Generated by Django 3.2.8 on 2021-10-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0002_auto_20211027_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantilla',
            name='enunciado',
            field=models.CharField(default=1111, max_length=500),
            preserve_default=False,
        ),
    ]