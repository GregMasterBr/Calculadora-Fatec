from django.shortcuts import render

# Create your views here.


def home_simulados(request):
    return render(request,'index-simulados.html')