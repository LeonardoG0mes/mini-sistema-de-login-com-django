from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('verificar_codigo/<str:email>/', views.verificar_codigo, name='verificar_codigo'),    path('login/', views.login, name='login'),
    path('excluir_perfil/<str:email>/', views.excluir_perfil_usuario, name='excluir_perfil'),
    path('reenviar_codigo/<str:email>/', views.reenviar_codigo, name='reenviar_codigo'),
    path('home/', views.home, name='home'), 
    path('trocar_senha/', views.trocar_senha, name='alterar_senha'),
]