from django.urls import path
from .views import index,equipos

urlpatterns = [
    path('',index, name='index'),
    path('equipos/',equipos, name='equipos')
]