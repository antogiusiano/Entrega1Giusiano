# Generated by Django 4.0.3 on 2022-04-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='folleto',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='campeonatos_mundiales',
            field=models.BooleanField(),
        ),
    ]
