# Generated by Django 4.0.3 on 2022-04-13 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0003_remove_piloto_folleto_piloto_tarjeta_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
