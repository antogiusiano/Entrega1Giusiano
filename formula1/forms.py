from django import forms
from ckeditor.fields import RichTextFormField

class PilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=40)
    titulo = RichTextFormField(required=False)
    subtitulo = RichTextFormField(required=False)
    cuerpo = RichTextFormField(required=False)
    imagen = forms.ImageField(required=False)
    fecha_imagen = forms.DateTimeField(required=False)

class EquipoFormulario(forms.Form):
    nombre_equipo = forms.CharField(max_length=30)
    motor = forms.CharField(max_length=20)
    campeonatos_mundiales = forms.BooleanField(required=False)

class CircuitoFormulario(forms.Form):
    nombre_circuito = forms.CharField(max_length=30)
    vueltas = forms.IntegerField()
    longitud = forms.IntegerField()

class PilotoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)