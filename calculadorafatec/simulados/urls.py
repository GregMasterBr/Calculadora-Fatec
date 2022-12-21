from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.home_simulados, name='home-simulados'),

]