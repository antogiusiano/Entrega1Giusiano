from django.shortcuts import render

def index(request):
     return render(request, 'index/index.html', {})

def equipos(request):
    return render(request, 'index/equipos.html', {})