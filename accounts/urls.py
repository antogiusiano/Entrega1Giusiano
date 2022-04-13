from django.urls import path
from .views import mi_login, registrarse, editar_usuario, usuario_datos
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',mi_login, name='login'),
    path('editar/',editar_usuario, name='editar_usuario'),
    path('datos/',usuario_datos, name='usuario_datos'),
    path('registrarse/',registrarse, name='registrarse'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),   
]
