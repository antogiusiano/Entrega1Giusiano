from django.urls import path
from .views import index,pilotos,equipos,circuitos

urlpatterns = [
    path('',index, name='index'),
    path('pilotos/',pilotos, name='pilotos'),
    path('equipos/',equipos, name='equipos'),
    path('circuitos/',circuitos, name='circuitos')
]