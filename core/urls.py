from django.urls import path, re_path
from . import views
from .views import AltaProductoView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contacto', views.contacto, name='contacto'),
    path('alta_figura/', AltaProductoView.as_view(), name='alta_figura'),
    path('personajes/alta', views.alta_personaje, name='alta_personaje'),
    path('compañias/alta', views.alta_compañia, name='alta_compañia'),
    path('listado_figuras', views.listar_productos, name='listado_figuras'),
    path('personajes/listado', views.listar_personajes, name='listado_personajes'),
    path('compañias/listado', views.listar_compañias, name='listado_compañias'),
    path('personajes/listado/<int:id>/', views.listar_personajes, name='listar_personajes'),
]
