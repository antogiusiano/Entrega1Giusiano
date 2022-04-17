from django.urls import path
from .import views

urlpatterns = [
    path('pages/', views.lista_pilotos, name='pilotos'),
    path('pages/crear/',views.crear_piloto, name='crear_piloto'),
    path('pages/<int:pk>',views.DetallePiloto.as_view(), name='detalle_piloto'),
    path('pages/<int:pk>/editar',views.EditarPiloto.as_view(), name='editar_piloto'),
    path('pages/<int:pk>/borrar',views.BorrarPiloto.as_view(), name='borrar_piloto'),
    
    path('equipo/crear/',views.crear_equipo, name='crear_equipo'),
    path('circuito/crear/',views.crear_circuito, name='crear_circuito'),
]