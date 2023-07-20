from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'), 
    path('trocar_senha/', views.trocar_senha, name='alterar_senha')
]