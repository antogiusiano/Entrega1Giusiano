# Generated by Django 4.0.3 on 2022-04-12 23:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0002_piloto_folleto_alter_equipos_campeonatos_mundiales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piloto',
            name='folleto',
        ),
        migrations.AddField(
            model_name='piloto',
            name='tarjeta_presentacion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]