from django.urls import path
from .import views

urlpatterns = [
    path('pages/', views.lista_pilotos, name='pilotos'),
    path('pages/crear/',views.crear_piloto, name='crear_piloto'),
    path('pages/<int:pk>',views.DetallePiloto.as_view(), name='detalle_piloto'),
    path('pages/<int:pk>/editar',views.EditarPiloto.as_view(), name='editar_piloto'),
    path('pages/<int:pk>/borrar',views.BorrarPiloto.as_view(), name='borrar_piloto')
]