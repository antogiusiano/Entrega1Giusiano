from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request):
    return HttpResponse('Bienvenidos')

def acerca_de_mi(request):
    
    template = loader.get_template('sobre_mi.html')
    
    template_generado = template.render({})
    
    return HttpResponse(template_generado)