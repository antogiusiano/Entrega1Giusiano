from django.urls import path
from .views import index,acerca_de_mi

urlpatterns = [
    path('',index, name='index'),
    path('acerca-de-mi/',acerca_de_mi, name='acerca_de_mi')
]