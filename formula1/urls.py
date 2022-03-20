from django.urls import path
from .import views

urlpatterns = [
    path('piloto/crear/',views.crear_piloto, name='crear_piloto'),
    path('equipo/crear/',views.crear_equipo, name='crear_equipo'),
    path('circuito/crear/',views.crear_circuito, name='crear_circuito'),
    path('pilotos/', views.lista_pilotos, name='lista_pilotos'),
]