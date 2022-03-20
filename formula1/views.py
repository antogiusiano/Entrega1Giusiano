from django.shortcuts import redirect, render
from .forms import PilotoFormulario,EquipoFormulario,CircuitoFormulario, PilotoBusqueda
from .models import Equipos, Piloto, Equipos, Circuito

def crear_piloto(request):
    
    if request.method == 'POST':
        form = PilotoFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            piloto = Piloto(nombre=data['nombre'], apellido=data['apellido'], equipo=data['equipo'], pais=data['pais'])
            piloto.save()
            return redirect('pilotos')
            
    form = PilotoFormulario()
    return render(request, 'formula1/crear_piloto.html', {'form': form})

def crear_equipo(request):
    
    if request.method == 'POST':
        form = EquipoFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            equipo = Equipos(nombre_equipo=data['nombre_equipo'], motor=data['motor'], campeonatos_mundiales=data['campeonatos_mundiales'])
            equipo.save()
            return redirect('equipos')    
    
    form = EquipoFormulario()
    return render(request, 'formula1/crear_equipo.html', {'form': form})

def crear_circuito(request):
    
    if request.method == 'POST':
        form = CircuitoFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            circuito = Circuito(nombre_circuito=data['nombre_circuito'], vueltas=data['vueltas'], longitud=data['longitud'])
            circuito.save()
            return redirect('circuitos')       
    
    form = CircuitoFormulario()
    return render(request, 'formula1/crear_circuito.html', {'form': form})

def lista_pilotos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        pilotos = Piloto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        pilotos = Piloto.objects.all()
        
    form = PilotoBusqueda()
    return render(request, 'formula1/lista_pilotos.html', {'form': form, 'pilotos':pilotos})