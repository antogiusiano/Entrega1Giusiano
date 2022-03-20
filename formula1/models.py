from django.db import models

class Piloto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    equipo = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.equipo}'
    
class Equipos(models.Model):
    nombre_equipo = models.CharField(max_length=30)
    motor = models.CharField(max_length=20)
    campeonatos_mundiales = models.BooleanField()

    def __str__(self):
        return f'{self.nombre_equipo} {self.motor} {self.campeonatos_mundiales}'
        
class Circuito(models.Model):
    nombre_circuito = models.CharField(max_length=30)
    vueltas = models.IntegerField()
    longitud = models.IntegerField()

    def __str__(self):
        return f'{self.nombre_circuito} {self.vueltas} {self.longitud}'