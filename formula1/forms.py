from django import forms


class PilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=20)

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