from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.home_simulados, name='home-simulados'),
    path('teste-simulado/', views.teste_simulado, name='teste-simulado'),
    path('simulado2/', views.simulado2, name='simulado2'),
    path('gabarito/', views.gabarito, name='gabarito'),


]
