# Generated by Django 4.1.3 on 2022-11-04 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroAsociado', '0009_alter_genero_nombregenero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombreGenero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tipodocumento',
            name='nombreDocumento',
            field=models.CharField(max_length=50),
        ),
    ]
