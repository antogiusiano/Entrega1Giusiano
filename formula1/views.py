from django.shortcuts import redirect, render
from .forms import PilotoFormulario, PilotoBusqueda
from .models import Piloto
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def crear_piloto(request):
    
    if request.method == 'POST':
        form = PilotoFormulario(request, data = request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            piloto = Piloto(nombre=data['nombre'], apellido=data['apellido'], equipo=data['equipo'], titulo=data['titulo'],subtitulo=data['subtitulo'], cuerpo=data['cuerpo'])
            piloto.save()
            return redirect('pilotos')
            
    form = PilotoFormulario()
    return render(request, 'formula1/crear_piloto.html', {'form': form})

def lista_pilotos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        pilotos = Piloto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        pilotos = Piloto.objects.all()
        
    form = PilotoBusqueda()
    return render(request, 'formula1/lista_pilotos.html', {'form': form, 'pilotos':pilotos})

class DetallePiloto(DetailView):
    model = Piloto
    template_name = 'formula1/detalle_piloto.html'


class EditarPiloto(LoginRequiredMixin,UpdateView):
    model = Piloto
    success_url = '/formula1/pages/'
    fields = ['nombre', 'apellido', 'equipo', 'titulo', 'subtitulo', 'cuerpo', 'imagen']


class BorrarPiloto(LoginRequiredMixin,DeleteView):
    model = Piloto
    success_url = '/formula1/pages/'