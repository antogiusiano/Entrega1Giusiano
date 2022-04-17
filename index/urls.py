from django.urls import path
from .views import index,about,pages,equipos,circuitos


urlpatterns = [
    path('',index, name='index'),
    path('about/', about, name='about'),
    path('pages/',pages, name='pilotos'),
    path('equipos/',equipos, name='equipos'),
    path('circuitos/',circuitos, name='circuitos')
]