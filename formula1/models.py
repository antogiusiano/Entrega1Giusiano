from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Piloto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    equipo = models.CharField(max_length=40)
    titulo = RichTextField(blank=True, null=True)
    subtitulo = RichTextField(blank=True, null=True)
    cuerpo = RichTextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='imagen', blank=True, null=True)
    fecha_imagen = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'