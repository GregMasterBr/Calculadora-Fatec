"""calculadorafatec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('materias-prova-peso2/', views.materias_prova_peso2, name='materias-prova-peso2'),
    path('materias-prova-peso2-com-js/', views.materias_prova_peso2_com_js, name='materias-prova-peso2-com-js'),
    path('cursos/', views.cursos, name='cursos'),
    path('fatecs/', views.fatecs, name='fatecs'),
    path('busca-slug-fatec/', views.busca_slug_fatec, name="busca_slug_fatec"), # intermediária. Usava para capturar o slug
    #path('detalhes-fatec/<int:id>', views.detalhes_fatec, name="detalhes_fatec"),
    path('detalhes-fatec/<slug:slug>/', views.detalhes_fatec, name="detalhes_fatec"),
    #path('detalhes-fatec/', views.detalhes_fatec, name="detalhes_fatec"),
    path('busca-slug-curso/', views.busca_slug_curso, name="busca_slug_curso"), # intermediária. Usava para capturar o slug
    path('detalhes-curso/<slug:slug>/', views.detalhes_curso, name="detalhes_curso"),
    path('nota-de-corte/', views.nota_de_corte, name='nota-de-corte'),
    path('detalhes-nota-de-corte/', views.detalhes_nota_de_corte, name='detalhes-nota-de-corte'),
    path('busca-cursos-da-fatec/', views.busca_cursos_da_fatec, name='busca-cursos-da-fatec'),

    path('contato/', views.contato, name='contato'),
    path('logout/', views.logout, name='logout'),
]
