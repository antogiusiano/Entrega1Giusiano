from django.shortcuts import render

def index(request):
     return render(request, 'index/index.html', {})

def pilotos(request):
    return render(request, 'index/pilotos.html', {})

def equipos(request):
    return render(request, 'index/equipos.html', {})

def circuitos(request):
    return render(request, 'index/circuitos.html', {})