from django.urls import path
from .import views

urlpatterns = [
    path('pilotos/', views.lista_pilotos, name='pilotos'),
    path('piloto/crear/',views.crear_piloto, name='crear_piloto'),
    path('piloto/<int:pk>',views.DetallePiloto.as_view(), name='detalle_piloto'),
    path('piloto/<int:pk>/editar',views.EditarPiloto.as_view(), name='editar_piloto'),
    path('piloto/<int:pk>/borrar',views.BorrarPiloto.as_view(), name='borrar_piloto'),
    
    path('equipo/crear/',views.crear_equipo, name='crear_equipo'),
    path('circuito/crear/',views.crear_circuito, name='crear_circuito'),
]