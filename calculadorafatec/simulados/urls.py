from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.home_simulados, name='home-simulados'),
    path('teste-simulado/', views.teste_simulado, name='teste-simulado'),
]