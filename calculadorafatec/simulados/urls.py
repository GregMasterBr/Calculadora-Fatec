from django.urls import path, include
from  . import views

app_name = 'simulados'


urlpatterns = [
    path('', views.home_simulados, name='home-simulados'),
    path('teste-simulado/', views.teste_simulado, name='teste-simulado'),
    path('simulado2/', views.simulado2, name='simulado2'),
    path('gabarito/', views.gabarito, name='gabarito'),

    # simulado endpoints
    path('simulado/<int:simulado_id>/start/', views.start_simulado, name='start-simulado'),
    path('simulado/<int:tentativa_id>/questao/<int:numero>/', views.exibir_questao, name='exibir-questao'),
    path('simulado/<int:tentativa_id>/responder/', views.responder_questao, name='responder-questao'),
    path('simulado/<int:tentativa_id>/finalizar/', views.finalizar_tentativa, name='finalizar-tentativa'),
    path('simulado/personalizado/criar/', views.criar_simulado_personalizado, name='criar-simulado'),
    path('simulado/<int:simulado_id>/ver/', views.ver_simulado, name='ver-simulado'),
]
