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

class PilotoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)