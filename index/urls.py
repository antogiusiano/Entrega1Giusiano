from django.urls import path
from .views import index,about,pages


urlpatterns = [
    path('',index, name='index'),
    path('about/', about, name='about'),
    path('pages/',pages, name='pilotos')
]