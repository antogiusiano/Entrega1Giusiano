# Generated by Django 4.0.3 on 2022-04-17 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0008_alter_piloto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='fecha_imagen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
