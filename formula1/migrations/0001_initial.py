# Generated by Django 4.0.3 on 2022-03-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_circuito', models.CharField(max_length=30)),
                ('vueltas', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=30)),
                ('motor', models.CharField(max_length=20)),
                ('campeonatos_mundiales', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('equipo', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=20)),
            ],
        ),
    ]
