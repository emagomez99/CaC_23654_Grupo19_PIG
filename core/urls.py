from django.urls import path, re_path
from . import views
from .views import AltaProductoView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contacto', views.contacto, name='contacto'),
    path('alta_producto/', AltaProductoView.as_view(), name='alta_producto'),
    path('personajes/alta', views.alta_personaje, name='alta_personaje'),
    path('compañias/alta', views.alta_empresa, name='alta_compañia'),
    path('listado_productos', views.listar_productos, name='listado_productos'), #cambiar el primero a productos/listado
    path('personajes/listado', views.listar_personajes, name='listado_personajes'),
    path('compañias/listado', views.listar_empresas, name='listado_compañias'),
]
