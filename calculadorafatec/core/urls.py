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
    path('cursos/', views.cursos, name='cursos'),
    path('fatecs/', views.fatecs, name='fatecs'),
    path('contato/', views.contato, name='contato'),
    path('logout/', views.logout, name='logout'),
]
